# Cognate redocking control — native 6WEW ligand (TZV)

**Referee question (gap item 1).** *Show the protocol reproduces a known pose
before I trust any score.*

**Design.** The native ENPP1 co-crystal ligand TZV (PDB ligand code TZV; the
quinoline-sulfuric-diamide inhibitor, "Ex54" in Dennis et al. 2020) was
extracted from 6WEW, re-prepared through the identical ligand pipeline, and
redocked into its own receptor with the production protocol (24 A cube on the
catalytic-Zn centroid, smina, exhaustiveness 16, 9 modes). Heavy-atom RMSD to
the crystal pose was measured for every sampled mode; Zn proximity checked.

## Result (`redock_validation.csv`, `fig_redock_validation.png`)

| mode | affinity (kcal/mol) | RMSD heavy (A) | in pocket |
|---|---|---|---|
| 1 | -9.0 | 3.44 | yes |
| 2 | -8.6 | 3.91 | yes |
| 3 | -8.6 | 3.55 | yes |
| 6 | -7.2 | **3.08** (best) | yes |
| 4,5,7,8,9 | -7.1 to -7.6 | 10.6-12.8 | no (surface decoys) |

**Honest reading.** The top-ranked modes land in the correct pocket with the
sulfamide engaging the catalytic Zn (2.2-2.3 A), clearly separated from the
10-13 A surface decoy poses — but no mode reproduces the crystal geometry to
the strict <2 A success line (best = 3.08 A, and it ranks 6th, not 1st). The
mechanistic reason is explicit: smina/Vina has no explicit metal-coordination
term, and TZV's sulfamide chelates the two catalytic Zn(2+) ions, so the exact
chelation geometry is not recovered. This **bounds** the claims rather than
inflating them: pose localisation is reliable ("right pocket, right metal
contact"), fine geometry is not — consistent with the "directional proxy only"
framing used throughout, and with the enrichment result.
