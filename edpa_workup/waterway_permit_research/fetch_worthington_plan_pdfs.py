"""Collect public combined plan PDFs linked from route-near Worthington utilities."""

import csv
import re
import sys
from collections import defaultdict
from pathlib import Path
from urllib.parse import urljoin

import fitz
import requests
from bs4 import BeautifulSoup


ROOT = Path(__file__).resolve().parent
SCREEN = ROOT / "worthington_public_utility_route_screen.csv"
OUT = ROOT / "row_pdf_evidence" / "S0" / "Worthington_Utility_Plans"
OUT.mkdir(parents=True, exist_ok=True)
SEARCH = "https://gis.worthington.org/engineering/plans/search_cp2.asp"
SESSION = requests.Session()
SESSION.headers["User-Agent"] = "route-evidence-library/1.0"


def main():
    with SCREEN.open(newline="", encoding="utf-8-sig") as handle:
        screen = list(csv.DictReader(handle))
    refs = defaultdict(list)
    for row in screen:
        ref = row["plan_document_ref"].strip()
        if ref and ref.lower() not in ("nan", "<null>"):
            refs[ref].append(row)
    found = defaultdict(lambda: {"refs": set(), "rows": []})
    unresolved = []
    for ref, rows in sorted(refs.items()):
        response = SESSION.get(SEARCH, params={"searchnum": "Go", "plan": ref}, timeout=30)
        response.raise_for_status()
        if response.content.startswith(b"%PDF-"):
            found[response.url]["refs"].add(ref)
            found[response.url]["rows"].extend(rows)
            continue
        soup = BeautifulSoup(response.text, "html.parser")
        pdf_urls = sorted({urljoin(response.url, a["href"]) for a in soup.select("a[href]")
                           if "pdfComb/" in a["href"] and a["href"].lower().endswith(".pdf")})
        if not pdf_urls:
            unresolved.append((ref, len(rows), response.url))
            continue
        for url in pdf_urls:
            found[url]["refs"].add(ref)
            found[url]["rows"].extend(rows)
    still_unresolved = []
    for ref, count, url in unresolved:
        base = re.sub(r"_\d+$", "", ref)
        match = next((pdf_url for pdf_url in found if pdf_url.rsplit("/", 1)[-1].lower() == f"{base.lower()}.pdf"), None)
        if match:
            found[match]["refs"].add(ref)
            found[match]["rows"].extend(refs[ref])
        else:
            still_unresolved.append((ref, count, url))
    unresolved = still_unresolved
    if "--discover-only" in sys.argv:
        for url, item in sorted(found.items()):
            print(url, "refs=" + ";".join(sorted(item["refs"])))
        print(f"{len(found)} candidate combined PDFs; {len(unresolved)} unresolved plan refs")
        return
    manifest = []
    for url, item in sorted(found.items()):
        code = url.rsplit("/", 1)[-1]
        if not re.fullmatch(r"[A-Za-z0-9_.-]+\.pdf", code):
            raise ValueError(f"Unexpected plan filename: {code}")
        path = OUT / f"Worthington_{code}"
        if not path.exists():
            response = SESSION.get(url, timeout=120)
            response.raise_for_status()
            if not response.content.startswith(b"%PDF-"):
                unresolved.append((";".join(item["refs"]), len(item["rows"]), f"non-PDF: {url}"))
                continue
            path.write_bytes(response.content)
        with fitz.open(path) as doc:
            pages = len(doc)
        features = sorted({row["feature_id"] for row in item["rows"]})
        kinds = sorted({row["utility_type"] for row in item["rows"]})
        stations = []
        for feature in features:
            vals = [float(row["station_ft_approx"]) for row in item["rows"] if row["feature_id"] == feature]
            stations.append(f"{feature}:{min(vals):.1f}-{max(vals):.1f}")
        manifest.append({
            "official_source_url": url,
            "document_title": f"Worthington utility-linked construction plan {code[:-4]}",
            "document_id": code[:-4],
            "road": "Worthington vicinity; inspect plan title and station before design use",
            "route_features": "; ".join(features),
            "station_ranges_ft": "; ".join(stations),
            "evidence_grade_A_B_C": "B",
            "what_it_proves": "Official combined plan linked from public GIS assets: " + ", ".join(kinds),
            "limitation_or_missing_record": "Historical plan candidate; utility location, current status, depth and work-envelope fit require as-built and field verification.",
            "relative_path": path.relative_to(ROOT).as_posix(),
            "page_count": pages,
            "source_plan_refs": "; ".join(sorted(item["refs"])),
        })
        print(f"{code}: {pages} pages, {len(item['rows'])} route-near utility links")
    with (ROOT / "Worthington_utility_plan_pdf_manifest.csv").open("w", newline="", encoding="utf-8-sig") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(manifest[0]) if manifest else ["official_source_url", "document_title", "document_id", "road", "route_features", "station_ranges_ft", "evidence_grade_A_B_C", "what_it_proves", "limitation_or_missing_record", "relative_path", "page_count", "source_plan_refs"])
        writer.writeheader()
        writer.writerows(manifest)
    with (ROOT / "Worthington_unresolved_plan_refs.csv").open("w", newline="", encoding="utf-8-sig") as handle:
        writer = csv.writer(handle)
        writer.writerow(["plan_ref", "route_near_utility_links", "search_or_failure_url"])
        writer.writerows(unresolved)
    print(f"{len(manifest)} PDFs; {len(unresolved)} unresolved plan refs")


if __name__ == "__main__":
    main()
