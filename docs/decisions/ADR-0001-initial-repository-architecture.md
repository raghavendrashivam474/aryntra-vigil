
ADR-0001: Initial Repository Architecture
Status
Approved

Context
Aryntra VIGIL requires a clean, standard-compliant development structure that establishes a predictable repository baseline before complex correlation, detection, or telemetry tools are built.

Decision
We established a standard Python-centric directory structure optimized for testing, isolated research, and documentation integrity.

Key Decisions:
Pyproject.toml Integration: Utilized Python's PEP 517/621 standard pyproject.toml to contain structural, build, dependency, and lint metadata under a single file.
Logical Isolation: Sub-split unit/integration tests and research experiments early to maintain pristine production package directories.
No Empty Placeholder Dirs: Retained actual implementation folders (src/vigil/core) but intentionally bypassed skeleton placeholder directories (src/vigil/prediction, etc.) until their logical development sprint begins.
Consequences
Future developers have clean import paths.
Local installs with editable environments (pip install -e .[dev]) are fully supported.
Clear segmentation ensures experimental sandbox tests cannot leak into core modules.