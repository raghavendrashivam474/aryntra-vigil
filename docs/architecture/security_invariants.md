
Security & Privacy Invariants
These tenets represent hard security limits that must never be bypassed during any active engineering sprint.

1. Authorized Environment Scope Only
VIGIL must never perform passive or active operations against targets where scanning permissions are not explicitly declared.

2. Absolutely No Message Interception
The capture or reading of communication payloads is strictly forbidden.

Prohibited operations: Packet decryption, reading messaging databases (Slack, WhatsApp, private mail, etc.), scanning audio/voice calls, keystroke logging.
Allowed operations: Environment telemetry, authorized network routing metadata, performance system characteristics.
3. No Exploitation or Persistence Vectors
VIGIL acts solely as an analytical tracking agent, never a cyber tool.

No payload injection, exploit execution, authentication bypasses, or obfuscated stealth modules.
4. Privacy-by-Design Defaults
Data storage policies must enforce short lifecycles for high-fidelity data, moving aggregated or low-granularity features to long-term storage only.

5. Statistical Detection Is Not Accusation
Anomaly detection implies variance from standard operating baselines. It does not dictate intent or verify malicious actors. The UI and alerts must reflect statistical probability, not dynamic finger-pointing.