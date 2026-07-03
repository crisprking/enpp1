# X thread — ENPP1 selectivity counter-screen

*16 beats. Figure attachments noted inline. Framing = open computational methods, not a drug announcement.*

---

**1/**
I ran a structure-based drug-discovery exercise against ENPP1 (a hot immuno-oncology target).

Docking picked a clean winner.

Then I ran the one test we'd skipped — and it told me to throw the winner away.

A thread on why the best-binding compound was the wrong one. 🧵
*[attach: enpp_selectivity.png]*

---

**2/**
ENPP1 has two close cousins: ENPP2 (autotaxin) and ENPP3.

A compound that hits all three isn't a clean drug — it's an off-target liability.

Our earlier round ranked candidates by how hard they bind ENPP1. It never checked the cousins. So I did.

---

**3/**
The method that makes this fair: dock into all 3 enzymes with an *identical* box, centered on the catalytic zinc every ENPP shares.

Same engine (smina), same settings, same ligand prep.

Metric = selectivity margin = (paralog affinity − ENPP1 affinity).
Positive = prefers ENPP1. Good.

---

**4/**
The reversal:

The top affinity compound — a hydroxamate — binds ENPP3 **1.5 kcal/mol BETTER** than ENPP1.

It's not an ENPP1 drug. It's an ENPP3 inhibitor that also hits ENPP1.

Both hydroxamates did this. The hardest binders discriminate the *least*.

---

**5/**
Meanwhile the two sulfamides — middling raw scores, would've been passed over — are the *only* leads that prefer ENPP1 over both cousins.

Bonus: they're more drug-like (QED 0.73 vs 0.50) and sit on ENPP1's validated native chemotype. No warhead alert.

---

**6/**
"But docking is noisy" — correct. So I re-docked everything across 42 runs — 21 seeds, each in duplicate — and bootstrapped 95% CIs on each margin.

The hydroxamate sits at −1.77 [−1.82, −1.72]: robustly anti-selective.
The sulfamides' positive margins clear their error bars. One borderline sulfonamide's CI crosses zero → honest verdict: can't call it.
*[attach: fig_margin_ci.png]*

---

**7/**
Then I stress-tested against 4 independent signals: smina ΔΔG, Vinardo ΔΔG, Zn-distance, interaction-fingerprint wall contacts.

Hydroxamates + native ref: 0/4 favor ENPP1 — unanimous rejection.
Sulfamides: 2/4 — directional support, not settled.

The demotion is firm; the promotion is a direction, not a proof.
*[attach: fig_consensus.png]*

---

**8/**
Does the protocol even work on this target? I checked — and report a negative result honestly.

• Redock the native ligand → right pocket + zinc contact (2.2–2.3 Å) but 3.08 Å RMSD (smina has no metal term).
• Actives-vs-decoys enrichment → ROC-AUC 0.44. Absolute score does NOT rank binders here.

That's the point 👇
*[attach: fig_enrichment.png]*

---

**9/**
Why doesn't that negative sink the study?

Because the enrichment test ranks *different* ligands by *absolute* score — which fails. The selectivity call uses the *same* ligand's ENPP1-vs-paralog *difference* (ΔΔG), where those systematic errors cancel.

So I never claim absolute affinity — only direction. The negative sharpens the framing.

---

**10/**
Why isn't this a fluke? It's structural.

The hydroxamate binds by chelating the catalytic zinc. Strong, but that zinc site is the MOST conserved feature of the whole family.

Grab the zinc → great affinity, zero selectivity. The three enzymes look identical from there.

---

**11/**
How much room is there to be selective? I superposed the pockets (RMSD 0.15–0.23 Å).

ENPP3 = identical to ENPP1 at all 14 core catalytic-pocket residues. The only differences are 2 residues out at the ~4Å rim — that's the entire ENPP3 selectivity budget (and exactly where clinical STF-1623 builds its >1,000× margin).
ENPP2 differs at just 2.

ENPP3 selectivity is the field's hardest problem — the pocket gives you almost nothing.
*[attach: enpp_active_site_conservation.png]*

---

**12/**
The literature agrees. Even Insilico's clinical ISM5939 reports its >3,400× ENPP3 selectivity as something *engineered*, not lucky.

Another good compound (Enpp-1-IN-27): ~410× over ENPP2 but only ~10× over ENPP3.

ENPP3 is the weak axis for everyone.

---

**13/**
Can we do better than triage? I designed 13 analogs of the lead sulfamide, growing toward the divergent pocket walls.

One — AN10, a piperidinol — improves BOTH predicted potency (−9.08 vs −8.10) and margin (+0.70 [0.39,0.95] vs +0.15). The pocket-wall vector is synthetically actionable.
*[attach: fig_analog_design.png]*

---

**14/**
Reality check on the field: this isn't a vacuum. 4 oral ENPP1 inhibitors are already in trials — RBS2418 & SR-8541A (Ph2), TXN10128 & ISM5939 (Ph1).

IP: the sulfamides map onto a granted composition-of-matter patent; hydroxamates only in a 2024 application. Structure-based triage sits upstream of all of it — the cheap filter before the assay queue.
*[attach: fig_clinical_patent_landscape.png]*

---

**15/**
So the call:
• Demote the "winning" hydroxamate → reference control (0/4 methods, Ames-liable)
• Co-nominate sulfamides CHEMBL5826130 + CHEMBL5915707
• Carry the designed AN10 analog as the novel arm

Then stop trusting the computer. Decision experiment = wet-lab 3-enzyme IC50 panel.

---

**16/**
The transferable lesson:

Against a conserved active site, optimize the MARGIN, not the score.

The most potent binder to a shared catalytic feature is often the least selective drug. Skip the counter-screen and you advance exactly the wrong molecule — confidently.

---

**Caveat (pinned reply):**
Docking ΔΔG is a *directional* proxy, not an IC50 ratio (~1 kcal/mol noise, weak metal-coordination physics). This flags direction, not fold-change. Zero wet-lab data — all hypothesis-generating until the assay runs.

Repo (fully reproducible): https://github.com/crisprking/enpp1
