# Four-Qubit Superconducting Chip — Design Summary

Reference document for `final_four_qubit_chip_design.ipynb` (Qiskit Metal). Captures the goal,
the full design/simulation workflow, the final tuned values, the tooling, and the hard-won
lessons — so the work can be continued in a fresh session.

---

## 1. Goal

Design a **4-qubit fixed-frequency transmon processor** in Qiskit Metal, tune every element to a
target spec via EM simulation (ANSYS HFSS/Q3D through pyEPR/pyaedt), and export fabrication GDS.
The four transmons are arranged so each couples to its neighbours through **bus resonators** and
is individually **read out** and **driven** (charge line).

### Target specification (from the notebook)
| Quantity | Target |
|---|---|
| Qubit frequencies f01 | **4.8, 5.0, 5.2, 5.4 GHz** (Q1–Q4) |
| Anharmonicity \|α\| | 300 MHz (target); LOM predicted ~282 MHz; **achieved ~200 MHz coupled** (see §7) |
| Qubit–bus coupling g | 80 MHz |
| Qubit–readout χ | 1 MHz |
| Readout frequencies | 6.8, 7.0, 7.2, 7.4 GHz (Q1–Q4) |
| Bus frequencies | bus_12=5.8, bus_14=6.0, bus_23=6.2, bus_34=6.4 GHz |
| Readout Q_external | ~2000 (not finalised — needs a driven/port sim) |

---

## 2. Layout & geometry

- **Design class:** `DesignPlanar`; GUI `MetalGUI`.
- **Chip:** 9 mm × 6.5 mm (`size_x=9mm`, `size_y=6.5mm`), silicon.
- **CPW:** `cpw_width=10 µm`, `cpw_gap=6 µm`.
- **Qubits:** `TransmonPocketCL` (transmon with charge line), `pad_width=550 µm` main pads,
  `gds_cell_name="FakeJunction_01"` (junctions render as placeholder cells for GDS).
  - Positions: Q1 (−2420, +69) orient 180; Q2 (0, +857.6) orient 90; Q3 (+2420, +69);
    Q4 (0, −857.6) orient 270. (µm; `offset_tm=69`.)
  - Each has 3 connection pads: `readout`, and two `bus_*` pads.

### Connectivity map (buses `connect()` wiring — critical for open-terminations)
| Bus (route) | = bus name | connects | target freq | route `start` / `end` |
|---|---|---|---|---|
| **cpw1** | bus_12 | Q1 ↔ Q2 | 5.8 GHz | start=Q1, end=Q2 |
| **cpw2** | bus_23 | Q3 ↔ Q2 | 6.2 GHz | start=Q3, end=Q2 |
| **cpw3** | bus_34 | Q3 ↔ Q4 | 6.4 GHz | start=Q3, end=Q4 |
| **cpw4** | bus_14 | Q1 ↔ Q4 | 6.0 GHz | start=Q1, end=Q4 |

Each qubit's couplers: **Q1**={Readout1, cpw1, cpw4}; **Q2**={Readout2, cpw1, cpw2};
**Q3**={Readout3, cpw2, cpw3}; **Q4**={Readout4, cpw3, cpw4}. Plus per-qubit **Charge_Line1–4**
(+ `Launch_CL_Q1–4`) and readout launchpads **Launch_RO_Q1–4**. Routes are `RouteMeander`.

---

## 3. Design workflow (the methodology — thesis core)

Standard superconducting-qubit flow: **LOM (fast seed) → eigenmode length sweeps (resonators) →
EPR (final qubit Lj)**. Each stage models more physics than the last.

1. **Layout** in Qiskit Metal (§2).
2. **LOM (Lumped Oscillator Model)** — `LOManalysis(design,"q3d")`. Q3D electrostatic capacitance
   on the **isolated** qubit → capacitance matrix → analytic transmon quantization. Used to:
   - tune **pad geometry** for EC/anharmonicity, and **connection-pad widths** for g and χ
     (sweeps: readout pad → χ≈1 MHz gives **optimal readout pad_width ≈ 185 µm**; bus pads →
     g≈80 MHz);
   - produce **seed Lj** per qubit. Fast (~seconds), ~3–4% accurate, but isolated (no resonator
     loading, no distributed fields).
