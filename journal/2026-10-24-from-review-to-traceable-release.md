# From a passing review to a traceable release

**Written:** 24 October 2026  
**Category:** Research software and evidence tracking  
**Evidence status:** Interpretation of the public historical records linked below. No new release, deployment or performance result is reported. Researcher review of this interpretation is pending.

## My question

When a review says that a change has passed, how do I know which running system that statement describes?

In my lysimeter work, similar revision labels have appeared in different components. The public [revision log](../revisions/README.md) records a sensor-firmware r7b correction on 19 October and a dashboard r7b r2 candidate on 20 October. These are different changes. The firmware record includes application and short observation windows. The dashboard article records author-reported corrections, with independent confirmation and deployment unconfirmed in the records reviewed for that article.

A bare label such as “r7b passed” would lose both the component and the evidence boundary. I need a record that connects a particular review to a particular candidate, then connects that candidate to any later application evidence.

## A small trace, rather than a single status

The following is an illustrative record design, not a report that all checks have been completed for a current release.

| Link in the trace | What I would record | What that record alone would not establish |
| --- | --- | --- |
| Candidate identity | Component, purpose, source snapshot and digest | That the candidate was reviewed or installed |
| Reproduction context | Dependencies, configuration boundary and actual build environment | Behaviour in every environment allowed by a version range |
| Review | Exact candidate, questions examined, findings and correction checks | Absence of defects outside the review scope |
| Build | Inputs used and the resulting artifact identity | That this artifact reached the intended system |
| Application | Identity checked against the intended artifact and a bounded application receipt | Correct measurement or long-term field performance |
| Follow-up | Observations for the relevant conditions and interval | Scientific validity beyond those observations |

A digest helps identify bytes. It does not explain their meaning, prove that the source is correct or replace a measurement check. The manifest also needs to say which files it covers: one interface overlay cannot identify the entire server, its dependencies and the firmware.

## What happens when the candidate changes?

The [bilingual-interface entry](2026-10-20-bilingual-dashboard.md) provides a useful historical example. It separates findings in r1 from corrections reported for r2. It does not promote the earlier review into independent confirmation of the revised candidate.

I want to preserve that distinction when following up a small fix. The earlier review remains evidence about the earlier snapshot. For the changed candidate, I need to identify the difference, decide which checks it affects and record the new results. Unchanged portions may still have useful prior evidence; that is different from declaring the whole candidate independently verified.

This also helps with open findings. A later correction should refer back to the finding and the affected component. A remaining limitation should stay visible when the candidate is applied. A successful installation does not turn an unresolved issue into a closed one.

## A public archive is another artifact

Publication introduces a further boundary. Removing private configuration or replacing an operational value changes the files. An original manifest may therefore no longer match the public derivative. I should preserve the original evidence separately and identify the selected public copy on its own terms, explaining the transformation without revealing private values.

An archived source snapshot may help trace development while still being unsuitable for execution. Missing configuration, dependencies or deliberately omitted components must remain explicit. I should not call a documentation archive a runnable release merely because it contains source files, nor treat uploading it as a deployment test.

## What this changes in my research notebook

For each future release case, I want the notebook to answer three questions: which component and snapshot changed, what the evidence supports, and what remains unconfirmed. Historical entries should retain their original evidence cutoff; a later result belongs in a dated follow-up linked to the same component.

The [evidence guide](../methods/evidence-and-limitations.md) and [sensor-readiness note](2026-10-23-from-sensor-ready-to-research-data.md) describe the next boundary. Even a well-traced software release does not establish sensor accuracy, complete data collection or the suitability of an interval for analysis. Those claims require their own methods and observations.

No equipment, operational service or release tool was run to prepare this note. AI assisted its English drafting; the [contribution statement](../docs/MY_CONTRIBUTIONS.md) describes my work and the support received.

[Research journal](README.md) · [Home](../README.md)
