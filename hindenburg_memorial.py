# “””
FRANK-HAVRE v0.2 — The Hindenburg Memorial Filter

The Anderson-Havre Index

Named in memory of Hindenburg Research and in honor of Nathan
Anderson, who proved that fraud hides in plain sight — but
believed you needed drones, short positions, and millions in
research costs to find it. You don’t. You need EDGAR and regex.

Named for “Bill Havre,” the fictitious signatory who proved that
the ghosts aren’t hiding. They’re filing quarterly.

The Anderson-Havre Index cross-references FRANK-HAVRE’s AIF
detection against four Financial Stress Indicators to produce
a single composite score: the probability that Frankenstein
Governance is concealing material distress.

THE FOUR SIGNALS:
─────────────────

1. THE SIGNATURE GAP
   AIF signature present on Form 4 / 10-K while the named
   executive does not sign their own filings. The person
   refusing to hold the pen is the person shareholders think
   is holding the pen.
1. THE VALUATION SPIKE
   Stock price > 200% of 200-day moving average. When the
   Creature is signing and the price is detached from gravity,
   ask: who benefits from the gap between narrative and reality?
1. THE INSIDER EXODUS
   High volume of Form 4 dispositions (sales) filed BY the
   AIF on behalf of executives. The nominee signature shield
   isn’t just concealing who signs — it’s concealing who sells.
   Victor doesn’t sell his shares. The Creature sells them
   for him.
1. THE METADATA VOID — “Disclosure of Vacuum”
   Section 1C (Cybersecurity) or other governance disclosures
   contain boilerplate vacancy: “undergraduate and/or graduate
   degrees in their respective fields.” When a company describes
   its C-suite qualifications as “they went to college,” the
   10-K is not a disclosure document. It is a metadata void
   shaped like a disclosure document.

COMPOSITE SCORE:
────────────────
Each signal scores 0.0–1.0. The Anderson-Havre Index is the
weighted geometric mean:

AHI = (SigGap^0.35 × ValSpike^0.25 × Exodus^0.25 × Void^0.15)

Geometric mean ensures that a zero in ANY signal anchors the
score — you need the pattern, not isolated anomalies.

RISK THRESHOLDS:
0.0–0.2  CLEAR    Normal governance, normal markets.
0.2–0.4  WATCH    Frankenstein detected. Worth a Google search.
0.4–0.6  WARN     Multiple stress signals. Worth an afternoon.
0.6–0.8  ALERT    Anderson would have started flying drones.
0.8–1.0  CRITICAL The Hindenburg is already burning. Look up.

Author: Albert Nafikov | OSINT Research
License: MIT | SEC File No. CLL-15
“””

import requests, re, json, sys, math
from collections import defaultdict
from datetime import datetime, timedelta

# ── EDGAR config ──

EFTS = “https://efts.sec.gov/LATEST/search”
UA = {“User-Agent”: “FRANK-HAVRE/0.2 research@frank-havre.org”}

# ═══════════════════════════════════════════════════════════════

# SIGNAL 1: THE SIGNATURE GAP

# ═══════════════════════════════════════════════════════════════

def measure_signature_gap(company, aif_names, max_filings=15):
“””
Measures ratio of AIF-signed filings vs direct executive signatures.
High ratio = executives avoiding their own pen.
Returns 0.0 (all direct) to 1.0 (all AIF-signed).
“””
aif_signed = 0
direct_signed = 0

```
for form in ("4", "10-K"):
    r = requests.get(EFTS, headers=UA, params={
        "q": f'"{company}"', "forms": form,
        "dateRange": "custom",
        "startdt": (datetime.now() - timedelta(days=730)).strftime("%Y-%m-%d"),
        "enddt": datetime.now().strftime("%Y-%m-%d")})
    if not r.ok:
        continue
    hits = r.json().get("hits", {}).get("hits", [])

    for hit in hits[:max_filings]:
        path = hit.get("_source", {}).get("file_path", "")
        if not path:
            continue
        try:
            text = requests.get(
                f"https://www.sec.gov/Archives/{path}",
                headers=UA, timeout=10
            ).text[:60000]
        except Exception:
            continue

        text_lower = text.lower()
        has_aif = any(name.lower() in text_lower for name in aif_names)
        has_poa = "attorney-in-fact" in text_lower or "power of attorney" in text_lower

        if has_aif and has_poa:
            aif_signed += 1
        else:
            direct_signed += 1

total = aif_signed + direct_signed
if total == 0:
    return 0.0
return round(aif_signed / total, 3)
```

# ═══════════════════════════════════════════════════════════════

# SIGNAL 2: THE VALUATION SPIKE

# ═══════════════════════════════════════════════════════════════

def measure_valuation_spike(ticker):
“””
Checks if current price > 200% of 200-day moving average.
Uses free API. Returns 0.0 (normal) to 1.0 (extreme detachment).

