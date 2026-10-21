# Two design decisions behind the measurement record

**Written:** 21 October 2026  
**Basis:** Existing public research notes, linked below. This page explains their engineering reasoning; it adds no measurements or new verification results.

My role in detailed design and overall implementation, together with professor guidance and AI assistance, is described in [My contributions](MY_CONTRIBUTIONS.md). The cases below connect that work with choices and principles already documented in this notebook. They do not reconstruct unrecorded conversations or claim that every current code path has been verified.

## 1. Keep a valid zero distinct from a missing or invalid reading

### The problem in the public record

The [HX711 retrospective](../journal/from-hx711-to-ads1256.md#a-displayed-zero-was-not-always-a-measured-zero) describes a missing sensor detection alongside a published zero value. Successful communication did not establish a valid mass measurement.

### Design principle

Treat measurement validity separately from its numerical value. A valid zero, a missing observation, a sensor read failure and a failed query need distinct meanings. The [measurement and quality notes](../methods/measurement-and-quality.md#missing-data-and-aggregation) make this distinction explicit.

### Why this choice matters

Filling a missing reading with zero can make an acquisition failure look like a physical mass change. Keeping validity visible helps a reader decide whether a point can be interpreted, needs investigation or belongs to an excluded interval. It also helps avoid treating receipt of a message as proof of measurement quality.

### What remains open

The retrospective does not establish the physical cause of the sensor detection failure. This principle is not a claim that all acquisition, storage and display paths now handle every missing-data case correctly. That would require checks against the selected software version and identified records.

## 2. Define where calibration is applied

### The problem in the public record

The [ADS1256 transition notes](../journal/from-hx711-to-ads1256.md#the-transition-happened-in-stages) describe mass values already calibrated on the device. Those values had to bypass the legacy HX711 server scaling. Applying both conversions would change the meaning of the reported mass.

### Documented decision

Keep the conversion responsibility explicit: device-calibrated ADS1256 mass should not receive the legacy HX711 conversion again. Sensor origin, units and calibration context must remain associated with the value. The [calibration and intervention notes](../methods/measurement-and-quality.md#calibration-and-intervention-boundaries) explain why replacement, zero and scale changes create boundaries that later analysis must consider.

### Why this choice matters

A number may look plausible even when it has crossed the wrong conversion path. A defined calibration boundary helps separate the meaning of a reported value from the location where software happens to process it. It also makes comparisons across a hardware change a question to verify, rather than an assumption.

### What remains open

This decision does not establish ADC superiority, low-load accuracy or long-term stability. The [existing worked example](../examples/l2-reference-mass-20260922/README.md) reproduces calculations from selected reported readings; it does not validate the acquisition process or the full calibration chain.

## How these decisions connect

The first decision asks whether a value represents a valid observation. The second asks which conversion gives that value its meaning. Together they connect the [system architecture](ARCHITECTURE.md) with the notebook's central question: which records can be interpreted and compared under documented conditions?

[About this notebook](../ABOUT.md) · [Home](../README.md)