3. **Eigenmode length sweeps** — `Sweeping(design)` +
   `sweep_one_option_get_eigenmode_solution_data` (HFSS eigenmode). Sweep each resonator's
   `total_length`, interpolate the length that hits target frequency. Tunes the **8 resonators**
   (4 readouts + 4 buses). See §5 for results and the mode-selection lessons.
4. **EPR (Energy Participation Ratio)** — `EPRanalysis(design,"hfss")`. HFSS eigenmode (junction
   as linear inductor) → energy participation → numerical diagonalization of the cosine
   Hamiltonian. Gives the **dressed f01, anharmonicity, χ, cross-Kerr** in the coupled system.
   Used to **finalise each qubit's Lj** (the LOM seed is ~130–200 MHz off once loading is included).
   Done with **reduced per-qubit models** (16 GB RAM budget → no full-chip EPR).
5. **Remaining:** apply final Lj, frequency-collision check, GDS export (§6).

**Key physics:** LOM is the isolated seed; EPR is the coupled truth. Adding the couplers
(readout + 2 buses + charge line) **lowers f01 ~130–200 MHz** (capacitive loading) and **dilutes
the anharmonicity** from ~282 MHz (LOM) to ~200 MHz (α ∝ participation², p≈0.93). Lj is the final
knob for f01 (`f01+EC ∝ Lj^(−1/2)`, so `ΔLj/Lj = −2·Δf/(f01+EC)`); geometry sets EC/α/g/χ.

---

## 4. FINAL tuned results

### Junction inductances & qubit frequencies (per-qubit reduced-model EPR)
| Qubit | **Lj (nH)** | f01 (GHz) | target | err | \|α\| (real) |
|---|---|---|---|---|---|
| Q1 | **11.66** | 4.800 | 4.8 | 0 | ~200 |
| Q2 | **11.773** | 5.010 | 5.0 | +10 MHz | ~200 |
| Q3 | **9.993** | 5.213 | 5.2 | +13 MHz | ~200 |
| Q4 | **9.939** | 5.394 | 5.4 | −6 MHz | ~200 |

Record **α ≈ 200 MHz for all four** (the 89 / 114 / 139 values some runs showed were
reduced-model bus-collision artifacts, not real — see §8). LOM seed Lj (pad_width 550 µm, EC≈248
MHz) were ~12.7/11.8/10.9/10.2 nH; EPR trimmed them **down** ~5–8% for the coupler loading.

### Resonator lengths (`total_length`, from eigenmode sweeps, mode0 = resonator)
| Resonator | length (mm) | target (GHz) |
|---|---|---|
| Readout1 | 7.915 | 6.8 |
| Readout2 | 7.915 | 7.0 |
| Readout3 | 7.330 | 7.2 |
| Readout4 | 7.350 | 7.4 |
| cpw1 (bus_12) | 9.689 | 5.8 |
| cpw2 (bus_23) | 9.071 | 6.2 |
| cpw3 (bus_34) | 8.657 | 6.4 |
| cpw4 (bus_14) | 9.381 | 6.0 |

(Saved in `results/resonator_length_sweep/length_summary.csv`; the `*_old.csv` were stale/clamped
and should be ignored.)

---

## 5. Key tools, functions & files

- **Renderers/analyses:** `EPRanalysis` (hfss), `LOManalysis` (q3d), `Sweeping`,
  `find_resonator_length` / `guided_wavelength` (analytic CPW length seed).
- **Custom helpers in the notebook:** `connect(...)` (builds `RouteMeander` buses/readouts),
  `newton_lj(Lj, f_now, f_target, EC)` (one Newton step for Lj), `sweep_resonator`,
  `length_grid`, the per-qubit auto-tune loop, and `extract(res)` (participation-based qubit ID).
