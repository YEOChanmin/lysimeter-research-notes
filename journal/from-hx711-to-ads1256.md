# From HX711 to ADS1256: learning what a mass reading means

**Written:** 20 October 2026  
**Attribution corrected:** 21 October 2026  
**Development period covered:** the early HX711 configuration through 22 September 2026  
**Status:** retrospective based on selected internal project records; no new experiments or statistical reanalysis were performed for this entry.

This notebook documents my MSc research on a lysimeter system, including the transition from HX711 to ADS1256. My professor established the overall research direction, and I developed the detailed design and overall implementation with AI assistance. The system was not inherited from the earlier undergraduate project.

The early measurement path used HX711 channels for the plant platform and drainage container. Looking back, the useful story is how the questions changed: from obtaining a reading to understanding whether it represented a valid, comparable measurement.

## A displayed zero was not always a measured zero

On 19 August, the L2 development record reported that the plant HX711 was not detected at boot, while plant mass was still published as `0 g` [E1]. The communication update succeeded, but that did not establish that the mass measurement was valid.

This exposed a distinction that now guides the notebook: a valid zero, a missing observation and a sensor read failure need different meanings in the data. The record did not establish the physical cause of the detection failure.

## The transition happened in stages

L1 ADS1256 software integration was recorded on 14 September [E2], before the weekend observations discussed below. The system subsequently operated with a mixed ADC configuration. The later weekend trial therefore cannot be described as the event that initiated the first ADS1256 transition.

The integration also changed the calibration boundary. ADS1256 mass values calibrated on the device had to bypass the legacy HX711 server scaling. Applying both conversions would change the meaning of the reported mass. The integration policy also excluded uncalibrated ADS1256 values from thesis-eligible measurements [E2].

## Continuous operation raised different questions

The 18-20 September weekend report recorded abrupt L2 mass steps and recovery patterns consistent with the smoothing used at the time. It also reported an association between LED operation and step frequency [E3]. Electrical interference and mechanically transmitted vibration remained possible explanations; the association did not identify a cause.

The trial included tray and lighting interventions, so the longer-term mass change could not be treated as fixed-load sensor drift. Collection and archive completion were assessed separately from measurement stability, which remained under review [E3]. A complete data trail made investigation possible; it did not certify the measurements.

## Replacement required another set of checks

The 22 September L2 ADS1256 record reported reference-mass checks and confirmed that the legacy server factor was not reapplied. Low-load and longer-duration checks remained pending in that record [E4]. Those historical checks should not be read as a statement of today's full system status.

The reviewed records do not establish a controlled HX711-ADS1256 comparison using the same load cell and test conditions [E5]. They therefore support a history of engineering decisions, rather than a general claim that the replacement ADC improved accuracy or resolved every instability.

## Questions to carry forward

- How do repeated load-and-remove checks behave at the small mass changes relevant to the experiment?
- Which changes come from the acquisition path, and which depend on loading, wiring, lighting or vibration?
- Can another reader reproduce one analysis from an identified dataset and code version?

A follow-up [worked analysis](../examples/l2-reference-mass-20260922/README.md) reproduces calculations from six reported L2 readings. It provides a small reproducible example while leaving the acquisition and validation limits explicit.

## Record basis and access limits

These are internal record descriptions, not links to publicly available datasets. The underlying logs and full reports are not included in this documentation edition; the follow-up example publishes only a transcription and its analysis. Quantitative performance claims have intentionally been left out of this entry.

| ID | Internal record | Used here for |
| --- | --- | --- |
| E1 | L2 status-delivery update, 19 August 2026 | Missing HX711 detection and a published zero |
| E2 | L1 ADS1256 integration record, 14 September 2026 | Integration date, calibration boundary and uncalibrated-value policy |
| E3 | Weekend trial report, written 21 September 2026, covering 18-20 September | Abrupt steps, interventions, possible causes and separate stability assessment |
| E4 | L2 laboratory update and checklist, 22 September 2026 | Reference checks, conversion handling and remaining checks |
| E5 | Evidence and gap review, 8 October 2026 | Research chronology and the missing controlled ADC comparison |

**Correction, 21 October 2026:** The opening and E5 description have been corrected to remove an unsupported inference that the system was inherited from an earlier project. The researcher's account of the division of work is documented in [My contributions and research support](../docs/MY_CONTRIBUTIONS.md).

[Measurement and quality](../methods/measurement-and-quality.md) · [Evidence and limitations](../methods/evidence-and-limitations.md) · [Journal](README.md) · [Home](../README.md)
