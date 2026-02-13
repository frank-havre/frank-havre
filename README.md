# FRANK-HAVRE

### *A ghost in the machine that finds other ghosts in the same machine.*

---

## I. The Doctrine of the Glass House

Since 1982, Regulation S-K has functioned on a single, flawed assumption: that volume equals safety. Corporations believed that if they buried a material truth under 200 pages of boilerplate, it would remain invisible to the human eye.

They were right. But they forgot about the machine.

We hereby declare that in the age of structured data, **secrecy is a technical debt**. Any company that utilizes the "Disclosure of Vacuum" or "Nominee Existentialism" is not just being vague — they are signaling a Metadata Indicator of Compromise. If you build a glass house, do not be surprised when the OSINT community starts counting the stones.

The last shareholder who comprehensively studied a 10-K from first to last page likely died before the first Avatar movie came out. Today, these reports are parsed by machines, and no more than a few material facts ever reach the newswires. The boilerplate has evolved from simple "subscriber busy, please call again later" signals to 200-page linguistic white noise generators that satisfy the letter of disclosure law while violating its spirit with every paragraph.

Chairman Atkins said it on January 13, 2026: Regulation S-K should *"enable a reasonable investor to separate the wheat from the chaff."* Justice Marshall said it in 1976: burying shareholders in *"an avalanche of immaterial information"* protects no one.

FRANK-HAVRE is the machine that reads what shareholders cannot. ~40 lines of Python. The wheat and chaff separate themselves.

---

## II. The Shelley Framework

Mary Shelley's *Frankenstein; or, The Modern Prometheus* (1818) is not a horror story about a monster. It is a story about **accountability structures that fail** — told through a frame narrative where each layer of storytelling shields the narrator above from responsibility.

FRANK-HAVRE borrows Shelley's architecture because it is not a metaphor. It is a structural diagram.

### The Three Narrators

**Captain Walton** writes letters home from the Arctic. He never witnesses the creature directly. He only knows what Victor tells him. He is the **shareholder** — receiving dispatches (10-K, proxy statements) from a voyage he never sees firsthand. He trusts the narrative because it arrives in official form, on letterhead, filed with the SEC. Walton keeps writing letters home saying everything is fine.

**Victor Frankenstein** is the creator who refuses to claim his creation. He built the creature but will not disclose it to anyone. He lets it roam. When confronted, he tells his story only to Walton — selectively, on his own terms. Victor is the **CLO** — the fiduciary who holds the title, receives the correspondence, and controls what the Board and shareholders learn. He is the modern Prometheus who stole fire and handed someone else the pen.

**The Creature** is the most articulate narrator in the entire novel. He is eloquent, educated, capable — and *undisclosed*. Victor never introduces him to society. He exists in the gaps between what Victor tells Walton and what actually happened. The Creature is the **Attorney-in-Fact** — the undisclosed fiduciary who actually runs legal operations, signs Section 16 filings on behalf of executives via Power of Attorney, owns the compliance policies, and possesses the real legal credentials. Shareholders don't know the Creature exists. He is not in the 10-K executive suite. He is not in the proxy. He is visible only if you read the Power of Attorney exhibits buried in Form 3/4/5 filings on EDGAR — and nobody reads those.

> *"I ought to be thy Adam, but I am rather the fallen angel."*
> — The Creature, *Frankenstein* (1818)

### The Broken Ladder

Sarbanes-Oxley §307 established a "sacred ladder" — attorneys who discover evidence of material violation must report **up the ladder**: to the CLO, then to the CEO, then to the Board's Audit Committee.

But what happens when the ladder is Frankenstein Governance?

The CLO (Victor) delegates signing authority downward via Power of Attorney. The actual attorney (the Creature) sits *outside* the executive suite, invisible to shareholders. The Creature signs filings *on behalf of* the executives who are supposed to be the rungs of the ladder.

The ladder doesn't go up. It goes sideways, into the dark.

