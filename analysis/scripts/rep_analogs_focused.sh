#!/bin/bash
set -u
cd /tmp
OUT="$1"
center_for(){ case $1 in
  enpp1) echo "21.01 -31.15 -27.70";; enpp2) echo "99.29 4.18 15.10";; enpp3) echo "110.04 135.94 65.60";; esac; }
rcp_for(){ case $1 in
  enpp1) echo "enpp1_6wew_receptor.pdbqt";; enpp2) echo "enpp2_5mhp_receptor.pdbqt";; enpp3) echo "enpp3_6c01_receptor.pdbqt";; esac; }
ANALOGS="AN00_parent AN10_piperidinol AN11_fluoro_pip"
SEEDS="42 1 2 3 4 5 6 7 8 9 10 11 12 13 14"
echo "target,analog,seed,affinity" > "$OUT"
for seed in $SEEDS; do
  for tgt in enpp1 enpp2 enpp3; do
    set -- $(center_for $tgt); cx=$1; cy=$2; cz=$3
    rcp=$(rcp_for $tgt)
    for lig in $ANALOGS; do
      aff=$(smina -r $rcp -l ${lig}.pdbqt \
        --center_x $cx --center_y $cy --center_z $cz \
        --size_x 24 --size_y 24 --size_z 24 \
        --exhaustiveness 16 --num_modes 5 --seed $seed \
        -o /tmp/_rf_${tgt}_${lig}_${seed}.pdbqt 2>/dev/null \
        | grep -A3 "mode |" | awk 'NR==4{print $2}')
      echo "${tgt},${lig},${seed},${aff}" >> "$OUT"
      rm -f /tmp/_rf_${tgt}_${lig}_${seed}.pdbqt
    done
  done
  echo "[focused seed $seed done]" >&2
done
echo "FOCUSED_ANALOG_DONE" >&2
