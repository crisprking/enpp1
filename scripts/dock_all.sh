#!/bin/bash
center_for(){ case $1 in
  enpp1) echo "21.01 -31.15 -27.70";;
  enpp2) echo "99.29 4.18 15.10";;
  enpp3) echo "110.04 135.94 65.60";; esac; }
rcp_for(){ case $1 in
  enpp1) echo "enpp1_6wew_receptor.pdbqt";;
  enpp2) echo "enpp2_5mhp_receptor.pdbqt";;
  enpp3) echo "enpp3_6c01_receptor.pdbqt";; esac; }
LIGS="CHEMBL5826130 CHEMBL5915707 CHEMBL5555976 CHEMBL6149286 CHEMBL6174154 TZV_native"
echo "target,ligand,affinity" > dock_results.csv
for tgt in enpp1 enpp2 enpp3; do
  set -- $(center_for $tgt); cx=$1; cy=$2; cz=$3
  rcp=$(rcp_for $tgt)
  for lig in $LIGS; do
    smina -r $rcp -l ${lig}.pdbqt \
      --center_x $cx --center_y $cy --center_z $cz \
      --size_x 24 --size_y 24 --size_z 24 \
      --exhaustiveness 16 --num_modes 5 --seed 42 \
      -o dock_${tgt}_${lig}.pdbqt > log_${tgt}_${lig}.txt 2>&1
    aff=$(grep -A3 "mode |" log_${tgt}_${lig}.txt | awk 'NR==4{print $2}')
    echo "${tgt},${lig},${aff}" >> dock_results.csv
    echo "done ${tgt} ${lig} -> ${aff} (rcp=$rcp cx=$cx)"
  done
done
echo "ALL DONE"
