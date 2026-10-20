# Moving Supply Decisions to the Device

**Record date:** 19 October 2026 · **Category:** Field revision  
**Status:** Summary of field and verification records, edited on 20 October 2026  
**Basis:** Field log, closeout report and r7a correction-review report  
No devices, cloud services or USB backups were rechecked while preparing this entry.

## A change in responsibility

The field records describe the transition to supply decisions made locally by each ESP32. The server connects measurement reception, event storage, queries and authorized management actions. The dashboard explains states reported by the devices.

That transition needs a more detailed account than simply saying that automatic supply was enabled. Manual dosing, automatic pulses, disturbance, hold states and release actions are different events.

## Making the interface reflect uncertainty

Soil-temperature and trial TDS displays were added, followed by a six-channel status board for water and nutrient supply across L1, L2 and L3. Alerts were grouped and the home view reorganized to make status and warnings easier to inspect. The field log records application of the r6 and r7a interface revisions.

Independent review identified cases where incomplete reports appeared normal and where a pulse with an unknown channel was presented as confirmed supply activity. The correction review records resolution of four findings, with no new P1/P2 findings identified within the reviewed changes. That scoped result does not guarantee system-wide safety or scientific accuracy.

## Lessons from the field

Repeated restarts and power-path problems were investigated separately. The records describe LittleFS-access crashes on L1 and L2, a recovery-handling revision, and separate power-connection repairs. The initial cause of filesystem corruption remains a hypothesis.

Lifting the L2 pot produced a mass disturbance associated with automatic water supply and a subsequent hold. The supply event remains in the ledger with its intervention context. Preserving the event and deciding how to treat the affected mass interval in analysis are separate tasks.

## What was supported by the records?

| Evidence | Recorded outcome | What it does not establish |
| --- | --- | --- |
| Field observation and device reports | Initial automatic supply, observed L3 nutrient inflow and stopping, followed by a report that verification ended | Measured volume for every pulse or long-term unattended reliability |
| Interface correction review | Resolution of findings concerning missing state, unknown channels and tab visibility | Complete verification of every operational screen and device condition |
| Comparison of a subset of the day's records | Five water events and one nutrient event; comparisons covering 45 documents and 13 files passed | Completion of the full-day backup for 19 October |

Pulse duration multiplied by nominal flow is an accounted volume, not a measured delivered volume. Verification of a subset of records must also remain distinct from the next scheduled full-day backup.

## Open questions

- How should replacement, calibration and cable-tension effects be represented as analysis intervals?
- How should intermittent soil-temperature reception and uncalibrated TDS indices be marked for quality?
- How can comparisons avoid treating the pre-transition and post-transition periods as an unchanged experimental protocol?

[Previous: design questions](2026-10-16-revision-questions.md) · [Next: bilingual display](2026-10-20-bilingual-dashboard.md) · [Journal index](README.md)
