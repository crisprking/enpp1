# Audit response — adjudication against primary sources

*Every external critique received on this project, adjudicated against the
primary source (RCSB PDB, live ChEMBL API, RDKit substructure match, published
literature). Format: claim → verdict → evidence → action taken.*

---

## Audit round 1 — structural / identity claims

**1.1 "6WEW's ligand is Ex54, not QPS2 / the repo mislabels it."**
→ **FALSE (claim mislocated).** RCSB PDB 6WEW lists exactly one non-polymer
inhibitor, PDB chemical-component code **TZV** (a 7-methoxyquinolin-4-yl-oxy
phenyl sulfuric diamide). This is the compound Dennis et al. 2020 call "Ex54"
in their medicinal-chemistry numbering; the two names denote the same molecule.
The repo never used the strings "QPS2" or "Ex54" as the 6WEW ligand identity.
*Action:* on first mention we now write "PDB ligand code TZV (named Ex54 in
Dennis et al. 2020)" so the crystallographic code and the paper's code are
explicitly reconciled. The sister structure 6WEV carries TZS (QPS2), correctly
labelled as a separate structure.

**1.2 "The five ChEMBL IDs are fabricated."**
→ **FALSE.** All five (CHEMBL5826130, CHEMBL5915707, CHEMBL5555976,
CHEMBL6149286, CHEMBL6174154) resolve on the live ChEMBL API, and each SMILES in
`data/ligands.csv` matches the ChEMBL record byte-for-byte. No action beyond
keeping the SMILES table in the writeups so structures are independently
checkable.

**1.3 "ENPP3 is not 100% identical to ENPP1."**
→ **PARTIALLY FAIR — tightened.** Our conservation map found ENPP3 identical to
ENPP1 at all **14 core catalytic-pocket residues we tracked** (within 6 A of the
Zn). The published STF-1623 co-crystal work finds ENPP3 diverges from ENPP1 by
~2 residues within 4 A of the ligand — the periphery, not the metal. A bare
"100%" overstated this. *Action:* every "100%" replaced with "identical at all
14 core catalytic-pocket residues; divergence only at the ~4 A periphery (2
residues per STF-1623)" across README, X pieces, and substack.

---

## Audit round 2 — writeup-level (written against the older v1 text)

Most points quoted v1 strings ("100%", "42 random seeds") already corrected in
v2; those are moot. Genuinely actionable items:

**2.4 "Define TZV on first mention."** → **ACCEPTED.** Done (see 1.1).
**2.8 "Patent-overlap language is too strong."** → **ACCEPTED, softened.** The
FTO statement now reads as a programmatic PubChem cross-reference, explicitly
"not a legal opinion," and frames the granted composition-of-matter patent
(US-11591313-B2) as a crowded-scaffold *flag* — one more argument for carrying
the novel AN10 analog.
**2.9 "Name the ENPP2 divergent residues."** → **ACCEPTED.** The two ENPP1→ENPP2
switch positions are now named: His→Leu and Ser→Phe (His260/Ser377 in ENPP1
numbering; Leu214/Phe313 in ENPP2 numbering).
**2.10 "The 'sulfamide' leads are actually sulfonamides."** → **FALSE per
RDKit.** SMARTS substructure matching confirms CHEMBL5826130, CHEMBL5915707, and
the native TZV each carry a **sulfamide** (N–SO2–N); CHEMBL5555976 carries an
aryl **sulfonamide** (C–SO2–N); the two hydroxamates carry C(=O)N–O. Our labels
are correct; the distinction is now stated explicitly in an appendix note.

---

## Audit round 3 — protocol-validation controls (accepted and integrated)

Round 3 was not an adversarial critique but a set of three referee-motivated
validation experiments, each run to completion with the production protocol and
reported honestly. All three are **accepted and folded into the repo**
(`analysis/validation/`) and the writeups.

**3.1 Cognate redocking control.** → **ACCEPTED.** Redocking native TZV into
6WEW localises the correct pocket with Zn engagement (2.2–2.3 A) but reaches
only 3.08 A best heavy-atom RMSD — fails the strict <2 A line because smina has
no explicit metal term. Bounds, does not inflate, the claims. (`REDOCK_README.md`)

**3.2 Actives-vs-decoys enrichment.** → **ACCEPTED (honest negative).** 30 known
ENPP1 actives (pChEMBL ≥7) vs 90 property-matched decoys, identical protocol:
ROC-AUC **0.44** (below random), EF5%/10% = 0, Mann–Whitney p = 0.85. Absolute
smina score does *not* rank ENPP1 binders — expected for a di-zinc metalloenzyme
scored without a metal term. **Does not invalidate the selectivity margins**,
which use the within-ligand ENPP1-vs-paralog *difference* (ΔΔG) where
ligand-specific scoring errors cancel; it forbids any cross-chemotype
absolute-affinity claim. (`ENRICHMENT_README.md`)

**3.3 Protonation / tautomer sensitivity.** → **ACCEPTED.** 8 protomer/tautomer
states across 3 paralogs. Directional calls are **sign-robust** (sulfamide
ENPP1-leaning vs ENPP2 in all states; hydroxamate anti-selective vs ENPP2 in all
states; phosphonate anti-selective vs ENPP3 in all states); magnitudes shift
0.4–1.0 kcal/mol — larger than the seed CIs, hard evidence for "directional, not
quantitative." (`PROTOMER_README.md`)

**Net effect.** These three controls move the repo from "assumes docking works
here" to "measured how well it works and calibrated every claim to that." The
full referee ledger, including the remaining OPEN items (orthogonal MM-GBSA /
metal-aware rescore; replicate CIs on the phosphonate screen), is in
`REVIEWER_GAP_ANALYSIS.md`.

---

## Standing conclusions unchanged by any audit
- Hydroxamate demotion is the firmest result: 0/4 consensus methods, margin
  −1.77 kcal/mol robust across 42 replicate runs, anti-selective in all
  protonation states, warhead-liable.
- Sulfamide co-nomination is *directional* (2/4 methods; Vinardo flips the
  smallest margins) — reported as suggestive, not settled.
- No wet-lab data exists; the decisive next step is a 3-enzyme biochemical
  IC50 panel.