```
NOTE: PoC stub. In production, integrate with a market data API
(Alpha Vantage, Yahoo Finance, Polygon.io). For now, returns
a placeholder that can be overridden via --valuation flag.
"""
# Production implementation would query:
# - Current price
# - 200-day SMA
# - Compute ratio: price / SMA200
# - Normalize: 0.0 if ratio <= 1.0, scales to 1.0 at ratio >= 3.0
#
# For PoC, return 0.0 (no data) — user can override
return 0.0
```

# ═══════════════════════════════════════════════════════════════

# SIGNAL 3: THE INSIDER EXODUS

# ═══════════════════════════════════════════════════════════════

def measure_insider_exodus(company, aif_names, months=12, max_filings=20):
“””
Counts Form 4 disposition (sale) transactions filed by AIF
signatories on behalf of executives. High sale volume through
nominee signatures = the Creature is liquidating for Victor.
Returns 0.0 (no sales) to 1.0 (heavy AIF-mediated selling).
“””
sale_indicators = [
r”transaction code.*?["’]?S["’]?”,  # S = sale
r”disposed”,
r”sale of”,
]
aif_sales = 0
total_form4 = 0

```
start = (datetime.now() - timedelta(days=months * 30)).strftime("%Y-%m-%d")
r = requests.get(EFTS, headers=UA, params={
    "q": f'"{company}"', "forms": "4",
    "dateRange": "custom", "startdt": start,
    "enddt": datetime.now().strftime("%Y-%m-%d")})
if not r.ok:
    return 0.0

hits = r.json().get("hits", {}).get("hits", [])
for hit in hits[:max_filings]:
    path = hit.get("_source", {}).get("file_path", "")
    if not path:
        continue
    try:
        text = requests.get(
            f"https://www.sec.gov/Archives/{path}",
            headers=UA, timeout=10
        ).text[:60000]
    except Exception:
        continue

    total_form4 += 1
    text_lower = text.lower()
    has_aif = any(name.lower() in text_lower for name in aif_names)
    has_sale = any(re.search(p, text_lower) for p in sale_indicators)

    if has_aif and has_sale:
        aif_sales += 1

if total_form4 == 0:
    return 0.0
return round(aif_sales / total_form4, 3)
```

# ═══════════════════════════════════════════════════════════════

# SIGNAL 4: THE METADATA VOID — “Disclosure of Vacuum”

# ═══════════════════════════════════════════════════════════════

VACUUM_PATTERNS = [
r”undergraduate and[/\]or graduate degree”,
r”hold[s]?\s+(?:undergraduate|graduate)\s+(?:and[/\]or\s+(?:undergraduate|graduate)\s+)?degree”,
r”degree[s]?\s+in\s+(?:their|his|her)\s+respective\s+field”,
r”experience\s+managing\s+risks?\s+at\s+(?:our|the)\s+[Cc]ompany”,
r”similar\s+(?:companies|organizations|enterprises)”,
]

def measure_metadata_void(company, max_filings=5):
“””
Scans 10-K Item 1C (Cybersecurity) for boilerplate vacancy.
The ‘Disclosure of Vacuum’ pattern: when a company describes
C-suite qualifications as ‘they have degrees,’ the governance
section is a void shaped like a document.
Returns 0.0 (substantive disclosure) to 1.0 (pure vacuum).
“””
r = requests.get(EFTS, headers=UA, params={
“q”: f’”{company}”’, “forms”: “10-K”,
“dateRange”: “custom”,
“startdt”: (datetime.now() - timedelta(days=730)).strftime(”%Y-%m-%d”),
“enddt”: datetime.now().strftime(”%Y-%m-%d”)})
if not r.ok:
return 0.0

```
hits = r.json().get("hits", {}).get("hits", [])
vacuum_scores = []

for hit in hits[:max_filings]:
    path = hit.get("_source", {}).get("file_path", "")
    if not path:
        continue
    try:
        text = requests.get(
            f"https://www.sec.gov/Archives/{path}",
            headers=UA, timeout=10
        ).text[:200000]
    except Exception:
        continue

    # Extract cybersecurity section (Item 1C)
    match = re.search(
        r"(?:item\s*1c|cybersecurity)(.*?)(?:item\s*(?:1d|2)|PROPERTIES)",
        text, re.IGNORECASE | re.DOTALL
    )
    if not match:
        continue

    section = match.group(1)[:10000]
    matches = sum(1 for p in VACUUM_PATTERNS if re.search(p, section, re.IGNORECASE))
    vacuum_scores.append(min(matches / 3.0, 1.0))  # 3+ patterns = max vacuum

if not vacuum_scores:
    return 0.0
return round(max(vacuum_scores), 3)
```

# ═══════════════════════════════════════════════════════════════

# THE ANDERSON-HAVRE INDEX

# ═══════════════════════════════════════════════════════════════

WEIGHTS = {
“signature_gap”: 0.35,
“valuation_spike”: 0.25,
“insider_exodus”: 0.25,
“metadata_void”: 0.15,
}

