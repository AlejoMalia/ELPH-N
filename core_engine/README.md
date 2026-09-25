# ELPH-N: Core Metrological Engine & Hardware Demonstrator
### Algorithmic Verification Engine and Hardware Specifications

This directory houses the central algorithmic implementation of the **ELPH-N · Elephant In Neuron** framework, responsible for strict verification of the 5 contract criteria ($A > 1 \iff \phi = 1$) and common-mode spatial affine error cancellation (**GATE-0**).

---

## 📂 Module Organization

```
core_engine/
├── src/                            # Executable Python algorithms
│   ├── verifier.py                 # 5-criteria cascading verification engine (CLI)
│   ├── gate0.py                    # Affine calibration and spatial correlation α solver
│   └── banco.py                    # Synthetic calibration image generator
│
├── hardware_specs/                 # Workshop drawings, tolerances, and BOM (~€260)
│   ├── plate_specifications.md     # 200x200 mm CNC plate geometry with 25 fiducials
│   └── assembly_procedure.md       # Kinematic seat assembly and dust purging protocol
│
└── test_bench/                     # Calibration images, signatures, and sample data
    ├── calib.json                  # Intrinsic optical calibration parameters
    ├── ordenes.csv                 # Blind seat-to-diameter allocation table
    ├── paquete.json                # Signed cryptographic state packet (SHA-256)
    └── *.png                       # High-resolution ground and act calibration captures
```

---

## ⚡ Quickstart Execution

```bash
# 1. Execute the GATE-0 affine cancellation model
python3 core_engine/src/gate0.py core_engine/test_bench/fid.png core_engine/test_bench/d0.png

# 2. Verify a configuration transfer act blind to the emitter
python3 core_engine/src/verifier.py verificar \
    core_engine/test_bench/paquete.json \
    'core_engine/test_bench/s*.png' \
    'core_engine/test_bench/d*.png'
```
