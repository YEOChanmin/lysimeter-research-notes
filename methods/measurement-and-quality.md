# Reading Measurements in Context

**Basis:** Local revision records reviewed on 20 October 2026. This is an interpretation guide rather than a completed analysis protocol.

| Item | Preserve in the record | Avoid |
| --- | --- | --- |
| Pot and drainage mass | Sensor, time, calibration identifier, unit and intervention | Treating every mass decrease as evapotranspiration |
| Accounted supply volume | Whether volume is calculated from nominal flow and pulse duration or directly measured | Labeling nominal mL as measured delivery |
| Soil temperature | DS18B20 origin and missing/error states | Filling gaps with DHT22 air temperature |
| Trial TDS display | Raw mV, uncalibrated index, sample time and trial state | Unvalidated conversion to measured EC or ppm |
| Supply events | Manual, automatic, disturbance-induced and hold-related events | Removing disturbed events from the ledger or treating them as routine observations |
| Time | Measurement, reception, aggregation and display timestamps | Replacing an older measurement time with the latest device-reception time |

## Calibration and intervention boundaries

Record sensor replacement, zero and scale changes, restarts, cable tension, pot movement and manual dosing as events. Whether measurements remain comparable across those events requires evidence.

The 19 October field records contain replacements, calibration changes, pot movement and exclusion intervals. This documentation release neither creates analysis files nor applies new exclusions. Analysis needs the confirmed research log, precise timestamps and the relevant raw-data version.

## Missing data and aggregation

A valid zero, an absent measurement, a failed query and an invalid sample are different states. Do not fill gaps with zero for convenience. Minute or hourly summaries may not preserve every sample-level trial field, so a summary chart should not be mistaken for the last raw measurement.

[Methods index](README.md) · [Evidence and limitations](evidence-and-limitations.md)
