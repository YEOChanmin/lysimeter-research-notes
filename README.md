# Lysimeter Research Notes

### Building, measuring and learning from an ESP32-based lysimeter system

This notebook follows the development of a lysimeter system for MSc research: the questions behind design decisions, the problems encountered in the field, and the evidence used to evaluate changes.

The focus is on making the reasoning traceable. What changed? What was observed? What remains uncertain?

> **Documentation edition: 20 October 2026.** This repository contains research notes and documentation templates. Application code, firmware, experimental datasets and field photographs are not included. Historical results below are summaries of local records; preparing these pages did not involve new operational tests.

## Start here

1. [About this notebook](ABOUT.md): research context and reading guide.
2. [Research journal](journal/README.md): design questions, field revisions and follow-up work.
3. [Methods notes](methods/README.md): measurement meaning, data quality and limitations.
4. [Revision log](revisions/README.md): candidate development, review and field application.

## Recent entries

| Date | Entry | Evidence status |
| --- | --- | --- |
| 20 Oct 2026 | [Bilingual interfaces and chart export](journal/2026-10-20-bilingual-dashboard.md) | Revised candidate; deployment unconfirmed in the records reviewed |
| 19 Oct 2026 | [Moving supply decisions to the device](journal/2026-10-19-field-revision.md) | Field records and verification of a subset of records |
| 16 Oct 2026 | [Keeping the data trail intact](journal/2026-10-16-revision-questions.md) | Historical design questions |

## Research questions

- How can device decisions, physical actions and stored events be traced to the same supply operation?
- How should missing measurements, failed queries and valid zero values be distinguished?
- What comparisons remain valid across hardware replacement, recalibration and manual intervention?
- What evidence shows that supply events have reached both the ledger and the backup?

These are research directions. This notebook does not establish improvements in crop performance, evapotranspiration accuracy or long-term reliability.

## Explore the system

| Topic | Contents |
| --- | --- |
| [Architecture](docs/ARCHITECTURE.md) | Boundaries between sensing, device decisions, storage and display |
| [Measurement and quality](methods/measurement-and-quality.md) | Mass, dose accounting, temperature and uncalibrated TDS indices |
| [Evidence and limitations](methods/evidence-and-limitations.md) | What different forms of verification support |
| [Repository contents](docs/REPOSITORY_CONTENTS.md) | Included documentation and future source selection |
| [Reproducibility](docs/REPRODUCIBILITY.md) | Requirements before publishing executable code |
| [Publication checklist](docs/PUBLICATION_CHECKLIST.md) | Checks for future additions |

Raw records and failure evidence are retained separately. Public entries present selected summaries. License and formal citation metadata have not yet been specified.
