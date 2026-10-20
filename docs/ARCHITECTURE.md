# System Architecture

This description reflects the device-local supply transition recorded on 19 October. Executable source is not included, and the complete system was not reverified for this edition.

~~~text
Sensors → ESP32 measurement and local supply decisions
                         │ samples / states / supply events
                         ▼
                  Server reception and storage
                         │ raw data / summaries / liquid ledger
                 ┌───────┴─────────┐
                 ▼                 ▼
           Dashboard          Export and backup
                 │                 │
      Authorized management   Isolated restoration
                 │             and comparison
                 └──→ Device
~~~

## Responsibility boundaries

- **Device:** measurement, local supply decisions, execution and event reporting. An unreported active channel should not be inferred by the display.
- **Server:** reception, event storage, the ledger, queries and management paths. Keep the current structure distinct from historical server-driven supply decisions.
- **Interface:** explain values, states, timestamps and quality. Missing reports and failed queries are not normal states or zero readings.
- **Analysis:** distinguish raw, aggregated, supplemented and synthetic data. Control references and scientific estimates serve different purposes.
- **Backup:** verify preservation and restoration of specified records. Scheduler success, content verification, partial dates and complete dates are different claims.

CO2, leaf temperature, CAM and B/BV planning, installation, component tests and research readiness need their own records. Completion of a lysimeter revision does not establish integration of every related instrument.

Future server, interface and firmware publication must reconcile candidate packages with application records. The working folder, reviewed candidate and deployed version are not assumed to be identical.

[Home](../README.md) · [Evidence and limitations](../methods/evidence-and-limitations.md)
