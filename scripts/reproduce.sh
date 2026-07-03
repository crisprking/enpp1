#!/bin/bash
# End-to-end reproduction driver for the ENPP selectivity counter-screen.
# Run from the repository root:  bash scripts/reproduce.sh
set -euo pipefail
cd "$(dirname "$0")/.."

echo "==> [1/4] preparing ligands (SMILES -> PDBQT)"
python scripts/prepare_ligands.py --ligands data/ligands.csv --outdir build/

echo "==> [2/4] converting receptors PDB -> PDBQT"
for p in enpp1_6wew enpp2_5mhp enpp3_6c01; do
  obabel "receptors/${p}_receptor.pdb" -O "build/${p}_receptor.pdbqt" -xr
done

echo "==> [3/4] docking (smina, 3 paralogs x 6 ligands)"
# dock_all.sh expects ligand + receptor PDBQTs in the working dir
( cd build && cp ../scripts/dock_all.sh . && bash dock_all.sh )
cp build/dock_results.csv data/docking_scores_raw.csv

echo "==> [4/4] building scorecard"
python scripts/build_scorecard.py

echo "==> done. See data/enpp_selectivity_scorecard.csv"
