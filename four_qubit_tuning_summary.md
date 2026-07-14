# Project handoff: 4-qubit superconducting chip tuning (qiskit-metal)

## Setup
- **Notebook:** `qiskit-metal-simulations/final_four_qubit_chip_design.ipynb`
- **Tools:** qiskit-metal + ANSYS HFSS via pyEPR; main object is `three_mode_EPR` (an `EPRanalysis`). `design` is the QDesign.
- **Constraint:** only **16 GB RAM** → cannot run a full-chip EPR; everything uses **per-qubit reduced models**.
- **Targets:** qubit f01 = **4.8 / 5.0 / 5.2 / 5.4 GHz**; anharmonicity ~EC (LOM gave ~248 MHz); readouts 6.8–7.4 GHz; buses 5.8/6.0/6.2/6.4 GHz.
- **Flow followed (standard):** LOM (geometry + seed Lj) → eigenmode length sweeps (resonators) → EPR (final qubit Lj).

## Current status — essentially tuned

| Qubit | Lj (nH) | f01 (GHz) | target | α (real) |
|-------|---------|-----------|--------|----------|
| Q1 | 11.660 | 4.800 | 4.8 | 203 |
| Q2 | 11.773 | 5.010 | 5.0 | ~200* |
| Q3 | 9.993  | 5.213 | 5.2 | 199 |
| Q4 | 9.939  | 5.394 | 5.4 | ~200* |

\* Q2/Q4's EPR printed α ≈ 89/139 — these are **reduced-model bus-collision artifacts**; the real value is ~200 MHz (same pad geometry as Q1/Q3).

- **Resonator/bus lengths:** done (length sweeps; fixed a stale cpw1: 9.510 → 9.689 mm).
- All qubit frequencies within ~13 MHz of target.

## Key methodology / gotchas (important)
- **Reduced single-qubit model:** components = `[Qn, Readoutn, Launch_RO_Qn, its 2 buses, Charge_Linen, Launch_CL_Qn]`; bus **far ends open-terminated**; `n_modes=5`, `cos_trunc=fock_trunc=6`.
- **Identify the qubit by max junction participation** (`Pm_normed`), never by frequency order.
- **Frequency from `f_ND`** (robust); **anharmonicity from `chi_O1`** — `chi_ND` is fragile (breaks to 0/garbage with many modes or near-degeneracy).
- **Junction hygiene:** clear **both** `three_mode_EPR.setup.junctions.clear()` **and** `three_mode_EPR.sim.renderer.pinfo.junctions.clear()` each run (`del_junction()` only deletes a junction literally named `"jj"`).
- **`newton_lj(Lj, f_now, f_target, EC)`** uses ΔLj/Lj = −2·Δf/(f+EC).
- **Don't over-mode the EPR:** 7 modes took 252 min and broke `chi_ND` (cost ~`fock^n_modes`). Recover a crashed `run_epr` from its `.npz` via `pyEPR.QuantumAnalysis(npz).analyze_all_variations(...)`; diagonalize a subset with `analyze_variation(..., modes=[...])`.
- **Charge line** matters (~16 MHz downward loading) — include it in the model.
- **Reduced-model limits at crowded qubits:** open-term buses can collide with the qubit (Q4); real terminations (neighbor qubits) cause qubit–qubit hybridization (Q2–Q3 414 MHz artifact). So the single-qubit model is used for the **frequency**, not the coupled parameters.
- **LOM overestimates α** (isolated qubit); the real coupled α ~200 MHz (participation dilution ≈ p²).

## TODO to finalize (all lightweight, fit in 16 GB)
1. **Final verification pass** — one EPR per qubit at its tuned Lj (single pass, no Newton). Fixed 3 bugs in that cell: initialize `final = {}`, use `name=f"{qn}_final"` (not `{it}`), remove the `break`, always record `final[qn]`.
2. **Apply Lj:** `design.variables["Lj_Qn"] = "... nH"` for all four → `design.rebuild()`.
3. **Frequency-collision check (do BEFORE GDS — real gate):** the uniform 200 MHz qubit ladder + α≈200 MHz means **f01(lower) = f12(upper)** for each coupled adjacent pair (Q1–Q2, Q2–Q3, Q3–Q4) — a genuine collision (resonant |11⟩↔|02⟩, ZZ/leakage; likely why Q2–Q3 hybridized). **Decide:** keep, or restagger frequencies (e.g. 4.8/5.05/5.2/5.45) and re-tune those Lj.
4. **GDS export:** `design.renderers.gds`, point at the fake-junction library (`FakeJunction_01`), `export_to_gds(...)`.
5. Record **α ≈ 200 MHz** for all four.

## Reference
A finalization plan with runnable code for steps 2–4 is saved at
`C:\Users\giann\.claude\plans\reactive-riding-milner.md`.