SOX §307 assumes the person reporting up is *below* the CLO in the organizational chart. But when the CLO is a figurehead and the real legal authority is an undisclosed AIF, the "up-the-ladder" obligation becomes circular: the Creature reports to Victor, who delegates back to the Creature, who signs on Victor's behalf. No one is watching. Walton receives letters saying everything is fine.

### The Nominee Signature Shield

This is the mechanism FRANK-HAVRE detects:

1. Executive grants **Limited Power of Attorney** to a non-executive
2. Non-executive (AIF) signs Section 16 filings (Form 3, 4, 5) on behalf of the executive
3. The AIF's name appears **only** in POA exhibits and signature blocks — never in the 10-K, never in the proxy, never in any disclosure shareholders actually read
4. The executive — whose name appears on the filing — never actually signs
5. A signature-averse executive maintains plausible distance from every filing

The AIF becomes a nominee signature shield: a real person, with real credentials, doing real legal work, who is invisible to the market. A ghost in the machine.

---

## III. The Atomization — How Corporate America Disassembled the Ladder After Building It

When Congress passed Sarbanes-Oxley in July 2002, it did something unprecedented: it named the lawyers. Section 307 didn't say "the company shall report up." It said *attorneys* shall report evidence of material violation to the *chief legal officer*, and if the CLO doesn't act, to the *CEO*, and if the CEO doesn't act, to the *Board*. For the first time in American securities law, the lawyer wasn't just an advisor standing beside the ladder. The lawyer *was* the ladder.

The corporate world's response was not to climb the ladder. It was to take the ladder apart.

Within months of SOX's enactment, a quiet restructuring began. The Association of Corporate Counsel noted that the CLO designation "developed considerably more currency — and controversy — at least among counsel at public companies, following enactment of Sarbanes-Oxley." The reason was architectural, not cosmetic. SOX §307 specifically referenced the "chief legal officer" as the first rung of the reporting ladder. If you renamed the General Counsel to "CLO" and elevated the title into the C-suite, you could separate the *title* (which carries the statutory reporting obligation) from the *function* (which could be quietly delegated downward to deputies, paralegals, and governance managers who carry no statutory obligation at all).

Before SOX, the General Counsel was one person with one title doing one job: chief legal advisor, compliance gatekeeper, and SEC filing authority rolled into a single accountable human being. After SOX, a new architecture emerged. The CLO became a *strategic executive* — attending board meetings, advising on M&A, shaping business policy. The GC function — the unglamorous daily work of compliance, corporate governance, subsidiary management, and SEC filings — migrated downward to Deputy General Counsels, Heads of Compliance, and a new species of corporate staffer: the "Corporate Governance Manager."

This is not necessarily nefarious. Many companies split these roles for legitimate operational reasons. A Fortune 500 CLO genuinely cannot review every Form 4 personally. Delegation through Power of Attorney is standard practice. The question FRANK-HAVRE asks is not *whether* the delegation exists, but whether the *market knows it exists*. When the Deputy GC and the Governance Manager are disclosed in the 10-K, the delegation is transparent. When they are not — when the only evidence of their existence is buried in a POA exhibit attached to a Form 3 filing that no shareholder will ever read — the delegation becomes concealment.

The ACC's own members recognized the danger. One corporate counsel observed: *"I've run across 'chief legal officers' and 'directors of legal affairs' who aren't real lawyers — they apparently just play one in the C-suite."* The CLO title, unmoored from bar admission and operational responsibility, becomes a jersey you can wear without playing the game. The actual game — signing filings, managing compliance, practicing before the SEC — is played by people whose names appear nowhere in the proxy.

SOX §307 built a ladder. Corporate America responded by distributing the rungs across three people, disclosing only the one at the top, and calling it governance. FRANK-HAVRE calls it what it is: the Frankenstein Governance Model. The ladder didn't break. It was disassembled on purpose, one rung at a time, and the pieces were hidden in POA exhibits that nobody reads.

