# About this notebook

A lysimeter system needs more than connected sensors. Its records need to explain when a measurement was taken, whether observations remain comparable after a repair, whether a supply event actually occurred, and whether the evidence can be recovered later.

This notebook connects those engineering questions with MSc research. Entries follow a simple sequence: question, decision, evidence, limitation and next question.

## Research purpose

My MSc work develops a lysimeter measurement and monitoring system to support plant-water research. This notebook examines how mass records can be interpreted and compared while acquisition hardware, calibration and field conditions change. It connects documented engineering revisions with measurement context, including supply events, missing-data meaning and intervention records.

The purpose is to make the basis for later analysis visible: what a value represents, which conditions changed, and which comparisons still need evidence. A mass decrease by itself does not establish evapotranspiration or a plant response. The [measurement notes](methods/measurement-and-quality.md) explain these distinctions, and two [design decisions](docs/DESIGN_DECISIONS.md) show how they shape the system's interpretation.

## My role and research support

I am Chanmin Yeo, an MSc researcher at PGIA, University of Peradeniya. My professor established the overall research direction. I developed the detailed design and overall implementation of the lysimeter system, with assistance from AI tools. The system was not inherited from an earlier project.

[My contributions and research support](docs/MY_CONTRIBUTIONS.md) explains these roles and links to selected work and its evidence limits.

## What you will find

- **Journal entries:** field observations, failures, revisions and open questions.
- **Methods notes:** measurement meaning, calibration, data quality and exclusion intervals.
- **Revision records:** the relationship between candidates, reviews and applied changes.
- **Worked analysis:** six transcribed reported readings with executable calculation, a figure and explicit limits.
- **Reproducibility documentation:** the requirements for future operational-source and test releases.

Literature notes may be added later. Each should identify the paper, its claims, methods, results and limitations, the relevant source locations, and questions for this system. No literature review or publication list is claimed in this edition.

## Reading the evidence

Historical plans remain distinct from later outcomes. An uncertain cause remains a hypothesis. Unless stated otherwise, dates and times use Sri Lanka Standard Time, SLT (UTC+05:30).

These pages were edited from development and field records with AI assistance. They distinguish recorded observations from interpretation and proposed work. They are not a peer-reviewed methods paper. Formal citation metadata and contributions specific to future operational-source or formal research releases remain to be documented for those releases.

[Home](README.md) · [Journal](journal/README.md)
