# From three evaporation references to a three-role reference setup

**Drafted:** 23 October 2026  
**Published:** 23 October 2026  
**Evidence status:** design revision confirmed by the researcher; field cutover, calibration and valid measurement records have not been verified for this note. No new experimental data or performance results are released here.

My MSc lysimeter project started with three unplanted reference pots intended to follow substrate evaporation near the planted lysimeters. I am revising that arrangement into three references with different purposes. The change is a measurement-design decision, and it needs an explicit record rather than a new label on the old observations.

## One setup, three questions

| Reference role | Pot contents and surface | Intended observation | Acquisition path |
| --- | --- | --- | --- |
| Transpiration-oriented reference | A plant in cocopeat, with the substrate surface covered and sealed around openings | Mass loss with surface evaporation suppressed | ADS1256 |
| Evaporation reference | Cocopeat without a plant | Mass loss from an exposed substrate surface | ADS1256, separate load-cell channel |
| Instrument-comparison reference | A separate planted pot | Contemporary behaviour of the HX711 measurement path alongside the ADS1256 paths | HX711 |

There are three pots, two plants and three distinct roles. This is not a set of three biological replicates of one treatment. The phrase *reference setup* describes the measurement roles; it does not mean the standardized grass reference used for FAO reference evapotranspiration, ET₀.

## What the mass records may mean

Evapotranspiration combines substrate evaporation and plant transpiration. A cover can suppress surface evaporation, while an unplanted pot provides an evaporation reference. Surface wetness, shading and growing conditions affect these processes. These general concepts are described in [FAO Irrigation and Drainage Paper 56, Chapter 1](https://www.fao.org/4/X0490E/x0490e04.htm).

For this setup, I will initially describe the covered pot as a **transpiration-oriented reference**, not a proven measurement of pure transpiration. Residual evaporation through openings, drainage, irrigation, handling and changes in the plant must be considered when selecting intervals. “Surface sealed” does not establish that the entire pot is airtight or that its drainage outlets are closed.

Likewise, the unplanted cocopeat pot does not automatically measure the evaporation occurring beneath another pot's canopy. I need to record surface exposure, water status and irrigation history before deciding which comparisons are defensible. Adding E from one pot to T from another is not, by itself, a validated partition of a planted lysimeter's ET.

## A contemporary HX711 comparison

The [earlier HX711-to-ADS1256 retrospective](from-hx711-to-ads1256.md) identified a gap: the historical records did not establish a controlled comparison of the two acquisition paths. Keeping a planted HX711 reference can support a contemporary observational comparison.

It still uses a different pot, plant and load cell. Differences may reflect those conditions, calibration, loading or the acquisition path. I will not attribute a difference to the ADC alone or claim improved accuracy from this arrangement without further evidence.

## Preserve the transition

The previous evaporation-reference observations should keep their original identities and methods. The new roles need their own effective start times, calibration references and intervention history. I will not invent a one-to-one physical mapping from the old three pot labels to the new roles.

Before interpreting the new records, I need to establish the actual cutover, first valid observations, cover condition, calibration checks and irrigation/drainage intervals. Those are verification tasks, not completed findings in this entry.

My professor established the overall research direction. I developed the detailed system and documentation with AI assistance. This note records the reasoning behind a revision while leaving its measurement performance open to testing.

[Research journal](README.md) · [Evidence and limitations](../methods/evidence-and-limitations.md) · [Home](../README.md)