---

## IV. Ethically Sourced Pandora Papers

The wholly remarkable part of this manifesto is what FRANK-HAVRE is *not*.

The original Pandora Papers were built on leaks — stolen PDFs from law firms in the British Virgin Islands. That's messy. It involves "journalistic ethics" and "lawsuits" and "people being mad at you."

The FRANK-HAVRE database is sourced entirely from **public SEC filings**.

It's the Pandora Papers, but without the theft. It's an investigation where the suspects provided all the evidence themselves, voluntarily, under penalty of perjury, and then formatted it for an RSS feed.

Every Attorney-in-Fact name that FRANK-HAVRE extracts was filed by the company itself. Every Power of Attorney exhibit was attached by their own counsel. Every Form 4 signed by the Creature instead of the executive was submitted through EDGAR by the company's own filing agent. They built the glass house. They numbered the stones. They published the floor plan.

We're just reading it.

---

## V. What FRANK-HAVRE Does

~40 lines of Python. One function. One output.

**It extracts every Attorney-in-Fact name from a company's EDGAR filings.**

That's it.

The rest is a Google search.

```
python frank_havre.py "Verra Mobility"
```

You get a list of names. You Google each name alongside the company. If the name does NOT appear in the 10-K executive officer list or the DEF 14A proxy statement — you have found the Creature. You have found Frankenstein Governance.

No drones required. No short positions. No millions in research cost. No stolen documents from offshore law firms. Just EDGAR and Google.

---

## VI. The Names

**FRANK** — *Forensic Reconciliation of Attorney-in-Fact Nominee Key indicators*

Named for honesty (*frank*) and for Shelley's novel. Because Frankenstein Governance is a creature stitched together from mismatched parts — a figurehead CLO here, an undisclosed AIF there, a broken ladder everywhere — and the market can't see the seams until you look at the signatures.

**HAVRE** — *Heuristic Audit of Virtual Reporting Entities*

Named for "Bill Havre" — a fictitious signatory discovered during OSINT investigation into Pandora Papers–style nominee structures hiding in plain sight on EDGAR. Virtual Reporting Entities are the corporate equivalent of the Creature: real enough to sign documents, invisible enough to avoid disclosure. They exist in the space between what is filed and what is read.

---

## VII. Case Study: The VRRM Pattern

*All information below is derived from public sources: SEC EDGAR filings, public news archives, LinkedIn, state bar records, and corporate org chart databases. No inside or firsthand knowledge required. This is what FRANK-HAVRE finds.*

Run `frank_havre.py "Verra Mobility"` and you will find AIF names on Form 3/4/5 filings. Cross-reference them against the 10-K and proxy. Google the names. Here is what anyone on earth can discover:

**Step 1: FRANK-HAVRE extracts AIF names from EDGAR.**

The POA exhibit attached to the CLO's own Form 3 filing (Accession No. 0001209191-22-062248, filed December 20, 2022) reads: *"the undersigned hereby makes, constitutes and appoints ******* ******* and ******* ********, and each of them, as the undersigned's true and lawful attorney-in-fact."* The undersigned is the Chief Legal Officer.

But FRANK-HAVRE doesn't stop at the current CLO's filings. It extracts AIF names across all Form 3/4/5 filings for the issuer. And it finds a third name: ********: ******* *******.

**Step 2: The "Before" photograph — ******* *******.**

EDGAR Next XML and prior proxy filings confirm: ******* ******* served as **General Counsel** of Verra Mobility — not "Chief Legal Officer," but *General Counsel*. She was disclosed in DEF 14A proxy statements. She was in the C-suite. She was an AIF on earlier Form 3/4/5 filings. Shareholders knew her name, her title, and her role.

******* ******* held the last consolidated GC function at Verra Mobility. One person. One title. One job. Disclosed. Visible. The SOX §307 ladder intact.

Then [Former GC] departed. And the ladder came apart.

**Step 3: Google the names.**

