# When drainage changes the meaning of a mass increase

**Written:** 27 October 2026  
**Published:** 28 October 2026  
**Category:** Measurement interpretation  
**Evidence status:** Method reasoning based on the sources and public notebook entries linked below. All numerical cases are invented. No new measurements, firmware application or field verification is reported.  
**Interpretation review:** Researcher review pending.

## My question

If water reaches a pot but its mass rises less than expected, what does that difference tell me?

My earlier [supply-evidence note](from-supply-event-to-evidence-of-delivery.md) separates device reports from physical delivery and measured quantity. Here I want to examine a different boundary: even when water enters, the pot's net mass change need not equal that input. I first need to know what the scale supports and what crosses that boundary during the selected interval.

## First define what is being weighed

For the cases below, the weighed assembly contains the pot, growing medium and plant. Drainage goes to a separate vessel whose load is not supported by the pot scale. Water that leaves the assembly therefore reduces its mass.

If the pot and collection vessel are fully supported by the same scale instead, transfer between them stays inside the combined weighed assembly. That transfer alone does not reduce its combined mass. This is a hypothetical boundary comparison, not a description or validation of the current hardware. A nearby vessel is not necessarily on the same weighing boundary.

FAO Irrigation and Drainage Paper 56 treats irrigation, storage change, evapotranspiration and deep percolation as distinct water-balance terms. Its [Chapter 8, “Soil water balance,” Equation 85](https://www.fao.org/4/X0490E/x0490e0e.htm) is a daily root-zone balance expressed in water depth. It supports keeping those terms distinct; it is not a short-event pot-mass equation or a specification for my firmware.

## Three entirely synthetic cases

**Every value in this table is invented.** Each case describes one defined interval with no evaporation, transpiration, other mass exchange or measurement error. Assume the stated drainage crosses the pot's weighing boundary and is completely collected outside it. These simplifying assumptions make the arithmetic visible; they are not established conditions in my experiment.

| Invented case | Water mass entering the pot assembly | Drainage mass leaving it | Ideal net mass change |
| --- | ---: | ---: | ---: |
| A | 60 g | 0 g | +60 g |
| B | 60 g | 20 g | +40 g |
| C | 40 g | 0 g | +40 g |

For these constructed cases only, the change is input mass minus drainage mass. B and C have the same net increase despite different inputs. The mass increase alone cannot distinguish them.

Under those assumptions, adding drainage mass to the pot's gain recovers the specified input. Real measurements need evidence for the assumptions, collection and interval before that arithmetic can estimate delivery. I keep the example in grams: conversion to volume would require a stated density assumption. These values are not readings, calibration results, controller limits or estimates of system accuracy.

## A drainage record needs context too

An increase in the collection vessel is not automatically the drainage from one particular supply event. Transit time and water retained in tubing can separate departure from the pot and arrival at the vessel. An interval may also contain drainage associated with earlier irrigation. Similar timestamps alone do not establish attribution.

I would need the collection path, compatible measurement intervals, calibration and handling records. Spills, vessel evaporation or emptying can make its mass change differ from collected inflow. Pot movement, cable forces, tare changes and instrument error can affect the scale signal without representing water transfer. The [measurement guide](../methods/measurement-and-quality.md) already calls for retaining this intervention context.

## What I can conclude, and what remains open

A small gain does not by itself demonstrate inadequate delivery. It also does not demonstrate that drainage caused the difference. A net loss is not automatically evapotranspiration, and an unchanged mass can conceal compensating input and output.

FAO's [Chapter 1, “Evapotranspiration” and “Determining evapotranspiration → Lysimeters”](https://www.fao.org/4/X0490E/x0490e04.htm) provides the broader distinction between evaporation, transpiration and measured balance terms. This note estimates neither process and does not validate their separation in the reference-pot design.

For a future interpretation, my next questions are:

- What load does each scale support, and which transfers cross that boundary?
- Do the pot, collection and supply records cover compatible intervals and the same physical path?
- Which interventions or missing records prevent a defensible comparison?

I can document those limits using the [change-and-exclusion ledger](../templates/change-and-exclusion-ledger.md), preserving original observations separately. Neither filling the ledger nor this example verifies firmware behaviour or scientific measurement performance.

## Sources and writing support

Allen, R. G., Pereira, L. S., Raes, D., and Smith, M. (1998). *Crop evapotranspiration: Guidelines for computing crop water requirements*. FAO Irrigation and Drainage Paper 56. [Official publication and contents](https://www.fao.org/4/X0490E/x0490e00.htm). The specific source locations are linked above; the numerical table is my own constructed illustration, not a reproduction of a FAO example.

My professor established the overall research direction. I developed the detailed system with AI assistance; AI also assisted with drafting and source checks for this note. Researcher review remains pending. See the [contribution statement](../docs/MY_CONTRIBUTIONS.md).

[Research journal](README.md) · [Home](../README.md)
