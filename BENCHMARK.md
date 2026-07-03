# Benchmarking against the field: literature, competitors, and open-source precedent

*How this project sits relative to the published ENPP1-inhibitor landscape. Every
external claim below is grounded in a retrieved, DOI-verified record (PubMed +
ChEMBL + ClinicalTrials.gov, queried programmatically). This document credits the
work we build on and states honestly where we add value and where others are ahead.*

**Sources:** 92 PubMed records triaged to 59 ENPP1 medicinal-chemistry / selectivity
/ structure papers; the full ChEMBL bioactivity landscape for ENPP1 (CHEMBL5925),
ENPP2/autotaxin (CHEMBL3691), and ENPP3 (CHEMBL5580); 23 ENPP1-related clinical
trials. Retrieval scripts and raw pulls are in `analysis/data/` and `benchmark/`.

---

## 1. The competitive landscape is real and moving fast

ENPP1 is a validated immuno-oncology target: it is the dominant extracellular
hydrolase of cGAMP, the second messenger of the cGAS–STING innate-immunity pathway,
so ENPP1 inhibition sustains STING signaling and anti-tumor immunity. The clinical
and medicinal-chemistry field is well ahead of any single computational screen:

- **Clinical stage.** Four dedicated ENPP1-inhibitor oncology programs are in Phase 1
  (NCT05978492, NCT05270213, NCT06063681 recruiting; NCT06724042 not-yet-recruiting).
  A separate ENPP1 axis — enzyme *replacement* (INZ-701) for ENPP1 deficiency / GACI —
  runs up to Phase 3 (the ENERGY program). ENPP1 is a two-sided target: inhibit it in
  cancer, restore it in calcification disease.
- **Best-in-class chemistry is already excellent.** The literature bar we hold
  ourselves against: **ISM5939** (Insilico Medicine, IND-cleared, 0.63 nM, >15,000x
  vs ENPP2, >3,400x vs ENPP3); **AVA-NP-695** (a *selective* ENPP1 inhibitor shown to
  activate STING and reduce metastasis, Baird et al. 2022, PMID 36235254); an oral ENPP1
  inhibitor **designed with generative AI** as a next-generation STING modulator
  (Nature Communications 2025, PMID 40410143); and an inhibitor with **ultralong
  target-residence time** framed as an innate-immune checkpoint (Cell Reports Medicine
  2025, PMID 40914167).
- **Active chemotype series (2020-2026).** At least a dozen distinct scaffolds are
  under public medicinal-chemistry optimization: imidazo[1,2-a]pyrazines, pyrrolo-
  pyrimidines/pyridines, [1,2,4]triazolo[1,5-a]pyrimidines, quinoline/quinazoline
  carboxylics, arylsulfonates, dihydropyrimido-pyrimidinones, benzotriazoles, and
  pyrazole derivatives (full DOI list in `benchmark/benchmark_literature_full.csv`).

**Where we stand:** we do not claim novel chemistry or a clinical candidate. Our
leads are existing ChEMBL sulfamides/sulfonamides. This project is a *method and a
counter-screen*, not a drug announcement — and that framing is honest about a field
that already has IND-cleared molecules.

---

## 2. The specific gap we fill: head-to-head paralog selectivity data barely exists

This is the strongest defensible contribution, and it comes straight from the data.
Querying ChEMBL for potent compounds (pChEMBL >= 7) across the three ENPP paralogs:

| Paralog | Target | Potent compounds (pChEMBL>=7) | Max pChEMBL |
|---|---|---|---|
| ENPP2 / autotaxin | CHEMBL3691 | **1,546** | 11.0 |
| ENPP1 | CHEMBL5925 | **199** | 10.05 |
| ENPP3 | CHEMBL5580 | **3** | 10.05 |

Two facts fall out of this table:

1. **The public bioactivity is wildly asymmetric.** Autotaxin has three decades of
   drug-discovery history (1,546 potent compounds); ENPP3 has essentially none (3).
   Any ENPP1 program that wants to claim ENPP3 selectivity cannot look it up — there
   is almost no public ENPP3 SAR to look up.
2. **Head-to-head selectivity data is almost non-existent.** Of every compound in
   ChEMBL across all three paralogs, **exactly one** (CHEMBL5566114) has been assayed
   on more than one ENPP paralog. Cross-paralog *selectivity* — the quantity every
   ENPP1 program needs — is almost never measured and published.

A structure-based computational counter-screen is a rational, cheap way to generate
selectivity *hypotheses* where the assay data does not exist. That is precisely what
this repository does, and the data gap above is *why* it is worth doing.

---

## 3. Biological validation that ENPP1-vs-ENPP3 selectivity matters

