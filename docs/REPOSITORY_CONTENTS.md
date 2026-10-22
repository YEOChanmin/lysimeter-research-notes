# Repository Contents

## Included in this edition

~~~text
README.md                   Research notebook home
ABOUT.md                    Context and reading guide
journal/                    Three dated entries, a retrospective, an interpretation note and an index
examples/                   A recorded-reading analysis and a separate synthetic teaching example
methods/                    Measurement, quality, evidence and limitations
revisions/                  Component-specific revision log
templates/research-note.md   Template for future entries
docs/                       Architecture and publication guidance
.github/                    Issue and pull-request templates
.gitignore / .gitattributes  File rules
~~~

This edition contains documentation and two offline examples. The [reference-mass analysis](../examples/l2-reference-mass-20260922/README.md) includes analysis code, six values transcribed from an internal measurement record, and generated results. The separate [valid-zero, missing and invalid example](../examples/valid-zero-missing-invalid/README.md) uses entirely invented inputs to demonstrate data meaning. No operational application source, raw telemetry, full experimental datasets, field photographs or old Git history is included.

## Future material

| Material | Required preparation | Current status |
| --- | --- | --- |
| Server and dependencies | Select the base and later overlays; remove private configuration and unnecessary operational tools | Not included |
| Dashboard source | Choose explicitly between the applied r7a line and the r7b r2 candidate | Not included |
| Firmware and shared modules | Confirm device roles, applied versions and secret-free source | Not included |
| Operational-source tests | Match the chosen source and isolate network and device access; label synthetic fixtures | Not included |
| Worked-example figure | Generated from the six published reported values; scope and provenance documented | Included in the example |
| Field photographs | Review rights, identifiers, provenance and captions | Not included |
| Literature and citation metadata | Verify actual sources, source locations and publication permissions | Not included |

Raw records, operational logs, backup originals, private institutional information, authorization documents and credentials are excluded by default. A complete research folder and its Git history must not be copied automatically.

## Reading and reuse

The notebook can be read directly as Markdown on GitHub. No Pages site, workflow or automatic deployment is configured. License and formal citation metadata remain unspecified; this edition does not add a LICENSE or CITATION file.

[Reproducibility](REPRODUCIBILITY.md) · [Publication checklist](PUBLICATION_CHECKLIST.md) · [Home](../README.md)
