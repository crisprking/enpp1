# Extended analysis: statistical rigor, mechanism, and analog design

This directory extends the headline counter-screen (`../README.md`) with four
orthogonal analyses that stress-test the nomination beyond a single docking
score, plus a rational analog-design campaign. **Everything here is still
in-silico** — the disclaimer in the root README applies in full.

## Why this exists

The headline result ranks six ligands by a single-seed smina score. Three fair
criticisms of that: (1) docking is stochastic, so is the ranking real or noise?
(2) a docking score is one opaque number — what is the *physical* basis of the
selectivity? (3) is the winner robust to the scoring function? These analyses
answer each, and then ask the forward question: can the margin be *widened* by
design?

## The analyses

### 1. Statistical replicates + bootstrap — `data/replicate_scores.csv`, `data/margin_confidence_intervals.csv`
Every ligand×target was docked with **42 independent seeds** (1–20, 42).
Figure `figures/fig_margin_ci.png`.
- Seed-to-seed SD: **0.05–0.29 kcal/mol** (median 0.08) — the empirical docking
  noise floor for this system.
- 95% bootstrap CIs (10k resamples) on each worst-case paralog margin. A verdict
  is only assigned when the CI excludes zero.
- **Result:** hydroxamates significantly **anti-selective** (CIs well below 0);
  both sulfamides significantly **ENPP1-preferring** (+0.42 and +0.12, CIs above
  0); sulfonamide **indistinguishable** from 0. The earlier "+0.0" ambiguity for
  CHEMBL5826130 is resolved to a small but significant +0.12.

### 2. Metal-coordination geometry — `data/zn_coordination_distances.csv`
Closest ligand-atom-to-catalytic-Zn distance per best-mode pose.
Figure `figures/fig_zn_mechanism.png`.
- **Mechanism of anti-selectivity, measured:** hydroxamates + native TZV directly
  coordinate the **ENPP3** zinc (1.74–2.23 Å = true metal bonds) but sit 3.2–3.5 Å
  away in ENPP1. Sulfamides never make a tight metal contact anywhere (2.7 Å in
  ENPP1, drifting to 4.5–6.0 Å in paralogs) → their affinity is **pocket-wall
  derived**, i.e. tunable for selectivity. This is the physical "why" behind the
  ranking flip.

### 3. Per-residue interaction fingerprints — `data/interaction_fingerprints.csv`
Contact classification (metal ≤2.8 Å, H-bond ≤3.5 Å, hydrophobic ≤4.5 Å,
aromatic ≤5.0 Å) against the correctly-numbered receptor PDBs.
Figure `figures/fig_ifp_heatmap.png`.
- Nominee **CHEMBL5826130 contacts 7 ENPP1 pocket residues vs 4 (ENPP2) and 2
  (ENPP3)** — the only lead engaging more ENPP1 wall residues than *either*
  paralog. Energy-independent corroboration of the nomination.

### 4. Consensus (second scoring function) — `data/vinardo_rescore.csv`, `data/consensus_selectivity.csv`
Best-mode poses rescored with smina's **Vinardo** function; combined with
smina ΔΔG, Zn-distance Δ, and IFP wall-advantage into a 4-method vote.
Figure `figures/fig_consensus.png`.
- Hydroxamates + TZV: **0/4 methods favor ENPP1** — anti-selectivity robust
  across scoring functions.
- Sulfamides: **2/4** — smina + structural signals lean ENPP1, but **Vinardo
  flips the sign** of the small margins. Reported honestly: the *demotion* is
  scoring-function-robust; the *promotion* is directional, not settled.

### 5. Rational analog design — `data/analog_library.csv`, `data/analog_selectivity_results.csv`
13 analogs of CHEMBL5826130 designed to grow into the **ENPP2 switch residues**
(His260→Leu214, Ser377→Phe313), preserving the quinoline-carbonitrile core and
sulfamide warhead. All 13 are Ro5-compliant. Re-docked across all three paralogs
(seed 42, exhaustiveness 16); top hits validated with a focused multi-seed
replicate (`analog_focused_scores.csv`, `rep_analogs_focused.sh`).
- Several analogs improve the *predicted* worst-case margin over the parent while
  retaining ENPP1 potency and QED — a concrete, synthesizable next iteration.
  **These are predictions to be assayed, not conclusions.**

**Multi-seed validation of the top analogs** (`data/analog_focused_ci.csv`,
`figures/fig_analog_validation.png`; 15 seeds × 3 targets, bootstrap 10k). The
standout **AN10_piperidinol** (3-hydroxy-piperidine) survives replication on both
axes: predicted ENPP1 affinity **−9.08** (parent −8.10, ~1 kcal/mol gain) and
worst-case margin **+0.70 [0.39, 0.95]** (parent +0.15 [0.08, 0.22]) — the CI
excludes zero, so the selectivity gain is resolved above docking noise. AN11_fluoro_pip
also holds a positive worst-margin (+0.45 [0.42, 0.47]) but shows no potency gain
over parent. One honest caveat: AN10's ENPP1 pose has higher seed-to-seed spread
(SD 0.55 vs parent 0.00), i.e. more pose variability, so the mean affinity is
less certain than the parent's despite being lower.

## Reproduce

```bash
# replicate campaign (long: 6 ligands × 3 targets × 21 seeds)
bash scripts/run_replicates.sh data/replicate_scores.csv
# focused analog replicate (3 analogs × 3 targets × 15 seeds)
bash scripts/rep_analogs_focused.sh data/analog_focused_scores.csv
# bootstrap CIs, Zn distances, fingerprints, consensus, figures
python scripts/run_analysis.py
```

## Caveats specific to this directory
- CIs quantify **docking reproducibility**, not experimental uncertainty. A tight
  CI means the *predictor* is stable, not that the *prediction* is correct.
- The +0.1 to +0.4 kcal/mol sulfamide margins are statistically resolved but
  **pharmacologically small** — direction, not fold-selectivity. The literature
  bar (ISM5939: >3,400× ENPP3) needs med-chem margin optimization, which is what
  analysis (5) begins.
- Analog docking inherits every limitation of the parent screen (apo ENPP3, no
  MD relaxation, no QM metal treatment).
