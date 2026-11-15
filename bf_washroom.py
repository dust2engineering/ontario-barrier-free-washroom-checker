#!/usr/bin/env python3
"""Barrier-free washroom dimension check — OBC 2024, 3.8.3.8 to 3.8.3.12.
Usage: python3 bf_washroom.py key=value [key=value ...]
Keys: turning_stall door_clear wc_centreline transfer_w transfer_d seat_height
side_bar_h rear_bar_len rear_bar_h lav_rim knee_front knee_200 uw_turning uw_min_dim
All values in millimetres. 2024 edition numbers (several changed from 2012).
"""
import json, os, sys

DATA = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "bf-washroom-data.json")))

def ok(item, v):
    lim = item["limit"]
    if item["kind"] == "min": return v >= lim
    if item["kind"] == "max": return v <= lim
    if item["kind"] == "exact": return v == lim
    return lim[0] <= v <= lim[1]

def main():
    items = {i["key"]: i for i in DATA["items"]}
    if len(sys.argv) < 2:
        print(__doc__); return
    bad = 0
    for arg in sys.argv[1:]:
        k, _, vs = arg.partition("=")
        if k not in items:
            print(f"unknown key {k}"); bad += 1; continue
        it, v = items[k], float(vs)
        good = ok(it, v)
        bad += 0 if good else 1
        lim = it["limit"]
        limtxt = f">= {lim}" if it["kind"] == "min" else f"<= {lim}" if it["kind"] == "max" else f"= {lim}" if it["kind"] == "exact" else f"{lim[0]}-{lim[1]}"
        print(f"{'PASS' if good else 'FAIL'}  {it['label']}: {v:g} mm (limit {limtxt}, {it['article']})")
    print("All checked dimensions comply." if bad == 0 else f"{bad} item(s) do not comply.")

if __name__ == "__main__":
    main()
