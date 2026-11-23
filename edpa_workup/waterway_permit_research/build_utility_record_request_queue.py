"""Group missing utility records by route jurisdiction and source-feature station."""

import csv
from collections import defaultdict
from pathlib import Path


WORK = Path(__file__).resolve().parent
SOURCE = WORK / "ROW_feasibility_station_overlay.csv"
TARGET = WORK / "utility_records_request_queue_by_jurisdiction.csv"

groups = defaultdict(lambda: defaultdict(list))
with SOURCE.open(newline="", encoding="utf-8-sig") as handle:
    for row in csv.DictReader(handle):
        key = (row["route_part"], row["county_boundary"], row["municipality_or_place_boundary"])
        groups[key][row["feature_id"]].append((float(row["station_start_ft_KMZ"]), float(row["station_end_ft_KMZ"])))

fields = ["route_part", "county_boundary", "place_boundary", "feature_station_extent_ft_approx",
          "public_utility_layers_screened", "missing_or_incomplete_online_records",
          "first_record_custodians_to_confirm", "request_content", "evidence_status"]
with TARGET.open("w", newline="", encoding="utf-8-sig") as handle:
    writer = csv.DictWriter(handle, fieldnames=fields)
    writer.writeheader()
    for (part, county, place), features in sorted(groups.items()):
        extents = "; ".join(
            f"{feature}:{min(a for a, _ in ranges):.1f}-{max(b for _, b in ranges):.1f}"
            for feature, ranges in sorted(features.items())
        )
        public = []
        if "UNION" in county:
            public.append("Union County sanitary sewer GIS (partial owner/network coverage)")
        if county == "Cook":
            public.append("MWRD interceptor/local sewer GIS (partial owner/network coverage)")
        if county == "Cook" and part in ("Spur3", "Spur4"):
            public.append("Elk Grove project plan PDFs (project footprints only; georeferencing pending)")
        if part.startswith("Spur"):
            custodians = "Elk Grove Village or Itasca as applicable; Cook/DuPage road/drainage owner; MWRD where asset IDs match; IDOT; private owners from JULIE"
        else:
            custodians = "City/village and county engineer or sewer/water district; ODOT where State ROW; private owners from OHIO811"
            if "COLUMBUS" in place:
                custodians += "; Columbus DPU Map Room for design/construction GIS"
        writer.writerow({
            "route_part": part,
            "county_boundary": county,
            "place_boundary": place,
            "feature_station_extent_ft_approx": extents,
            "public_utility_layers_screened": "; ".join(public) or "No complete line-level public asset layer obtained",
            "missing_or_incomplete_online_records": "Current water, sanitary, storm/culverts, gas, electric, telecom/fiber, lighting/signals, abandoned/relocated facilities, capital-project as-builts, utility easements",
            "first_record_custodians_to_confirm": custodians,
            "request_content": "Send route corridor polygon and feature/station ranges; ask for current GIS/CAD/as-builts, plan/profile, owner and size, invert/depth, active status, date, proposed work, easements and crossing requirements; include bore pits, vaults, staging and access",
            "evidence_status": "Jurisdiction is a routing lead, not proof of utility ownership; no request sent",
        })

print(f"Wrote {len(groups)} jurisdiction/route groups to {TARGET}")