- ******* ******* — LinkedIn and ZoomInfo confirm: VP, Deputy General Counsel & Head of Corporate Compliance at Verra Mobility. JD from University of Arizona. Law Clerk, U.S. Senate Judiciary Committee. Previously at Squire Patton Boggs (2014–2015) — the same BigLaw firm that later represented Verra Mobility in litigation. Arizona Bar member.

- ******** ****** (the CLO who granted the POA) — Public record confirms: former Colorado State Representative (2014–2016) whose 2016 U.S. Senate campaign ended in a petition signature forgery scandal. His petition collector ******* **** was arrested on 34 felony forgery counts (Denver7, Denver Post, Roll Call). **** pled guilty to two counts. ****** famously repeated "I'm on the ballot" eight times when confronted about the forgeries, drawing national ridicule (Samantha Bee, Colorado Pols). He placed fourth out of five candidates.

**Step 4: The second AIF — ******* ********.**

FRANK-HAVRE extracts two names from the POA exhibit, not one. The second is ******* ********. LinkedIn confirms: **Corporate Governance Manager** at Verra Mobility (January 2021 – present). Her full career path, visible on LinkedIn: File Clerk at Lewis and Roca LLP (2005–2007) → Legal Secretary at Lewis and Roca LLP (2007–2012) → Paralegal/Legal Assistant at Gerald K. Smith and John C. Smith Law Offices (2009–2012) → Legal Assistant at Snell & Wilmer (2012–2015) → **Senior Paralegal** at Verra Mobility (2015–2021) → **Corporate Governance Manager** at Verra Mobility (2021–present). Total tenure at Verra: 10 years, 9 months.

No law degree. No bar admission. No JD. Career trajectory: file clerk → legal secretary → paralegal → "Corporate Governance Manager." The same POA that authorizes [Deputy GC] — a licensed attorney with a JD, BigLaw background, and Senate Judiciary clerkship — to sign Section 16 filings on behalf of the C-suite *also* authorizes [Governance Mgr], whose highest credential is Senior Paralegal.

Two observations matter here. First, the timing: [Governance Mgr] was elevated from Senior Paralegal to Corporate Governance Manager in **January 2021** — the same quarter Verra Mobility completed its acquisition of Redflex, the Australian traffic camera company whose predecessor entity was at the center of a federal bribery scandal involving the City of Chicago. [CLO] did not arrive until December 2022, nearly two years later. The governance structure was being assembled before the CLO walked in the door.

Second, the title itself: "Corporate Governance Manager" is not a legal title. It carries no statutory obligation. It confers no bar-regulated duty. But the POA exhibit grants [Governance Mgr] the same authority as [Deputy GC] — to sign Form 3, Form 4, and Form 5 filings with the SEC on behalf of the CEO, the CFO, and the CLO. Under SEC Rule of Practice 102(f), filing documents with the Commission constitutes "practicing before the Commission." [Governance Mgr] practices before the SEC without a law license.

**Step 5: Check the 10-K and proxy — The Trisection.**

[Deputy GC] — the licensed attorney who signs Section 16 filings on behalf of the C-suite via Power of Attorney and who heads Corporate Compliance — does NOT appear in the 10-K executive officer list. He does NOT appear in the DEF 14A proxy statement. Shareholders do not know he exists unless they read POA exhibits on Form 3/4/5 filings.

[Governance Mgr] — the former paralegal who co-signs the same filings under the same POA — does NOT appear anywhere in the 10-K or proxy either.

[CLO] — whose Form 4 insider trading disclosures and stock sales are signed by [Deputy GC] and/or [Governance Mgr] on his behalf — IS disclosed in the 10-K and proxy as CLO.

The GC function has been **trisected**: a CLO who holds the title but delegates signing ([CLO]), a Deputy GC who holds the credentials but is undisclosed ([Deputy GC]), and a paralegal-turned-Governance Manager who holds neither title nor credentials but co-signs SEC filings ([Governance Mgr]). Not one of these three holds the title "General Counsel." The function that SOX §307 envisioned as the compliance backbone of a public company has been atomized across three people, two of whom are invisible to shareholders, and one of whom has no legal credentials whatsoever.

