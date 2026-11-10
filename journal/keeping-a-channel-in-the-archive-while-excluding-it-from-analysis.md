# Keeping a channel in the archive while excluding it from analysis

My weighing lysimeter system recorded a channel intended to track total dissolved solids (TDS). When I reviewed the variables for the first two cycles, I set that channel aside for research analysis and retained the original records. I treated dashboard visibility as a separate decision. This matters when I return to an old export and find a column that does not appear in my analysis table.

I use three questions when reviewing a channel. Was an observation saved, and what checks did it pass? Should the dashboard show this series? Does the observation qualify for the analysis I am doing? Those answers can differ for the same record. A reading can pass a basic recording check while still being unsuitable for a particular analysis.

## Worked example with the blank ledger

The service event, dates, channel, source labels and reviewer below are fictional. They illustrate the [change-and-exclusion ledger](../templates/change-and-exclusion-ledger.md) using its [blank CSV header](../templates/change-and-exclusion-ledger.csv).

Imagine that a monitoring channel continues to record while its sensor is isolated for service. The saved observations pass the example’s basic format and timestamp checks. During isolation, however, the sensor is outside the system the daily trend is meant to describe. The first service note gives 09:40 UTC as the reconnection time. A later reconnection record confirms that the sensor was back at 09:25 UTC, so the reviewer appends a corrected decision.

```csv
entry_id,interval_start,interval_end,time_zone,channel_or_role,change_or_reason,source_reference,observation_state,selection_status,decision_basis,analysis_scope,reviewer,decision_date,corrects_entry
EX-01,2099-03-10T09:10:00Z,2099-03-10T09:40:00Z,UTC,Demo monitoring channel,Sensor isolated for service,DEMO-SERVICE-NOTE,valid,exclude,"Format and timestamp checks passed. The service note places isolation in [start, end).",Demo daily trend,Example reviewer,2099-03-10,
EX-02,2099-03-10T09:10:00Z,2099-03-10T09:25:00Z,UTC,Demo monitoring channel,Reconnection time corrected,DEMO-SERVICE-NOTE + DEMO-RECONNECT-RECORD,valid,exclude,"Format and timestamp checks passed. The reconnection record corrects the end of [start, end).",Demo daily trend,Example reviewer,2099-03-11,EX-01
```

Both decisions stay in the ledger, and `EX-02` is the active exclusion for the demo daily trend. A reading at 09:15 is inside that window. A reading at 09:25 or 09:30 is outside it and goes through the normal checks for the trend. No readings need to be removed from the archive. The correction changes where one exclusion ends, and the analysis counts it as one exclusion.

When I hand off an analysis, I want someone else to be able to start from the saved observations and explain the same selection. The ledger records the scope of that selection and the evidence behind it.

[Earlier notes on observation and selection](2026-10-23-from-sensor-ready-to-research-data.md) · [Research journal](README.md)