- **EPR result access (programmatic):**
  `three_mode_EPR.sim.renderer.epr_quantum_analysis.results[var]` → keys `f_0` (linear MHz),
  `f_1` (O1 PT), `f_ND` (numerical-diag), `chi_O1`, `chi_ND` (MHz; diag=anharmonicity,
  off-diag=cross-Kerr), `Pm_normed`, `Pm_raw` (participation), `ZPF`.
- **pyEPR internals used:** `epr.QuantumAnalysis(data_filename)` +
  `analyze_all_variations(cos_trunc, fock_trunc)`; `analyze_variation(var, modes=[...])` for a
  mode subset; distributed data saved at
  `C:\data-pyEPR\<Project>\<design>_hfss\<timestamp>.npz`.
- **Results dir:** `results/` (pad sweeps, `resonator_length_sweep/`, etc.).
- **Env note:** GUI needs the `qiskit-metal` (PySide2) conda env; PySide6 envs crash the GUI.

---

## 6. Remaining work (all lightweight — no more heavy EM sim)

1. **Apply final Lj** as design variables and rebuild:
   ```python
   Lj_final = {"Q1":11.66,"Q2":11.773,"Q3":9.993,"Q4":9.939}   # nH
   for q,v in Lj_final.items():
       design.variables[f"Lj_{q}"]=f"{v} nH"; design.variables[f"Cj_{q}"]="0 fF"
   design.rebuild()
   ```
   (Lj is a *fab* parameter — junction area/oxidation — so this documents the target; it does not
   change the GDS geometry.)
2. **Frequency-collision check** (before GDS): with f01={4.8,5.01,5.21,5.39} and α≈200, the
   **uniform ~200 MHz ladder** puts `f01(lower) ≈ f12(upper)` for coupled adjacent pairs
   (Q1-Q2, Q2-Q3, Q3-Q4) — a real collision type (resonant |11⟩↔|02⟩, ZZ/leakage). Decide: keep
   (if gates tolerate) or **restagger targets** (e.g. non-arithmetic set) and re-tune the moved
   qubits' Lj with the single-qubit loop.
3. **GDS export** — junctions are `FakeJunction_01`; point `design.renderers.gds` at the
   `Fake_Junctions.gds` library, then `export_to_gds("four_qubit_chip.gds")`.
4. **(Optional) readout κ / Q_external** — needs a *driven/port* simulation (not eigenmode).
5. **(Optional) full-chip EPR** — for authoritative χ/ZZ and the real close-qubit hybridization,
   if RAM allows.

---

## 7. Open questions / design flags

- **Anharmonicity below target:** target 300 MHz, LOM ~282, **achieved coupled ~200 MHz**. If the
  architecture needs ~300, EC must go up (smaller pads / larger `pad_gap`) → then re-trim Lj. 200
  MHz is usable for most gates.
- **Frequency crowding:** 200 MHz spacing + 200 MHz α → `f01=f12` adjacent collisions (see §6.2).
- **χ / g:** set via LOM pad sweeps (isolated); not yet re-verified in a full-wave coupled model.

---

## 8. Hard-won lessons (pitfalls & fixes — read before re-running anything)

1. **Resonator mode ID:** for these devices **mode0 (lowest) is the CPW resonator** (verified by
   E-field plots), *not* the mode picked by "closest to target" or by the `f·L`/slope heuristic —
   those are biased by end-loading and mislead. Fit the length on the field-verified mode.
2. **`np.interp` clamps silently:** an out-of-range target returns a boundary length that *looks*
   valid (this produced a stale cpw1=9.510). **Guard on frequency**, not length:
   `f.min() <= target <= f.max()`.
3. **LOM ≠ EPR:** LOM (isolated, lumped-capacitance) runs ~130–200 MHz high on f01 and ~80 MHz
   high on α vs the full-wave coupled EPR. LOM = seed, EPR = final.
4. **`run_sim` (linear) vs `run_epr` (ND):** the linear eigenmode is the plasma frequency
   (`√8EJEC`); the real f01 = that − EC (~one E_C lower). Tune Lj off the **ND** value.
