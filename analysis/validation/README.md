# Protocol validation suite

Three controls that calibrate how far the docking protocol can be trusted on
this target. All were run with the identical production protocol (24 A cube on
the catalytic-Zn centroid, smina, exhaustiveness 16). The headline is honest in
both directions: absolute scoring is weak here (as expected for a di-zinc
metalloenzyme scored without a metal term), which is exactly why every claim in
this repo is framed as a *within-ligand ENPP1-vs-paralog difference* (ddG), not
an absolute affinity.

| control | file | question | verdict |
|---|---|---|---|
| Cognate redocking | `REDOCK_README.md` | does the protocol reproduce a known pose? | right pocket + Zn engaged (2.2-2.3 A); 3.08 A best RMSD, fails strict <2 A (no metal term) |
| Actives/decoys enrichment | `ENRICHMENT_README.md` | does absolute score rank known binders? | **no** — ROC-AUC 0.44, EF5%/10%=0 (honest negative) |
| Protonation sensitivity | `PROTOMER_README.md` | is the call an artifact of one protomer? | directional calls **sign-robust** over 8 states; magnitudes move 0.4-1.0 kcal/mol |

**Why the enrichment negative does not sink the study.** The enrichment
benchmark tests *absolute* affinity ranking *across different ligands* — which
fails. The selectivity analysis uses the *difference* in score for the *same*
ligand across paralogs, in which ligand-specific systematic scoring errors
largely cancel. Reporting the negative result raises credibility: it converts
"we assume docking works here" into "we measured how well it works and
calibrated every claim to that." See `../../REVIEWER_GAP_ANALYSIS.md` for the
full referee-perspective ledger.
