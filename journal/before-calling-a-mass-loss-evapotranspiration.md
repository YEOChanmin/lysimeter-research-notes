# Before calling a mass loss evapotranspiration

**Written:** 3 November 2026  
**Published:** 3 November 2026  
**Category:** Literature / measurement interpretation  
**Evidence status:** A focused methods reading. Paper findings, my interpretation and proposed checks are distinguished below. No new experimental data are released.  
**Source check:** Cited passages, Table 1 and Figure 3 were checked directly in the publisher PDF supplied for review. This is a focused reading, not an exhaustive assessment of the study.  
**Interpretation review:** Researcher review pending.

## My question

What evidence would let me interpret a decrease in a weighing record as evapotranspiration (ET)?

My earlier [drainage note](when-drainage-changes-a-mass-increase.md) uses invented cases to show why a net mass change does not identify the individual transfers that produced it. For this reading, I want to move from that accounting question to the decisions required before calculating ET from a record.

## The paper I am reading

Evett, S. R., Colaizzi, P. D., Marek, G. W., Copeland, K. S., and Ruthardt, B. B. (2025). *Analysis and quality control of weighing lysimeter water storage data*. **Agricultural Water Management, 317**, 109674. [DOI and article](https://doi.org/10.1016/j.agwat.2025.109674). Bibliographic details were cross-checked against the [USDA ARS publication record](https://www.ars.usda.gov/research/publications/publication/?seqNo115=417947).

### Findings selected for this note

- **C1 — Method and scope.** The paper describes a spreadsheet workflow for five-minute lysimeter storage records that separates ET and other water-balance components. The abstract reports application to over thirty years of records, with examples from 2018. **Location:** Abstract, p. 1; Section 1, pp. 1–2.
- **C2 — Weighing boundary.** At Bushland, drainage enters tanks supported by the lysimeter. That internal transfer does not change the combined weighing signal; tank emptying does. **Location:** Section 2.2, pp. 3–4.
- **C3 — Classification.** Automatic flags need human checking because noise can produce false event classifications. Activity logs help review them. **Location:** Section 2.2 and Table 1, p. 4.
- **C4 — Calculation check.** Daily ET calculated from adjusted storage is compared with a calculation using water-balance components. **Location:** Section 2.2.2, pp. 6–7.
- **C5 — Reported example.** Figure 3 describes a 0.27 mm ET overcalculation when closely spaced intervention spikes are processed without the authors' `NL` flag. In that procedure, `NL` prevents selected event-boundary ET-rate calculations. **Location:** Section 2.2.1.3, pp. 5–6; Figure 3 and caption, p. 6. This is one reported processing example, not an accuracy specification.
- **C6 — Accuracy evaluation.** The authors explicitly distinguish calculation cross-checks from independent ET accuracy evaluation. Their approach uses calibration and a separate field soil-water balance based on neutron-probe profile measurements, irrigation and precipitation. **Location:** Section 3.2.2, p. 13.

The locations above refer to the [article](https://www.sciencedirect.com/science/article/pii/S0378377425003889). Page references follow the article pagination, counting the unnumbered first page as p. 1; they match the PDF page numbers in the supplied copy. In Figure 3, the displayed daily adjusted-storage values for day 183 are 5.55 mm in panel (a) and 5.82 mm in panel (b). Their difference is 0.27 mm, consistent with the caption. This checks the displayed arithmetic, not the underlying spreadsheet or measurements. These millimetres are water depth, not pot mass in grams.

## My interpretation: identify the assembly before naming the process

C2 makes the physical boundary the first question I would ask. For a future pot record, I would draw what the scale actually supports: pot, growing medium, plant, tubing and any supported collection vessel. I would then identify which transfers cross that boundary. A label such as “drainage” is not enough to specify the sign or timing of its effect on that scale.

This connects to my earlier note, but it does not establish the current arrangement or performance of my hardware. I would need the actual installation and handling record for the interval being analysed. I should not choose a correction merely because a trace resembles an example in a paper.

## My interpretation: choose evidence for the claim

C4 and C6 help me separate two questions: did the processing account for its components consistently, and how well does the resulting estimate represent the physical process? The paper itself makes this distinction; it is not a new finding of my notebook.

For my system, I would ask whether two calculations share the same mass record, calibration or event decisions. Agreement could then coexist with a shared error. Before making a performance claim, I would need a justified reference, an uncertainty assessment and an explicit comparison interval. A separate comparison can also share some inputs, so I would document those dependencies rather than treat the word “independent” as a guarantee. I have read the paper's description of its accuracy-evaluation approach; I have not reproduced that evaluation or assessed all of its supporting studies.

## My interpretation: preserve the decision behind a correction

C3 and C5 lead me to a documentation question: could another reader reconstruct why I classified an interval and how that choice affected the calculation?

For a future analysis, I would keep the original observations separate from derived values and record the event source, interval, reason, reviewer and later corrections. The existing [change-and-exclusion ledger](../templates/change-and-exclusion-ledger.md) is a starting point for recording those decisions. Using it would not itself validate a classification. An event flag, a numerical adjustment and exclusion from a particular analysis are different decisions.

When evidence cannot distinguish possible causes, I would retain that uncertainty rather than assign a definite ET interpretation. This is a proposed approach; no current research interval has been corrected or excluded for this note.

## What I would check next

Before adapting any part of the method, I would ask:

1. What is on each weighing boundary, and when was anything added, removed or handled?
2. Do mass records, delivery observations and intervention logs cover compatible intervals and time conventions?
3. What evidence supports each event classification, including cases in which several events overlap?
4. Which checks assess processing consistency, and which assess measurement performance against a separate reference?

I have not run the authors' spreadsheet, reproduced their reported result or implemented their flags. This reading does not select correction thresholds, validate ET or separate evaporation from transpiration in my reference-pot setup. The [three-role design note](2026-10-23-three-role-reference-setup.md) remains a design account with its own limitations.

My immediate output is a set of questions for a defensible analysis, rather than an ET result. A later worked example could explore the decisions with explicitly synthetic records, after the assumptions and method have been reviewed.

## Sources, review and writing support

The paper citation and stable source links appear above; all summaries are in original wording. No paper PDF, figure, dataset or spreadsheet is redistributed. This is a selective reading of the cited passages, not an exhaustive review of the study or a comparison of all available processing methods.

My professor established the overall research direction. I developed the detailed system with AI assistance; AI also assisted with preparing this note and checking source locations. The first-person interpretation is proposed wording for researcher review. See the [contribution statement](../docs/MY_CONTRIBUTIONS.md).

[Research journal](README.md) · [Home](../README.md)
