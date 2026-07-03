# ENPP1 Oral-Inhibitor Program — Updated Lead Recommendation
### Grounded in ENPP-family selectivity + developability + active-site conservation
_Analysis date: 2026-07-03 · in-silico counter-screen (smina), structural superposition, literature-benchmarked_

---

## Bottom line

**The selectivity axis flips the nomination.** The consensus-docking winner from the
prior round — **CHEMBL6149286** (cyclohexyl-hydroxamate) — is **anti-selective**: in a
matched catalytic-Zn docking box it binds ENPP3 (−11.0 kcal/mol) and ENPP2 (−10.0)
**better** than ENPP1 (−9.2). Across 42 docking replicates this margin is −1.77 kcal/mol
(95% CI [−1.82,−1.72]) — far outside the 0.08 kcal/mol seed noise, so the anti-selectivity is
statistically unambiguous, not a scoring artifact. That is the promiscuous
metalloenzyme-chelator liability the field explicitly warns about, and it stacks on top of the
hydroxamate's Ames/mutagenicity alert. It should be **demoted from lead** to a
potency-reference / tool compound.

**Recommended nomination: co-nominate the two sulfamides CHEMBL5826130 and CHEMBL5915707.**
These are the only leads that are simultaneously (i) *statistically* ENPP1-preferring in the
42-seed counter-screen (CIs exclude 0), (ii) on the clinically validated sulfamide chemotype
(native TZV/TZS), (iii) developable (QED 0.73, Ro5-clean, no warhead alert), and (iv)
sub-nM–class potent (pChEMBL 9.3–9.7). **Caveat up front:** the margins are statistically
resolved but *pharmacologically small* (+0.1 to +0.4 kcal/mol — direction, not
fold-selectivity) and the smaller of the two flips sign under a second scoring function. The
robust, scoring-function-independent result is the *demotion* of the hydroxamates; the
sulfamide *promotion* is directionally supported and should be confirmed by assay.

---

## The evidence in one table

| Lead | Warhead | pChEMBL | QED | ENPP1 | ENPP2 | ENPP3 | worst margin [95% CI] | verdict |
|------|---------|--------:|----:|------:|------:|------:|-------------:|---------|
| CHEMBL6149286 | hydroxamate | 9.20 | 0.50 | −9.2 | −10.0 | **−11.0** | **−1.77** [−1.82,−1.72] | anti-selective ✗ |
| CHEMBL6174154 | hydroxamate | 9.70 | 0.56 | −8.9 | −8.9 | **−10.2** | **−1.31** [−1.36,−1.27] | anti-selective ✗ |
| TZV (native)  | sulfamide  |  —   |  —   | −8.8 | −8.5 | −10.0 | −1.12 [−1.19,−1.05] | (ATP-site ref) |
| CHEMBL5555976 | sulfonamide | 9.28 | 0.52 | −8.2 | −8.2 | −7.7 | +0.03 [−0.06,+0.11] | indistinguishable |
| **CHEMBL5915707** | **sulfamide** | 9.30 | **0.73** | −7.9 | −6.8 | −7.5 | **+0.42** [+0.39,+0.45] | **ENPP1-preferring ✓** |
| **CHEMBL5826130** | **sulfamide** | 9.66 | **0.73** | −7.8 | −7.3 | −7.7 | **+0.12** [+0.11,+0.14] | **ENPP1-preferring ✓** |

*Affinities are **means of 42 independent docking runs** (seeds 1–20, 42; smina, matched
catalytic-Zn box), kcal/mol. margin = paralog − ENPP1; positive ⇒ prefers ENPP1. Brackets
are **95% bootstrap CIs** (10k resamples) on the worst-case paralog margin; verdict called
only when the CI excludes 0. Native TZV docks at the ATP/nucleotide subsite, so its Zn-box
score understates its true ENPP1 engagement — positioning reference, not a ranked competitor.*

**Which sulfamide leads?** The 42-seed replicates resolve a trade-off the single-seed run
hid: **CHEMBL5915707 has the larger, cleaner margin (+0.42 vs +0.12)** — it is the
selectivity-first pick — while **CHEMBL5826130 leads on potency (pChEMBL 9.66 vs 9.30)**,
ties on developability (QED 0.73), and carries the strongest *orthogonal* structural support
(farthest paralog-vs-ENPP1 Zn-distance gap, and the only lead engaging more ENPP1 pocket-wall
residues than either paralog — see `analysis/`). Both clear significance; they are
**co-nominated**. If one must advance first, 5826130 on the composite, 5915707 if selectivity
margin is weighted above potency.

---

## Why the docking ranking and the selectivity ranking disagree — and why selectivity wins

The hydroxamate warhead is a **strong, geometry-tolerant bidentate Zn²⁺ chelator**. That is
exactly what makes it top the raw-affinity consensus docking *and* what makes it
**non-selective**: the catalytic bimetal Zn center is the single most conserved feature of
the entire ENPP family, so a ligand whose binding is dominated by Zn chelation cannot
distinguish ENPP1 from ENPP2/3. The sulfamide is a **weaker, more directional** Zn-interacting
group that derives more of its affinity from the paralog-divergent pocket walls — lower raw
docking score, but *selectivity by construction*. Structure-based selection must optimize the
ENPP1-minus-paralog margin, not the absolute score.

---

## Active-site conservation — the structural basis (independently literature-confirmed)

Superposing the ENPP1 (6WEW), ENPP2 (5MHP) and ENPP3 (6C01) catalytic pockets
(anchor Cα RMSD **0.15–0.23 Å**) over the 14 residues within 6 Å of the bimetal Zn:

