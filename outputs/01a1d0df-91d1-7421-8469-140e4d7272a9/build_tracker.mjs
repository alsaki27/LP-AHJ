import fs from 'node:fs/promises';
import path from 'node:path';
import { SpreadsheetFile, Workbook } from '@oai/artifact-tool';

const root='C:/Users/sakis/Documents/ChatGPT/LP';
const src=path.join(root,'edpa_workup');
const out=path.join(root,'outputs/01a1d0df-91d1-7421-8469-140e4d7272a9');
function parseCsv(s){
  const rows=[]; let row=[], v='', q=false;
  for(let i=0;i<s.length;i++){const c=s[i]; if(q){if(c==='"'&&s[i+1]==='"'){v+='"';i++;}else if(c==='"'){q=false;}else v+=c;}else if(c==='"')q=true;else if(c===','){row.push(v);v='';}else if(c==='\n'){row.push(v.replace(/\r$/,''));rows.push(row);row=[];v='';}else v+=c;}
  if(v.length||row.length){row.push(v.replace(/\r$/,''));rows.push(row);} return rows;
}
async function csv(file){return parseCsv(await fs.readFile(path.join(src,file),'utf8'));}
function setTable(sheet, rows, tableName, widths=[]){
  if(!rows.length)return;
  const n=rows[0].length; const endCol=col(n); const endRow=rows.length;
  sheet.getRange(`A1:${endCol}${endRow}`).values=rows;
  const tbl=sheet.tables.add(`A1:${endCol}${endRow}`,true,tableName);
  try{tbl.style='TableStyleMedium2';}catch{}
  sheet.showGridLines=false;
  sheet.freezePanes.freezeRows(1);
  sheet.getRange(`A1:${endCol}1`).format={fill:'#1F4E78',font:{bold:true,color:'#FFFFFF',size:10},wrapText:true,verticalAlignment:'center',horizontalAlignment:'center'};
  sheet.getRange(`A1:${endCol}${endRow}`).format.verticalAlignment='center';
  sheet.getRange(`A2:${endCol}${endRow}`).format.wrapText=true;
  if(endRow>1) sheet.getRange(`A2:${endCol}${endRow}`).format.rowHeight=42;
  sheet.getRange(`A1:${endCol}${endRow}`).format.font={name:'Arial',size:9,color:'#243447'};
  sheet.getRange(`A1:${endCol}1`).format.font={name:'Arial',size:10,bold:true,color:'#FFFFFF'};
  sheet.getRange(`A1:${endCol}1`).format.rowHeight=36;
  if(widths.length) widths.forEach((w,i)=>{sheet.getRange(`${col(i+1)}:${col(i+1)}`).format.columnWidth=w;});
  else sheet.getRange(`A1:${endCol}${endRow}`).format.autofitColumns();
}
function col(n){let s='';while(n){let r=(n-1)%26;s=String.fromCharCode(65+r)+s;n=Math.floor((n-1)/26)}return s;}
function addSheet(wb,name){return wb.worksheets.add(name);}
function omitCols(rows, names){if(!rows.length)return rows;const h=rows[0], ids=h.map((x,i)=>names.includes(x)?i:-1).filter(i=>i>=0);return rows.map(r=>r.filter((_,i)=>!ids.includes(i)));}

