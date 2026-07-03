# Protonation / tautomer sensitivity of selectivity margins

**Referee concern (gap item 4).** Only one protonation state (obabel -p 7.4)
was docked in the main screen. The warheads here (sulfamide, hydroxamate,
phosphonate) are exactly the ionizable groups whose charge state governs
metal-site engagement — so the selectivity call could be an artifact of the
chosen state. This module tests that directly.

**Design.** One representative lead per warhead class; all chemically plausible
protonation/tautomer states enumerated explicitly (RDKit-validated SMILES) and
docked into all three paralogs with the identical protocol. 8 states x 3
receptors = 24 docks. Margin = paralog_affinity - ENPP1_affinity (>0 = prefers
ENPP1).

| lead | states tested | ENPP2 margin range | ENPP3 margin range |
|---|---|---|---|
| CHEMBL5915707 (sulfamide) | neutral, N-deprotonated | **+0.2 to +0.6** (sign robust) | -0.2 to -0.8 |
| CHEMBL6149286 (hydroxamate) | neutral, N-deprot, O-deprot | **-0.6 to -1.6** (anti-selective in ALL) | -0.4 to -1.2 |
| CHEMBL5566114 (phosphonate) | neutral, mono-, di-anion | +0.1 to +0.7 | **-0.2 to -0.6** (anti-selective vs ENPP3 in ALL) |

## Conclusion
**The directional calls are robust to protonation state; the magnitudes are
not.**
- Sulfamide stays ENPP1-leaning vs ENPP2 in both states (never flips sign).
- Hydroxamate is anti-selective vs ENPP2 in **all three** states — independent
  confirmation of the earlier scoring-function-independent demotion, now also
  protonation-independent.
- Phosphonate stays anti-selective vs ENPP3 in **all three** states.
- Margin magnitudes shift by 0.4-1.0 kcal/mol across states. This is *larger*
  than the seed-noise bootstrap CIs (+/-0.05) and on the order of the margins
  themselves — direct evidence that the numbers must be read as **directional,
  not quantitative**, exactly as the study frames them.

This strengthens the qualitative selectivity thesis (warhead class drives the
direction) while explicitly bounding the quantitative precision. It does not
substitute for the wet-lab panel.
