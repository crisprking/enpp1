# Contributing

This is an open computational-methods exercise. Corrections, replications, and
methodological critiques are genuinely welcome — the point is to do structure-based
triage in public and get the caveats right.

## Good ways to contribute

- **Replicate the docking.** Re-run `scripts/reproduce.sh` and report whether the
  selectivity *direction* holds (hydroxamates anti-selective, sulfamides
  ENPP1-preferring). Exact scores will drift ≈0.1–0.3 kcal/mol run to run; the
  ranking is the claim, not the digits.
- **Stress-test the protocol.** Different box size, exhaustiveness, scoring
  function (e.g. Vina vs smina default), or an MD-relaxed pose. Does the flip
  survive?
- **Improve the metal treatment.** The biggest known weakness is that smina models
  Zn coordination poorly. A QM/MM or explicit-metal-restraint pass on the top
  compounds would materially strengthen (or overturn) the conclusion.
- **Add compounds.** More sulfamides / non-chelating chemotypes to test whether
  the margin-vs-score pattern generalizes.

## Please keep the framing honest

This repo makes **no therapeutic claim** and contains **no wet-lab data**. Any PR
that presents docking ΔΔG as an IC50 ratio, or the nominee as a validated
candidate, will be asked to reword. The credibility of the piece rests on the
limitations being stated plainly — see the DISCLAIMER in `README.md`.

## Reporting issues

Open an issue with: what you ran, the environment (OS, smina/obabel/RDKit
versions), and the output. For scientific disagreements, cite the structure or
paper you're arguing from.
