# Retrospective enrichment benchmark — ENPP1 (6WEW), actives vs decoys

**Question a referee asks:** does the docking score actually separate known
ENPP1 binders from non-binders? If not, absolute scores are uninformative.

**Design.** 30 known ENPP1 actives (pChEMBL >=7, spread across 7.0-10.05,
ChEMBL target CHEMBL5925) + 90 property-matched presumed-inactive decoys
(same MW 320-580 / ALogP window, drawn from ChEMBL, not associated with ENPP1;
salts/mixtures excluded). All 3D-embedded (obabel --gen3d -p 7.4) and docked
into 6WEW with the identical protocol (box 21.01/-31.15/-27.70, 24 A cube,
exhaustiveness 16, seed 42). 119/120 docked successfully.

## Result (`enrichment_actives_decoys.csv`, `fig_enrichment.png`)

| metric | value | meaning |
|---|---|---|
| actives mean affinity | -8.74 | |
| decoys mean affinity | -8.97 | decoys score *slightly better* |
| median (both) | -8.90 | indistinguishable |
| Mann-Whitney p | 0.85 | no separation |
| **ROC-AUC** | **0.44** | **below random (0.50)** |
| EF 5% / 10% | 0.0 / 0.0 | no early enrichment |
| EF 20% | 0.51 | worse than random |

**Honest conclusion.** Raw smina/Vina affinity does **not** rank-order ENPP1
binders on this target. This is a common outcome for a metalloenzyme with a
buried di-zinc active site scored by a function with no explicit metal term
(consistent with the redocking control, which also localised the pocket but
missed sub-2 A chelation geometry).

## What this does and does NOT undermine — read carefully

**Does NOT invalidate the selectivity margins.** The selectivity analysis does
not use *absolute* affinity to rank *different* ligands (which is what this
benchmark tests and what fails). It uses the *difference* in score for the
*same* ligand docked into ENPP1 vs ENPP2/3 (ΔΔG). Ligand-specific systematic
errors of the scoring function — the dominant error mode here — **cancel in
that within-ligand difference**. The two questions are distinct.

**DOES cap the confidence and sharpen the framing:**
1. Any claim that rested on absolute affinity ranking across chemotypes is
   unsupported and must not be made.
2. The selectivity ΔΔG proxy is only trustworthy to the extent the *pose* is
   right in each paralog. The redocking control shows pose localisation is
   decent (right pocket, Zn engaged) but chelation geometry is not — so the
   margins remain **directional**, exactly as stated.
3. This is the strongest possible motivation for the wet-lab 3-enzyme panel and
   for a metal-aware / MM-GBSA rescore before any quantitative selectivity
   claim.

**Net for reviewers:** running this benchmark and reporting a *negative* result
is what raises the study's credibility. It converts "we assume docking works
here" into "we measured how well it works, and calibrated our claims to that."
