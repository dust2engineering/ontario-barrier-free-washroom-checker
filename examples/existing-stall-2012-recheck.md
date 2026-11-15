# Worked example 2 — a 2012-era stall re-checked under the 2024 Code

`python3 bf_washroom.py door_clear=810 seat_height=450 uw_turning=1500`

- door_clear 810 mm → **FAIL** (2024 requires 850 mm; 810 mm was the 2012 value)
- seat_height 450 mm → PASS (inside 430–485)
- uw_turning 1,500 mm → **FAIL** (2024 universal washrooms need a 1,700 mm turning space)

Two of three fail — a washroom built to the 2012 Code does not automatically
comply with the 2024 Code.
