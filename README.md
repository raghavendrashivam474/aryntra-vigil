# Aryntra VIGIL

Aryntra VIGIL is a privacy-preserving digital-environment intelligence system.

Its core conceptual vision is structured to scale sequentially:
```text
Observe → Detect → Correlate → Remember → Reason → Predict → Controlled Escalation
This repository implements S0.1 (Foundation). It establishes the canonical structure, development standards, and architectural/security boundaries before implementing active capabilities.
```
## 1. Safety Boundaries & Security Invariants
VIGIL operates under strict architectural constraints. These are hard security invariants, not optional features:

Authorized Observation Only: Active monitoring is strictly restricted to technical systems where explicitly permitted.
No Communications Interception: VIGIL does not capture, process, read, or decrypt private communications, voice, text, or application data payloads.
No Unauthorized System Access: VIGIL contains no exploitation vectors, unauthorized backdoors, persistence exploits, or stealth mechanisms.
Privacy by Design: Focus on technical operational metadata over raw data extraction.
Detection is Not Accusation: System anomalies signify variance from statistical baselines, not malicious human behavior.

## 2. Directory Structure
```text
aryntra-vigil/
├── README.md             # This file
├── LICENSE               # Proprietary Licensing terms
├── pyproject.toml        # Unified Python build & dependency metadata
├── .venv/                # Isolated virtual environment
├── src/
│   └── vigil/
│       ├── __init__.py   # Version baseline
│       └── core/
│           ├── __init__.py
│           └── system.py # Foundation lifecycle initializer
├── tests/
│   ├── unit/             # Core component logic checks
│   ├── integration/      # System flow validation tests
│   └── fixtures/         # Static test data
├── docs/
│   ├── vision/           # Long-term conceptual progression
│   ├── architecture/     # Structural design and security principles
│   └── decisions/        # Architectural Decision Records (ADRs)
├── experiments/          # Sandbox area for modeling & prototype trials
├── configs/              # Environment configurations
└── scripts/              # Local development tooling automation
```
## 3. Getting Started

### Prerequisites

>Python 3.11+ (Development tested on Python 3.13.14)

### Installation
Set up the environment and install VIGIL in editable mode with development dependencies:

```Bash

# Create Virtual Environment
python -m venv .venv
```
```bash
# Activate (Windows PowerShell)
.venv\Scripts\Activate.ps1
```
```bash
# Activate (Linux/Mac)
source .venv/bin/activate
```
```bash
# Install development build
pip install -e .[dev]
Verification & Testing
Run pytest to verify the foundational baseline:
```
```bash
pytest tests/ -v
Static Analysis & Formatting
VIGIL relies on ruff for code quality checks:
```
```bash
# Check formatting and style issues
ruff check .
```
```bash
# Apply automatic fixes
ruff check . --fix
```