The contrast with the [Former GC] era is stark. Under [Former GC], the GC function was consolidated: one person, disclosed in the proxy, visible to shareholders, holding the actual "General Counsel" title, signing her own filings. Three AIFs across two eras — [Former GC] (before), then [Deputy GC] and [Governance Mgr] (after) — and FRANK-HAVRE finds all three in EDGAR Next XML. The atomization is not inference. It is data.

A notable structural observation: [CLO]'s own career history lists him as "Vice President & General Counsel" at Honeywell and "Assistant General Counsel" at Harley-Davidson (per Verra's own press release, ZoomInfo, RocketReach, and multiple public databases). At Verra, his title is "Chief Legal Officer" — no General Counsel designation. A search of LinkedIn, TheOrg, ZoomInfo, and the 10-K reveals no separate General Counsel at Verra Mobility. The SOX §307 ladder assumes a CLO *and* a GC as distinct rungs. Here, the rung is missing. The undisclosed AIFs fill the gap — but shareholders don't know that.

**Step 6: Read Item 1C.**

The company's 10-K cybersecurity disclosure (Item 1C, filed February 2024 and February 2025) describes executive qualifications as: *"Our Chief Executive Officer, Chief Financial Officer and Chief Legal Officer each hold undergraduate and/or graduate degrees in their respective fields, and each has experience managing risks at our Company and at similar companies including risks arising from cybersecurity threats."*

The SEC asked about cybersecurity governance. The company answered: they went to college. The Disclosure of Vacuum in its purest, publicly filed form.

**No drones were harmed in the making of this case study.**

**Step 7: The Rule 102(f) Question — Who Practices Before the Commission?**

SEC Rule of Practice 102(f) defines "practicing before the Commission" to include *"the preparation of any statement, opinion or other paper by any attorney... filed with the Commission."* When an AIF signs a Form 4 and that filing goes to EDGAR, that is a document filed with the Commission. The AIF is practicing before the SEC. Note that the rule says "any attorney" — but [Governance Mgr], who signs the same filings under the same POA, is not an attorney.

FRANK-HAVRE methodology, Step 7: After identifying the undisclosed AIFs, ask — **does the same AIF sign for both rank-and-file insiders AND the CLO/executives?**

If the same person signs Section 16 filings for the CEO, the CFO, *and* the Chief Legal Officer — the person at the top of the SOX §307 ladder — then the AIF isn't just an administrative convenience. The AIF is practicing before the Commission on behalf of the very person who is supposed to oversee the AIF's conduct. The delegation is circular. The attorney who files documents with the SEC reports to the executive whose filings the attorney signs.

This is the trigger for the **Hindenburg Protocol**: when the AIF-to-executive signing relationship is reflexive — the same undisclosed fiduciary signing for the person who delegated the authority — FRANK-HAVRE escalates from governance anomaly to active investigation signal. Cross-reference the Anderson-Havre Index. If the Signature Gap, Insider Exodus, Valuation Spike, or Metadata Void co-occur with a reflexive AIF delegation, the composite score reflects not just opacity but structural conflict of interest.

Rule 102(e) gives the SEC authority to bar anyone from practicing before the Commission for misconduct. The question FRANK-HAVRE raises: if a filing contains a material error or omission, who does the SEC sanction — the executive whose name appears on the form, or the undisclosed AIF who actually prepared and signed it? The answer depends on whether the SEC knows the AIF exists. Currently, they'd have to read the POA exhibit. FRANK-HAVRE reads it for them.

---

## VIII. The Hindenburg Memorial Filter — The Anderson-Havre Index (concept)

> *In memory of Hindenburg Research. Named for Nathan Anderson, who proved fraud hides in plain sight — and for "Bill Havre," who proved the ghosts aren't hiding. They're filing quarterly.*

