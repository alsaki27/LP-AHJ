# CHI Spurs and Marysville–New Albany RFP: review and improvement plan

**Review date:** 13 November 2026  
**Working deadline:** 22 November 2026, as recorded from the earlier RFP email screenshot in `lp_source_copy/edpa_workup/vendor_master_analysis.md`. The screenshot itself was not found in the copied folder.  
**Status:** internal working review, not a submission or permit determination.

## What was preserved and reviewed

- `rfp_source/` contains the four supplied files from the Downloads RFP folder. Their SHA-256 hashes match the copies in `lp_source_copy/edpa_workup/source_files/`.
- `lp_source_copy/` preserves the LP folder outside this workspace. All 8,384 regular source files were found in the copy at matching sizes. A source `node_modules` junction was followed during copying, so the copy also contains runtime dependency files that are not project evidence.
- The six-page `EDPA Process.pdf` was read in full. It requires an EDPA for every route and A/Z pair, an annotated GIS package, AHJ permit matrix with durations and source evidence, crossing/constraint and method tables, risk assessment, maps, and a separately colored KMZ for proposed route changes with footage and impact explanations.
- The prior work includes a 52-feature route inventory, a 1,362-row station/AHJ candidate ledger, an eight-tab permit-readiness workbook, area-specific reports and exhibits, parcel/ROW screens, railroad and waterway diligence reports, and a 182-entry v4 ZIP. These provide a strong research base. GIS and parcel hits remain leads until the legal corridor, issuer, construction footprint, and method are confirmed.
- The separate railroad and waterway diligence documents now in `lp_source_copy/edpa_workup/railroad_permit_research/` and this workspace were not listed in the v4 ZIP. Rebuild the final package from the current reviewed sources instead of treating v4 as the submission snapshot.

## Submission readiness

| Buyer requirement | Existing evidence | Required improvement before issue |
| --- | --- | --- |
| Separate Chicago and Ohio engineering prices, with $/LF | Pricing architecture and source-KMZ lengths in the master analysis; no actual fee schedule in v4 | Build a priced fee sheet using the vendor rate card and an agreed LF denominator. Show Chicago, Ohio S0, Ohio S1, Ohio aggregate, and inclusions/allowances. |
| Separate route-feasibility-study price | Work breakdown and candidate alternatives in reports | Price the study separately with deliverables, iterations, survey/ROW assumptions, and decision date. |
| EDPA for every route/A–Z pair | Three area reports; Chicago report covers four spurs | Add one clear decision summary per Chicago spur and confirm every A/Z facility/tie-in. Retain feature IDs across report, map and matrix. |
| Route integrity | 52 original features and lengths have been inventoried | Use all supplied parcels and route features for the current ROW/utility feasibility pass. Resolve the roughly 31.1 m S0/S1 join and smaller topology details when freezing a later issued route version; they do not block this evidence screen. |
| AHJ matrix with standard/expedited duration, fees, moratoria, and source | Candidate matrices and workbook contain published rules and planning allowances | Convert candidate rows into one row per actual approval/property instrument and station band. Separate published clock, vendor allowance, and written agency confirmation. Record dated source/contact evidence. |
| Crossings, methods and risk | Water, rail, road, parcel and environmental registers; three reports and maps | Resolve identities and legal/property triggers at the highest-risk stations; add preliminary method/profile, work area, cost and schedule consequence, owner, and decision date to each red gate. |
| Suggested route changes and alternate KMZ | Narrative concepts around reservoir, highway, rail, wetland and ROW risks | Produce a distinct-color, endpoint-preserving alternative only after its geometry and property assumptions are explicit. Measure added/removed footage and compare approvals, method, cost and schedule. If no defensible change can be drawn by bid time, state that clearly and price the feasibility study as the route-selection gate. |
| Clean final package | v4 ZIP contains 182 entries, including scripts, raw evidence and temporary images | Issue a short client-facing package: signed/dated EDPA, permit and constraint tables, annotated original KMZ, alternatives KMZ if supported, map sheets, fee proposal, and a concise evidence appendix. Keep raw GIS, scripts and scratch files in an internal archive. |

## Highest-leverage decisions

