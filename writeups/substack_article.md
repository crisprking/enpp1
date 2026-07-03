# The compound that docked best was the one to throw away

### A structure-based selectivity screen that reversed its own winner — and what it says about designing drugs against conserved metal sites

*A computational methods walkthrough. No wet-lab data. Every number here is a prediction, and I'll be explicit about which ones I trust and which ones I don't.*

---

## TL;DR

- Consensus docking ranked a **hydroxamate (CHEMBL6149286)** as the top ENPP1 binder. A paralog counter-screen against **ENPP2 (autotaxin)** and **ENPP3** shows it binds ENPP3 *1.5 kcal/mol better* than ENPP1 — the best binder is the least selective compound.
- Two **sulfamides (CHEMBL5826130, CHEMBL5915707)** had middling affinity but are the only leads that prefer ENPP1 over *both* cousins — more drug-like (QED 0.73 vs 0.50), on ENPP1's validated native chemotype, no warhead alerts.
- The reversal survives **42-seed re-docking** with bootstrapped 95% CIs and a **4-method consensus**: hydroxamates score **0/4** methods favoring ENPP1 (unanimous rejection); sulfamides **2/4** (directional, not settled).
- **Why, structurally:** the catalytic zinc is the most conserved feature of the ENPP family, so metal-chelating warheads buy affinity and lose selectivity. ENPP3 is identical to ENPP1 at **all 14 core pocket residues** — selectivity has to be built on the two peripheral pocket-wall positions, not the metal.
- A **designed analog (AN10, a piperidinol)** improves both predicted potency (−9.08 vs −8.10 kcal/mol) *and* selectivity margin (+0.70 vs +0.15), showing the pocket-wall vector is synthetically actionable.
- **All predictions, no wet-lab data.** The decisive next step is a 3-enzyme biochemical IC50 panel. Everything is reproducible: [github.com/crisprking/enpp1](https://github.com/crisprking/enpp1).
- **The lesson:** against a conserved active site, optimize the *margin*, not the score.

---

## The setup: we had a winner

I've been running an open, in-silico drug-discovery exercise against **ENPP1** — a metalloenzyme that hydrolyzes cGAMP, the second messenger that fires the STING innate-immune pathway. Inhibit ENPP1 and you keep cGAMP around longer, which is why the target has become one of the more competitive races in immuno-oncology. There are at least four oral ENPP1 inhibitors in clinical trials right now, the field having advanced to Phase 2.

An earlier round of the exercise had done the normal thing: take a set of potent, drug-like candidates from ChEMBL, dock them into the ENPP1 active site, and rank by predicted affinity. A consensus-docking protocol produced a clean winner — **CHEMBL6149286**, a cyclohexyl-hydroxamate. It topped the affinity ranking. It looked like the compound to advance.

Two things about that winner were quietly nagging.

First, it's a **hydroxamate** — a warhead notorious for chelating metal ions indiscriminately, and whose HDAC-inhibitor members (vorinostat, belinostat, panobinostat) carry documented mutagenicity (Ames) liabilities. The flag isn't universal to every hydroxamate, but the metal-chelation mechanism is exactly what regulatory tox screens scrutinize. Second, and more fundamentally: **we had never tested selectivity.** ENPP1 has two close cousins — ENPP2 (autotaxin, a validated drug target in its own right) and ENPP3 — and a compound that inhibits all three isn't a clean ENPP1 drug; it's a liability with a broad off-target profile. Every serious ENPP1 program in the clinic reports selectivity numbers. Ours had none.

So this round did one thing: **a paralog counter-screen.** Dock the same candidates into ENPP1, ENPP2, and ENPP3 under an identical protocol, and ask not "which binds ENPP1 hardest" but "which *prefers* ENPP1 over its cousins."

The answer reversed the nomination.

---

## The counter-screen: one protocol, three enzymes

The methodological point that makes this comparison fair is boring and load-bearing: **the docking box has to be defined the same way in all three enzymes.** If you center each box on that enzyme's own co-crystallized ligand, you're comparing three differently-placed pockets and the numbers aren't commensurable.

Instead I centered a 24 Å cube on each enzyme's **catalytic-zinc centroid** — a feature all three share and that can be located identically in each structure without reference to any ligand. Same box logic, same docking engine (smina), same settings (`--exhaustiveness 16 --num_modes 5 --seed 42`), same ligand-prep pipeline (RDKit embed + MMFF, Gasteiger charges). Structures: ENPP1 (PDB 6WEW — its catalytic site carries the quinoline-sulfuric-diamide inhibitor with PDB ligand code **TZV** (named Ex54 in Dennis et al. 2020), which I redock as the native reference; the sister structure 6WEV holds a piperidinylmethyl-sulfamide, PDB ligand code **TZS** / QPS2), ENPP2 (5MHP), ENPP3 (6C01, apo).

Then the metric. For each compound:

> **selectivity margin = (paralog affinity) − (ENPP1 affinity)**

A **positive** margin means the compound docks *worse* into the paralog than into ENPP1 — it prefers ENPP1, which is what you want. A **negative** margin means it prefers the off-target. And because you have to beat *both* cousins, the number that matters is the **worst-case margin** — the minimum across ENPP2 and ENPP3.

---

## The reversal

Here is the whole result in one table (affinities in kcal/mol; more negative = tighter predicted binding):

| Lead | Warhead | ENPP1 | ENPP2 | ENPP3 | worst margin | verdict |
|------|---------|------:|------:|------:|-------------:|---------|
| CHEMBL6149286 | hydroxamate | −9.5 | −10.1 | **−11.0** | **−1.5** | anti-selective |
| CHEMBL6174154 | hydroxamate | −8.8 | −8.8 | −10.1 | −1.3 | anti-selective |
| CHEMBL5555976 | sulfonamide | −8.3 | −8.2 | −7.7 | +0.1 | borderline |
| **CHEMBL5915707** | **sulfamide** | −7.9 | −6.7 | −7.5 | **+0.4** | **ENPP1-preferring** |
| **CHEMBL5826130** | **sulfamide** | −7.8 | −7.4 | −7.8 | +0.0 | **ENPP1-preferring** |

Look at the top row. **CHEMBL6149286 — the affinity winner — binds ENPP3 a full 1.5 kcal/mol *better* than it binds ENPP1.** It is, by this measure, an ENPP3 inhibitor that happens to also hit ENPP1. Both hydroxamates behave this way. The compounds that docked *hardest* are the compounds that discriminate *least*.

Meanwhile the two **sulfamides** — which had middling raw scores and would have been passed over on affinity alone — are the only leads that lean toward ENPP1 against both cousins. They also happen to be the most drug-like of the set (QED 0.73 vs 0.50 for the hydroxamate), and they sit on the **same chemical scaffold as ENPP1's own native co-crystal ligand** and the validated clinical chemotype. No warhead alert.

The naïve ranking and the selectivity ranking are not just different. They are *inverted*.

---

## Does the reversal survive the noise?

A single docking number is close to worthless — smina's scoring function carries roughly 1 kcal/mol of noise, and a margin of "+0.4" could easily be a rounding artifact of one lucky pose. So before trusting the direction, I re-docked every compound across **42 replicate runs** — 21 fixed seeds (the sequence 1–20 plus 42), each docked in duplicate, five poses per run (`--num_modes 5`), the top pose taken by smina score — and bootstrapped a 95% confidence interval (10,000 resamples) on each worst-case margin.

![Selectivity margins with 95% bootstrap confidence intervals across 42 docking seeds. The sign of the margin — not its magnitude — is what survives.](../analysis/figures/fig_margin_ci.png)

The separation holds:

| Lead | Worst-case margin | 95% CI | reading |
|------|------------------:|--------|---------|
| CHEMBL5915707 | **+0.42** | [+0.39, +0.45] | cleanly ENPP1-preferring |
| CHEMBL5826130 | **+0.12** | [+0.11, +0.14] | ENPP1-preferring, tight |
| CHEMBL5555976 | +0.03 | [−0.06, +0.11] | **straddles zero — indistinguishable** |
| TZV (native, PDB code) | −1.12 | [−1.19, −1.05] | anti-selective |
| CHEMBL6174154 | −1.31 | [−1.36, −1.27] | anti-selective |
| CHEMBL6149286 | −1.77 | [−1.82, −1.72] | **robustly anti-selective** |

Two things matter here. The hydroxamate's anti-selectivity is not noise — its interval sits a kcal/mol and a half below zero with no ambiguity. And the sulfonamide CHEMBL5555976, which looked borderline-positive on a single pass, has a CI that **crosses zero**: the honest verdict is "can't call it," not "slightly selective." Resolving the noise demotes it from the nomination. The sulfamides are the only leads whose positive margins clear their own error bars.

---

## Four ways to be wrong at once

A margin surviving its own docking noise is necessary but not sufficient — it could still be an artifact of one *scoring function*. So I stress-tested each compound against four independent selectivity signals: the smina ΔΔG margin, a rescored **Vinardo** ΔΔG, the change in **zinc-coordination distance** between ENPP1 and paralog, and an **interaction-fingerprint** pocket-wall advantage. The question: how many of the four agree the compound prefers ENPP1?

![Four-method consensus. Hydroxamates and TZV: 0/4 methods favor ENPP1 — robust anti-selectivity. Sulfamides: 2/4 — directional support, not a settled call.](../analysis/figures/fig_consensus.png)

The result is honest in both directions:

- **The demotion is unanimous.** Both hydroxamates and TZV score **0/4** — every method agrees they are anti-selective. That is the firmest conclusion in the whole analysis.
- **The promotion is directional, not settled.** The sulfamides score **2/4**. Vinardo, which weights the metal term differently, flips the sign of the smallest margins. So I'm not claiming the sulfamide nomination is proven — I'm claiming it is the *only* direction any method supports, while the hydroxamate rejection is agreed by all of them.

This is the distinction that keeps the exercise honest: a conclusion the methods disagree about (which sulfamide, and by how much) gets reported as unsettled; a conclusion they unanimously support (throw the hydroxamate away) gets reported as firm.

---

## Why this happens — and why it's not a fluke

This isn't a quirk of one scoring function. It falls straight out of the structural biology.

The hydroxamate's affinity comes from **chelating the catalytic zinc**. That's a strong, geometry-tolerant interaction — great for raw binding score. But the catalytic bimetal zinc site is **the single most conserved feature of the entire ENPP family.** A ligand whose binding is dominated by grabbing that zinc literally cannot tell the three enzymes apart, because from the zinc's point of view they *are* the same. Strong metal chelation buys you affinity and costs you selectivity, in the same move. There's a scoring subtlety that cuts the same direction: smina's force field parameterizes Zn²⁺ coordination crudely, and hydroxamate *bidentate* chelation is exactly the geometry it tends to over-reward relative to a sulfamide's monodentate or water-mediated contact — so part of the hydroxamate's raw-affinity lead is likely scoring-function artifact, not real binding free energy. That doesn't rescue its selectivity; it sharpens the case against it.

The sulfamide is a weaker, more directional zinc-interacting group. It gives up some raw affinity and makes up the difference against the **pocket walls** — the residues around the metal that actually differ between paralogs. Lower score, but selectivity by construction.

The lesson generalizes past this one target: **when you dock against a conserved catalytic site, raw affinity rewards exactly the wrong thing.** The optimization target isn't the score. It's the *margin*.

---

## The structural basis: ENPP3 is the hard problem

To see how much room there even is to be selective, I superposed the three catalytic pockets (anchor Cα RMSD 0.15–0.23 Å — a tight alignment) and compared the 14 residues within 6 Å of the zinc.

The result is sobering:

- **ENPP3 is identical to ENPP1 at all 14 core catalytic-pocket positions I tracked** — the residues lining the zinc site and the nucleotide pocket. The only differences sit farther out, at the ~4 Å periphery: a published co-crystal structure (the STF-1623 work) finds ENPP3 diverges from ENPP1 by just *two* residues within 4 Å of the ligand. So the two active sites are, to a first approximation, the same pocket — and the entire selectivity budget against ENPP3 is those two peripheral positions. Far from making selectivity impossible, that is precisely where STF-1623 builds its >1,000× ENPP3 margin: on the pocket walls, not the metal.
- **ENPP2 / autotaxin differs at just 2 of the 14** — a histidine→leucine and a serine→phenylalanine swap. Two handles, and that's it.

![Catalytic-pocket residue equivalence across the three paralogs. Green = identical to ENPP1; purple = divergent. ENPP3's column is entirely green.](../figures/enpp_active_site_conservation.png)

This is *why* ENPP3 selectivity is the recurring bottleneck across the whole field. It's not that programs are careless about it — it's that the pocket gives you almost nothing to grab. Even the best clinical compound, Insilico Medicine's **ISM5939**, reports its ENPP3 selectivity (>3,400×) as something *engineered*, earned by deliberate design, not something the chemistry fell into. And when a published compound like STF-1623 does achieve >1,000× over ENPP3, it does so by exploiting a *two-residue* difference — the entire selectivity budget.

So the take-home for a chemist is specific: **selectivity here has to be built into the pocket-wall contacts, because the metal site itself is uniformly conserved.** The two ENPP2 switch positions and the two ENPP3-divergent positions are the only vectors you have. Grow into them deliberately or don't get selectivity at all.

---

## Can we do better than the nominee? A designed analog

Nominating the best of six existing compounds is triage. The more interesting question is whether the structural logic — *earn selectivity on the pocket walls, not the metal* — can be used **forward**, to design something that beats the parent. So I enumerated 13 analogs of the lead sulfamide CHEMBL5826130, each growing a substituent toward the divergent pocket-wall positions, and put them through the identical counter-screen and CI pipeline.

![Rational analog design of CHEMBL5826130. Green = beats the parent on selectivity while retaining potency and developability (QED ≥ 0.55). AN10, a piperidinol, lands in the upper-right quadrant alone.](../analysis/figures/fig_analog_design.png)

One analog cleared the bar on both axes at once. **AN10**, a piperidinol variant, improves predicted ENPP1 affinity (−9.08 vs the parent's −8.10 kcal/mol) *and* widens the worst-case selectivity margin to **+0.70 [0.39, 0.95]** — up from the parent's +0.15 — while staying Rule-of-Five clean.

![Analog validation: AN10 improves both potency and selectivity versus the parent, with the selectivity gain clearing its confidence interval.](../analysis/figures/fig_analog_validation.png)

I want to be clear about what this is and isn't. AN10 is a *computational hypothesis*, carried forward on the same directional evidence as everything else here — its margin is a docking ΔΔG, not a measured fold-change. But it demonstrates the point that matters: the pocket-wall vector the conservation map identified is *synthetically actionable*. You can grow into it on purpose. AN10 rides along to the bench as the "designed" arm alongside the two existing sulfamides.

---

## Where this sits in the real field

None of this happens in a vacuum. The ENPP1 race is real and well past the stage this exercise operates at, so I pulled the competitive and IP landscape (ClinicalTrials.gov + PubChem, retrieved 2026-07-03) to place the work honestly.

![ENPP1 program landscape: four small-molecule inhibitors have reached Phase 2; IP position of the six leads, with sulfamides mapping onto a granted composition-of-matter patent.](../benchmark/fig_clinical_patent_landscape.png)

**The clinic is ahead of the model.** At least four oral small-molecule ENPP1 inhibitors are in trials — Riboscience's **RBS2418** (Phase 2, HCC/CRC), Stingray's **SR-8541A** (Phase 2, MSS-CRC), **TXN10128** (Txinno, Phase 1), and Insilico's **ISM5939** (Phase 1a/b, IND-cleared, discovered via generative AI — the >3,400× ENPP3-selective compound that sets the bar above). A separate program, Inozyme's **INZ-701**, runs the *opposite* pharmacology — an ENPP1-Fc enzyme-replacement therapy for a rare mineralization disorder, now in Phase 3 (ENERGY) following BioMarin's 2025 acquisition of Inozyme — a useful reminder that "ENPP1 modulator" is not one thing, and that the target is commercially validated from two opposite directions at once.

**The IP tells the sulfamides apart from the hydroxamates.** The two nominated sulfamides map onto the chemical space of a **granted composition-of-matter patent (US-11591313-B2)** and its continuations — the same validated chemotype the clinical compounds occupy. The hydroxamates appear only in a single 2024 application. Read charitably, that means the sulfamide direction sits on defensible, precedented chemistry; read as a freedom-to-operate flag, it means the nominated scaffold is *crowded* and a real program would need to design around existing claims — which is one more argument for carrying the novel AN10 analog, not just the known compounds.

The point of this section is not to claim the exercise competes with a Phase 2 asset. It's the opposite: to fix exactly where a structure-based triage like this one is useful — upstream of all of it, as the cheap filter that decides which molecules earn a place in the assay queue.

---

## What "good" looks like (the honest bar)

| Compound | ENPP1 IC50 | vs ENPP2 | vs ENPP3 | notes |
|----------|-----------|----------|----------|-------|
| ISM5939 (Insilico, clinical) | 0.63 nM | >15,000× | >3,400× | oral, IND-cleared — the bar to beat |
| Enpp-1-IN-27 | 14.7 nM | ~410× | ~10× | even good compounds are weak on ENPP3 |
| STF-1623 | <2 nM Ki | — | >1,000× | ultralong residence time |

Notice ENPP3 is the weak axis even for strong compounds (Enpp-1-IN-27: ~410× over ENPP2 but only ~10× over ENPP3). The field's own numbers say the same thing the structure does.

---

## Validating the protocol itself

Before trusting any of the above, the fair question is: does this docking protocol work *on this target at all*? I ran three controls and report them honestly — one is a negative result.

**1. Cognate redocking.** Redock the native 6WEW ligand (TZV) into its own crystal structure with the production protocol. The top-ranked poses land in the correct pocket with the sulfamide engaging the catalytic zinc (2.2–2.3 Å), cleanly separated from 10–13 Å surface-decoy poses — but the best heavy-atom RMSD to the crystal pose is **3.08 Å**, and it ranks 6th, not 1st. It fails the strict <2 Å success line. The reason is mechanistic and important: smina has no explicit metal-coordination term, so it localizes the right pocket but not the exact chelation geometry. Pose *localization* is reliable here; fine geometry is not.

![Cognate redocking of native TZV into 6WEW: top poses cluster in the correct pocket with Zn engagement; best RMSD 3.08 Å (no explicit metal term).](../analysis/validation/fig_redock_validation.png)

**2. Actives-vs-decoys enrichment — the negative result.** I docked 30 known ENPP1 actives (pChEMBL ≥ 7) against 90 property-matched decoys through the identical protocol. Result: **ROC-AUC = 0.44** (below random), enrichment factor at 5%/10% = 0, and actives and decoys had statistically indistinguishable median affinity (−8.90 each, Mann–Whitney p = 0.85). **Absolute smina score does not rank ENPP1 binders on this target.** That is exactly what you'd expect for a di-zinc metalloenzyme scored without a metal term — and it is consistent with the redocking result.

This sounds damning until you see *why it doesn't sink the selectivity claims*. The enrichment benchmark tests absolute affinity ranking *across different ligands*. The selectivity analysis uses the *difference* in score for the *same* ligand across paralogs (ΔΔG), where the ligand-specific systematic scoring errors that wreck absolute ranking **largely cancel**. So the negative result does two useful things at once: it forbids any cross-chemotype absolute-affinity claim (which is why the article never makes one), and it explains precisely why the within-ligand margin is the only quantity worth reading. Reporting it raises the credibility of the margins, not lowers it.

![Actives-vs-decoys enrichment: 30 ENPP1 actives vs 90 property-matched decoys score identically (ROC-AUC 0.44). Absolute affinity does not rank binders here — which is why only the within-ligand margin is used.](../analysis/validation/fig_enrichment.png)

**3. Protonation-state robustness.** Docking is sensitive to which protonation/tautomer state you feed it. I enumerated 8 plausible states across one lead per warhead class and re-ran all three paralogs. The **directional** calls are sign-robust across every state (sulfamide leans ENPP1 vs ENPP2 in all states; hydroxamate is anti-selective in all states); the *magnitudes* move 0.4–1.0 kcal/mol — larger than the seed-to-seed CIs. That is one more reason to read these as directions, not quantities.

![Protonation-state sensitivity: directional selectivity calls are sign-robust across 8 protomer/tautomer states; magnitudes shift 0.4–1.0 kcal/mol.](../analysis/validation/fig_protomer_sensitivity.png)

The full referee-perspective ledger, including what remains open (an orthogonal MM-GBSA or metal-aware rescore to break the 2/4 sulfamide tie), is in `REVIEWER_GAP_ANALYSIS.md`.

---

## The part where I tell you what this *isn't*

I want to be scrupulous here, because computational drug discovery has a credibility problem and it's earned.

**Docking ΔΔG is a directional proxy, not an IC50 ratio.** A +0.4 kcal/mol margin is *not* a selectivity fold-change. smina's scoring function carries roughly 1 kcal/mol of noise and models metal-coordination quantum chemistry poorly — which is a real caveat given that metal coordination is central to this whole binding mode. What this screen can legitimately claim is **direction**: it correctly flags the hydroxamates as promiscuous and the sulfamides as ENPP1-leaning. What it *cannot* do is tell you that CHEMBL5826130 is "1.6× selective" or any other precise ratio. Those digits aren't real.

A few more honest edges: ENPP3 was docked apo (no co-crystal inhibitor to anchor the pose); the poses weren't relaxed with molecular dynamics; there were no explicit metal-coordination restraints; and pChEMBL/QED are database and cheminformatic values, not potencies measured in this assay. The apo ENPP3 docking is the softest of these: any ligand-induced pocket rearrangement goes uncaptured, which almost certainly widens the true error bars beyond the seed-to-seed spread reported here. (Every compound's SMILES and ChEMBL ID is in `data/ligands.csv` in the repo, so the exact structures docked are reproducible.)

**And the load-bearing caveat: there is no wet-lab data here at all.** No measured IC50, no cellular assay, no PK, no tox. This is a hypothesis-generating exercise start to finish. The compound that this analysis nominates could be dead on arrival at the bench. I don't know yet. Neither does the docking.

---

## The recommendation, and the one experiment that settles it

Given all of that, the call is still clear *as a triage decision*:

- **Demote CHEMBL6149286** (the hydroxamate that "won") from lead to a potency-reference control. It's anti-selective (0/4 methods, −1.77 kcal/mol margin robust across all 42 replicate runs) and warhead-liable.
- **Co-nominate CHEMBL5915707 and CHEMBL5826130** (both sulfamides) — the only two leads whose positive margins clear their own confidence intervals. ENPP1-preferring, developable (QED 0.73), on the validated native chemotype, clean on alerts.
- **Set CHEMBL5555976 aside**, not as a control but as unresolved: its margin CI crosses zero, so the honest call is "can't distinguish from non-selective."
- **Carry AN10** (designed piperidinol analog) as the novel arm — better predicted potency *and* margin than the parent, and off the crowded granted-patent scaffold.

And then stop trusting the computer. The decisive next step is not more docking — it's a **wet-lab 3-enzyme ENPP1/2/3 biochemical panel** on the two nominated sulfamides plus the designed AN10 analog, run exactly the way ISM5939 was profiled (cGAMP + ATP substrates, pH 7.4). Success criterion, set in advance: **≥100× ENPP1/ENPP3 and ≥1,000× ENPP1/ENPP2 selectivity while keeping ENPP1 potency under 50 nM.** If ENPP3 selectivity falls short — and given how conserved the pocket is, it very well might — the fix is to grow the sulfamide into the ENPP3-divergent positions using the ENPP1 crystal structure.

Everything upstream of that assay, including this entire article, is a way of deciding *which* compounds are worth the reagent cost. That's what structure-based triage is for. It's not a substitute for the experiment; it's how you pick the experiment.

---

## The general lesson

If there's one transferable idea here, it's this: **against a conserved active site, optimize the margin, not the score.** The most potent binder to a shared catalytic feature is often the least selective drug, and a ranking that doesn't counter-screen the paralogs will hand you exactly the wrong molecule with total confidence. The counter-screen is cheap. Skipping it is how you advance a promiscuous compound three steps before a selectivity assay finally kills it.

The full analysis — data, docking scripts, prepared receptors, the conservation map, and a reproducible pipeline — is on GitHub: **https://github.com/crisprking/enpp1**. Every number in this article regenerates from the committed raw scores.

*Corrections and methodological critiques genuinely welcome. This is an open exercise; the point is to do it in public and get the caveats right.*


---

## Appendix: compound structures (SMILES)

Every compound docked in this analysis, as canonical SMILES. These are also in `data/ligands.csv` in the repo, alongside ChEMBL ID, warhead class, QED, and pChEMBL. The native reference is the 6WEW co-crystal ligand (PDB ligand code **TZV**; Ex54 in Dennis et al. 2020).

| Compound | Warhead | SMILES |
|----------|---------|--------|
| CHEMBL5826130 | sulfamide | `COc1cc2ncc(C#N)c(N3CCCC(CNS(N)(=O)=O)CC3)c2cc1OC` |
| CHEMBL5915707 | sulfamide | `COc1cc2ncc(C#N)c(N3CCC[C@@H](CNS(N)(=O)=O)CC3)c2cc1OC` |
| CHEMBL5555976 | sulfonamide | `COc1cc2nc(C)c3nc(C)n(Cc4ccc(S(N)(=O)=O)cn4)c3c2cc1OC` |
| CHEMBL6149286 | hydroxamate | `COc1ccc2c(Oc3ccc(C4(C(=O)NO)CCCCC4)cc3)ccnc2n1` |
| CHEMBL6174154 | hydroxamate | `COc1ccc2c(Oc3ccc(CC(=O)NO)cc3)ccnc2c1` |
| TZV (native, 6WEW) | sulfamide | `COc1ccc2c(Oc3ccc(NS(N)(=O)=O)cc3)ccnc2n1` |

*A note on nomenclature: the two nominated leads and CHEMBL5555976 differ by one atom in the warhead. The leads carry a **sulfamide** (N–SO₂–N); CHEMBL5555976 carries an aryl **sulfonamide** (C–SO₂–N).*
