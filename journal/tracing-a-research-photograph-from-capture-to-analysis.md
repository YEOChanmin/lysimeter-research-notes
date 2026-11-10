# Tracing a research photograph from capture to analysis

When photographs arrived around a growing-cycle changeover, I could see that the files had reached the server. The accompanying labels still needed checking against the new plant assignments. For camera-based analysis, I need to be able to trace both when a frame was captured and which plant it shows.

## Three records to keep together

| Record | What I use it to check |
| --- | --- |
| Server receipt time | When a file reached the collection system. A queued file can arrive after newer images have been captured. |
| Capture time and clock evidence | When the camera recorded the scene, how the timestamp was established and whether the time zone and clock status are known. |
| Plant and cycle assignment | Which plant was in the camera's view at capture. The original label and any corrected assignment remain traceable. |

## A worked example with fictional metadata

Suppose a fictional camera starts viewing a different plant at 10:00 UTC. All times, assignment labels and frames below are invented. Each frame still needs image and geometry checks before measurement.

| Frame | Capture evidence | Receipt time (UTC) | Original cycle label | Assignment review |
| --- | --- | --- | --- | --- |
| Demo A | 09:55 UTC, clock synchronization recorded | 10:12 | Before change | The capture precedes the switch. Check the earlier plant assignment even though the file arrived later. |
| Demo B | 10:05 UTC, clock synchronization recorded | 10:06 | Before change | The capture follows the switch. Check the new plant assignment against the changeover log and retain the original label with any correction. |
| Demo C | Capture time uncertain, camera clock status unknown | 10:07 | After change | Leave the assignment for review until another record establishes when the frame was captured. |

When an assignment is confirmed, I record its evidence and keep the original metadata available for audit. For a projected leaf area analysis, I also check that the relevant plant and reference objects are visible and that the frame has the geometry information required by the method. This gives me a record of both the image's identity and its eligibility for the intended analysis.

[Notes on freezing the area method](freezing-an-analysis-method-before-the-next-dataset.md) · [Research journal](README.md)
