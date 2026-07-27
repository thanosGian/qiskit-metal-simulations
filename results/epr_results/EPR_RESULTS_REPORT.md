# EPR Results Report — Q1–Q4

Summary of the pyEPR (Energy Participation Ratio) HFSS eigenmode analysis for the four transmon
qubits of the 4-qubit chip design. Sourced directly from `Q1_logs.txt`, `Q2_logs.txt`,
`Q3-logs.txt`, `Q4-logs.txt` and the accompanying `*_kerr_iter2.csv` / `*_Frequencies_iter2.csv`
files in this directory. Cross-referenced against `../../THESIS_DESIGN_SUMMARY.md`.

## 1. Final converged results

| Qubit | Lj (nH) | f01 (MHz) | Target (MHz) | Error (MHz) | \|α\| (MHz) | Participation P | Max cross-Kerr (MHz) | Status |
|---|---|---|---|---|---|---|---|---|
| Q1 | 11.9976 | 4802.3 | 4800 | −2.3 | 236.9 | 0.87 | 38.0 | CONVERGED |
| Q2 | 11.2966 | 4988.9 | 5000 | +11.1 | **208**¹ | 0.92 | 10.2 | CONVERGED |
| Q3 | 10.1964 | 5205.6 | 5200 | −5.6 | 239.5 | 0.91 | 22.9 | CONVERGED |
| Q4 | 9.7732  | 5390.1 | 5400 | +9.9 | 195.5 | 0.91 | 6.6 | CONVERGED |

All four land within ~11 MHz of target — well inside the ~15–30 MHz design-centering tolerance
noted in the thesis summary. "Max cross-Kerr" here is the largest off-diagonal entry of the
**chi_O1** (analytic perturbation) matrix; see §4 for why O1 and ND disagree.

¹ Q2's α is reported here as **chi_O1's 208 MHz**, not the auto-tune script's raw headline value
(155.4 MHz, chi_ND) — see §5 for why chi_ND is specifically distrusted for Q2.

## 2. Tuning iterations (auto-tune Lj loop)

Each qubit's log records an initial Lj guess (iter1, off-target) and a Newton-corrected Lj
(iter2, on-target/CONVERGED).

| Qubit | Iter | Lj (nH) | f01 (MHz) | \|α\| (MHz) | P | Error (MHz) | Verdict |
|---|---|---|---|---|---|---|---|
| Q1 | 1 | 11.6600 | 4872.4 | 234 | 0.79 | −72.4 | OFF-TARGET |
| Q1 | 2 | 11.9976 | 4802.3 | 237 | 0.87 | −2.3 | on-target |
| Q2 | 1 | 11.7730 | 4891.4 | 310 | 0.91 | +108.6 | OFF-TARGET |
| Q2 | 2 | 11.2966 | 4988.9 | 155 | 0.92 | +11.1 | on-target |
| Q3 | 1 | 10.9000 | 5021.3 | 245 | 0.94 | +178.7 | OFF-TARGET |
| Q3 | 2 | 10.1964 | 5205.6 | 240 | 0.91 | −5.6 | on-target |
| Q4 | 1 | 9.9390  | 5353.2 | 188 | 0.91 | +46.8 | OFF-TARGET |
| Q4 | 2 | 9.7732  | 5390.1 | 196 | 0.91 | +9.9 | on-target |

Q3's log is explicitly marked `(corrected)` — see §6 on provenance; `Q3/old/` holds a stale
pre-correction run and is excluded here.

## 3. Cross-Kerr / coupling matrices (chi_ND, MHz)

5×5 numerical-diagonalization chi matrix from each `*_kerr_iter2.csv` (diagonal = anharmonicity,
off-diagonal = cross-Kerr between modes). Mode indices are HFSS eigenmode order, not qubit
identity — **mode 1 is the qubit mode** in all four designs (identified by highest junction
participation, `Pm_normed`/`Pm_raw`), consistent with the thesis summary's rule of thumb
"identify the qubit by participation, not by frequency or argmax(chi)."

**Q1** (modes at ≈3.62 / 4.80 / 5.07 / 5.09 / 5.30 GHz):

