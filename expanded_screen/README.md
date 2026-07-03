# Expanded generalization screen — 7 phosphonate ENPP1 inhibitors

**Question.** Does the warhead→selectivity pattern from the main 6-lead screen
(metal-chelating warheads lose ENPP3 selectivity; pocket-wall binders keep it)
generalize to a *different, more potent* chemotype?

**Design.** Seven additional public ENPP1 inhibitors (pChEMBL 9.18–10.05,
grounded live from ChEMBL) — which all turned out to be **phosphonates**, a
fourth warhead class beyond the original sulfamide/sulfonamide/hydroxamate set —
were docked with the identical protocol (same receptors, matched catalytic-Zn
boxes, smina). `phosphonate_selectivity_scorecard.csv` holds the per-compound
margins; `phosphonate_ligands.csv` the grounded properties.

## Result (`fig_phosphonate_selectivity.png`)

The structural thesis holds:

- **ENPP2 discrimination is broadly attainable** — mean margin **+0.80 kcal/mol**,
  ≥0 for all 7 compounds. The two ENPP2 switch residues (His→Leu, Ser→Phe) are
  exploitable by many chemotypes.
- **ENPP1-vs-ENPP3 discrimination is hard** — mean **−0.21 kcal/mol**, with
  **3 of 7 anti-selective**. The pocket ENPP3 shares with ENPP1 defeats
  metal-engaging warheads.
- **Potency does not rescue the hard axis.** The most potent compound in the
  entire program, **CHEMBL5566114 (pChEMBL 10.05)**, is anti-selective vs ENPP3
  (margin −0.5).

This independently reproduces the central finding on a chemotype the original
screen never touched: the conserved di-zinc pocket, not raw affinity, sets the
ENPP3 selectivity ceiling.

> Single-seed scores (generalization screen); the headline 6-lead margins use the
> full 42-seed bootstrap. See `../REVIEWER_GAP_ANALYSIS.md` item 6.