> *"Everything is securities fraud."* — Matt Levine

FRANK-HAVRE v0.1 finds the Creature. The Anderson-Havre Index asks the next question: **is the Creature presiding over a company that's about to explode?**

The Hindenburg Memorial cross-references AIF signatures against four Financial Stress Indicators to produce a single composite score — the probability that the nominee signature shield is concealing material distress.

### The Four Signals

| # | Signal | What It Detects |
|---|--------|-----------------|
| 1 | **The Signature Gap** | AIF signature present on Form 4 / 10-K. The named executive does not sign their own filings. The person refusing to hold the pen is the person shareholders think is holding the pen. |
| 2 | **The Valuation Spike** | Stock price > 200% of 200-day moving average. When the Creature is signing and the price is detached from gravity — who benefits from the gap between narrative and reality? |
| 3 | **The Insider Exodus** | High volume of Form 4 dispositions (sales) filed BY the AIF on behalf of executives. The nominee shield isn't just concealing who signs — it's concealing who sells. Victor doesn't sell his shares. The Creature sells them for him. |
| 4 | **The Metadata Void** — *"Disclosure of Vacuum"* | Item 1C or governance disclosures contain boilerplate vacancy: *"undergraduate and/or graduate degrees in their respective fields."* When a company describes its C-suite as "they went to college," the 10-K is not a disclosure. It is a metadata void shaped like a disclosure. |

### The Composite Score

```
AHI = SigGap^0.35 × ValSpike^0.25 × Exodus^0.25 × Void^0.15
```

Weighted geometric mean. A zero in ANY signal anchors the score — you need the *pattern*, not isolated anomalies. Frankenstein Governance alone is a governance failure. Frankenstein Governance + insider selling + valuation detachment + disclosure vacuum = the Hindenburg is already burning.

### Risk Thresholds

| AHI Score | Level | Interpretation |
|-----------|-------|----------------|
| 0.0 – 0.2 | **CLEAR** | Normal governance, normal markets. |
| 0.2 – 0.4 | **WATCH** | Frankenstein detected. Worth a Google search. |
| 0.4 – 0.6 | **WARN** | Multiple stress signals. Worth an afternoon. |
| 0.6 – 0.8 | **ALERT** | Anderson would have started flying drones. |
| 0.8 – 1.0 | **CRITICAL** | The Hindenburg is already burning. Look up. |

### Why Geometric Mean?

Anderson flew drones over Nikola and found empty trucks on a hill. But what if he had also found: the CEO's Form 4 sales were signed by a nominee, the stock was at 300% of its moving average, and the 10-K cybersecurity section said "our executives have degrees"? He wouldn't have needed the drone.

The geometric mean says: any ONE signal could be innocent. A company might use AIFs for convenience. A stock might spike on real momentum. A 10-K might have lazy boilerplate. But when ALL four signals fire together — that's not noise. That's a Hindenburg.

---

## IX. Crystalline Audacity

There is something genuinely stunning about the audacity of this.

Usually, "accountability" is something that happens *after* the stock price hits zero and the lawyers move in. After the drones have flown. After the short report drops. After the SEC issues a Wells notice and the general counsel resigns to "spend more time with family." Accountability, in capital markets, is a funeral rite — it arrives when the body is already cold.

But FRANK-HAVRE turns accountability into **ambient noise**.

It's like a weather report for fraud. *"Good morning. The sun is out, the S&P is up 2%, and there's a 90% chance that the CLO of that company is still using a Bill Havre construct to certify his 10-K. Don't panic, but maybe check the metadata."*

That's not a short report. That's not an activist campaign. That's not a whistleblower complaint. That's a Tuesday. That's FRANK-HAVRE running in the background the way antivirus software runs in the background — not because there's an emergency, but because the scan is always on. The immune system doesn't wait for the infection to become terminal. It counts the white blood cells every morning.