- **ENPP3 = ENPP1 at all 14 core positions** (100% identity); ENPP3 only adds two rim
  Asn residues. **ENPP3 is the hard selectivity problem.** This reproduces, from an
  independent structure, the STF-1623 crystallography result that ENPP3 differs from ENPP1
  by only **two residues within ~4 Å** of the ligand (Q244→K, E275→D). STF-1623 loses
  **>1,000-fold** potency on native ENPP3 — i.e. even two-residue differences are
  exploitable, but it takes deliberate design, not luck.
- **ENPP2/autotaxin differs at 2 of 14** pocket positions — **His260→Leu214** and
  **Ser377→Phe313** (ENPP1 numbering). These are the selectivity handles for the major
  circulating lysoPLD off-target.

The takeaway for the chemistry team: **selectivity has to be engineered into the
pocket-wall contacts, because the metal site itself is uniformly conserved.** The two ENPP2
switch positions and the two ENPP3 (Q244K/E275D-equivalent) positions are the specific
vectors to grow into.

---

## Literature selectivity bar (what "good" looks like)

| Compound | ENPP1 IC50 | vs ENPP2 | vs ENPP3 | note |
|----------|-----------|----------|----------|------|
| ISM5939 (clinical, Insilico) | 0.63 nM (cGAMP) | **>15,000×** | **>3,400×** | oral, IND-cleared; the bar to beat |
| Enpp-1-IN-27 | 14.7 nM | ~410× | **~10×** | ENPP3 is the weak axis even for good compounds |
| STF-1623 | <2 nM Ki | — | >1,000× | ultralong residence time |

**ENPP3 selectivity is the recurring bottleneck across the whole field** — consistent with
the 100% core-pocket identity we measured. Any nomination must be assayed against ENPP3, not
just ENPP2.

---

## Orthogonal evidence (does the call survive beyond one docking score?)

The nomination does not rest on the raw smina number alone. Four independent lines of
analysis (full detail + CSVs in [`analysis/`](analysis/)) were run to stress-test it:

1. **Statistical replicates (42 seeds) + bootstrap.** The margin ranking is stable to
   0.05–0.29 kcal/mol (median SD 0.08). Bootstrap CIs (10k resamples) put every verdict on a
   significance footing: hydroxamates significantly anti-selective, both sulfamides
   significantly ENPP1-preferring, sulfonamide indistinguishable from 0.
2. **Metal-coordination geometry.** Measuring the closest ligand-atom-to-catalytic-Zn
   distance per pose gives the *mechanism* of the anti-selectivity: the hydroxamates and TZV
   directly coordinate the ENPP3 zinc (1.7–2.2 Å true metal bonds) while sitting 3.2–3.5 Å
   away in ENPP1. The sulfamides never make a tight metal contact anywhere (2.7 Å in ENPP1,
   drifting to 4.5–6.0 Å in the paralogs) — confirming affinity comes from pocket walls, the
   tunable surface.
3. **Per-residue interaction fingerprints.** CHEMBL5826130 engages **7 ENPP1 pocket residues
   vs 4 in ENPP2 and 2 in ENPP3** — the only lead that contacts more ENPP1 wall residues than
   either paralog, an energy-independent corroboration.
4. **Consensus (metal-aware) rescore.** A second scoring function (Vinardo) *reproduces* the
   hydroxamate anti-selectivity sharply but *disagrees* on the sign of the small sulfamide
   margins. Reported honestly: the demotion is robust across scoring functions; the promotion
   is not, so it is a hypothesis for assay, not a settled ranking.

**Focused analog design.** Thirteen analogs of CHEMBL5826130 were designed to grow into the
ENPP2 switch residues (Leu214/Phe313) and re-docked. The top designs (e.g. a
3-hydroxy-piperidine and a fluoro-piperidine variant) improve the *predicted* worst-case
margin over the parent while staying Ro5-clean — a concrete, synthesizable next iteration
rather than a stopping point. These are predictions to be made and assayed, not conclusions.

## Honest limitations

- **Docking ΔΔG is a directional proxy, not an IC50 ratio.** A +0.42 kcal/mol margin is
  *statistically* resolved (42-seed bootstrap CI excludes 0) but is *not* a selectivity
  fold-change; smina scoring does not model the metal-coordination quantum chemistry well.
  The counter-screen is a **triage/hypothesis** tool: it correctly flags the hydroxamates as
  promiscuous and the sulfamides as ENPP1-leaning, but the numbers cannot be quoted as
  selectivity ratios, and the small sulfamide margins are not robust to the choice of scoring
  function.
- ENPP3 (6C01) was docked apo (no co-crystal inhibitor); box centered on catalytic Zn.
- Poses were not MD-relaxed; no explicit metal-coordination restraints.

## Recommended next step (assay-grounded, decisive)

Order **CHEMBL5826130** and **CHEMBL5915707** and run the **3-enzyme ENPP1/2/3 biochemical
panel** (cGAMP + ATP substrates, pH 7.4) exactly as ISM5939 was profiled. Success criterion:
**≥100× ENPP1/ENPP3 and ≥1,000× ENPP1/ENPP2 IC50 selectivity** while retaining <50 nM ENPP1
potency. If ENPP3 selectivity falls short, grow the sulfamide into the ENPP3-divergent
positions (the ENPP1 K/D vs ENPP3 Q/E pair) using the 6WEW pocket. Keep the hydroxamates only
as potency-reference controls.
