# From an archived file to a traceable analysis input

As I prepare analysis for my lysimeter study, I need to follow a result back through the processing run to the observations it used. The first step is to identify the input file precisely. I then need a separate record of how its contents were interpreted and selected.

## A small example with invented files

The following filenames, timestamps and values are fictional. Each CSV block uses UTF-8, LF line endings and a final newline. The hash entries below describe those exact bytes.

`demo-original.csv` and `demo-copy.csv` both contain this text.

```csv
time_utc,value
2099-03-10T09:00:00Z,10
2099-03-10T09:01:00Z,12
```

A third file, `demo-v2.csv`, uses a different column name.

```csv
time_utc,reading
2099-03-10T09:00:00Z,10
2099-03-10T09:01:00Z,12
```

| File | SHA-256 | Interpretation record |
| --- | --- | --- |
| `demo-original.csv` | `133f8fe5fbecc07b400eafe6edbfd09d188b8c3d345ae4755e7143f7f9284ce4` | Header matches the fictional `demo-1` schema. Source context and analysis eligibility still require review. |
| `demo-copy.csv` | `133f8fe5fbecc07b400eafe6edbfd09d188b8c3d345ae4755e7143f7f9284ce4` | Bytes match the original. The copy can refer to the same source identity and interpretation record. |
| `demo-v2.csv` | `e103c19bc282a81b58e7349c6c55391ba3477ea81bf15dc91fd955d9f76ad036` | Header differs. Record a new schema or an explicit mapping before processing this version. |

The hash lets me check that I am looking at the same bytes. To interpret `value` or `reading`, I also need the schema's definition, including the unit, time basis and missing-value rules. Similar-looking columns need an explicit relationship before I combine them.

## What I keep beside an analysis run

For an input, I record a source label, the original checksum, its schema and the covered interval. If I make a transformed copy, I record its checksum and the transformation too. The original identity remains available when I inspect the derived file.

For a processing run, I record the code revision, configuration and input identities. I retain the number of rows read, the rows selected and the reasons for exclusions. If a boundary decision changes, the next export can refer to that corrected decision while retaining the earlier run's record.

This is particularly useful at a cycle transition. A file can contain observations from both sides of a field intervention, so its analysis role may differ by interval. The [change-and-exclusion ledger](../templates/change-and-exclusion-ledger.md) provides a place to record those decisions.

## The question I want a result to answer

When I return to a figure or table, I want to identify the files, schema, selection decisions and processing version that produced it. I can then examine the measurement context and the method's suitability for that research question. Recording the chain makes that review possible.

[Backup verification](2026-10-24-what-a-recovered-backup-proves.md) · [Method versioning](freezing-an-analysis-method-before-the-next-dataset.md) · [Research journal](README.md)
