# Starting a new cycle without losing the data trail

On 5 November 2026, I harvested the plants from the first cycle of my weighing lysimeter study and transplanted the plants for the second cycle. Routine irrigation was re-enabled the following day. When I came back to the time series, I needed to separate the start of the growing cycle from the point at which routine measurement could be assessed again.

## One changeover, two timelines

| Field record | How I use it |
| --- | --- |
| Cycle 1 harvest and Cycle 2 transplanting on 5 November | The transplant date starts the Cycle 2 field calendar. Readings collected earlier that day may still belong to Cycle 1. |
| Drainage container replacement and a firmware update during the changeover | I keep these interventions alongside the measurement record because they can affect how I interpret readings around the changeover. Their completion tells me what changed in the field. |
| Routine irrigation was re-enabled on 6 November | The restart record is the basis for the end boundary of the analysis exclusion window. Readings from that boundary onward go through the usual checks. |

Grouping the readings by calendar date alone would hide the changeover. It could also assign ordinary pre-harvest readings to Cycle 2 simply because transplanting happened later that day.

## Mark the interval and keep the readings

In my analysis record, **T** is the recorded start of the harvest intervention and **R** is the boundary based on the irrigation restart record. I recorded the transition as **[T, R)** for all devices. The window includes records at T and ends just before R. A record at R can enter the usual screening for Cycle 2. Its eventual inclusion still depends on those checks.

The rule goes into the analysis record, alongside the evidence used to place the boundaries. The original observations stay in the archive. The 6 November freeze record identifies a fixed backup copy for the defined Cycle 1 analysis period and provides for separate records of any later corrections. This lets me revisit a boundary if I find a better event record or trace a gap in an analysis export back to the device reports.

Before using an export to compare the cycles, I check how it applies the two boundaries to per-record timestamps and how it handles summaries that straddle a boundary. I also assess comparability where the setup changed. In a weighing study, plant handling, drainage and irrigation can all change the recorded mass around a transition. The recorded changeover gives those readings context for the mass-balance review.

[Earlier notes on interpreting a mass change](before-calling-a-mass-loss-evapotranspiration.md) · [Research journal](README.md)
