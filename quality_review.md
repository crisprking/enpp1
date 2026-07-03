# Self-review: what this repo does and does not establish

An honest, adversarial assessment of the ENPP-family selectivity counter-screen,
written to the same bar a skeptical reviewer would apply. This is shipped *with*
the work deliberately: the value of an in-silico triage is only as good as its
stated limits.

## Novelty — calibrated

- **As drug discovery:** LOW. The leads are known ChEMBL compounds, the targets
  are solved structures, and docking-based paralog counter-screening is standard
  practice. Nothing here is a new molecule or a new binding mode.
- **As open methods:** MODERATE. The contribution is a *fully reproducible,
  limitations-first, statistically-controlled* paralog-selectivity workflow with
  the mechanism made explicit (metal-coordination geometry), an orthogonal
  4-method consensus, and a self-critique. Packaging rigor of this kind is
  uncommon in public repos, even if each individual technique is textbook.

## Grading by testable dimension

| Dimension | Grade | Basis |
|-----------|:-----:|-------|
| Honesty / limitations | A | Disclaimer up front, no IC50 claims, caveats co-located with results |
| Reproducibility (scorecard) | A− | `build_scorecard.py` + `run_analysis.py` regenerate every table/figure from committed CSVs |
| Provenance | A− | Every lead traced to ChEMBL ID + pChEMBL; structures to PDB ID |
| Packaging | A− | License, citation, contributing, metadata, requirements all present |
| Statistical rigor | A− | **42-seed replicates + bootstrap CIs** (was C at n=1) |
| Reproducibility (full re-dock) | B | `dock_all.sh` needs receptor `.pdbqt` (prep step documented, files not committed for size) |
| Structural scope | B− | 6 Å pocket panel cannot see ENPP3 divergent rim residues; apo ENPP3 |
| Internal consistency | A− | **Nomination now matches scorecard verdict** (was C — see below) |

## The defect we found and fixed

An earlier version labeled CHEMBL5826130 "ENPP1-preferring ✓" while its own
scorecard listed a worst-case margin of **+0.0** — the label contradicted the
number, and the nomination was implicitly driven by potency (pChEMBL 9.66) over
the selectivity margin the project exists to measure. The fix:
1. **Replicates resolve the ambiguity.** With 42 seeds the margin is +0.12
   [+0.11, +0.14] — small but statistically significant, so the verdict is now
   *earned* rather than asserted.
2. **Co-nomination with honest trade-off.** CHEMBL5915707 has the larger, cleaner
   margin (+0.42); CHEMBL5826130 leads on potency and structural corroboration.
   Both are named, and the trade-off is stated rather than hidden.
3. **The robust claim is the demotion.** The scoring-function-independent,
   large-effect result is that the hydroxamates are anti-selective. The sulfamide
   promotion is directionally supported but not robust to the Vinardo rescore —
   and we say so.

## What would move the grades

- **Full re-dock reproducibility → A:** commit receptor `.pdbqt` files or a
  `prepare_receptors.sh` that regenerates them deterministically.
- **Structural scope → A:** MD relaxation of the apo ENPP3 pocket; a wider shell
  to capture rim divergence; an induced-fit or ensemble dock.
- **Selectivity claim → confirmed:** the only real fix is a wet-lab ENPP1/2/3
  enzyme panel. Everything here is a *prioritization hypothesis* for that assay.

## One-line verdict

A rigorously packaged, honestly bounded in-silico **triage** that correctly and
robustly *demotes* a promiscuous chelator and *directionally* promotes a
developable sulfamide chemotype — useful for prioritization, not a substitute for
assay.
