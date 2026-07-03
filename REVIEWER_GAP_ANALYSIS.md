# Reviewer-perspective gap analysis

*What a skeptical computational-chemistry / methods referee would flag, ranked
by impact, with current status. Written against this repository as of the
validation update.*

## Verdict
A well-documented, honestly-caveated **in-silico hypothesis-generating study** —
above the bar for an open methods repo, **below the bar for a standalone
methods paper** without the items marked [OPEN] below. The science is sound;
the gaps are about *calibration and validation of the docking protocol*, not
about the biology or the framing.

## Ranked referee critiques

### 1. Docking protocol validation — [ADDRESSED this update]
*"Show the protocol reproduces a known pose before I trust any score."*
Cognate redocking of the native 6WEW ligand TZV now exists
(`analysis/validation/`). Result is honest and instructive: correct pocket +
Zn engagement (2.2-2.3 A), but 3.08-3.44 A RMSD — fails strict <2 A because the
Vina scoring function has no explicit metal term. This **bounds** the claims
rather than inflating them, and is consistent with the "directional proxy"
framing used throughout.

### 2. Actives-vs-decoys discrimination / enrichment — [ADDRESSED this update]
Ran it: 30 known ENPP1 actives (pChEMBL >=7) vs 90 property-matched decoys,
docked into 6WEW with the identical protocol (`analysis/validation/`,
`ENRICHMENT_README.md`). **Result is a negative one, reported honestly:**
ROC-AUC = **0.44** (below random), EF 5%/10% = 0, actives and decoys have
identical median affinity (-8.90, Mann-Whitney p=0.85). Absolute smina score
does *not* rank ENPP1 binders — expected for a di-zinc metalloenzyme scored
without an explicit metal term, and consistent with the redocking control.
**Crucially this does NOT invalidate the selectivity margins:** those use the
*within-ligand* ENPP1-vs-paralog score *difference* (ddG), in which the
ligand-specific systematic errors that sink the absolute-ranking benchmark
largely cancel. It does forbid any cross-chemotype absolute-affinity claim and
sharpens the "directional proxy only" framing. Reporting this negative result
raises credibility rather than lowering it.

### 3. Margins vs the scoring function's intrinsic error — [PARTLY ADDRESSED]
Bootstrap CIs (+/-0.05) capture *seed noise*, not the ~1-2 kcal/mol systematic
error of the scoring function. A +0.12 margin with a tight CI is still inside
docking's accuracy floor. Stated in DISCLAIMER; the redocking result now makes
it concrete. Fully resolving it needs item 2 (calibration) + item 5 (orthogonal
rescore).

### 4. Single protonation / tautomer state — [ADDRESSED this update]
Enumerated all plausible protonation/tautomer states for one lead per warhead
(8 states) and docked each into all three paralogs. Directional selectivity
calls are **sign-robust** across states; magnitudes shift 0.4-1.0 kcal/mol.
See `analysis/validation/PROTOMER_README.md`. Remaining nuance: only three
representative leads tested, not the full set.

### 5. Sulfamide edge rests on 2/4 scoring methods — [OPEN, high value]
Vinardo flips the sign of the small sulfamide margins; the benzotriazole paper
(10.1016/j.ejmech.2026.118666) contradicts the mechanism. A third *orthogonal*
method (MM-GBSA-style endpoint rescore, or a metal-aware protocol) is needed to
break the tie. Until then the developable-lead edge is "directionally
suggestive," which the repo already says.

### 6. Expanded phosphonate screen is single-run — [OPEN, low effort]
The 7-phosphonate generalisation screen used single-seed scores, not the
42-seed bootstrap of the main leads. Add replicate seeds + CIs for parity.

### 7. Rigid receptor, apo ENPP3, no ensemble — [DOCUMENTED, not addressed]
Acknowledged limitation. Would need flexible-sidechain or ensemble docking /
short MD relaxation to close.

### 8. Multiple-comparison discipline — [MINOR]
Many pairwise margins are compared; no explicit correction is discussed. Low
stakes given the directional framing, but a referee may note it.

### 9. FTO is programmatic, not legal — [DOCUMENTED]
Patent xrefs are retrieved from PubChem, not a legal opinion. Already stated.

## What is genuinely solid (defensible as-is)
- 42-seed replicates + 10k-sample bootstrap CIs on the main leads.
- Scoring-*independent* robustness of the hydroxamate anti-selectivity demotion.
- Active-site conservation analysis tying discrimination to specific ENPP2
  switch residues (His->Leu, Ser->Phe) and near-identical ENPP3 pocket.
- Live-retrieved clinical/IP landscape; all literature/patent/trial claims
  grounded in retrieved records, not memory.
- Limitations-first framing; no therapeutic claim; prior work credited.

## Update: three highest-impact items now DONE this session
- Item 1 (cognate redocking control) — done. Pocket + Zn localised; strict
  <2 A not met (no metal term). `analysis/validation/`.
- Item 2 (actives/decoys enrichment) — done. Honest negative: AUC 0.44, absolute
  score uninformative; selectivity ddG survives because errors cancel in the
  within-ligand difference. `analysis/validation/ENRICHMENT_README.md`.
- Item 4 (protonation/tautomer sensitivity) — done. 8 states x 3 paralogs.
  Directional calls (sulfamide ENPP1-leaning; hydroxamate anti-selective vs
  ENPP2 in ALL states; phosphonate anti-selective vs ENPP3 in ALL states) are
  **sign-robust**; magnitudes move 0.4-1.0 kcal/mol — larger than the seed CIs,
  hard evidence for "directional not quantitative." `PROTOMER_README.md`.

These convert unstated assumptions into measured, bounded claims — the single
biggest credibility gain available without a wet lab.

## If you do two more things (ranked by remaining reviewer impact)
1. **Orthogonal rescore (MM-GBSA or metal-aware docking)** of the sulfamide
   leads (item 5) — resolves the one contested directional claim; also the only
   route to a scoring approach that might pass the enrichment test. NOTE: a
   proper endpoint needs explicit di-zinc parameters (AmberTools/OpenMM, not
   installed here) and would inherit the same metal-parameterisation weakness
   the redocking control exposed — so it must be done carefully or it adds a
   method that needs as many caveats as the one it backstops.
2. **Replicate seeds + CIs on the 7-phosphonate expanded screen** (item 6) —
   parity with the main leads; low effort.

None change the honest conclusion; they change whether a referee signs off. With
the redocking, enrichment, and protonation-sensitivity controls now in place,
the repo has moved from "assumes docking works here" to "measured how well it
works and calibrated every claim to that" — the substantive difference between a
data dump and a methods release.
