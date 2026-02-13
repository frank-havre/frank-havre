# “””
FRANK-HAVRE v0.1 — Proof of Concept

FRANK: Forensic Reconciliation of Attorney-in-Fact Nominee Key indicators
HAVRE: Heuristic Audit of Virtual Reporting Entities

A ghost in the machine that finds other ghosts in the same machine.

The algorithm is simple: extract every Attorney-in-Fact name from a
company’s EDGAR filings. That’s it. One search. The rest is Google.

When you find an AIF who is NOT in the executive suite disclosed in
the 10-K or proxy — you’ve found your Frankenstein Governance.
The creature that shareholders never consented to create.

Author: Albert Nafikov | OSINT Research
License: MIT | SEC File No. CLL-15 (Regulation S-K Reform)
“””

import requests, re, json, sys
from collections import defaultdict

EFTS = “https://efts.sec.gov/LATEST/search”
UA = {“User-Agent”: “FRANK-HAVRE/0.1 research@frank-havre.org”}

def search_filings(company, forms=(“3”,“4”,“5”,“10-K”,“10-Q”,“8-K”,“DEF 14A”)):
“”“Query EDGAR full-text search for a company across form types.”””
hits = {}
for form in forms:
r = requests.get(EFTS, headers=UA, params={
“q”: f’”{company}”’, “forms”: form,
“dateRange”: “custom”, “startdt”: “2022-01-01”,
“enddt”: “2026-12-31”})
if r.ok:
hits[form] = r.json().get(“hits”, {}).get(“hits”, [])
return hits

STOPWORDS = {
“the”, “and”, “for”, “with”, “from”, “that”, “this”, “which”, “their”,
“each”, “such”, “full”, “true”, “lawful”, “any”, “all”, “not”, “but”,
“his”, “her”, “its”, “our”, “who”, “may”, “shall”, “will”, “can”,
“has”, “had”, “have”, “been”, “was”, “were”, “are”, “does”, “did”,
“act”, “behalf”, “independent”, “without”, “upon”, “into”, “also”,
“pursuant”, “respect”, “hereof”, “thereof”, “hereby”,
}

def _is_likely_name(text):
“”“Filter false positives — must look like an actual human name.”””
parts = text.strip().split()
if len(parts) < 2:
return False
if not all(p[0].isupper() for p in parts):
return False
if any(p.lower() in STOPWORDS for p in parts):
return False
if any(len(p) < 2 for p in parts):
return False
if any(c.isdigit() for c in text):
return False
return True

def extract_aif_names(text):
“”“Extract Attorney-in-Fact names from filing text.”””
NAME = r”([A-Z][a-z]{1,20}\s+(?:[A-Z].?\s+)?[A-Z][a-z]{1,20})”
patterns = [
r”appoints?\s+” + NAME + r”(?:\s+and\s+” + NAME + r”)?.*?attorney[- ]in[- ]fact”,
r”by\s+” + NAME + r”,?\s*(?:as\s+)?[Aa]ttorney[- ]in[- ][Ff]act”,
NAME + r”,?\s*[Aa]ttorney[- ]in[- ][Ff]act”,
r”[Pp]ower of [Aa]ttorney.*?appoints?\s+” + NAME,
]
found = set()
for p in patterns:
for match in re.finditer(p, text, re.DOTALL):
for group in match.groups():
if group and _is_likely_name(group):
found.add(group.strip())
return found

def find_ghosts(company, max_per_form=10):
“”“Core FRANK-HAVRE: find every AIF name across all filing types.”””
filings = search_filings(company)
aif_map = defaultdict(lambda: {“forms”: set(), “filings”: []})

```
total_scanned = 0
for form, hits in filings.items():
    for hit in hits[:max_per_form]:
        src = hit.get("_source", {})
        path = src.get("file_path", "")
        if not path:
            continue
        url = f"https://www.sec.gov/Archives/{path}"
        try:
            text = requests.get(url, headers=UA, timeout=10).text[:80000]
        except Exception:
            continue
        total_scanned += 1
        for name in extract_aif_names(text):
            aif_map[name]["forms"].add(form)
            aif_map[name]["filings"].append({
                "form": form,
                "date": src.get("file_date", "unknown"),
                "url": url
            })

return {
    "company": company,
    "total_filings_scanned": total_scanned,
    "attorneys_in_fact": {
        name: {
            "form_types": sorted(data["forms"]),
            "filing_count": len(data["filings"]),
            "filings": data["filings"][:5]
        }
        for name, data in sorted(aif_map.items())
    },
    "aif_count": len(aif_map),
    "instruction": (
        "NEXT STEP: Google each AIF name + company. "
        "If an AIF is NOT disclosed in the 10-K executive suite "
        "or proxy statement — you have found Frankenstein Governance. "
        "The creature shareholders never consented to create."
    )
}
```

if **name** == “**main**”:
target = “ “.join(sys.argv[1:]) if len(sys.argv) > 1 else “Verra Mobility”
print(f”\n{’=’*60}”)
print(f”  FRANK-HAVRE v0.1 | Extracting AIFs for: {target}”)
print(f”  ‘A ghost that finds other ghosts in the same machine’”)
print(f”{’=’*60}\n”)

```
result = find_ghosts(target)
print(json.dumps(result, indent=2, default=list))

print(f"\n{'='*60}")
print(f"  Found {result['aif_count']} Attorney(s)-in-Fact")
print(f"  Scanned {result['total_filings_scanned']} filings")
print(f"  Next: Google each name. Find the creature.")
print(f"{'='*60}\n")
```
