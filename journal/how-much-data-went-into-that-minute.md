# How much data went into that minute?

When I read a minute-level export from my lysimeter system, I want to know which samples contributed to each row. A mean can look ordinary even when it comes from only part of its time window. This matters near interruptions and interventions, where the samples that survived may cover a different part of the event from the ones I expected.

## A worked example with invented data

Suppose a fictional channel expects a sample at each of four evenly spaced points in a minute. Each window includes its start and ends before the next minute begins. The cadence, values and screening decisions below are invented.

| Window | Start | +15 s | +30 s | +45 s | Received | Accepted | Mean of accepted samples |
| --- | --- | --- | --- | --- | ---: | ---: | ---: |
| A | 9 | 11 | 13 | 15 | 4 | 4 | 12 |
| B | 10 | Missing | Rejected by a quality check | 14 | 3 | 2 | 12 |
| C | Missing | Missing | Missing | Missing | 0 | 0 |  |

A and B have the same mean. In A, all four expected slots contributed. In B, one slot has no received sample and one received sample failed a check. The two accepted values come from the first and last scheduled slots. C has no mean to report. A summary that retains the accepted count, expected count and reasons for gaps makes these cases distinguishable.

## Use the flag with an analysis question

I keep coverage and eligibility separate. A display can show B with a partial-coverage label. An analysis that requires all four slots would skip B and record why. A review of data availability would keep the partial minute in its counts. Each of these uses answers a different question about the same records.

When I review an export, I look for the window boundaries, the expected schedule, the number of accepted samples and any missing or rejected slots. If sampling schedules vary, I need the expected count for the actual interval. If a minute overlaps a known intervention, I check the event boundary separately from sample coverage.

[Earlier notes on cloud and local views](2026-10-23-cloud-and-local-research-views.md) · [Research journal](README.md)
