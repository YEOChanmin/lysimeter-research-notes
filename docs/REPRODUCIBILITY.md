# Reproducibility Preparation

This edition contains no executable source or dependency lockfile. Installation, server-start and full-system test commands will be documented only after they have actually been verified for a selected source release.

## Requirements for an executable release

1. A selected source version, defined changes, lockfile and tested runtime versions.
2. Configuration examples without operational addresses, identifiers or secrets.
3. Offline tests and clearly labeled synthetic fixtures.
4. Schemas, units, quality flags and time conventions for raw, summarized, supplemented and estimated data.
5. Separate software, device and field verification results, including unverified scope.

A runtime range in a package file is not the same as a tested range. The existence of a test script does not establish that it passed.

## Offline boundaries

- Begin without production credentials, real device addresses or operational network access.
- Direct generated files to isolated paths that cannot overwrite raw data or sealed artifacts.
- Check whether importing a module accesses an operational database or device.
- GET /api/device-command can generate commands; it is not a harmless operational status query.
- Do not automatically run release, recovery or deployment tools as reproducibility checks.

No CI workflow is included. Future automation should use explicitly selected offline-safe tests and must not acquire operational credentials or deployment rights implicitly.

## Report the evidence

| Item | Record |
| --- | --- |
| Code | Snapshot or commit, changed files and hashes |
| Environment | Actual runtime, OS and dependency versions |
| Data | Synthetic, replayed or measured; provenance and permitted scope |
| Test | Expected and observed outcomes, scope and limitations |
| Operation | Device, cloud and field confirmation separately |
| Limitations | Missing observations, replay assumptions and absence of measured delivery |

Observed mass change is not automatically evapotranspiration. Flow-based supply accounting is not direct measurement. Scientific equations should be published with their methods and verified sources.

[Repository contents](REPOSITORY_CONTENTS.md)
