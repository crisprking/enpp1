#!/usr/bin/env python3
"""
Extended ENPP1 selectivity analysis: bootstrap CIs on replicate docking margins,
plus the figures in ../figures/. Mechanism (Zn-distance), interaction-fingerprint,
and consensus tables are produced by the pose-parsing steps documented in
../README.md and shipped as CSVs in ../data/ (they require the docked pose PDBQT
files and receptor PDBs, not re-derived here).

Usage:  python run_analysis.py
Inputs: ../data/replicate_scores.csv        (target,ligand,seed,affinity)
Outputs:../data/margin_confidence_intervals.csv
        ../figures/fig_margin_ci.png
"""
import os, numpy as np, pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "..", "data")
FIGS = os.path.join(HERE, "..", "figures")
SEED = 42; NBOOT = 10000
rng = np.random.default_rng(SEED)

rep = pd.read_csv(os.path.join(DATA, "replicate_scores.csv"))

def boot_ci(vals, nboot=NBOOT):
    vals = np.asarray(vals, float)
    means = rng.choice(vals, size=(nboot, len(vals)), replace=True).mean(axis=1)
    return np.percentile(means, [2.5, 97.5])

rows = []
for lig in rep.ligand.unique():
    e1 = rep[(rep.ligand == lig) & (rep.target == "enpp1")].affinity.values
    for par in ["enpp2", "enpp3"]:
        ep = rep[(rep.ligand == lig) & (rep.target == par)].affinity.values
        n = min(len(e1), len(ep))
        margins = ep[:n] - e1[:n]                 # paralog - ENPP1
        lo, hi = boot_ci(margins)
        p_pref = float((rng.choice(margins, size=(NBOOT, n)).mean(axis=1) > 0).mean())
        rows.append(dict(ligand=lig, paralog=par, margin=round(margins.mean(), 2),
                         ci_lo=round(lo, 2), ci_hi=round(hi, 2),
                         p_ENPP1_pref=round(p_pref, 3),
                         sig="yes" if (lo > 0 or hi < 0) else "no"))
mar = pd.DataFrame(rows)
mar.to_csv(os.path.join(DATA, "margin_confidence_intervals.csv"), index=False)
print("wrote margin_confidence_intervals.csv")

# worst-case (least selective) margin per ligand
worst = (mar.loc[mar.groupby("ligand").margin.idxmin()]
            .set_index("ligand").sort_values("margin"))

lig_wh = {'CHEMBL6149286':'hydroxamate','CHEMBL6174154':'hydroxamate',
          'TZV_native':'sulfamide','CHEMBL5555976':'sulfonamide',
          'CHEMBL5915707':'sulfamide','CHEMBL5826130':'sulfamide'}
WH = {'hydroxamate':'#b2182b','sulfamide':'#2166ac','sulfonamide':'#4d4d4d'}

fig, ax = plt.subplots(figsize=(7.2, 4.0))
for i, (lig, r) in enumerate(worst.iterrows()):
    c = WH[lig_wh[lig]]
    ax.errorbar(r.margin, i, xerr=[[r.margin - r.ci_lo], [r.ci_hi - r.margin]],
                fmt='o', color=c, ecolor=c, capsize=3, markersize=7, elinewidth=1.6, zorder=3)
    ax.annotate(f"{r.margin:+.2f}", (r.margin, i), xytext=(0, 9),
                textcoords='offset points', ha='center', fontsize=6, color=c)
ax.axvspan(-2.2, 0, color='#fbe9e9', zorder=0); ax.axvline(0, color='#888', lw=0.8)
ax.set_yticks(range(len(worst)))
ax.set_yticklabels([f"{l}\n(vs {r.paralog.upper()})" for l, r in worst.iterrows()], fontsize=6)
ax.set_xlabel("worst-case selectivity margin (kcal/mol)  —  95% CI, 42 seeds")
ax.set_title("Selectivity margins resolved against docking noise", fontsize=8)
ax.set_xlim(-2.2, 0.85)
ax.legend(handles=[Patch(color=WH['sulfamide'], label='sulfamide'),
                   Patch(color=WH['hydroxamate'], label='hydroxamate'),
                   Patch(color=WH['sulfonamide'], label='sulfonamide')],
          loc='lower left', fontsize=5.5, frameon=False)
fig.tight_layout()
fig.savefig(os.path.join(FIGS, "fig_margin_ci.png"), dpi=300, bbox_inches='tight')
print("wrote fig_margin_ci.png")