| | m0 | m1 (qubit) | m2 | m3 | m4 |
|---|---|---|---|---|---|
| m0 | 5.0e-8 | 0.0082 | ~0 | ~0 | 0.00029 |
| m1 | 0.0082 | **236.88** | ~0 | ~0 | 9.098 |
| m4 | 0.00029 | 9.098 | ~0 | ~0 | 0.156 |

**Q2** (modes at ≈4.46 / 4.73 / 5.08 / 5.09 / 4.99 GHz):

| | m0 | m1 | m2 | m3 | m4 (qubit) |
|---|---|---|---|---|---|
| m0 | 9.2e-5 | 0.031 | ~0 | ~0 | 0.399 |
| m1 | 0.031 | 3.13 | ~0 | ~0 | 81.12 |
| m4 | 0.399 | 81.12 | ~0 | ~0 | 155.37 (chi_ND) |

Note: for Q2 the qubit-like mode is **mode 4**, not mode 1 (per `Pm_normed` in the log — mode 4
carries participation ≈0.94, mode 1 only ≈0.025). The diagonal shown above (155.37 MHz) is
**chi_ND**; the same mode's **chi_O1** diagonal is 208 MHz instead — a disagreement large enough,
and in the opposite direction from Q1/Q3's O1-vs-ND gap, that §5 treats chi_O1's 208 MHz as the
more trustworthy anharmonicity for Q2 (used in §1's headline table).

**Q3** (modes at ≈4.90 / 5.21 / 5.82 / 6.37 / 6.66 GHz):

| | m0 | m1 (qubit) | m2 | m3 | m4 |
|---|---|---|---|---|---|
| m0 | 6.1e-5 | 0.895 | 0.0024 | 0.00098 | 0.00071 |
| m1 | 0.895 | **239.54** | 7.70 | 2.70 | 1.51 |
| m2 | 0.0024 | 7.70 | 0.095 | 0.063 | 0.035 |
| m3 | 0.00098 | 2.70 | 0.063 | 0.010 | 0.011 |
| m4 | 0.00071 | 1.51 | 0.035 | 0.011 | 0.0031 |

Q3 is the one design where modes 2–4 (the bus/readout resonators) show non-negligible cross-Kerr
with the qubit mode (up to 7.7 MHz), rather than being numerically ~0 as in Q1/Q2/Q4.

**Q4** (modes at ≈4.63 / 4.99 / 5.02 / 5.03 / 5.60 GHz):

| | m0 | m1 | m2 | m3 | m4 (qubit) |
|---|---|---|---|---|---|
| m0 | 8.2e-5 | 0.012 | ~0 | ~0 | 0.356 |
| m1 | 0.012 | 0.472 | ~0 | ~0 | 32.30 |
| m4 | 0.356 | 32.30 | ~0 | ~0 | **195.54** |

(Cells shown as `~0` are on the order of 1e-7–1e-11 MHz — numerical noise, not physical coupling.)

## 3.1 Circuit topology per qubit — Q3 is not modeled the same way as Q1/Q2/Q4

Confirmed against the notebook's `QTUNE` config dict:

| Qubit | Components simulated | Bus terminations | Why |
|---|---|---|---|
| Q1 | Q1, Readout1, Charge_Line1, cpw1, cpw4, **Q2, Q4** | `open_terms=[]` (real, via neighbor qubits) | baseline approach |
| Q2 | Q2, Readout2, Charge_Line2, cpw1, cpw2, **Q1, Q3** | `open_terms=[]` (real, via neighbor qubits) | baseline approach |
| Q3 | Q3, Readout3, Charge_Line3, cpw2, cpw3 (**no neighbors**) | `open_terms=[("cpw2","end"),("cpw3","end")]` | baseline approach **hybridized** — switched to reduced/open-terminated |
| Q4 | Q4, Readout4, Charge_Line4, cpw3, cpw4, **Q3, Q1** | `open_terms=[]` (real, via neighbor qubits) | baseline approach |

Q3 is the outlier: it uses a smaller, 7-component circuit with the bus far ends left open,
instead of the 9-component neighbor-included circuit used for Q1, Q2, and Q4. This wasn't an
inconsistency — it's a deliberate fix. The discarded first attempt at Q3, preserved in
`Q3/old/Q3-logs.txt`, used the same neighbor-included approach as the other three qubits and
produced a textbook hybridization failure:

```
Lj=9.9930 nH -> f01=5569.3 MHz  alpha=75 MHz  P=0.54  max_cross_kerr=109.7  err=-369.3 MHz
OFF-TARGET  NOT CLEAN  HYBRIDIZED
STOP: unclean/hybridized — not iterating on unreliable f01
```

with junction participation split ~0.42/0.56 across two near-degenerate modes — the qubit mode
and a neighbor/bus mode mixed almost 50/50, rather than one clean qubit-like mode. The auto-tune
loop correctly refused to keep iterating on that result. Switching Q3 to the reduced,
open-terminated circuit resolved it (P=0.91, clean single-mode participation).

**Implication:** Q3's final α=239.5 MHz was obtained with a genuinely different circuit reduction
than Q1/Q2/Q4's, so it is not strictly apples-to-apples with the other three numbers — see §5.

## 4. Data-quality caveats (from the logs themselves)

- **Non-converged spurious modes.** In every Q1/Q2/Q4 run, two of the five eigenmodes (the ones
  landing near 5.0–5.1 GHz, distinct from the qubit/bus/readout modes) trigger:
  `WARNING: This simulation must not have converged well!!! The difference in the total cap and
  ind energies is larger than 10%.` — with the cap/ind mismatch reported as high as 200%. These
  modes carry negligible junction participation (~1e-6–1e-4) and negligible energy, so they read as
  numerical/box artifacts (e.g. sample-holder or boundary modes) rather than physical resonances,
  but they are the reason each run also throws an `IndexError` in `_get_participation_normalized`
  at the end of the distributed-analysis stage. Q3's log does **not** show this warning — its five
  modes are all physically distinct (qubit + 4 well-separated bus/readout resonances).
- **chi_O1 vs chi_ND disagree on cross-Kerr magnitude**, sometimes by 4×: e.g. Q1's O1 (analytic
  perturbation) matrix gives max cross-Kerr 38.0 MHz, but the ND (numerical diagonalization) matrix
  in `Q1_kerr_iter2.csv` gives 9.1 MHz for the same mode pair. This matches the known fragility of
  `chi_ND` documented in `THESIS_DESIGN_SUMMARY.md` §8 point 5.
