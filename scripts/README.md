# Scripts — protocol notes

The pipeline has three stages. Only stage 3 is needed to reproduce the headline
scorecard from the committed raw scores; stages 1–2 regenerate those scores.

### 1. `prepare_ligands.py` — SMILES → docking-ready PDBQT
```bash
python scripts/prepare_ligands.py --ligands data/ligands.csv --outdir build/
```
RDKit ETKDGv3 embedding (seed 42) + MMFF optimization, then `obabel` adds
Gasteiger charges and writes AutoDock PDBQT. Produces `build/<cid>.pdbqt`.

### 2. `dock_all.sh` — smina across 3 paralogs × 6 ligands
```bash
# expects receptor PDBQTs + ligand PDBQTs in the working directory
bash scripts/dock_all.sh
```
Docks every ligand into ENPP1 (6WEW), ENPP2 (5MHP), ENPP3 (6C01) using a 24 Å
cube centered on each enzyme's **catalytic-Zn centroid**:

| target | box center (x y z, Å) | receptor |
|--------|-----------------------|----------|
| ENPP1  | 21.01 −31.15 −27.70   | enpp1_6wew_receptor.pdbqt |
| ENPP2  | 99.29  4.18  15.10    | enpp2_5mhp_receptor.pdbqt |
| ENPP3  | 110.04 135.94 65.60   | enpp3_6c01_receptor.pdbqt |

smina flags: `--exhaustiveness 16 --num_modes 5 --seed 42`. Writes
`dock_results.csv` (target, ligand, best-mode affinity) and per-run pose PDBQTs.

> **Receptor PDBQTs:** the repo ships the prepared receptor **PDBs** under
> `receptors/`. Convert to PDBQT before docking, e.g.
> `obabel receptors/enpp1_6wew_receptor.pdb -O enpp1_6wew_receptor.pdbqt -xr`.

### 3. `build_scorecard.py` — raw scores → selectivity verdicts
```bash
python scripts/build_scorecard.py
```
Pivots `data/docking_scores_raw.csv` to wide form, computes per-paralog margins
(paralog − ENPP1) and the worst-case margin, assigns a verdict
(anti-selective / borderline / ENPP1-preferring), and writes
`data/enpp_selectivity_scorecard.csv`. Deterministic; reproduces the committed
file exactly.

### `reproduce.sh` — end-to-end driver
Runs stages 1→2→3. Docking is stochastic; with the fixed seed and
exhaustiveness 16, best-mode scores are stable to ≈0.1–0.3 kcal/mol.