5. **`chi_ND` is fragile:** with many modes or near-degeneracy the numerical-diagonalization Kerr
   comes out 0 or garbage (e.g. −0.8 MHz vs the true 203). **Use `chi_O1`** (analytic) for the
   anharmonicity; `f_ND` for the frequency is robust (it's an eigenvalue). Best: prefer `chi_ND`
   only if it's in range *and* agrees with `chi_O1`, else fall back to `chi_O1`.
6. **n_modes cost is exponential:** the diagonalization Hilbert space is `fock_trunc^n_modes` and
   `cos_trunc` matrix-powers it. **n_modes=7 caused a 252-min hang**; keep n_modes small (5–6),
   `fock_trunc≈4–6`, `cos_trunc≈5–6`. To use more solved modes cheaply, diagonalize a subset via
   `analyze_variation(modes=[...])` — but that path is index-fragile; the plain `run_epr` on 5–6
   modes is more reliable.
7. **Crash recovery:** the `.npz` (distributed analysis) is saved *before* the diagonalization, so
   a crashed `run_epr` is recoverable with `epr.QuantumAnalysis(NPZ).analyze_all_variations(...)`
   in a fresh kernel — no HFSS re-run.
8. **Junction registry lives in two places:** clear **both** `three_mode_EPR.setup.junctions` and
   `three_mode_EPR.sim.renderer.pinfo.junctions` each iteration (the latter accumulates and causes
   `validate_junction_info` AssertionErrors about stale `jj1/Lj_Q1`). Note `del_junction()`
   defaults to deleting a junction literally named `"jj"`, so it's a no-op for `jj1/jj2/...`.
9. **Bus terminations — the central tension in reduced models:**
   - **Open-terminate** the bus far ends → the bus frequency is wrong and can **collide** with the
     qubit (Q4: a bus landed on 5.4 GHz → hybridization, −130 MHz cross-Kerr, split anharmonicity).
   - **Real-terminate** (include the far qubit) → bus is correct, but the **neighbour qubit
     hybridizes** with the target when they're close (Q2–Q3: 414 MHz cross-Kerr, 0.6/0.3
     participation split — an artifact inflated by near-degeneracy where even O1 PT breaks down).
   - **Neither is perfect** in a reduced model; the frequencies are fine either way (~few MHz), the
     hybridized cases only corrupt the **anharmonicity/χ**. A clever mitigation used late: include
     neighbour pads for correct bus termination **but pin the neighbour Lj huge (~1000 nH)** so its
     mode drops below `min_freq_ghz` and can't hybridize.
10. **Identify the qubit by participation**, not `argmax(chi)`: the qubit mode is the one with the
    largest **junction participation** (`Pm_raw`/`Pm_normed`). Flag "not clean" when participation
    is low or a second mode shares it (hybridization). Anharmonicity dilutes as participation² — a
    low α with split participation ⇒ artifact, not a real qubit change.
11. **Tolerance sanity:** `err = (target_GHz − f01)*1e3` is in **MHz**. A qubit at 5.29 for a 5.2
    target is **90 MHz** off, not "close." Design-centering tolerance ~15–30 MHz is sensible (the
    reduced model itself carries ~few–10 MHz systematic uncertainty; 90 MHz is a coarse pass only).
12. **ANSYS connection:** a hang at `get_app_desktop()`/`GetAppDesktop()` (COM) means the renderer
    lost its ANSYS link and is trying to reconnect to a closed/unresponsive/dialog-blocked ANSYS —
    open ANSYS Electronics Desktop, clear dialogs, restart the kernel + re-run setup cells if needed.

---

## 9. Status snapshot
- **Layout:** complete. **LOM pad tuning (EC/g/χ):** complete (readout pad ≈185 µm; bus pads tuned).
- **Resonator lengths:** complete (§4). **Qubit Lj / f01:** complete, all within ~13 MHz (§4).
- **Anharmonicity:** ~200 MHz all four (record this; ignore reduced-model artifacts).
- **Not done:** apply-Lj + collision decision + GDS (§6); optional readout κ and full-chip χ/ZZ.
