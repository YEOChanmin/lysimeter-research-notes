# Freezing an analysis method before the next dataset

I use overhead images to estimate projected leaf area for my lysimeter study. During Cycle 1, I used a set of hand-traced leaf outlines to compare processing choices. Those images helped me choose version 6. Once they had shaped that choice, I recorded them as development data. On 3 November 2026, I recorded which version and settings I planned to carry forward into later evaluation.

## What I fixed and what I record separately

| Record | How I handle it |
| --- | --- |
| Image-processing code and settings | I record the version, file checksums and parameter set. A change that can affect estimated area through the processing rules belongs in a new version. |
| Camera and reference geometry | I can update measured inputs when the physical setup changes or a measurement is corrected. I record the source and which images the change affects so another person can reproduce the run. |
| Decisions about individual images | I keep a separate record of the image, the reason for the decision and any override. An override can change an image’s eligibility or interpretation, so the decision has to remain visible. |

An update on 4 November made contact with the edge of the analysis region visible as a flag. I record that change separately because a flag can change which images contribute to a summary, even when the area calculation stays the same. The image selection rule is part of the analysis record.

## When a later image can be used for evaluation

For an independent evaluation, I need a documented image set and reference outlines. For each candidate image, I need to verify that its camera metadata and geometry are suitable and that the image and its reference were both kept separate from tuning and version selection. I track images used to investigate or refine the method separately.

If evaluation leads me to revise the area calculation, I will record the revision under a new version and label the results used to guide that revision as development evidence. An independent assessment of the revised version would require a separate set. The freeze gives me a way to trace what I used when I eventually report a comparison against independent reference outlines.

[Earlier notes on tracking changes through a release](2026-10-24-from-review-to-traceable-release.md) · [Research journal](README.md)