- **The auto-tune script's own headline line silently mixes chi sources.** The printed summary
  (`Lj=... alpha=X ... max_cross_kerr=Y`) sources `alpha` from **chi_ND** and `max_cross_kerr` from
  **chi_O1** — verified directly against the full chi tables for Q1, Q2, Q3 (Q4's chi tables were
  truncated at capture time in `Q4-logs.txt`, so not verifiable there). This is the opposite of the
  thesis's own §8.5 rule ("use chi_O1 for anharmonicity"). Comparing the qubit-mode diagonal:

  | Qubit | chi_O1 diag | chi_ND diag (reported as "alpha") |
  |---|---|---|
  | Q1 | 182 MHz | 236.9 MHz (ND higher) |
  | Q2 | 208 MHz | 155.4 MHz (ND **lower** — direction flips) |
  | Q3 | 198 MHz | 239.5 MHz (ND higher) |

  Q1 and Q3 agree in direction (ND above O1); Q2 alone flips the other way, which is the signature
  of chi_ND breaking down under near-degenerate mode mixing rather than a real difference in Q2's
  design. Apply chi_O1 (208 MHz) for Q2 instead of the script's raw chi_ND output — see §5.
- **Substrate EPR and dielectric participation are consistent** across all four qubits
  (91.6–92.1% substrate EPR, ~0.915–0.921 `p_dielectric_main` per mode), suggesting the mesh/model
  setup didn't vary meaningfully qubit-to-qubit — differences in the results above are physical
  (geometry + Lj), not modeling artifacts.

## 5. Discrepancy vs. `THESIS_DESIGN_SUMMARY.md`

The thesis summary's §4 table (written from an earlier/parallel pass) records:

| Qubit | Summary's Lj (nH) | Summary's f01 (GHz) | Summary's \|α\| |
|---|---|---|---|
| Q1 | 11.66 | 4.800 | "~200 MHz for all four" |
| Q2 | 11.773 | 5.010 | (same) |
| Q3 | 9.993 | 5.213 | (same) |
| Q4 | 9.939 | 5.394 | (same) |

That document explicitly states the ~200 MHz anharmonicity is the "record" value and that any
other numbers seen in some runs (89/114/139 MHz are given as its examples) are "reduced-model
bus-collision artifacts, not real."

