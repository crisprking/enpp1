#!/usr/bin/env python3
"""Turn raw docking scores into the selectivity scorecard.

Reads:
  data/docking_scores_raw.csv   (target, ligand, affinity)  -- long form
  data/ligands.csv              (cid, smiles, warhead, qed, pchembl)

Writes:
  data/enpp_selectivity_scorecard.csv

Selectivity margin = paralog_affinity - ENPP1_affinity  (kcal/mol).
Positive margin => the ligand docks WORSE (less negative) into the paralog
than into ENPP1, i.e. it is ENPP1-preferring. The worst-case margin is the
minimum over {ENPP2, ENPP3}; a compound is only "selective" if BOTH paralogs
are disfavoured.

NOTE: docking Delta-Delta-G is a DIRECTIONAL PROXY, not an IC50 ratio. See the
DISCLAIMER in README.md.
"""
import sys
from pathlib import Path

import pandas as pd


def verdict(worst: float) -> str:
    if worst <= -0.5:
        return "anti-selective (binds paralogs \u2265 ENPP1)"
    if worst >= 0.3:
        return "ENPP1-preferring"
    return "borderline/non-selective"


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    raw = pd.read_csv(root / "data" / "docking_scores_raw.csv")
    ligs = pd.read_csv(root / "data" / "ligands.csv")

    wide = raw.pivot(index="ligand", columns="target", values="affinity").reset_index()
    wide = wide.rename(columns={"ligand": "compound",
                                "enpp1": "ENPP1", "enpp2": "ENPP2", "enpp3": "ENPP3"})
    wide["margin_ENPP2"] = (wide["ENPP2"] - wide["ENPP1"]).round(2)
    wide["margin_ENPP3"] = (wide["ENPP3"] - wide["ENPP1"]).round(2)
    wide["worst_paralog_margin"] = wide[["margin_ENPP2", "margin_ENPP3"]].min(axis=1)
    wide["selectivity_verdict"] = wide["worst_paralog_margin"].map(verdict)

    meta = ligs.rename(columns={"cid": "compound"})[["compound", "warhead", "qed", "pchembl"]]
    out = meta.merge(wide, on="compound", how="right")
    out = out.sort_values("worst_paralog_margin")
    dest = root / "data" / "enpp_selectivity_scorecard.csv"
    out.to_csv(dest, index=False)
    print(out.to_string(index=False))
    print(f"\nwrote {dest}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
