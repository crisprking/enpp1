# The compound that docked best was the one to throw away

*A structure-based selectivity screen that reversed its own winner. Computational methods, no wet-lab data — every number below is a prediction.*

---

I've been running an open in-silico drug-discovery exercise against **ENPP1**, the enzyme that degrades cGAMP and dampens STING innate-immune signaling — one of the more competitive targets in immuno-oncology, with multiple oral inhibitors in trials and the lead programs at Phase 2.

An earlier round did the obvious thing: dock a set of potent, drug-like ChEMBL candidates into ENPP1 and rank by affinity. It produced a clean winner — **CHEMBL6149286**, a cyclohexyl-hydroxamate. Top score. Looked like the one to advance.

Two things nagged. It's a hydroxamate — a warhead known for indiscriminate metal chelation, and whose HDAC-inhibitor members carry Ames liabilities. And we'd **never tested selectivity** against ENPP1's two close cousins, ENPP2 (autotaxin) and ENPP3. A compound that hits all three isn't a clean drug.

So this round ran the counter-screen.

**The method.** Dock into all three enzymes with an identical box centered on the **catalytic zinc** they all share — same engine (smina), same settings, same ligand prep — so the numbers are commensurable. Metric: *selectivity margin = paralog affinity − ENPP1 affinity*. Positive means the compound prefers ENPP1. You have to beat both cousins, so the worst-case margin is what counts.

**The reversal.**

| Lead | Warhead | ENPP1 | ENPP2 | ENPP3 | worst margin |
|------|---------|------:|------:|------:|-------------:|
| CHEMBL6149286 | hydroxamate | −9.5 | −10.1 | **−11.0** | **−1.5** (anti-selective) |
| CHEMBL6174154 | hydroxamate | −8.8 | −8.8 | −10.1 | −1.3 (anti-selective) |
| **CHEMBL5915707** | sulfamide | −7.9 | −6.7 | −7.5 | **+0.4** (ENPP1-preferring) |
| **CHEMBL5826130** | sulfamide | −7.8 | −7.4 | −7.8 | +0.0 (ENPP1-preferring) |

The affinity winner binds ENPP3 **1.5 kcal/mol better** than ENPP1. It's effectively an ENPP3 inhibitor. Both hydroxamates behave this way; the hardest binders discriminate least. The two sulfamides — lower raw scores, more drug-like (QED 0.73), on ENPP1's validated native chemotype — are the only ones that lean toward ENPP1.

**Does it survive the noise?** Docking carries ~1 kcal/mol of error, so I re-docked across **42 runs** (21 seeds, each in duplicate; 5 poses/run) and bootstrapped 95% CIs. The hydroxamate is robustly anti-selective (−1.77 [−1.82,−1.72]); the sulfamides' positive margins clear their error bars; a borderline sulfonamide's CI crosses zero (honest verdict: can't call it). I then stress-tested against four independent signals — smina ΔΔG, Vinardo ΔΔG, Zn-coordination distance, interaction-fingerprint wall contacts. **Hydroxamates + native reference: 0/4 favor ENPP1 (unanimous rejection). Sulfamides: 2/4 (directional, not settled).** The demotion is firm; the promotion is the only direction any method supports.

**Why it's structural, not a fluke.** The hydroxamate binds by chelating the catalytic zinc — a strong interaction, but that zinc site is the most conserved feature of the entire family. Grab the zinc and you get affinity with no selectivity, because from the metal's vantage the three enzymes are the same. The sulfamide gives up raw affinity and earns it back on the divergent pocket walls — selectivity by construction.

**How little room there is.** Superposing the pockets (anchor RMSD 0.15–0.23 Å): **ENPP3 matches ENPP1 at all 14 core catalytic-pocket residues**; the only ENPP1/ENPP3 differences are two residues out at the ~4 Å periphery (ENPP2 differs at two core positions). That's why ENPP3 selectivity is the field's recurring bottleneck — and why the published leader STF-1623 has to *build* its >1,000× ENPP3 selectivity on exactly those two peripheral residues. It isn't lucky; it's engineered.

**Forward, not just triage.** The same logic — earn selectivity on the walls, not the metal — runs in design. Of 13 enumerated analogs of the lead sulfamide, one (**AN10**, a piperidinol) improves *both* predicted potency (−9.08 vs −8.10) and worst-case margin (+0.70 [0.39,0.95] vs +0.15) while staying Rule-of-Five clean. A computational hypothesis, but it shows the pocket-wall vector is synthetically actionable.

**Where it sits in the field.** Four oral ENPP1 inhibitors are already in trials — RBS2418 and SR-8541A (Phase 2), TXN10128 and ISM5939 (Phase 1; ISM5939 was designed with generative AI). On IP (ClinicalTrials.gov + PubChem, retrieved 2026-07-03), the nominated sulfamides map onto a granted composition-of-matter patent (US-11591313-B2); the hydroxamates appear only in a 2024 application. Structure-based triage like this sits upstream of all of it — the cheap filter that decides which molecules earn a place in the assay queue.

**Does the protocol even work here?** Three controls, reported honestly. Cognate redocking of the native ligand localizes the right pocket + zinc contact (2.2–2.3 Å) but only to 3.08 Å RMSD — smina has no explicit metal term. An actives-vs-decoys enrichment benchmark is a **negative result**: ROC-AUC 0.44, absolute score doesn't rank binders (expected for a di-zinc site scored without a metal term). That's exactly why every claim uses the *within-ligand* ENPP1-vs-paralog **difference** (ΔΔG), where those systematic errors cancel — not absolute affinity. Directional calls are also sign-robust across 8 protonation states. The negatives sharpen the framing rather than break it.

**The honest limits.** Docking ΔΔG is a *directional* proxy, not an IC50 ratio (~1 kcal/mol noise, poor metal-coordination physics). This screen flags direction — promiscuous vs ENPP1-leaning — not fold-changes. ENPP3 was docked apo; poses weren't MD-relaxed. And there's no wet-lab data: it's all hypothesis-generating until a 3-enzyme biochemical IC50 panel runs.

**The call.** Demote the hydroxamate to a reference control; co-nominate the sulfamides **CHEMBL5826130** and **CHEMBL5915707**; carry the designed **AN10** analog as the novel arm; then settle it with a wet-lab 3-enzyme IC50 panel — at the bench, not the keyboard.

**The lesson.** Against a conserved active site, optimize the *margin*, not the score. The most potent binder to a shared catalytic feature is often the least selective drug — and a ranking without a paralog counter-screen hands you the wrong molecule with full confidence.

Fully reproducible repo: **https://github.com/crisprking/enpp1**