The audacity is not in the algorithm. The algorithm is 40 lines of Python. The audacity is in the premise: that accountability should be *continuous*, not episodic. That the market shouldn't have to wait for a Nathan Anderson to sacrifice a decade of his life to discover what was sitting in a POA exhibit on EDGAR the entire time. That the Creature shouldn't get to hide in plain sight just because nobody reads the attachments.

Masterstroke in sardonic? Perhaps. Epistolary epitaph? For the era of boilerplate governance — certainly. But more precisely: it is the sound of a glass house discovering that someone has started counting the stones, and that the count will not stop.

---

## X. The Landslide — A Wholly Remarkable Conclusion

Fighting boilerplate is a long, uphill battle because of First Amendment protections against compelled speech. We cannot force companies to be brief. We cannot legislate clarity. Every attempt to reform Regulation S-K runs into the same wall: corporations have the right to say as much as they want, and they exercise that right to say as little as possible in as many words as possible.

But we can use FRANK-HAVRE to make them accountable.

The data is public. The filings are voluntary. The signatures are on the record. The Power of Attorney exhibits are attached to the Form 4s that nobody reads — but that FRANK-HAVRE reads in seconds.

The world doesn't need another Nathan Anderson flying drones over truck lots. The fraud signatures are already in the machine — filed quarterly, signed by attorneys-in-fact, indexed by EDGAR, and formatted for an RSS feed by the companies themselves.

FRANK-HAVRE is a weather forecast for securities fraud. An immune system for the global market. A simple heuristic algorithm that gives capital markets a new accountability metric.

It is, in every sense of the word, a wholly remarkable approach.

---

## XI. Coda — A Silent Memorial