const wb=Workbook.create();
const start=addSheet(wb,'Start Here');
start.showGridLines=false;
const startRows=[
 ['AHJ / ROW PERMIT READINESS — CHI SPURS + OHIO S0/S1'],
 ['As of','12 Nov 2026'],
 ['Direct answer','ODOT D6: state-route candidates identified across Franklin, Delaware and Union overlays. ODOT D5: geographic coverage in Licking County (~3.03 route mi), but no State-classified road candidate identified there in the current screen. No ODOT ROW is legally confirmed yet.'],
 ['What triggers a permit','Work envelope inside the controlling owner’s actual ROW/property (cable, bore pits, access, staging, restoration) or a crossing/structure approval. County/city/district polygon alone is not a permit trigger.'],
 ['How to use this workbook','Filter Authority Rules for package / utilities / timeline. Filter Ohio State Gates and Chicago Gates by feature and station. Filter Station Ledger for county, place, township, road candidate and confirming record. Stations are feet from supplied KMZ feature start—not surveyed or road logpoints.'],
 ['Key answer: utilities shown?','Default to show all known/available existing utilities with source/date/confidence and conflict notes. Ohio ORC 3781.27 creates a statewide designer utility-information duty. Local checklists differ: Columbus and Union explicitly list existing utilities; Cook County asks all public/private utilities; Itasca asks crossing/parallel utilities; a silent checklist is not permission to omit them. Illinois JULIE design notice is separate from dig-ticket locate.'],
 ['Published clocks vs planning allowances','Only report published clocks as such. Columbus plan routing: 20 business days initial per department; 10 business days resubmittal per department. Union County complete permit target: generally 2 business days. Delaware County asks submit 4–8 weeks ahead. Cook County says apply 2–3 months ahead. ODOT utility permit, IDOT D1, most other local agencies: no utility-specific guaranteed SLA found. Vendor allowances are separate estimates.'],
 ['Immediate P0 actions','1) Get OhROW acquisition plans at D6 state-road candidate stations and confirm exact ROW owner in writing. 2) Resolve Columbus, Delaware, Franklin, Union, Licking and township road-controller spans from official ROW plans/delegations. 3) Request utility as-builts/design tickets and build SUE plan. 4) Confirm bridge/rail/water/property rights before fixing route or price. 5) Check pavement moratoria and active capital projects by road/station.'],
 ['Critical scope caveat','The route is conceptual, labels (Bore/Water/HW/RR) are unverified, and OH S0/S1 has a ~31.1 m join gap. Route endpoint/tie-in, installed LF basis and exact road/ROW stationing remain open. No agency has been contacted.'],
 ['Definitions','AHJ = authority having jurisdiction. “Candidate” = GIS/record lead requiring ROW/title/owner confirmation. “Trigger” = confirmed work/occupancy in owner-controlled property or a separate crossing/structure requirement. “No SLA found” means no published commitment located, not zero review time.']
];
start.getRange(`A1:B${startRows.length}`).values=startRows;
start.getRange('A1:B1').merge(); start.getRange('A1').format={font:{name:'Arial',size:15,bold:true,color:'#17365D'},rowHeight:30};
start.getRange('A2:B10').format={font:{name:'Arial',size:10,color:'#243447'},wrapText:true,verticalAlignment:'top'};
start.getRange('A2:A10').format={font:{name:'Arial',size:10,bold:true,color:'#1F4E78'},columnWidth:32};
start.getRange('B2:B10').format.columnWidth=120;
for(let i=2;i<=startRows.length;i++)start.getRange(`A${i}:B${i}`).format.rowHeight=i===2?22: i===3?58: i===4?48: i===5?50: i===6?65: i===7?64: i===8?58: i===9?50:40;

