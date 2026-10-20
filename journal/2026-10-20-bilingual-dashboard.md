# Bilingual Interfaces and Chart Export

**Record date:** 20 October 2026 · **Category:** Interface development  
**Status:** Revised r7b r2 candidate  
**Basis:** Independent review of r7b r1, the r2 candidate notes and the day's field log  
Production deployment of r2 was not confirmed in the records reviewed. Fixes are reported by the candidate author and were not independently retested for this entry.

## Why these features?

A research interface supports both field inspection and communication of findings. This candidate combines Korean/English display switching, PNG export of canvas charts and revised alert grouping. Exported figures still require separate checks of units, time ranges and data provenance before research use.

## What translation must preserve

Translating interface instructions is different from changing a researcher's notes. Independent review of r1 found that some user-written text was being translated. The r2 notes report exclusions for observations, reasons, comments and code areas, including dynamically updated text.

The review also found that an English calibration-blocking message could remain after reception recovered, and that the mobile title became compressed. Both were included in the reported corrections. Language changes therefore need checks of state display and layout as well as vocabulary.

## Information that alert grouping must retain

A sensor can be flat and outside its limits at the same time. In r1, low-limit and high-limit alerts could be combined under an unchanged-value category. The r2 notes report giving recognized limit conditions priority so that the categories remain separate.

Reducing the number of summary lines should preserve differences in the action a researcher needs to take. This revision changes display grouping, not server-side alert policy or supply decisions.

## Current stage and limitations

- Independent review of r1: one P2 and three P3 findings; changes required.
- Author-reported r2 results: four findings addressed; r7b focused checks 18/18 and r7a checks 21/21.
- Independent confirmation of r2 and production verification: completion evidence was not confirmed in the records read for this edition.
- A reported display limitation remains: a PNG button can overlap some chart-axis text. The candidate notes state that the button is not included in the exported image.

Results from an earlier version cannot substitute for evidence about the revised candidate. Successful PNG export also does not establish that a figure is publication-ready.

[Previous: field revision](2026-10-19-field-revision.md) · [Revision log](../revisions/README.md) · [Journal index](README.md)