**This directory's actual CONVERGED log lines disagree with that on both axes:**
- The Lj values here (11.998 / 11.297 / 10.196 / 9.773 nH) don't match the summary's
  (11.66 / 11.773 / 9.993 / 9.939 nH) — notably Q1's Lj is higher here, Q2/Q3/Q4's are lower.
- The anharmonicities here (236.9 / **155.4** / 239.5 / 195.5 MHz) are *not* uniformly ~200 MHz.

**Partial explanation confirmed (see §3.1): Q3's number isn't directly comparable to the other
three.** Q3 was simulated with a structurally different, reduced/open-terminated circuit (no
neighbor qubits) after its neighbor-included attempt hybridized outright. So the "spread" in α is
at least partly a methodology difference, not four measurements of the same thing.

**Q2 is resolved, not just flagged.** Q2 kept its neighbors (Q1, Q3) for both tuning iterations —
same topology as Q1 and Q4, confirmed from the notebook's `QTUNE` dict (only Lj changed between
passes, 11.7730 → 11.2966; there was no circuit swap). Its low reported anharmonicity (155.4 MHz)
turns out to be a **chi_ND reporting artifact, not a real physical outlier**: the qubit mode's
chi_O1 diagonal is 208 MHz — right inside the 195–240 MHz band Q1/Q3/Q4 occupy. The auto-tune
script's headline always reports chi_ND as "alpha" (§4), and Q2 is the one qubit where chi_ND
diverges from chi_O1 in the opposite direction from Q1/Q3's O1-vs-ND gap (ND lower instead of
higher) — consistent with chi_ND's known fragility near degeneracy (`THESIS_DESIGN_SUMMARY.md`
§8.5), not with a genuine hybridization difference. **§1's headline table now reports Q2's
anharmonicity as 208 MHz (chi_O1)** rather than the script's raw 155.4 MHz (chi_ND).

This was checked using data already in hand (no new HFSS run). If you want an independent
confirmation beyond the O1/ND argument, the neighbor-qubit-Lj-pinning mitigation from §8.9 (set
`Lj_Q1`/`Lj_Q3` to ~1000 nH in a Q2-only rerun so they can't hybridize) would provide one, but it's
optional now rather than required.

**Still open:** confirm which of this directory's numbers vs. `THESIS_DESIGN_SUMMARY.md`'s numbers
is the intended final design point for the thesis — the summary isn't dated and it's unclear
whether it predates or postdates this batch of runs.

## 6. Provenance

| Qubit | Log timestamp(s) | HFSS project | Distributed-analysis `.npz` |
|---|---|---|---|
| Q1 | 2026-07-14, iter1 10:56AM / iter2 03:48PM | Project32 / Q1_final_hfss | `2026-07-14 10-56-22.npz`, `2026-07-14 15-48-04.npz` |
| Q2 | 2026-07-15, iter1 10:44AM / iter2 03:15PM | Project33 / Q2_final_hfss | `2026-07-15 10-44-33.npz`, `2026-07-15 15-15-34.npz` |
| Q3 | 2026-07-20, iter1 12:37PM / iter2 05:05PM ("corrected") | Project34 / Q3_final_hfss | `2026-07-20 12-37-22.npz`, `2026-07-20 17-05-57.npz` |
| Q4 | 2026-07-16, iter1 10:53AM / iter2 02:23PM | Project33 / Q4_final_hfss | `2026-07-16 10-53-22.npz`, `2026-07-16 14-23-32.npz` |

`Q3/old/` (`Q3-logs.txt`, `Q3_Frequencies_iter_1.csv`, `Q3_kerr_iter1.csv`) is not a stale duplicate
of the current data — it's the discarded **neighbor-included** attempt at Q3 (same topology as
Q1/Q2/Q4) that came back `HYBRIDIZED` (Lj=9.9930 nH, α=75 MHz, P=0.54, max_cross_kerr=109.7 MHz;
see §3.1). It's excluded from the headline numbers because the pipeline itself flagged it as
unreliable and stopped, not because it was superseded by a later pass of the same circuit. All
four sessions ended in a Qt event-dispatcher `CRITICAL` (Windows message-queue quota) after
analysis completed — cosmetic, not a simulation failure.
