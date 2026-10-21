# My contributions and research support

**Researcher:** Chanmin Yeo  
**Context:** MSc research, PGIA, University of Peradeniya  
**Updated:** 21 October 2026

## The research question behind this notebook

My focus here is a practical measurement question: how can lysimeter records remain interpretable and comparable when acquisition hardware, calibration and field conditions change?

This notebook documents the development process, the evidence available for particular decisions, and the checks that remain open. It does not present a completed thesis or a general validation of the whole system.

## My role and the support I receive

My professor established the overall research direction. I developed the detailed design and overall implementation of the lysimeter system for my MSc research, with assistance from AI tools. The system was not inherited from an earlier project.

| Contributor | Role |
| --- | --- |
| Chanmin Yeo | Detailed system design and overall implementation for this MSc project |
| My professor | Overall research direction and guidance |
| AI tools | Assistance with software development, the selected offline analysis example, and preparation of these research notes |

This is my account of the division of work. The use of AI assistance is part of that account: the repository should not be read as a claim that I wrote every line of code or documentation without assistance. Specific contributions to future formal research outputs will be described for those outputs.

## Selected work documented here

| Area | What a reader can inspect | Evidence boundary |
| --- | --- | --- |
| Measurement development | [HX711-to-ADS1256 retrospective](../journal/from-hx711-to-ads1256.md) | A history of decisions; no controlled comparison establishing that one ADC is more accurate |
| System integration | [Architecture and responsibility boundaries](ARCHITECTURE.md) | A description of device, server, interface and backup roles; the full operational source is not published here |
| Field revisions | [Device-local supply and interface revisions](../journal/2026-10-19-field-revision.md) | Selected recorded observations and scoped reviews; not proof of long-term unattended reliability |
| Measurement interpretation | [Measurement and quality notes](../methods/measurement-and-quality.md) | Calibration boundaries, interventions and missing-data meanings; not a completed analysis protocol |
| Reproducible analysis | [L2 reference-mass worked example](../examples/l2-reference-mass-20260922/README.md) | Code, inputs and a figure for six transcribed reported readings; not raw telemetry or a full sensor validation |

These pages let readers inspect selected work from the project. They do not independently establish who performed every individual wiring, coding or experimental step. The role statement above distinguishes my overall responsibility from the support I received.

## How to read AI-assisted work

AI tools have assisted both development and communication. The published offline example and the English research notes were prepared with AI assistance. Experimental observations come from project records, not from an AI tool observing the equipment.

An executable calculation, a software review and a field observation support different claims. I keep those distinctions visible in the notebook, together with [evidence limits](../methods/evidence-and-limitations.md) and [reproducibility requirements](REPRODUCIBILITY.md).

## Questions I am carrying forward

- How should small mass changes be checked with repeated loading and removal under documented conditions?
- How should replacement, calibration and physical interventions define comparable analysis intervals?
- What additional versioned data and acquisition context would let another reader reproduce an analysis beyond the small worked example?

[About this notebook](../ABOUT.md) · [Home](../README.md)