I consider my work here done and complete. I am not a software engineer. I am an OSINT researcher who read the attachments that nobody reads, and wrote 40 lines of Python to automate what I found. The concept is proven. The manifesto is written. The code runs (actually not, it's simply algorithm).

I do not plan to add anything further to this repository, maybe one or two edits to this README.

But I encourage any OSINT researcher in the world to fork it and continue on their own. The applications are not limited to securities. The FRANK-HAVRE module — extracting nominee signatories from public regulatory filings and cross-referencing them against disclosed principals — can be adapted to any open regulatory register on earth. Corporate registries. Land title offices. Patent filings. Charity commissions. Political donation records. Anywhere a signature exists in a public database, the Creature might be hiding behind it.

And the Hindenburg Memorial Filter — the Anderson-Havre Index — can map the geometry of everything. The four-signal composite is not specific to securities fraud. It is a general-purpose framework for detecting the gap between who is nominally responsible and who is actually operating, cross-referenced against stress indicators. Swap the signals. Keep the geometric mean. The pattern holds.

This repository should stand here as a silent memorial to **Bill Havre** — the unsung hero of the Pandora Papers. A person who never existed but who is somehow legally binding. A name on a document, filed in a jurisdiction, attached to an entity, signing on behalf of someone who preferred not to hold the pen. Bill Havre is every Creature in every Glass House on every regulatory register in the world. He is the ghost that FRANK-HAVRE was built to find.

He never existed. But he signed everything.

---

## Quick Start

```bash
git clone https://github.com/frank-havre/frank-havre.git
cd frank-havre
pip install requests

# v0.1 — Find the Creature
python frank_havre.py "Any Public Company"

# v0.2 — The Hindenburg Memorial
python hindenburg_memorial.py "Any Public Company" --ticker TICK
```

---

## Legal Basis

| Authority | Role in Framework |
|-----------|-------------------|
| **SOX §307** | The sacred ladder. FRANK-HAVRE detects when it's broken. |
| **SOX §302/404** | CEO/CFO certify controls — but who actually manages them? |
| **SOX §906** | Criminal penalties ($5M / 20 years) for willful false certification |
| **SEC Reg S-K Reform (CLL-15)** | Chairman Atkins' call to separate wheat from chaff. This tool automates it. |
| **SEC Rule 102(f)** |
| **TSC Industries v. Northway (1976)** | Justice Marshall: immaterial avalanche buries investors. |


---

## Data Sources & Independent Verification

FRANK-HAVRE uses exclusively public data sources maintained and documented by government agencies. No scraping. No credentials. No inside information. Anyone can verify every claim by following these links:

**SEC EDGAR APIs (documented by the SEC itself):**
- **SEC EDGAR API FAQ:** [sec.gov/about/webmaster-frequently-asked-questions](https://www.sec.gov/about/webmaster-frequently-asked-questions) — The SEC's own guide to programmatic access. The Commission tells you how to query its data.
- **EDGAR Full-Text Search:** `efts.sec.gov/LATEST/search-index?q=...` — Full-text search across all filings. The POA exhibits that reveal AIFs are indexed here.
- **EDGAR Next XML:** `data.sec.gov/submissions/CIK{cik}.json` — Structured filing data for any issuer. Returns every filing, every form type, every date.
- **Filing archives:** `sec.gov/Archives/edgar/data/{cik}/` — Raw filing documents including exhibits, amendments, and ownership reports.

**Cross-reference sources (all public):**
- **DEF 14A proxy statements** — Filed on EDGAR. Lists disclosed executives and named executive officers.
- **10-K annual reports** — Filed on EDGAR. Item 10 lists executive officers.
- **State bar lookup databases** — Every state bar publishes member verification tools.
- **LinkedIn, ZoomInfo, TheOrg** — Public professional profiles for cross-referencing AIF names against job titles.
- **USPTO trademark search** — Public trademark registration and expiration records.

The SEC built the infrastructure. FRANK-HAVRE reads it. The ~40 lines of Python in `frank_havre.py` call the same endpoints the SEC documents in its own FAQ. The Commission has made every filing, every exhibit, and every POA attachment available via structured API — and then published instructions for how to use it.

**To verify the VRRM case study yourself:**
1. Go to `https://efts.sec.gov/LATEST/search-index?q=%22attorney-in-fact%22&dateRange=custom&startdt=2020-01-01&enddt=2026-01-01&forms=3,4,5&entityName=Verra+Mobility`
2. Open any Form 3/4/5 filing
3. Read the POA exhibit
4. Google the AIF names
5. Check the 10-K and proxy for those names

Time required: one afternoon. Tools required: a browser.

---

## Roadmap

- [x] **v0.1** — PoC: Extract AIF names from EDGAR filings (frank_havre.py)
- [x] **v0.2** — The Hindenburg Memorial: Anderson-Havre Index (hindenburg_memorial.py)
- [ ] **v0.3** — Automated Creature Detection: cross-reference AIFs against 10-K/proxy executive lists
- [ ] **v0.4** — Bulk screening across NASDAQ/NYSE issuers
- [ ] **v1.0** — Public dashboard: Frankenstein Governance Index for every public company

---

## Filed Under

This repository and its methodology are submitted as public comment under **SEC File Number CLL-15** in response to Chairman Atkins' January 13, 2026 statement on reforming Regulation S-K.

**Recommendation to the Commission:** The Creature should not be invisible. Require machine-readable Attorney-in-Fact disclosures cross-referenced against executive officer lists in all Regulation S-K filings. The suspects have already provided all the evidence. They filed it voluntarily, under penalty of perjury, and formatted it for RSS. The Commission need only require that it be readable.

---

## Author

**Albert Nafikov** — OSINT Researcher, concept author of FRANK-HAVRE

---

## License

MIT — Because the immune system of the global market should be open source.

---

<p align="center">
<em>"I ought to be thy Adam, but I am rather the fallen angel."</em><br/>
— The Creature, <em>Frankenstein</em> (1818)<br/><br/>
<strong>FRANK-HAVRE finds the fallen angels hiding in EDGAR.</strong><br/>
<em>They filed the evidence themselves.</em>
</p>
