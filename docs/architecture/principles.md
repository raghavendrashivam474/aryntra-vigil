
Architectural Principles
All future developments of the Aryntra VIGIL system must align with these core guidelines:

1. Stable Contracts, Replaceable Implementations
Keep interfaces, schemas, and schemas of internal structures cleanly abstracted from concrete databases, file systems, or specific analytical models.

Why: Enables swapping databases (e.g., SQLite to PostgreSQL) or modeling frameworks without altering core business rules.
2. Minimal Core
Keep dependencies light. Every third-party library introduced must serve an active, validated need.

Why: Minimizes dependencies, licensing footprints, and vulnerability vectors.
3. High Modularity
Avoid bloated modules. Ensure collection, correlation, detection, and notification structures run in distinct boundaries.

4. Research-First System
VIGIL bridges system monitoring with applied engineering research.

Sandboxed configurations, synthetic generation logs, and negative research outcomes are treated as highly valuable deliverables.