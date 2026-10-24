# What a recovered backup actually proves

**Drafted:** 24 October 2026  
**Evidence status:** Research-process note based on saved project records and the public notes linked below. No new backup operation, restoration trial or experimental measurement was performed for this entry.  
**Interpretation review:** Researcher review pending.

## My question

If I can recover a backup file, what can I reasonably claim about the research records inside it?

While developing my lysimeter system, I began treating backup verification as a chain of questions rather than one successful job. A file can exist without containing the interval I need. It can open without preserving every selected record. A faithful copy can also preserve incomplete or unsuitable measurements.

The [field-revision entry](2026-10-19-field-revision.md) already records this boundary: comparison of a selected subset passed, but that did not establish completion of the full-day backup. I want this new note to make the different claims easier to keep apart.

## The evidence has several boundaries

| Check | What it can support | What it does not establish alone |
| --- | --- | --- |
| File presence | A file was found at the inspected destination | Correct contents, period or source |
| Readability | The selected file can be opened and parsed | Completeness or successful restoration |
| Hash comparison | Compared bytes match the recorded reference | That the reference is complete or scientifically valid |
| Source comparison | Selected records agree with a specified source and selection | Records outside that selection or unavailable earlier versions |
| Isolated restoration | The tested software can load the selected recovered material in the tested environment | Production recovery, every dependency or every future backup |

These are separate checks, not a list of operations completed for this entry. A useful verification statement identifies the source, selected interval, software version, comparison method and unresolved scope.

## A successful old run cannot certify a new selection

Saved project reviews distinguish activating a revised backup path from confirming that newly selected document types actually appear in a subsequent archive. Those records describe different stages. An earlier runner's successful exit cannot demonstrate inclusion of material added by a later revision.

For example, consider a **hypothetical** backup that originally preserves mass records. A later revision adds installation and intervention records. Finding the older archive proves nothing about whether those additions were collected. Finding the new archive is still only a starting point: I need to check its selection and contents against the intended source. This is an illustration, not a reported run or a new result.

I also need to distinguish a record's existence from its meaning. An installation date does not establish measurement eligibility, just as a registered target does not repeat calibration. The [sensor-readiness note](2026-10-23-from-sensor-ready-to-research-data.md) explains why those decisions need their own evidence.

## An empty result needs an explanation

If a selected query returns no records, I should retain its scope and outcome. “No records returned by this query” differs from “the source contains no records,” and both differ from a measured zero. A failed query must remain a failure rather than becoming an apparently successful empty export.

Likewise, preserving current documents does not necessarily preserve every earlier edit. If the source overwrites a value, copying its latest state cannot recover a history that the source no longer retains. I need to state which history was available instead of letting the word “backup” imply more.

## What I want the next verification record to say

I want a short record of the intended selection, the actual package and version, what was compared, and what remains unverified. A limited comparison should retain that label. Restoration should use an isolated destination and documented dependencies; opening production connections or overwriting original records is not a documentation check.

This entry starts a continuing research-records topic. It does not announce that all scheduled backups, cloud checksums or restoration paths have passed. Operational logs and recovered records remain outside this public note, so readers cannot independently reproduce a project-wide recovery from it. The [reproducibility guide](../docs/REPRODUCIBILITY.md) describes the separation between offline examples and operational systems.

My professor established the overall research direction. I developed the detailed system with AI assistance; AI also assisted with this English draft. The [contribution statement](../docs/MY_CONTRIBUTIONS.md) records that division of work.

[Research journal](README.md) · [Home](../README.md)