const ohioRules=await csv('ohio_ahj_permit_requirements_matrix.csv');
const chicago=await csv('chicago_permit_station_candidate_matrix.csv');
const district=await csv('ohio_odot_district_station_intervals.csv');
const state=await csv('ohio_state_route_station_summary.csv');
const stations=await csv('route_station_ahj_candidate_register.csv');
const water=await csv('route_water_crossing_concept_register.csv');
const rail=await csv('route_rail_intersections_all_features.csv');
function numericCols(rows, indexes){for(let r=1;r<rows.length;r++)for(const i of indexes){const v=rows[r][i];if(typeof v==='string'&&/^\s*-?\d+(?:\.\d+)?\s*$/.test(v))rows[r][i]=Number(v);}}
numericCols(district,[5,6,7,8]);
numericCols(state,[5,6,7]);
numericCols(chicago,[1,2,3,4,6,13]);
numericCols(stations,[3,4,5]);
numericCols(water,[3,4]);
numericCols(rail,[2,3,4]);
const rulesSheet=addSheet(wb,'Authority Rules');
let rules=[ohioRules[0],...ohioRules.slice(1)];
// Add Illinois authority-specific operating rules and timeline distinction.
rules.push(
 ['IDOT District 1','Only if proposed work occupies State-maintained highway ROW; three exact centerline intersection gates listed in Chicago Gates.','Spur1-S03 Higgins 7,224–7,428 ft; Spur3-S01 Busse 11,707–11,907 ft; Spur4-S01 Busse 9,074–9,275 ft. Verify acquisition ROW and portal owner.','Owner/municipality applicant; current OPER1113; State route/county/municipality/from-to; plan/map, scaled design and traffic control; separate application at county boundary.','Plan/map must show work limits, utility type/size/material/method, ROW line and fixed road reference, existing conditions reasonably available, crossings, MOT.','No published review SLA found. District 1 guide has winter moratorium Nov 1–Apr 15; confirm exception/seasonal controls.','Current fees/bond based on permit; confirm in guide/portal.','District 1 permit only where IDOT ROW. County/city permits can also apply. Avoid treating centerline hit as ROW confirmation.','No SLA; winter stop and revisions can shift critical path.','Official D1 Utility Permit Guide; current row/owner verification required.','https://idot.illinois.gov/doing-business/permit-and-sales-marketplace/utility-permits.html; https://idot.illinois.gov/content/dam/soi/en/web/idot/documents/doing-business/memorandums-and-letters/permits/district-1-utility-permit-guide.pdf'],
 ['Cook County DoTH','Only where work enters an actual Cook County highway ROW; boundary or route adjacency alone does not trigger.','Devon Spur1-S01 1,603–1,803 ft; Landmeier Spur1-S03 3,129–3,343 ft; verify County jurisdiction map/ROW.','Electronic packet; utility owner applicant, exact County route/section, signed plat/legal description, work and ROW dimensions, traffic-control/closures, other approvals.','Explicit: show all public and private utilities in County ROW; include existing/proposed conditions, roadway context (~300 ft), elevation/topography/drainage, ROW line/offset; PE stamp/signature.','Apply 2–3 months ahead (published lead-time advice, not guaranteed SLA); 2-day advance notice before work.','$100 nonrefundable application fee plus permit fees; packet includes $50,000 bond/insurance path for certain multiple permits—confirm applicability.','Only permit County highway ROW; separate municipality, state or waterway permits remain.','Long lead-time; bonding/insurance and County ROW proof; incomplete utility/plat package.','County source + permit packet; station spans are road-centerline GIS leads.','https://www.cookcountyil.gov/service/constructionmaintenance-permits; https://www.cookcountyil.gov/sites/g/files/ywwepo161/files/documents/2025-04/Construction%20Permit%20Packet%20utilities%202024-11.pdf'],
 ['Elk Grove Village','If facilities occupy/disrupt Village ROW or facilities; check franchise/license and route station.','Dominant spur overlay (~48,181 ft total boundary screen); road candidates in Chicago Gates. Itasca interval Spur1-S01 730.5–1,704.2 ft.','Application, certified engineered utility plans, traffic control + emergency contingency, insurance/security; permit before install/change/disruption.','Show proposed/known utilities and ROW. Underground comms near ROW line (within 5 ft where code applies); roadway crossing near 90 degrees. Do not cross culverts; bridge attachments only after alternatives.','General plan-review benchmark ~10 working days for most complete plans; not a utility ROW issuance SLA. Planning allowance 2–4 weeks, not published.','$1,500 application fee unless franchise/license exception; $500/LF parallel under-road duct manual fee could apply; perpendicular HDD crossing excluded. Get written ruling for telecom scope/length.','Under-road parallel is high price risk; route around or use perpendicular HDD only where engineering/ROW feasible.','Fee scope/franchise interpretation; insurance/security; parallel fee; permit package completeness.','Official code/manual; confirm utility fee and franchise applicability with Village.','https://codelibrary.amlegal.com/codes/elkgrovevillageil/latest/elkgrovevillage_il/0-0-0-6832; https://www.elkgrove.org/home/showpublisheddocument/14605/638962210206270000'],
 ['Itasca','If work enters Itasca Village ROW/property; corporate-boundary interval is not ROW proof.','Spur1-S01 730.5–1,704.2 ft (~974 ft) boundary span.','Plan per construction segment with method, length, ROW/easements, traffic control; complete new permit on resubmittal.','Explicit: show utilities crossing/parallel/near route; method and segment lengths, offsets, ROW/easements; nearby floodplain/wetlands and tree/hydrant protection. Standard notes: 5-ft horizontal from Village utilities.','No utility-specific SLA. Generic FAQ 10–14 days for most permits, not utility-specific; planning 3–4 weeks is an allowance.','Fee/security/insurance need current intake confirmation.','Restore pavement/landscape within 14 days; separate Village utility clearances.','Utility conflict checks and resubmittal; no committed utility clock.','Official utility checklist; general review clock not specific to fiber.','https://www.itasca.com/DocumentCenter/View/16622/Utility-Permit-projects-Requirmentspdf; https://itasca.com/286/Building-Division'],
 ['Illinois JULIE / design notice','Design phase planning notice across route; not a construction permit and not the later excavation ticket.','Apply to all IL spur route areas where member utility facilities may conflict.','Designer sends plans or provides plan access to member utilities; capture owner response and utility location/confidence.','Utility owners return best available facility location/type info within 10 days for a valid Planning/Design Stage request. Put data into base utility composite.','10-day statutory/design process response framework; excavation dig ticket is separate (2 working days min, max 10 days before dig under current law).','No permit fee in this row; separate from authority permits.','A JULIE design request does not replace SUE, engineering, permit plan review or the excavation ticket.','Utility response gaps, stale records and potholes can control plan completion.','Official JULIE and Illinois statute.','https://www.illinois1call.com/planning-design/; https://www.illinois1call.com/excavatorsafetyguide/types-of-requests/; https://www.ilga.gov/Legislation/ILCS/Articles?ActID=1286&ChapterID=23&Print=True'],
 ['New Albany','If work enters City ROW/property; corporate boundary does not alone trigger.','Feature intervals in Station Ledger; verify specific City road or facility at ROW limits.','CAD + PDF utility plans, all existing/proposed utilities, pavement, buildings, addressed property lines, hardscape/landscape, poles/pedestals/vaults/handholes/transformers, retaining walls and culverts; MOT, COI, bond, construction schedule; pre-application site visit.','Explicitly requires all existing and proposed utilities plotted.','No application review SLA. 5 business days for lane closure notice; final schedule 14 working days before start; 48-hour start notice after approval. Six-month permit validity.','$75 per permit; City-set bond; inspection may be billed.','Must complete pre-application site visit; confirm City/ODOT split at US/State route.','Site-visit sequencing, bond, lane closure and existing utility mapping.','2026 City ROW application; use current application at design.','https://newalbanyohio.org/right-of-way/; https://newalbanyohio.org/wp-content/uploads/2026/01/Right-of-way-Permit-Application-Fillable-1.26-1.pdf'],
 ['Marysville','If work enters City ROW; confirm city/state split near US36/US33 and ramps.','Feature intervals in Station Ledger; road ownership to confirm per station.','City contractor license/registration; ROW permit; scaled facility and work drawing dimensioned to landmarks/road edge/ROW; MOT if lane closure; inspection and restoration provisions.','Scaled facility/work drawing is explicit; surfaced requirements do not explicitly enumerate all existing utilities. Show known utilities as vendor standard; request checklist.','No plan-review SLA found. Schedule inspector 24h ahead; OUPS notice 48h before construction; restore within 30 days.','ROW construction fee shown as TBD; confirm current fees.','Secure City road-owner direction and ODOT D6 concurrence if State-controlled ROW/structure is implicated.','Route owner overlap and fee schedule uncertainty.','Official Marysville form/FAQ; verify current city contractor registration.','https://www.marysvilleohio.org/FormCenter/Engineering-19/RightofWay-Work-132; https://www.marysvilleohio.org/m/faq; https://www.marysvilleohio.org/DocumentCenter/View/275'],
 ['Powell','If provider actually occupies City ROW; check franchise/service agreement.','Feature boundary spans in Station Ledger; confirm City-owned road ROW.','Annual provider certificate/ROW registration with utility mapping, contacts, insurance and bond; construction permit; approved traffic control and schedule.','Utility mapping is required in provider registration; current construction drawing list not fully enumerated in reviewed source. Plot all known utilities and ask City to confirm details.','No standard utility review duration found.','2026: $1,000 registration; annual maintenance $5,000 (<10 ROW mi) or $10,000 (>=10 ROW mi), possible agreement exception; $100 base construction permit; actual plan review; base inspection $250 in roadway/sidewalk/pathway ($100 outside) plus actual; $50 supplemental.','Confirm qualifying franchise/service agreement and City ROW miles before price.','Potential annual cost, agreement exception and no review SLA.','2026 official fee schedule and City development toolkit.','https://www.cityofpowell.us/About-Us/Departments/Planning-Department/Development-Toolkit; https://www.cityofpowell.us/files/assets/city/v/1/finance/documents/2026-fee-schedule_to-publish.pdf'],
 ['Worthington','If work enters City ROW; separate utility/telecom ROW permit.','Feature boundary intervals in Station Ledger; verify City ROW roads, particularly near state-route candidates.','Permittee field-locates/exposes all utilities whether or not depicted; survey HDD path and stake entry/exit; sewer video before/after if crossed; provide as-built/no-damage closeout.','Must field-locate/expose all existing utilities whether or not they appear on plans.','No permit review SLA found. Notify City 72 working hours ahead; property owners 1 week; 48h before outage/access disruption.','Fee total not established in reviewed source; confirm.','HDD/sewer inspection and closeout are additional design/construction schedule tasks.','Utility exposure, sewer-video closeout and notice windows.','Official current ROW standards and permit page.','https://www.worthington.org/298/Right-of-Way-Work-Permits; https://www.worthington.org/DocumentCenter/View/4888/Worthington-Work-in-Right-of-Way-Standards']
);
setTable(rulesSheet,rules,'AuthorityRules',[26,34,34,38,40,34,32,38,34,32,42]);
rulesSheet.getRange(`A2:K${rules.length}`).format.rowHeight=106;
const stateSheet=addSheet(wb,'Ohio State Gates');
setTable(stateSheet,[state[0],...state.slice(1)],'OhioStateGates',[15,28,22,22,12,24,24,20,26,34]);
const districtSheet=addSheet(wb,'Ohio District Coverage');
setTable(districtSheet,[district[0],...district.slice(1)],'OhioDistrictCoverage',[12,28,20,14,26,25,25,26,24,44,54,65]);
const ilSheet=addSheet(wb,'Chicago Gates');
setTable(ilSheet,chicago,'ChicagoPermitGates',[28,18,20,20,28,14,20,17,22,34,40,28,28,28,34,60,24,36,36,50,50,44]);
const stSheet=addSheet(wb,'Station Ledger');
setTable(stSheet,stations,'StationLedger',[14,27,18,22,22,18,24,34,34,48,54,50,74,74]);
const watSheet=addSheet(wb,'Water Gates');
setTable(watSheet,water,'WaterGates',[20,28,24,25,23,22,26,40,65,65,60,62,55,72]);
const railSheet=addSheet(wb,'Rail Gates');
setTable(railSheet,rail,'RailGates',[28,14,20,24,24,25,26,20,40,30,24,14,25,25,70,70]);

await wb.recalculate();
const summary=await wb.inspect({kind:'workbook,sheet,table',maxChars:4500,tableMaxRows:3,tableMaxCols:6,tableMaxCellChars:45});
await fs.writeFile(path.join(out,'workbook_inspect.json'),JSON.stringify(summary,null,2));
const file=await SpreadsheetFile.exportXlsx(wb);
await file.save(path.join(out,'AHJ_Permit_Readiness_Tracker.xlsx'));
for(const name of ['Start Here','Authority Rules','Ohio State Gates','Chicago Gates']){
  const preview=await wb.render({sheetName:name,autoCrop:'all',scale:0.7,format:'png'});
  await fs.writeFile(path.join(out,`${name.replaceAll(' ','_')}_preview.png`),new Uint8Array(await preview.arrayBuffer()));
}
console.log(JSON.stringify({sheets:8,authorityRows:rules.length-1,ilCandidates:chicago.length-1,ohioStateBands:state.length-1,stationRows:stations.length-1,waterRows:water.length-1,railRows:rail.length-1,out:path.join(out,'AHJ_Permit_Readiness_Tracker.xlsx')}));