1. **Parcel, ROW and utility feasibility basis.** Use every supplied route feature and its 250-ft parcel corridor for the current evidence screen. Retrieve controlling ROW documents by feature station and test the complete proposed work footprint. Then overlay public utilities and make station-bounded requests for missing records. Ohio S0/S1 join resolution is deferred for route issue and pricing; it does not stop this screen. The present source lengths are about 49,155 ft Chicago and 270,642 ft Ohio; they are screening centerlines, not final installed quantities.
2. **Property and permit path.** Retrieve controlling ROW plans, plats, deeds and railroad property maps at the flagged stations. Determine road/asset owner and permit issuer from the actual work footprint, including pits, access and traffic control. ODOT states its permits cover only state ROW and directs work within corporate limits to the appropriate city or village; the Ohio candidate matrix therefore needs station-specific reconciliation before assigning ODOT as issuer. [ODOT permit guidance](https://www.transportation.ohio.gov/business/permits/row-permits).
3. **Critical crossings.** Resolve S1-S033 at the Scioto/O'Shaughnessy Reservoir, the highway and railroad cases, Salt Creek, and uncertain water labels before presenting a selected method or construction date. The railroad report identifies eleven geometric route/track intersection stations; that is an engineering coordination count, not eleven proven license instruments.
4. **Seasonal and environmental gates.** IDOT District 1's 2026 guide describes a November 1–April 15 winter moratorium for open pavement cuts and work affecting the traveled way; applicability depends on the actual State ROW activity and any written exception. [IDOT District 1 guide](https://idot.illinois.gov/content/dam/soi/en/web/idot/documents/doing-business/memorandums-and-letters/permits/district-1-utility-permit-guide.pdf). USACE's 2026 NWP 57 may be relevant to telecommunications work in regulated waters, but the activity, impacts, regional conditions and notification triggers must be determined for each design. [USACE NWP 57](https://www.nab.usace.army.mil/Portals/63/docs/Regulatory/NWP/NWP%2057.Electric%20Utility%20Line%20and%20Telecommunications%20Activities-%20with%20General%20Conditions.pdf?ver=uBhGacdjjonoiRLgAHrZXw%3D%3D).
5. **Commercial inputs.** Obtain the vendor labor/rate card, target margin or fee policy, proposed design level, deliverable count, review rounds, survey/SUE/geotech scope, and pass-through treatment. No dollar bid can be inferred from the supplied four RFP files or prior desktop analysis.

## Proposed response architecture

1. **Executive decision sheet:** Chicago and Ohio quantities, complexity, top risks, pricing summary, feasibility study, and client decisions.
2. **Technical EDPA:** common methods and evidence standard, then distinct Chicago Spur 1–4, Ohio S0, and Ohio S1 sections. Each section uses the same feature IDs and station convention as its map and register.
3. **Approval and crossing schedules:** one approval/property instrument per row; each crossing linked to method, owner, permit trigger, duration basis and next verification.
4. **Map package:** original route in one color, confirmed/proposed alternatives in another, AHJ and constraint overlays, feature callouts, and a measured change log.
5. **Fee proposal:** separate engineering prices, $/LF calculation and denominator, feasibility-study price, reimbursables, exclusions, allowances and validity/assumptions.
6. **Evidence appendix:** dated primary source links, record identifiers, agency contact log, route version and unresolved decisions.

## Sequence to the 22 November deadline

- **13–15 November:** freeze the source inventory; send route/design-basis questions to the client; identify the bid denominator and rate inputs; prune the v4 material into a client-facing outline.
- **15–18 November:** retrieve priority ROW/rail/bridge records, verify high-risk water and state-road triggers, and record any agency responses with name, date and scope. Survey/field findings remain separately scoped if they cannot be completed before bid.
- **18–20 November:** develop the feasible alternative geometry and quantified comparison, build the approval dependency schedule, and complete the three priced lines (Chicago engineering, Ohio engineering, feasibility study).
- **20–21 November:** peer review topology, quantities, legal/permit status labels, crossings, methods, sources, maps, pricing and package contents; close or visibly price remaining uncertainty.
- **22 November:** submit only the reviewed, client-facing package.

## Review boundary

No agency was contacted, no permit or records request was submitted, and no route alternative or price was invented in this review. The existing desktop screens remain valuable as a queue for verification. They should not be converted into confirmed ROW, permit, construction method or date assertions without the named record or authority response.
