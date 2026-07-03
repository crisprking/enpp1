#!/bin/bash
# Multi-seed replicate docking for selectivity-margin confidence intervals.
# 6 ligands x 3 paralogs x 21 seeds, matched catalytic-Zn box, exhaustiveness 16.
set -u
cd /tmp
OUT="$1"
center_for(){ case $1 in
  enpp1) echo "21.01 -31.15 -27.70";;
  enpp2) echo "99.29 4.18 15.10";;
  enpp3) echo "110.04 135.94 65.60";; esac; }
rcp_for(){ case $1 in
  enpp1) echo "enpp1_6wew_receptor.pdbqt";;
  enpp2) echo "enpp2_5mhp_receptor.pdbqt";;
  enpp3) echo "enpp3_6c01_receptor.pdbqt";; esac; }
LIGS="CHEMBL5826130 CHEMBL5915707 CHEMBL5555976 CHEMBL6149286 CHEMBL6174154 TZV_native"
SEEDS="42 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20"
echo "target,ligand,seed,affinity" > "$OUT"
n=0
for seed in $SEEDS; do
  for tgt in enpp1 enpp2 enpp3; do
    set -- $(center_for $tgt); cx=$1; cy=$2; cz=$3
    rcp=$(rcp_for $tgt)
    for lig in $LIGS; do
      aff=$(smina -r $rcp -l ${lig}.pdbqt \
        --center_x $cx --center_y $cy --center_z $cz \
        --size_x 24 --size_y 24 --size_z 24 \
        --exhaustiveness 16 --num_modes 5 --seed $seed \
        -o /tmp/_rep_${tgt}_${lig}_${seed}.pdbqt 2>/dev/null \
        | grep -A3 "mode |" | awk 'NR==4{print $2}')
      echo "${tgt},${lig},${seed},${aff}" >> "$OUT"
      rm -f /tmp/_rep_${tgt}_${lig}_${seed}.pdbqt
      n=$((n+1))
    done
  done
  echo "[seed $seed done] $n runs total so far" >&2
done
echo "ALL_REPLICATES_DONE $n runs" >&2
