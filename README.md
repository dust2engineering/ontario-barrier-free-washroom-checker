# Ontario Barrier-Free Washroom Checker (OBC 3.8.3.8–3.8.3.12)

Checks measured or drawn barrier-free washroom dimensions against the 2024 Ontario Building Code — stall turning space, door width, water closet position, grab bars, seat height, lavatory knee clearance, and universal washroom size. Several limits changed from the 2012 Code and are flagged.

**Live web tool:** https://dust2engineering.github.io/ontario-barrier-free-washroom-checker/web/

## How it works

- Enter any subset of 14 dimensions; each is compared with its 3.8.3.8–3.8.3.12 limit and reported PASS/FAIL with the article reference.
- Fixed (non-dimensional) requirements — grab bar strength and diameter, fold-down bar position, power door operator and emergency call system in universal washrooms — are listed in the data file.
- 2024 changes flagged in the data: door 810 → 850 mm, seat 400–460 → 430–485 mm, universal turning space 1,500 → 1,700 mm, fixed stall size removed.

## Data in this repository

- `bf-washroom-data.json` — all 14 dimensional limits with article references, the fixed requirements, and the 2024 edition changes, transcribed from the 2024 Building Code Compendium on ontario.ca, checked 2026-11-15.
- `bf_washroom.py` — command-line checker using the same data.

## Command line

```bash
python3 bf_washroom.py door_clear=850 seat_height=460 wc_centreline=470
```

## Worked examples

- [new-stall-2024.md](examples/new-stall-2024.md)
- [existing-stall-2012-recheck.md](examples/existing-stall-2012-recheck.md)

## Scope and limits

Preliminary design aid only. It does not replace the current Ontario Building Code, the Canadian Electrical Code or CSA B149.1, or the judgement of the designer of record. Verify all values against the Code in force for your project before submitting drawings for permit.

## About

Maintained by **Dust 2 Engineering Inc.** (Mississauga, Ontario) — building permit drawings
(architectural, HVAC, plumbing, sprinkler, electrical) for restaurants and small commercial
projects across the Greater Toronto Area, stamped by an Ontario P.Eng. Flat rate $3,500–$5,000.

Category: Accessibility. More free Ontario code tools: see the full index at
https://github.com/dust2engineering
