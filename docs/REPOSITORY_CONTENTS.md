# Repository Contents

**Documentation guide updated:** 24 October 2026. This is a selected research notebook, not an operational deployment package.

## Where to start

| Location | What is included |
| --- | --- |
| [Home](../README.md) and [About](../ABOUT.md) | Research purpose, reading guide and project context |
| [Research journal](../journal/README.md) | Dated field entries, hardware retrospective, design revisions and interpretation notes |
| [Methods](../methods/README.md) | Measurement meaning, quality, evidence and limitations |
| [Revision log](../revisions/README.md) | Historical component-specific revisions and their evidence boundaries |
| [Examples](#offline-examples) | One selected recorded-reading analysis and one entirely synthetic teaching example |
| [Templates](#documentation-templates) | Research-note outline and a blank change-and-exclusion ledger |
| [Architecture](ARCHITECTURE.md), [design decisions](DESIGN_DECISIONS.md) and [contributions](MY_CONTRIBUTIONS.md) | System responsibilities, reasoning and the division of work |
| `.github/`, `.gitignore` and `.gitattributes` | Issue/PR forms and file rules; no operational workflow is configured |

## Recent topics and evidence status

| Topic | Public material | Boundary |
| --- | --- | --- |
| Reference roles | [Three-role reference setup](../journal/2026-10-23-three-role-reference-setup.md) | Design revision; field validation is not established by the note |
| Measurement selection | [Sensor readiness and research data](../journal/2026-10-23-from-sensor-ready-to-research-data.md) | Initialization, receipt, measurement checks and selection are separate claims |
| Display interpretation | [Cloud and local views](../journal/2026-10-23-cloud-and-local-research-views.md) | Source, time and aggregation; figure uses fictional times |
| Backup verification | [What a recovered backup actually proves](../journal/2026-10-24-what-a-recovered-backup-proves.md) | Continuing process topic; no new backup or restoration operation reported |
| Release tracking | [From review to a traceable release](../journal/2026-10-24-from-review-to-traceable-release.md) | Historical component example and illustrative record design; no new software release |

The [journal index](../journal/README.md) distinguishes event dates, writing dates and the publication dates already recorded for earlier entries. Historical uncertainty is retained at the original evidence cutoff; a later version's result does not silently replace it.

## Offline examples

- [Reference-mass analysis](../examples/l2-reference-mass-20260922/README.md): two analysis outputs, source code and plotting requirements, based on six values transcribed from an internal measurement record. The input and generated results are selected reported measurements, not synthetic data or a full calibration dataset.
- [Valid zero, missing and invalid](../examples/valid-zero-missing-invalid/README.md): entirely invented inputs, a standard-library Python script and generated teaching outputs. It demonstrates data meaning, not sensor accuracy or system performance.

Both examples document their provenance and limitations. Neither reproduces device acquisition. Their presence does not make the operational system reproducible from this repository.

## Documentation templates

- [Research-note outline](../templates/research-note.md): question, change, evidence, limitations and next check.
- [Change-and-exclusion ledger guide](../templates/change-and-exclusion-ledger.md) and [blank CSV](../templates/change-and-exclusion-ledger.csv): observation state and analysis selection, with reasons and correction references. The CSV has column names only, no observations or decisions. Excluding an interval from analysis does not mean deleting raw records.

Only the named blank ledger CSV is added to the file-rule exceptions. Other CSV files remain excluded unless separately selected. A populated ledger needs its own content and publication review.

## Outside the current public edition

| Material | Current boundary |
| --- | --- |
| Operational application, dashboard and firmware source | Not included; any future release needs exact source selection, dependencies and a separate review |
| Runtime configuration, credentials and operational identifiers | Not included |
| Raw telemetry, full experimental datasets and backup originals | Not included; the bounded recorded-reading example above is a separate explicit selection |
| Operational logs, deployment receipts and authorization documents | Not included |
| Field photographs, video and private institutional material | Not included |
| Literature PDFs and formal citation metadata | Not included; external sources are linked rather than republished |

A whole research folder, backup archive or Git history must not be copied automatically. Public notes contain selected summaries and clearly labeled illustrations, not the private evidence needed to repeat every project operation.

## Reading and reuse

Read the notebook directly as Markdown on GitHub. No Pages site, CI workflow or automatic deployment is configured. License and formal citation metadata remain unspecified; this update adds neither a LICENSE nor a CITATION file. Publishing documentation is not an operational release.

[Reproducibility](REPRODUCIBILITY.md) · [Publication checklist](PUBLICATION_CHECKLIST.md) · [Home](../README.md)
