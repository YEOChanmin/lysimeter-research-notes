# From a sensor-ready flag to usable research data

**Drafted:** 23 October 2026  
**Published:** 23 October 2026  
**Evidence status:** Research-process note based on saved project records and the public methods notes linked below. No new measurements or performance results are released here.

## My question

When a sensor reports that it is ready, how much of the measurement problem have I actually solved?

This question became concrete while updating the reference-pot system for my MSc lysimeter research. The records I reviewed from 23 October include a firmware update, brief startup checks and a later server-receipt check. Those are useful steps. They do not, by themselves, establish that the resulting measurements are accurate or suitable for a particular analysis.

I want the notebook to preserve that distinction before the records become part of a research dataset.

## The checks answer different questions

| Check | What I can say within its scope | What still needs separate evidence |
| --- | --- | --- |
| Firmware application | The specified application was written and its version checked | Whether the measurement system performs adequately in the field |
| Sensor initialization | The device reported a ready or running state during the check | Accuracy, continuity and behaviour over a longer period |
| Data receipt | The server received the selected records that were checked | Complete records for the intended interval |
| Identity and timing | A record can be associated with a channel, role, version and time when that information is verified | Whether records across a physical change are comparable |
| Measurement check | A documented check can support a bounded statement about the tested load or conditions | Performance outside that check and its uncertainty |
| Research-data selection | An interval meets the stated inclusion rules for a particular question | Suitability for a different question or experimental comparison |

This is an interpretation framework, not a report that every row has passed. It extends the public [evidence guide](../methods/evidence-and-limitations.md) and [measurement notes](../methods/measurement-and-quality.md) to the reference-pot revision.

## A calibration value is also a limited claim

After a firmware update, checking that stored calibration settings were retained helps me detect an unintended configuration change. It does not repeat the original calibration or demonstrate the accuracy of a current mass reading. The load, reference, method and conditions still need their own record.

Likewise, a plausible number on a chart is not a measurement check. An unchanged mass-acquisition function does not establish that other firmware work had no effect on collection timing. I need to keep gaps, resets and acquisition delays available for assessment rather than infer their absence from a successful startup.

## Keep exclusions visible

For the current research cycle, my project records include decisions to exclude selected auxiliary sensor channels from the research dataset. An operational display and an analysis dataset can therefore legitimately contain different selections. I need to retain the channel, applicable period, reason and decision record so that a later reader can understand the exclusion.

The [three-role reference setup](2026-10-23-three-role-reference-setup.md) adds another boundary: a channel's new role must not silently change the meaning of its older observations. Cutover, calibration, irrigation, drainage and handling belong beside the mass record when I select an interval.

Missing, invalid and excluded observations also need distinct meanings. I do not want an absent or excluded reading to become a measured zero simply because a chart or calculation expects a number. The existing [synthetic example](../examples/valid-zero-missing-invalid/README.md) illustrates the zero/missing/invalid distinction; it does not validate this hardware.

## Follow-up: a blank selection record

Added on 24 October 2026: the [change-and-exclusion ledger](../templates/change-and-exclusion-ledger.md) turns these questions into a blank record with separate observation state, analysis selection, reasons and correction links. It supplies no completed exclusions and does not establish measurement eligibility.

## What I will document next

For an interval I intend to analyse, I want to be able to answer:

- Which physical reference role and acquisition path produced it?
- Which calibration and intervention records apply?
- Which gaps or exclusions are present, and why?
- Which measurement checks support its intended use, and what remains untested?

These are documentation and verification goals, not completed findings. This note does not establish long-term reliability, ADC accuracy or a validated separation of evaporation and transpiration. The operational logs remain private, so this public summary is not an independently reproducible sensor-validation package. I did not repeat field observations or operate the equipment while preparing it.

My professor established the overall research direction. I developed the detailed system with AI assistance; AI also assisted the preparation of this English note. The [contribution statement](../docs/MY_CONTRIBUTIONS.md) describes that division of work.

[Research journal](README.md) · [Home](../README.md)
