# Keeping the Data Trail Intact

**Record date:** 16 October 2026 · **Category:** Design note  
**Status:** Historical proposal, summarized on 20 October 2026  
**Basis:** Local integrated-revision proposal and preparation plan

## The starting question

Does a measurement appearing on a dashboard mean it is ready for research use? This revision began by asking whether supply decisions, cloud records, dashboard states and backups preserved the same meaning throughout the system.

Moving supply decisions to the device also requires the server and interface to describe the resulting events consistently. Backups need to include the new event records and liquid ledger, rather than only the older measurement paths.

## Design direction

The first goal was to separate device decisions and execution from server recording. The second was to keep unknown states distinct from normal operation and numeric zero. The third was to go beyond checking that files existed: exported records should be readable and comparable in an isolated restoration workflow.

The intended approach was to preserve working code and address specific defects and mismatched connections.

## What this stage did not establish

Initial failure hypotheses must remain separate from subsequent observations. Power-path problems and repeated restarts should not automatically be assigned the same cause. A preparation plan is not evidence that an installation succeeded.

There were no long-term reliability or research-performance comparisons at this stage. The next entry follows the field revision and its remaining uncertainties.

## Follow-up questions

- Can device reports, server events and liquid-ledger entries be linked to the same operation?
- Can analysis distinguish intervals before and after hardware replacement or calibration?
- Have partial restoration checks and full-day scheduled backups been assessed separately?

[Next: field revision](2026-10-19-field-revision.md) · [Journal index](README.md)
