# A small change-and-exclusion ledger for research sensors

**Prepared:** 24 October 2026  
**Status:** Blank documentation template. No observation or data-selection decision is recorded here.

## Why I need this record

In my lysimeter work, a sensor-ready flag and a plausible chart value do not answer whether an interval belongs in a particular analysis. A channel can change roles, calibration can change, or an intervention can make neighbouring readings difficult to compare. I want those decisions to remain visible beside the data.

This ledger accompanies [From a sensor-ready flag to usable research data](../journal/2026-10-23-from-sensor-ready-to-research-data.md). Its [CSV file](change-and-exclusion-ledger.csv) contains a header only: it is a starting form, not a dataset or a completed exclusion record.

## Use it in four steps

1. **Identify the interval and question.** Give the entry a unique ID, identify the channel or role, and name the intended analysis. Record known boundaries with an explicit time zone. Leave unknown boundaries blank and describe the uncertainty in `decision_basis`; do not invent a precise cutover time.
2. **Preserve the source.** Keep the original observations and intervention records separately. Add a stable reference that an authorized researcher can resolve. A public copy should use a safe reference label rather than a private path, access link or operational identifier. Exclusion from an analysis does not mean deleting the original record.
3. **Separate observation state from selection.** A valid zero is a value; missing means no observation; invalid means an observation failed a stated check. Selection is a separate decision for a stated question. Start unresolved decisions as `pending` or `review_required`, rather than silently treating them as included, excluded or zero.
4. **Review and retain corrections.** Record the reason, supporting evidence, reviewer and decision date when a decision is made. Calibration, hardware or role changes require an explicit comparability assessment; they do not prove earlier or later data usable. Append a correction with a new entry ID and `corrects_entry` pointing to the prior entry. Preserve the earlier reasoning and avoid counting both entries as separate events.

## Fields

| Column | What to record |
| --- | --- |
| `entry_id` | Unique reference for this decision record |
| `interval_start` | Known beginning, preferably an ISO 8601 timestamp |
| `interval_end` | Known end; state whether the end is inclusive in the decision basis |
| `time_zone` | Explicit zone or UTC offset used for the boundaries |
| `channel_or_role` | Channel and the physical role relevant to this interval |
| `change_or_reason` | Change, intervention or quality concern being considered |
| `source_reference` | Stable, appropriately restricted supporting-record reference |
| `observation_state` | `valid`, `missing`, `invalid` or `unknown`, with criteria in the basis |
| `selection_status` | `pending`, `include`, `exclude` or `review_required` |
| `decision_basis` | Evidence, rule, uncertainty and boundary convention |
| `analysis_scope` | Research question or analysis to which this decision applies |
| `reviewer` | Person responsible for the decision; blank until assigned |
| `decision_date` | Date the decision was actually made; blank while pending |
| `corrects_entry` | Earlier entry corrected by this one, if applicable |

Use separate entries when one interval contains different states or roles. Overlapping intervals and corrections need deliberate reconciliation before reporting record counts.

## Limits

This form does not filter data, enforce labels, verify calibration or establish scientific validity. Completing a row does not show that a check passed. Selection for one analysis does not establish suitability for another. Review evidence and permissions before sharing a populated copy. This blank template contains no measurements or operational events and adds no reuse license.

[Evidence and limitations](../methods/evidence-and-limitations.md) · [Research-note template](research-note.md) · [Home](../README.md)
