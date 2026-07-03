#!/usr/bin/env python3
"""Prepare docking-ready ligands from SMILES.

For each row in data/ligands.csv:
  1. Parse SMILES (RDKit), add explicit H
  2. Embed a 3D conformer (ETKDGv3, fixed seed) and MMFF-optimize
  3. Write <cid>.mol, then convert to <cid>.pdbqt with obabel

Output .pdbqt files are the inputs consumed by scripts/dock_all.sh.

Usage:
    python scripts/prepare_ligands.py --ligands data/ligands.csv --outdir build/
"""
import argparse
import subprocess
import sys
from pathlib import Path

import pandas as pd
from rdkit import Chem
from rdkit.Chem import AllChem

SEED = 42


def prep_one(cid: str, smiles: str, outdir: Path) -> Path:
    mol = Chem.MolFromSmiles(smiles)
    if mol is None:
        raise ValueError(f"unparseable SMILES for {cid}: {smiles}")
    mol = Chem.AddHs(mol)
    params = AllChem.ETKDGv3()
    params.randomSeed = SEED
    if AllChem.EmbedMolecule(mol, params) != 0:
        raise RuntimeError(f"embedding failed for {cid}")
    AllChem.MMFFOptimizeMolecule(mol)
    molpath = outdir / f"{cid}.mol"
    Chem.MolToMolFile(mol, str(molpath))
    pdbqt = outdir / f"{cid}.pdbqt"
    # obabel: add Gasteiger charges, output AutoDock PDBQT
    subprocess.run(
        ["obabel", str(molpath), "-O", str(pdbqt), "--partialcharge", "gasteiger"],
        check=True, capture_output=True,
    )
    return pdbqt


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--ligands", default="data/ligands.csv")
    ap.add_argument("--outdir", default="build")
    args = ap.parse_args()
    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)
    df = pd.read_csv(args.ligands)
    for _, row in df.iterrows():
        p = prep_one(row["cid"], row["smiles"], outdir)
        print(f"prepared {row['cid']} -> {p}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