Our selectivity argument is not just a docking artifact — it was independently
motivated in 2024. Li et al. (Cell Reports 2024, PMID 38749434) identified **ENPP3 as
the second and likely only other metazoan cGAMP hydrolase**, accounting for all
cGAMP-hydrolysis activity in ENPP1-deficient mice, and showed that selectively
abolishing ENPP3's cGAMP hydrolysis restrains tumor growth. Implication: an ENPP1
inhibitor that *also* hits ENPP3 may be pharmacologically fine (both are immune
checkpoints), but one that spares ENPP3 isolates the ENPP1 mechanism. Either way,
knowing the ENPP1/ENPP3 margin is decisionrelevant — and our screen provides it.

This also sharpens a limitation we already state: our own conservation analysis shows
the ENPP1 and ENPP3 catalytic pockets are ~identical in core residues, so ENPP1/ENPP3
selectivity can only come from pocket *shape*, not residue identity. The 2024 biology
explains why that is a hard but worthwhile target.

---

## 4. Open-source computational precedent we build on

We are not the first to dock small molecules into ENPP1, and we credit the prior work:

- **Myricetin-to-natural-products virtual screen** (Front. era, PMC9573336): a
  virtual-screening -> docking -> molecular-dynamics -> MM/GBSA pipeline for natural
  ENPP1 inhibitors. This is the closest open computational analog to our workflow — but
  it is single-target (ENPP1 only), not a paralog counter-screen, and does not report
  cross-paralog selectivity margins with replicate statistics.
- **Benzotriazole docking-SAR** (Eur. J. Med. Chem. 2026, DOI 10.1016/j.ejmech.2026.118666):
  reports that the sulfamide warhead coordinates the ENPP1 Zn ion and hydrogen-bonds
  to Asp. **This is an important external check on our mechanism claim** — our own
  Zn-coordination analysis found sulfamides do *not* tightly coordinate Zn (2.7A in
  ENPP1). The disagreement is worth flagging and re-examining; it may reflect docking
  protocol, pose selection, or the specific sulfamide series. We record it rather than
  hide it.
- **Open-source docking tooling.** Our stack (smina/AutoDock Vina lineage + Open Babel
  + RDKit) is the standard open molecular-modeling toolchain catalogued by the
  Open Source Molecular Modeling community; recent reviews (PMC13073925) position this
  exact class of open, reproducible docking workflow as the accessible tier of
  structure-based design. We add: replicate statistics with bootstrap CIs, a 4-method
  consensus, interaction-fingerprint and Zn-coordination mechanism analysis, and a
  rational-analog round — layered on top of that shared foundation.

---

## 5. What we add, stated plainly

Building on the shoulders above, the incremental contributions of this repo are:

1. **A three-paralog counter-screen with replicate statistics**, where the public
   record has head-to-head data for one compound. (novelty: the *comparison*, done
   with uncertainty quantification.)
2. **A statistical noise floor.** 42-seed replicates + 10k-bootstrap CIs turn "docking
   score X" into "margin +/- CI", separating resolved directional signal from noise.
3. **Orthogonal mechanism evidence** (Zn-coordination distances, interaction
   fingerprints, Vinardo consensus) that agrees on the robust claim (hydroxamate
   anti-selectivity) and flags where the promotable claim is scoring-function
   dependent (sulfamide direction).
4. **A rational-analog round** (AN10_piperidinol) that improves both predicted potency
   and selectivity margin over the parent, with the margin CI excluding zero — a
   concrete, synthesizable, assay-ready hypothesis.
5. **Full open reproducibility** — every score, CI, figure, and receptor regenerable
   from committed scripts.

## 6. Honest scorecard vs the field

| Dimension | Field best | This project | Verdict |
|---|---|---|---|
| Potency (ENPP1) | ISM5939 0.63 nM (assay) | leads pChEMBL 9.3-9.7 (public assay); docking only | field far ahead; we screen, don't measure |
| Selectivity data | ISM5939 >3,400x ENPP3 (assay) | directional margins +/- CI (docking) | we generate hypotheses where public assay data is absent |
| Clinical maturity | Phase 1 (x4) + Phase 3 (INZ-701) | none | field far ahead; not our aim |
| Cross-paralog head-to-head | ~none in ChEMBL (n=1) | all 6 leads x 3 paralogs, replicated | **we lead on open, systematic comparison** |
| Statistical rigor of docking | rarely reported | 42-seed + bootstrap CI + consensus | **above the typical open docking paper** |
| Reproducibility | variable | fully scripted, open | **strong** |

**Bottom line:** the field owns potency, selectivity *measurement*, and the clinic.
This project owns the open, statistically-honest, three-paralog *counter-screen* and
the mechanism analysis behind it — a genuine, if narrow, contribution built explicitly
on the tools and biology cited above.

---

*Retrieval provenance: PubMed E-utilities, ChEMBL API, ClinicalTrials.gov API, all
queried programmatically July 2026. DOIs cross-verified via Crossref. See
`benchmark/` for the raw pulls and `benchmark/benchmark_literature_full.csv` for the
full DOI-linked reference list.*