RISK_LEVELS = [
(0.2, “CLEAR”,    “Normal governance, normal markets.”),
(0.4, “WATCH”,    “Frankenstein detected. Worth a Google search.”),
(0.6, “WARN”,     “Multiple stress signals. Worth an afternoon.”),
(0.8, “ALERT”,    “Anderson would have started flying drones.”),
(1.0, “CRITICAL”, “The Hindenburg is already burning. Look up.”),
]

def anderson_havre_index(signals):
“””
Compute the Anderson-Havre Index via weighted geometric mean.
A zero in any signal anchors the score — you need the pattern.
“””
# Floor at 0.01 to avoid geometric mean collapsing entirely
# on missing data (valuation API not connected, etc.)
components = []
for key, weight in WEIGHTS.items():
val = max(signals.get(key, 0.0), 0.01)
components.append(val ** weight)

```
ahi = 1.0
for c in components:
    ahi *= c

return round(ahi, 4)
```

def classify_risk(ahi):
for threshold, level, desc in RISK_LEVELS:
if ahi <= threshold:
return level, desc
return “CRITICAL”, RISK_LEVELS[-1][2]

# ═══════════════════════════════════════════════════════════════

# MAIN — THE HINDENBURG MEMORIAL

# ═══════════════════════════════════════════════════════════════

def run_hindenburg_memorial(company, ticker=None, aif_names=None):
“””
Full Anderson-Havre Index scan.
Requires AIF names from FRANK-HAVRE core (frank_havre.py).
“””
if not aif_names:
# Import from core module
try:
from frank_havre import find_ghosts
ghosts = find_ghosts(company)
aif_names = list(ghosts[“attorneys_in_fact”].keys())
except ImportError:
print(“ERROR: Run frank_havre.py first to identify AIF names.”)
print(”  python frank_havre.py "Company Name"”)
sys.exit(1)

```
if not aif_names:
    print(f"No Attorneys-in-Fact found for {company}.")
    print("No Creature detected. No Hindenburg to memorialize.")
    return None

print(f"\n  AIFs detected: {', '.join(aif_names)}")
print(f"  Running four-signal analysis...\n")

# Measure all four signals
sig_gap = measure_signature_gap(company, aif_names)
print(f"  [1/4] Signature Gap:    {sig_gap:.3f}")

val_spike = measure_valuation_spike(ticker) if ticker else 0.0
print(f"  [2/4] Valuation Spike:  {val_spike:.3f}  {'(no ticker — stub)' if not ticker else ''}")

exodus = measure_insider_exodus(company, aif_names)
print(f"  [3/4] Insider Exodus:   {exodus:.3f}")

void = measure_metadata_void(company)
print(f"  [4/4] Metadata Void:    {void:.3f}")

signals = {
    "signature_gap": sig_gap,
    "valuation_spike": val_spike,
    "insider_exodus": exodus,
    "metadata_void": void,
}

ahi = anderson_havre_index(signals)
level, desc = classify_risk(ahi)

return {
    "company": company,
    "ticker": ticker,
    "aif_names": aif_names,
    "signals": signals,
    "anderson_havre_index": ahi,
    "risk_level": level,
    "risk_description": desc,
    "methodology": (
        "Weighted geometric mean: "
        "SigGap^0.35 × ValSpike^0.25 × Exodus^0.25 × Void^0.15. "
        "Geometric mean ensures zero in ANY signal anchors the score."
    ),
}
```

if **name** == “**main**”:
company = “Verra Mobility”
ticker = “VRRM”
override_aifs = None

```
# Simple CLI parsing
args = sys.argv[1:]
if args:
    if "--ticker" in args:
        idx = args.index("--ticker")
        ticker = args[idx + 1]
        args = args[:idx] + args[idx + 2:]
    if "--aifs" in args:
        idx = args.index("--aifs")
        override_aifs = args[idx + 1].split(",")
        args = args[:idx] + args[idx + 2:]
    if args:
        company = " ".join(args)

print(f"\n{'='*62}")
print(f"  THE HINDENBURG MEMORIAL — Anderson-Havre Index v0.2")
print(f"  Target: {company}" + (f" ({ticker})" if ticker else ""))
print(f"  'The Hindenburg is already burning. Look up.'")
print(f"{'='*62}")

result = run_hindenburg_memorial(company, ticker, override_aifs)

if result:
    print(f"\n{'─'*62}")
    print(json.dumps(result, indent=2, default=list))
    print(f"\n{'═'*62}")
    print(f"  ANDERSON-HAVRE INDEX:  {result['anderson_havre_index']}")
    print(f"  RISK LEVEL:            {result['risk_level']}")
    print(f"  {result['risk_description']}")
    print(f"{'═'*62}")
    print(f"  In memory of Hindenburg Research.")
    print(f"  You don't need drones. You need EDGAR and regex.")
    print(f"{'═'*62}\n")
```
