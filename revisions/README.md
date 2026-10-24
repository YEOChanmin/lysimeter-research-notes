# Revision Log

**Compiled:** 20 October 2026 SLT. This table summarizes local records; it is not a live operational status page. Firmware and interface revisions both use the label r7b, so the component is always identified.

| Component | Date and version | Purpose | Evidence stage |
| --- | --- | --- | --- |
| Integrated design | 16 Oct proposal | Connect supply, display, storage and backup | Historical plan; not a declaration that every task is complete |
| Device-local supply | 19 Oct r10 package | Local decisions and field replacement records | Application recorded; r10 documentation and executable-code versions must be distinguished |
| Sensor firmware | 19 Oct r7b correction | LittleFS recovery handling | Upload and short observation windows recorded; long-term reliability separate |
| Dashboard | 19 Oct r6 | Soil-temperature and trial TDS displays | Application recorded |
| Dashboard | 19 Oct r7a | Six-channel board, alerts and home layout | Four review findings resolved; application recorded |
| Backup | 19 Oct D-19 | Link supply events and ledger records | Subset passed; distinct from a full day |
| Dashboard | 20 Oct r7b r2 | Bilingual display, PNG export and alert grouping | Author-reported fixes and tests; independent confirmation and deployment unconfirmed |

## Tracking the evidence for a release

[From a passing review to a traceable release](../journal/2026-10-24-from-review-to-traceable-release.md), written on 24 October 2026, uses the component-label distinction in this historical log as a case study. It adds an illustrative trace from candidate identity to follow-up evidence; it does not update the deployment status recorded above.

## Follow the reasoning

[Design questions](../journal/2026-10-16-revision-questions.md) → [Field revision](../journal/2026-10-19-field-revision.md) → [Follow-up interface candidate](../journal/2026-10-20-bilingual-dashboard.md)

Deployment commands, operational identifiers and authorization text are omitted. A future source release needs component-specific snapshots and verification scope. A UI overlay does not establish the version of the entire server or firmware.

[Repository contents](../docs/REPOSITORY_CONTENTS.md) · [Home](../README.md)
