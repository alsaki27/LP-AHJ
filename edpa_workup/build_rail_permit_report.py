from pathlib import Path
import csv
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_CELL_VERTICAL_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

ROOT=Path(__file__).parent
OUT=ROOT/'railroad_permit_research'
OUT.mkdir(exist_ok=True)
with (ROOT/'route_rail_intersections_all_features.csv').open(encoding='utf-8-sig',newline='') as f:
    src=list(csv.DictReader(f))
with (ROOT/'spurs_rail_route_crossings_fra.csv').open(encoding='utf-8-sig',newline='') as f:
    spur=list(csv.DictReader(f))
sl={(r['route_feature'],round(float(r['route_station_ft_from_KMZ_start']))):r for r in spur}

def part(fid): return 'Segment 0' if fid.startswith('S0-') else ('Segment 1' if fid.startswith('S1-') else 'Chicago spurs')
def carrier(r):
    code=r['reported_owner_or_operator_codes']
    return {'CSXT':'CSX Transportation','NS':'Norfolk Southern','CJR':'Chicago Junction Railway; UP property-owner lead'}.get(code,code)

candidates=[]
for r in src:
    exact=r['exact_geometry_intersection']=='Y'
    candidates.append({'route_part':part(r['feature_id']),'feature_id':r['feature_id'],'state':r['state'],
      'route_station_ft_from_KMZ_start':r['feature_station_ft_from_KMZ_start'],'feature_length_ft':r['feature_length_ft_projected'],
      'nearest_track_centerline_offset_ft':r['route_to_track_min_offset_ft'],'exact_geometry_intersection':'Yes' if exact else 'No',
      'railroad_candidate':carrier(r),'NARN_RROWNER_code':r['reported_owner_or_operator_codes'],'FRAARCID':r['rail_arc_id'],
      'NARN_OBJECTID':r['narn_objectid'],'subdivision_or_line':r['subdivision'],'branch':r['branch'],'track_count_field':r['tracks'],
      'action':'Confirm exact intersection, legal ROW and license signatory.' if exact else 'Proximity lead only; screen final route, pits and railroad property before counting as a crossing.',
      'caveat':r['owner_operator_caveat'],'source':r['source_url']})
with (OUT/'rail_corridor_candidate_register.csv').open('w',encoding='utf-8-sig',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(candidates[0]));w.writeheader();w.writerows(candidates)

crossings=[]
for r in src:
    if r['exact_geometry_intersection']!='Y': continue
    fid=r['feature_id']; code=r['reported_owner_or_operator_codes']
    for st in [float(v) for v in r['feature_station_ft_from_KMZ_start'].split('|') if v]:
        if code=='CSXT':
            line='CSX / '+r['subdivision']; path='CSX Property Portal utility wireline agreement'; contact='CSX Property Portal; validate current Ohio engineering specialist in Contacts by Territory'
            issue='NARN carrier lead only; obtain valuation map, active-track confirmation and written title/operator/signatory.'
        elif code=='NS':
            line='Norfolk Southern / '+r['subdivision']; path='NS occupational license through RailPros'; contact='NS.Permitting@RailPros.com; https://ns.railprospermitting.com'
            issue='Confirm property boundary/signatory, and survey both tracks, switches, control point, signals and structures.'
        else:
            line='CJR operator / UP property owner lead / '+r['branch']; path='UP Real Estate wireline license plus CJR operations/entry concurrence'; contact='UP online application; CJR Layne Leitner, LLeitner@progressiverail.com'
            issue='UP profile and STB notice support UP ownership/CJR lease operation; obtain current title, lease scope and executing party in writing.'
        x=sl.get((fid,round(st)),{}) if fid.startswith('Spur') else {}
        crossings.append({'route_part':part(fid),'feature_id':fid,'route_station_ft_from_KMZ_start':f'{st:.1f}',
          'railroad_line':line,'track_count_field':r['tracks'],'FRAARCID':r['rail_arc_id'],'NARN_OBJECTID':r['narn_objectid'],
          'nearby_FRA_highway_crossing_ID_not_route_crossing':x.get('nearest_crossing_ID',''),
          'nearby_road_reference':x.get('nearest_crossing_street',''),'FRA_point_offset_ft':x.get('nearest_crossing_distance_ft',''),
          'permit_path':path,'first_contact':contact,'issue_to_close':issue,
          'status':'Exact route/track-centerline GIS intersection; legal ROW, method, title and approval remain open.'})
part_order={'Segment 0':0,'Segment 1':1,'Chicago spurs':2}
crossings.sort(key=lambda x:(part_order[x['route_part']],x['feature_id'],float(x['route_station_ft_from_KMZ_start'])))
with (OUT/'rail_crossing_action_register.csv').open('w',encoding='utf-8-sig',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(crossings[0]));w.writeheader();w.writerows(crossings)

online=[
 {'railroad_party':'CSX Transportation','public_role':'Owner / utility licensor for CSX corridors','online_system':'CSX Property Portal (external users register as CSX Customer); case dashboard, notes, uploads, status tracking, agreement distribution; separate Outside Party request for construction scheduling.','published_standard_clock':'Average about 30 days for CSX review; not a guaranteed completion SLA. Acknowledgement/invoice and estimated review time are sent after receipt. Variance, site assessment, incomplete package and third-party/internal review add time.','published_expedite':'$7,500 surcharge plus normal review/license charges; target 15 working days to agreement for individually pre-approved eligible cases. Published stage targets: receipt confirmation 1 business day; initial engineering review 5 business days; applicant revision due 3 business days; one re-review 2 business days; contract preparation 4 business days.','key_exclusions':'No expedite for spec deviations, shortline-leased track, rights-of-entry, bridge/MOW/public-project signoffs, drainage or casing over 36 in; expedite does not schedule flagging/construction.','published_base_cost':'Per location: underground casing <10 in $1,910 standard / $4,420 variance; higher casing sizes cost more. Add agreement/license, RPL/insurance, protection, signal locate, construction management and possible extra review costs.','source_urls':'https://www.csx.com/index.cfm/customers/value-added-services/property-real-estate/permitting-utility-wireless-infrastructure-installations-and-rights-of-entry/utility-permits/ | https://www.csx.com/index.cfm/library/files/customers/property-real-estate/permitting/utility-permits/review-fees | https://www.csx.com/index.cfm/library/files/customers/property-real-estate/permitting/expedited-service-guidelines'},
 {'railroad_party':'Norfolk Southern / RailPros','public_role':'NS pipe/wire application manager and engineering/agreement processor','online_system':'NS RailPros Permit Management Portal: register account; pipe/wire application; attachments; messages; real-time status; agreement execution; fee payment; field service coordination.','published_standard_clock':'No standard end-to-end review duration located in public NS pipe/wire program pages. RailPros states processing starts only after complete form, engineered plan/profile, scope, prior agreement if applicable and fee are received.','published_expedite':'Published portal procedure: plan review target 2 business days; draft agreement target 3 business days after engineering approval; fully executed agreement target 4 business days after applicant execution and delivery of required insurance/fees. Revisions, variance, bridge review and excluded occupancy types are outside these stage clocks.','key_exclusions':'Check current portal procedure for eligibility; expedited handling is not a blanket end-to-end SLA. Construction still requires license, written proceed authorization and scheduling of flagging/monitoring.','published_base_cost':'Underground wireline application $2,250; expedited underground wireline $8,000 additional; variance $3,500; additional reviews after first two $500 each. License, insurance/RPL or risk fee, flagging, inspection/monitoring and other services are extra.','source_urls':'https://www.norfolksouthern.com/en/rail-development-property/ns-property/projects-on-ns-property/pipe-and-wire | https://ns.railprospermitting.com/Login.aspx?ReturnUrl=%2F | https://www.norfolksouthern.com/content/dam/nscorp/rail-development-and-property/ns-property/projects-on-ns-property/pipe-and-wire/2-6-2025/Pipe%20and%20Wire%20Program%20Fees%202025.pdf | https://railpros.com/wireline'},
 {'railroad_party':'Union Pacific Real Estate','public_role':'UP property owner / permanent utility license signatory for Chicago CJR territory','online_system':'UP online Utilities Installations application. Select wireline crossing, encroachment, modification or maintenance; distinguish crossing (enters and exits ROW) from encroachment (longitudinal/does not exit). Use combined crossing+encroachment classification if both apply.','published_standard_clock':'Wireline crossing agreement processing approximately 30–45 days after a complete conforming online application. License fee based on property value is provided after review/approval. Agreements must be executed before work; verbal authorization is not allowed.','published_expedite':'Tier I $12,055 / 5 UP business days; Tier II $6,055 / 15 UP business days. Only crossing applications; combined crossing+encroachment, encroachments, deviations from standards, and pipeline crossings over 40 in cannot be rushed. Published turnaround is for application handling, not construction access or field scheduling.','key_exclusions':'Survey entry is separate temporary ROE if needed. A crossing that also occupies ROW longitudinally must follow both processes and cannot use rush handling. Coordinate CJR operations separately because UP owns property but CJR operates the short line.','published_base_cost':'No standard fee stated online for license: property-value based, set after review. Add insurance/RPL, license rent, flagging/signal protection and CJR operating/entry charges as applicable.','source_urls':'https://www.up.com/real_estate/utilities | https://www.up.com/real_estate/utilities/wireline/wireline-procedure | https://www.up.com/real_estate/utilities/wireline/wirespecs/ | https://www.up.com/shipping/short-line/lines/ctm'},
 {'railroad_party':'Chicago Junction Railway / Progressive Rail','public_role':'CJR is the local operator; UP owns the Centex/Elk Grove rail property','online_system':'CJR railroad page links to Progressive Rail Jotform Right of Entry “info/permit request.” Form captures requestor/contractor/billing, work type, location, milepost and coordinates. Treat it as a request/intake and temporary-access workflow; UP’s online Utilities application remains the permanent property license path.','published_standard_clock':'Jotform states allow up to 3–5 business days for processing. It does not promise a fully executed permanent utility license or construction release in that time. Public CJR materials reviewed did not publish a separate utility crossing review SLA, utility fee schedule or agreement lifecycle.','published_expedite':'No CJR-specific expedite tier or published permanent-license SLA found in public sources. After intake, expect further instructions/packet; obtain CJR operations concurrence, track access, signal/utility locate, flagging/monitoring and any CJR-specific agreement requirements.','key_exclusions':'A CJR Right of Entry request does not replace UP property approval. Progressive Rail generic/facility-entry terms are not proof of the CJR construction terms; do not import rates or insurance requirements from another PGR railroad/location.','published_base_cost':'CJR-specific permanent wireline application/license fees, insurance, flagging and inspection/monitoring pricing not publicly established in sources reviewed; request a written estimate through the form/contact after submitting a complete location packet.','source_urls':'https://www.progressiverail.com/rrcjr/cjr.html | https://form.jotform.com/200714027979156 | https://www.up.com/shipping/short-line/lines/ctm | https://www.govinfo.gov/content/pkg/FR-2018-05-18/pdf/2018-10665.pdf'}]
with (OUT/'railroad_online_intake_sla_register.csv').open('w',encoding='utf-8-sig',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(online[0]));w.writeheader();w.writerows(online)

def shade(c,color):
    sh=OxmlElement('w:shd');sh.set(qn('w:fill'),color);c._tc.get_or_add_tcPr().append(sh)
def margins(c):
    tc=c._tc.get_or_add_tcPr();m=OxmlElement('w:tcMar')
    for side in ('top','start','bottom','end'):
        e=OxmlElement('w:'+side);e.set(qn('w:w'),'90');e.set(qn('w:type'),'dxa');m.append(e)
    tc.append(m)
def add_table(doc,heads,rows,widths=None,fs=8):
    t=doc.add_table(rows=1,cols=len(heads));t.alignment=WD_TABLE_ALIGNMENT.CENTER;t.autofit=False
    pr=t._tbl.tblPr;b=OxmlElement('w:tblBorders')
    for edge in ('top','left','bottom','right','insideH','insideV'):
        e=OxmlElement('w:'+edge);e.set(qn('w:val'),'single');e.set(qn('w:sz'),'4');e.set(qn('w:color'),'D9E1E8');b.append(e)
    pr.append(b)
    hr=t.rows[0]._tr.get_or_add_trPr();h=OxmlElement('w:tblHeader');h.set(qn('w:val'),'true');hr.append(h)
    for i,v in enumerate(heads):
        c=t.rows[0].cells[i];c.text=v;shade(c,'17365D');margins(c);c.vertical_alignment=WD_CELL_VERTICAL_ALIGNMENT.CENTER
        if widths:c.width=Inches(widths[i])
        for p in c.paragraphs:
            p.paragraph_format.space_after=Pt(0)
            for r in p.runs:r.font.name='Aptos';r.font.size=Pt(fs);r.font.bold=True;r.font.color.rgb=RGBColor(255,255,255)
    for n,row in enumerate(rows):
        cells=t.add_row().cells
        for i,v in enumerate(row):
            c=cells[i];c.text=str(v);margins(c);c.vertical_alignment=WD_CELL_VERTICAL_ALIGNMENT.CENTER
            if n%2:shade(c,'F2F6FA')
            if widths:c.width=Inches(widths[i])
            for p in c.paragraphs:
                p.paragraph_format.space_after=Pt(0);p.paragraph_format.line_spacing=1.0
                for r in p.runs:r.font.name='Aptos';r.font.size=Pt(fs);r.font.color.rgb=RGBColor(36,48,60)
    doc.add_paragraph().paragraph_format.space_after=Pt(0)
def bullet(doc,text):
    p=doc.add_paragraph(style='List Bullet');p.paragraph_format.space_after=Pt(4);p.add_run(text)
def para(doc,lead,text):
    p=doc.add_paragraph();p.paragraph_format.space_after=Pt(6);p.add_run(lead).bold=True;p.add_run(text)

doc=Document();s=doc.sections[0]
s.top_margin=Inches(.65);s.bottom_margin=Inches(.65);s.left_margin=Inches(.72);s.right_margin=Inches(.72)
for name,size,color in [('Normal',10.5,'23303C'),('Title',27,'17365D'),('Heading 1',17,'17365D'),('Heading 2',12,'2F5597')]:
    st=doc.styles[name];st.font.name='Aptos Display' if name in ('Title','Heading 1') else 'Aptos';st.font.size=Pt(size);st.font.color.rgb=RGBColor.from_string(color)
    if name!='Normal':st.font.bold=True
head=s.header.paragraphs[0];head.text='LIGHTPATH  |  ENGINEERING DUE DILIGENCE';head.alignment=WD_ALIGN_PARAGRAPH.RIGHT
for r in head.runs:r.font.size=Pt(8);r.font.bold=True;r.font.color.rgb=RGBColor(92,107,122)
foot=s.footer.paragraphs[0];foot.alignment=WD_ALIGN_PARAGRAPH.CENTER;rr=foot.add_run('Railroad permit and property due diligence  •  13 November 2026  •  ');rr.font.size=Pt(8);rr.font.color.rgb=RGBColor(92,107,122)
fld=OxmlElement('w:fldSimple');fld.set(qn('w:instr'),'PAGE');foot._p.append(fld)

doc.add_paragraph('Railroad Crossing Permit Due Diligence',style='Title')
p=doc.add_paragraph();r=p.add_run('Chicago spurs and Marysville to New Albany engineering route');r.bold=True;r.font.size=Pt(13);r.font.color.rgb=RGBColor(77,93,110)
p=doc.add_paragraph('Vendor planning report  |  13 November 2026  |  Supplied Segment 0, Segment 1 and Chicago Spurs KMZs');p.paragraph_format.space_after=Pt(14)
para(doc,'Decision. ','Carry eleven railroad coordination cases: five on the Ohio route and six on the Chicago spurs. Ohio maps to CSX and Norfolk Southern; Chicago maps to CJR-operated tracks on UP-owned property. Keep eleven additional near-track candidates in design review until the route is frozen. A GIS track intersection does not establish legal railroad ROW, property title, final crossing method, or the license signatory.')

doc.add_heading('Executive readout',1)
for t in [
'Segment 0 has three route/track intersections: CSXT Busch Lead and two separate lines on S0-S024, CSX Columbus Line and NS Sandusky District. Segment 1 has two CSX intersections: Columbus and Scottslawn Secondary. The adjacent CSX and NS cases are separate applications and agreements.',
'The Chicago spur alignment has six intersection stations: five on Spur 3 near Touhy Avenue and Nicholas Boulevard inventory crossings, and one on Spur 4 near Lively Boulevard. UP’s short-line profile and STB FD 36193 notice support UP as underlying property owner and CJR as leased-track operator. Require a written determination of the utility-license signatory and CJR operating review.',
'Start with underground, near-perpendicular trenchless design and pits outside railroad property where practical. This is a concept only. CSX treats HDD as a variance and requires a site-specific frac-out mitigation plan. NS and UP publish materially different cover, geometry, switch, bridge and casing rules.',
'Budget risk sits in title/ROW confirmation, incomplete submittals, redesign/variance, railroad protection, signal locating, flagging and construction windows. CSX averages about 30 days for review; UP estimates about 30–45 days for agreement processing. NS publishes a detailed expedited sequence but no standard review duration on its fee page. These clocks do not equal time to mobilization.'
]:bullet(doc,t)

doc.add_heading('What the route data says',1)
doc.add_paragraph('The FRA/BTS NARN candidate file has 21 rail-line records within the screening envelope. Ten candidate records are marked as exact geometry intersections; they resolve to eleven station points because one Spur 3 rail-line record intersects the route twice. Eleven other candidate records are nearby leads, not crossings. Ohio offsets run from 26.8 to 84.6 ft; the additional Chicago candidate is 69.9 ft. Chicago FRA crossing points are reference locations, not the route/track intersection coordinates. Route stations below are KMZ-based, not railroad mileposts.')

doc.add_heading('Confirmed geometric crossing register',1)
doc.add_paragraph('Rows below are GIS intersections of the supplied route line with FRA/BTS track centerline geometry. Chicago FRA IDs and road names are nearby reference records only. Property lines and final stations require railroad maps and survey.')
cross_table=[]
for x in crossings:
    road=x['nearby_road_reference'] or '—';dot=x['nearby_FRA_highway_crossing_ID_not_route_crossing']
    ref=(road+' / FRA '+dot) if dot else 'No matched public-crossing ID in this register'
    cross_table.append([x['route_part'],x['feature_id'],x['route_station_ft_from_KMZ_start'],x['railroad_line'],x['track_count_field'],ref])
add_table(doc,['Route part','Feature','Station ft','Railroad / line','Tracks field','Nearby public crossing reference'],cross_table,[.84,1.0,.63,1.55,.5,2.55],7.5)

doc.add_heading('Near-track candidates',1)
near=[]
for x in candidates:
    if x['exact_geometry_intersection']=='No':near.append([x['route_part'],x['feature_id'],x['railroad_candidate'],x['subdivision_or_line'],x['nearest_track_centerline_offset_ft'],x['feature_length_ft']])
add_table(doc,['Route part','Feature','Railroad lead','Line','Min offset ft','Feature length ft'],near,[.85,1.0,1.62,1.3,.75,.9],7.6)
doc.add_paragraph('Overlay the final alignment, bore pits and access against railroad valuation maps and track survey. A 27–85 ft offset can still create ROW, pit, access or protection issues, but the route length is not railroad occupancy length. Do not open a crossing application solely because NARN returned a nearby line.')

doc.add_heading('Segment-by-segment findings',1)
doc.add_heading('Segment 0',2)
for t in [
'S0-S020-RR intersects the one-track CSXT Busch Lead at feature station 29.1 ft. The source feature is only 71.4 ft long; its label and length do not establish whether the design crosses perpendicular, follows an approach, or proposes bridge/rail attachment. Start a CSX property and method inquiry.',
'S0-S024-RR intersects CSX Columbus Line at station 66.4 ft and NS Sandusky District at 149.0 ft, roughly 82.6 ft apart along the supplied station axis. NARN lists one CSX track and two NS tracks. Get separate valuation/property maps, verify property and trackage rights, and obtain separate written signatory and engineering responses. Do not assume one carrier can license the other.',
'S0-S019, S0-S021 and S0-S023 are 26.8, 40.8 and 63.0/81.2 ft from track centerlines. Verify property line and construction footprint before finalizing bore pits, access or temporary workspace.'
]:bullet(doc,t)
doc.add_heading('Segment 1',2)
for t in [
'S1-S031-RR intersects the two-track CSX Columbus line at station 49.6 ft. Survey tracks, property boundary, switch/signal layout, crossing angle and bore profile before application.',
'S1-S045-RR intersects one-track CSX Scottslawn Secondary at station 35.8 ft. Confirm current track activity, ownership/operator, property width and whether CSX categorizes it as industrial, branch or running track for standards and protection.',
'S1-S030, S1-S032, S1-S044 and S1-S046 are 33.2–84.6 ft from CSX track centerlines. Treat as pit/access/property screening, not exact crossings; the long source-feature lengths do not establish parallel occupancy.'
]:bullet(doc,t)
doc.add_heading('Chicago Spurs',2)
for t in [
'Spur 3 exact stations are approximately 6,839, 12,634, 14,864, 15,519 and 16,255 ft. Nearby FRA IDs are 174076L and 174062D near Touhy, and 174061W, 174059V and 174057G near Nicholas. The recorded points are about 29.7–47.8 ft from the route/track intersections; use them as vicinity references only.',
'Spur 4 intersects CJR 709 Lead near station 5,840 ft; nearby FRA crossing 174080B is Lively Boulevard, about 19.1 ft from the route/track intersection.',
'UP’s current profile says CJR leases the Centex Industrial Park from UP and began operating June 1, 2018. The STB notice identifies UP as owner of the rail lines and CJR as the operator under lease. Apply to UP Real Estate for property rights and seek CJR operational concurrence in parallel. Obtain a written answer identifying the agreement signatory, track access, signal protection and construction monitor.'
]:bullet(doc,t)

doc.add_heading('Railroad-specific permit plan',1)
doc.add_heading('CSX Transportation',2)
para(doc,'Online system and contacts. ','Register an external account as “CSX Customer,” submit a utility wireline application, upload drawings, and track its case through Pre-Submittal, Submitted, Quality Assurance Review, Technical Review, Contract Development, and Document Distribution. The portal dashboard/status view, application notes, and attachment uploads remain available during review. Once the utility agreement and plans are approved and executed, construction is scheduled through a separate Outside Party Request in the same portal. The official Contacts by Territory sheet was revised 16 September 2024: Nick Jenkins (Nicholas_Jenkins@csx.com) is engineering/specification contact for Ohio; John White (John_C_White@csx.com) handles contract/insurance/fee compliance for Ohio. These public roles are better-supported than the old 2021 directory reference.')
para(doc,'Design. ','CSX’s wireline spec (revised 2016) calls for crossings as near 90° as practicable, never below 45°, excludes switch limits, and says no wireline under a railroad bridge, in a culvert, or within 45 ft of a bridge/building/important structure absent special approval. Low-voltage subgrade wireline design refers to CSX pipeline specs. A limited special-case jack-and-bore provision lists 4 ft below base of rail and 3 ft below ditch bottoms; casing length must account for angle, fill and multiple tracks. Confirm the currently applicable minimums with CSX for the proposed conduit size and installation. HDD is not standard and is a variance; CSX requires a project-specific frac-out mitigation plan.')
para(doc,'Review clock and price. ','CSX says its review averages around 30 days, but the portal packet does not define this as business days or guarantee an end-to-end permit date; the portal acknowledgement/invoice supplies the current estimate. Variance, site assessment, incomplete submittals and outside/internal railroad reviews add time. February 2026 published per-location underground review fee for casing under 10 in is $1,910 standard or $4,420 variance; larger casing tiers cost more. HDD is a variance. CSX may invoice protection at about $2,100/day per protection provider, signal locate at $2,100/day and construction manager at $1,500/day. Packet insurance baseline is $5M CGL plus $5M occurrence/$10M aggregate RPL, subject to agreement and possible approved risk fee. Expedite is $7,500 extra, requires prior approval, and targets an agreement for signature in 15 working days. The older detailed expedite guideline breaks that into receipt confirmation (1 business day), initial engineering review (5), applicant revisions due (3), re-review (2), and contract preparation (4); late/incomplete resubmittal falls back to standard queue. Exclusions include leased shortline trackage, rights-of-entry, bridge/MOW/public-project signoffs, drainage and casing over 36 in. It does not expedite flagging or construction scheduling.')
para(doc,'Bid allowance. ','Carry review fee per verified location, plus separate protection, signal, construction-monitor, insurance/RPL and rental allowances. Do not treat expedited agreement review as a construction-date commitment.')

doc.add_heading('Norfolk Southern',2)
para(doc,'Online system and contact. ','NS directs all pipe/wire and maintenance ROE applications to the RailPros Permit Management Portal. Register a user account to file, track status, upload attachments, message reviewers, execute agreements, pay fees, and coordinate field services. Choose the pipe/wire application; submit plan/profile, project scope, existing agreement if applicable and application fee. RailPros says review processing does not start until that complete package is received. Use NS.Permitting@RailPros.com for portal/process questions; the S0-S024 NS crossing remains a separate case and license from CSX.')
para(doc,'Design. ','NSCE-4 (24 January 2024) calls for scaled plan/profile, track and property lines, coordinates, crossing angle, nearest public grade-crossing distance and DOT ID where available, nearby utilities/signals, construction specs and engineering calculations. Cross near perpendicular and preferably at least 45°; avoid a turnout and control-point area within 50 ft, and avoid under/within 50 ft of bridge/building/important structure unless specially approved. HDD cover differs by method/material: Method A steel >10 ft below rail base or rock; plastic >15 ft. Method B steel >5.5 ft, plastic >15 ft, and it is limited to conduit up to 6 in. Over 6 in requires steel casing, with conduit limited to 8 in. NS may require track/ground monitoring, signal protection, construction procedures, flagging and monitoring. A license and written authorization to proceed are required before construction.')
para(doc,'Review clock and price. ','NS’s public pipe/wire materials do not state a standard end-to-end review duration; the portal publishes expedited-stage targets only. The February 2025 fee schedule lists $2,250 underground wireline application; $3,500 variance; $500 each review after the first two; and $8,000 expedited underground handling. License rent, insurance, flagging, monitoring, inspection and other railroad services are extra. The published expedited workflow targets plan review in 2 business days, draft agreement in 3 business days after engineering approval, and executed agreement in 4 business days after applicant execution and required insurance/fees. These are sequential stage clocks, not an overall clock from first upload to construction. Revisions, variance and excluded technical cases extend schedule; longitudinal/lateral occupancy, leased or abandoned track and under-bridge work are not eligible. The portal also offers a $1,900 NS Risk Fee in some cases instead of buying separate RPL; eligibility and coverage terms need confirmation.')
para(doc,'Bid allowance. ','Carry the $2,250 base and possible $3,500 variance per applicable case plus risk-priced railroad services; do not promise expedited completion before NS confirms eligibility.')

doc.add_heading('Union Pacific Real Estate — property license',2)
para(doc,'Online system and workflow. ','UP requires the online Utilities Installations application. Select wireline crossing, encroachment, modification or maintenance; classify the project as a crossing (traverses from one side of UP ROW to the other), encroachment (enters but does not leave/follows the ROW), or both. A combined crossing-and-encroachment package must follow both procedures and cannot be rushed. The procedure requires a complete standard Exhibit A, plan/location information and crossing tied to a fixed railroad object; if survey entry is needed, obtain a separate temporary survey ROE. UP reviews first; fee information is provided after approval, then license fees and required insurance accompany signed agreement return. No construction on verbal authority.')
para(doc,'Published clock and price. ','UP publishes approximately 30–45 days for a wireline crossing agreement; treat as a planning estimate rather than a construction-release SLA. Online rush tiers are $12,055 for a 5 UP-business-day turnaround or $6,055 for 15 UP business days. Only crossing applications qualify: encroachments, combined crossing/encroachment cases and deviations from standard engineering cannot be rushed; pipeline crossings over 40 in also cannot be rushed. Rush review does not schedule CJR operational protection, flagging, signal representative or field work. UP’s license fee is property-value based and is disclosed only after application review; insurance/RPL and field services are additional.')
para(doc,'Design. ','UP’s wireline specifications call for fiber at least 5 ft below base of rail and 5 ft below natural grade; casing extends at least 30 ft beyond the nearest track centerline each side (measured at right angles). HDD only if burial is at least 15 ft, conduit/casing is 6 in or less, and interim HDD rules are met. Do not cross under or within 150 ft of a bridge end, culvert centerline or switch. Cross near perpendicular and not below 60°. UP may require a signal representative nearby.')
para(doc,'Rail-specific constraints affecting schedule. ','UP’s wireline specification requires fiber at least 5 ft below base of rail and 5 ft below natural grade; casing extends at least 30 ft beyond nearest track centerline each side. HDD only if burial is at least 15 ft, conduit/casing is 6 in or less and UP interim criteria are met. Avoid under/within 150 ft of bridge end, culvert centerline or switch; cross at least 60° from track centerline. Signal representative may be required. The fiber hotline/CBUD is a locating step only, requires 48-hour preconstruction notice, and does not grant property rights or authorize work.')
doc.add_heading('Chicago Junction Railway / Progressive Rail — operator coordination and access',2)
para(doc,'Public system and role. ','CJR’s railroad page links directly to the Progressive Rail “Right of Entry — Info/permit request” Jotform. This is a public intake for entry/operations; the form collects requester and contractor, billing party, utility new-install or maintenance type, nearest roadway, milepost, latitude/longitude and project details. CJR’s UP-hosted short-line profile says CJR leases the Centex Industrial Park from UP; the STB filing says UP owns the lines and CJR operates under a lease. Consequently, use the UP online utility application for the permanent license and the CJR/PGR form for local operating concurrence, access, and any required ROE packet.')
para(doc,'Published clock and cost boundary. ','The Progressive Rail form states “allow up to 3–5 business days for processing.” That is an intake/processing estimate—not a guarantee of completed engineering review, signed UP license, CJR approval or work release. The public CJR page/form reviewed does not publish a CJR-specific permanent utility crossing SLA, license fee schedule, expedite tier, insurance terms or a full online status lifecycle. Do not import charges or insurance terms from a generic Progressive Rail document for a different railroad/property. After submission, the form says Layne Leitner (LLeitner@progressiverail.com) is the contact; collect current track chart, proposed dates, signal/utility locate process, flagging/monitoring and any CJR agreement/rates through the official process.')
para(doc,'Bid allowance. ','Carry separate UP application/license and CJR operational review/entry tasks; identify UP rent and railroad services as open allowances until written cost and schedule responses are received.')

doc.add_heading('Recommended delivery workflow and schedule gates',1)
steps=[
('0  Freeze the route baseline','Confirm endpoints, route direction, KMZ version, station origin, datum and design footprint. Distinguish cable centerline from pits, access and work limits. Resolve any route join gaps before railroad filing.'),
('1  Request railroad records and written jurisdiction','Send pre-application inquiries to CSX, NS/RailPros, UP Real Estate and CJR. Request valuation/property maps; owner/operator/signatory; track, switch, bridge, culvert and signal data; existing railroad utilities; required plan set; fees/rent/insurance; expected review, field-service and work-window dates.'),
('2  Survey only under authorized entry','Survey track centers, ROW/property limits, switches, signals/control points, bridges and culverts. Run SUE for railroad communication and signal lines. Tie each crossing angle and route station to a fixed railroad object and stated datum.'),
('3  Develop separate railroad-compliant concepts','Compare perpendicular HDD, approved jack-and-bore, authorized spare casing, and endpoint-preserving reroute. Show cover, casing limits, pits outside property where practical, geotechnical basis, monitoring and frac-out response, access, construction sequence, spoils and restoration.'),
('4  File separate complete cases','Open one case per actual owner/property interest with CSX, NS and UP; pair UP property application with CJR operating concurrence. Use unique case IDs and railroad-specific drawings. Combine cases only if each railroad accepts it in writing.'),
('5  Close comments, license and construction release','Track review cycles, variances, insurance and license terms. Obtain executed license and written permission to proceed; separately schedule ROW entry, flagging, signal protection, monitoring and work window.'),
('6  Finalize bid schedule after responses','Use published review clocks as anchors; add design revisions, title resolution, insurance, CJR operational review, railroad contractor services and actual work-window availability. Permit processing time is not total time to mobilize.')]
for title,body in steps:para(doc,title+'. ',body)

doc.add_heading('Online intake and published service clocks — four railroad parties',1)
doc.add_paragraph('This is the online-first path. “Turnaround” clocks below apply to specific application stages or stated agreement review only; none is a promise that flagging, field access, construction windows or all other permits will be ready by that date. No applications, emails, record requests or permits were submitted during this review.')
add_table(doc,['Party','Online system and what it does','Published SLA / fee basis / limits'],[
['CSX — owner / licensor','CSX Property Portal: external account; utility application; QA/technical/contract lifecycle; live case status, messages and attachments. Separate Outside Party Request schedules construction after signed agreement/approved plans.','Standard review averages ~30 days (not defined as business days; estimate, not guarantee). Casing <10 in: $1,910 standard / $4,420 variance. $7,500 expedite for eligible, pre-approved jobs targets 15 working days to agreement; stage targets 1/5/3/2/4 business days (receipt/first review/applicant revision/re-review/contract). Exclusions and protection costs apply.'],
['Norfolk Southern — application manager','NS RailPros Permit Management Portal: pipe/wire app, account-based tracking, attachments, messaging, agreement execution, online payments and field-service coordination.','No public standard end-to-end SLA found. Complete application + engineered plan/profile + scope + prior agreement if relevant + fee starts review. Underground wireline $2,250; $8,000 expedite extra. Expedited stages target 2 business days for plan, 3 after engineering approval for draft, 4 after applicant signature/insurance/fees for execution.'],
['Union Pacific Real Estate — owner','UP online Utilities application: crossing, encroachment, both, modification or maintenance. Fee and insurance steps follow engineering review; separate survey ROE may be needed.','Wireline crossing estimate 30–45 days. Rush: $12,055/5 UP business days or $6,055/15; pure eligible crossings only. No rush for encroachment/combined/deviation cases. Property-value license rent, insurance and field services are additional.'],
['CJR / Progressive Rail — operator','CJR page → Progressive Rail “Right of Entry — Info/permit request” Jotform. It collects requester/contractor, billing, new utility vs. maintenance, location, MP and coordinates. This is entry/intake, not UP’s permanent property license.','Form says allow up to 3–5 business days to process intake. Public CJR materials reviewed do not publish a utility-license SLA, fee schedule, expedite tier or online engineering-status lifecycle. CJR operating concurrence, any ROE packet and work protection remain separate.']],[1.35,2.55,3.18],7.2)

doc.add_heading('What online research resolves — and what remains a case-specific question',2)
for t in [
'Resolved before filing: which system handles each application; the published standard or expedited review clocks; application fees and published exclusions; required plans/track geometry; whether agreements, fees and insurance must be in hand before entry; and which railroad is owner versus operator in the Chicago spurs.',
'Not resolved by public pages: railroad valuation/title map at each route station; current legal license signatory and exact ROW limits; confirmation that the GIS crossing actually occupies railroad-owned land; current active tracks, switches, signals, culverts/bridges and fiber; final method acceptability/variance; exact rents, RPL premium, protection/flagging/inspection cost; and firm dates for railroad field windows.',
'Vendor scheduling rule: start route/property classification and portal account setup now; prepare one complete engineered plan/profile package for each confirmed property interest. Run UP permanent license and CJR operation/entry coordination in parallel. Do not include a field-mobilization date until executed license, written proceed authorization, insurance, locates, flagging and work window are all confirmed.'
]:bullet(doc,t)

doc.add_heading('Records and plan set before filing',1)
for t in [
'One-page route key map: project, municipality/county, railroad, line name, road reference, station, north arrow and design limits. Include railroad milepost after confirmed.',
'Per-crossing scaled plan and profile: title/ROW limits, tracks and track centers, angle, cover, casing/conduit, casing extents, pits, access, road ROW, utilities, bridge/culvert/switch/control-point/signal offsets, restoration and work limits.',
'Survey control/datum, professional engineer calculations when requested, geotechnical and groundwater data, SUE and railroad signal/fiber locate results.',
'For HDD: frac-out/returns containment and response plan, pressure/fluid controls, workspace, monitoring, contingency and abandonment procedure, and railroad variance approval.',
'Execution items: written owner/signatory evidence, valuation map, signed permanent license and temporary ROE, road-authority permits, insurance/RPL, fee payment, flagging/monitoring plan, construction schedule and required pre-work locates.'
]:bullet(doc,t)

doc.add_heading('Evidence and bid status',1)
doc.add_paragraph('The supplied KMZ route lines were screened against FRA/BTS NARN line geometry; Chicago public crossing IDs were cross-checked against FRA grade-crossing records. Carrier permit standards, public fee pages and UP/STB CJR ownership-operation records were reviewed 13 November 2026. Inventory track count is not field-confirmed. Stations are approximate GIS values and must be re-established in survey.')
doc.add_paragraph('This is bid planning, not final design, title opinion, railroad concurrence, right-of-entry, permit, or construction authorization. NARN owner/responsibility codes do not prove deeded title or signatory. Ohio CSX/NS carrier leads support starting separate inquiries, but title and operating rights must be confirmed. In Chicago, UP ownership/CJR leased operation is supported by UP’s current short-line profile and STB FD 36193, but current title, lease scope and signatory remain open. No carrier or agency was contacted.')

doc.add_heading('Primary sources',1)
sources=[
('FRA/BTS North American Rail Network Lines','https://services.arcgis.com/xOi1kZaI0eWDREZv/arcgis/rest/services/NTAD_North_American_Rail_Network_Lines/FeatureServer/0'),
('FRA Railroad Grade Crossings','https://services.arcgis.com/xOi1kZaI0eWDREZv/arcgis/rest/services/NTAD_Railroad_Grade_Crossings/FeatureServer/0'),
('CSX utility permit process and portal','https://www.csx.com/index.cfm/customers/value-added-services/property-real-estate/permitting-utility-wireless-infrastructure-installations-and-rights-of-entry/utility-permits/'),
('CSX Permit Information Packet, February 2026','https://www.csx.com/share/wwwcsx15/assets/File/Customers/Property/permit-information-packet.pdf'),
('CSX Property Portal lifecycle and applicant tutorial','https://www.csx.com/index.cfm/library/files/customers/property-real-estate/permitting/utility-permits/property-portal-tutorial/'),
('CSX utility review fee schedule, February 2026','https://www.csx.com/index.cfm/library/files/customers/property-real-estate/permitting/utility-permits/review-fees'),
('CSX expedited service guidelines','https://www.csx.com/index.cfm/library/files/customers/property-real-estate/permitting/expedited-service-guidelines'),
('CSX contacts by territory, revised 16 September 2024','https://www.csx.com/index.cfm/library/files/customers/property-real-estate/permitting/utility-permits/contacts-by-territory'),
('CSX Wireline Specifications, revised December 2016','https://www.csx.com/index.cfm/library/files/customers/property-real-estate/permitting/wireline-design-construction-specifications'),
('Norfolk Southern pipe and wire permits and fees','https://www.norfolksouthern.com/en/rail-development-property/ns-property/projects-on-ns-property/pipe-and-wire'),
('NSCE-4 Wireline Occupancy Specifications, January 2024','https://www.norfolksouthern.com/content/dam/nscorp/pdf/public-projects/Specs-wire-conduit-cable-occupations-NSCE-4%20-1.24.24.pdf'),
('NS Pipe and Wire Program Fees, February 2025','https://www.norfolksouthern.com/content/dam/nscorp/rail-development-and-property/ns-property/projects-on-ns-property/pipe-and-wire/2-6-2025/Pipe%20and%20Wire%20Program%20Fees%202025.pdf'),
('RailPros online wireline application requirements','https://railpros.com/wireline'),
('UP Wireline Procedure','https://www.up.com/real_estate/utilities/wireline/wireline-procedure'),
('UP Utilities Installations online process and rush handling','https://www.up.com/real_estate/utilities'),
('UP Wireline Engineering Specifications','https://www.up.com/real_estate/utilities/wireline/wirespecs/'),
('UP CJR short-line profile','https://www.up.com/customers/shortline/lines/ctm/'),
('STB/Federal Register, CJR FD 36193, May 18, 2018','https://www.govinfo.gov/content/pkg/FR-2018-05-18/pdf/2018-10665.pdf'),
('Progressive Rail CJR Right-of-Entry request','https://form.jotform.com/200714027979156'),
('Progressive Rail Chicago Junction Railway page','https://www.progressiverail.com/rrcjr/cjr.html'),
('Illinois Commerce Commission 2026 Railroad CEOs and Designated Agents','https://icc.illinois.gov/api/web-management/documents/downloads/public/rr/2026%20Railroad%20CEOs%20and%20Designated%20Agents.pdf')]
for label,url in sources:
    p=doc.add_paragraph(style='List Bullet');p.paragraph_format.space_after=Pt(2);p.add_run(label+': ');r=p.add_run(url);r.font.size=Pt(8.2);r.font.color.rgb=RGBColor(31,78,121)

# Word's built-in Title style can inject a horizontal paragraph border in compatibility mode.
title_style=doc.styles['Title']._element
title_ppr=title_style.find(qn('w:pPr'))
if title_ppr is not None:
    border=title_ppr.find(qn('w:pBdr'))
    if border is not None:title_ppr.remove(border)
title_ppr_direct=doc.paragraphs[0]._p.get_or_add_pPr()
border=title_ppr_direct.find(qn('w:pBdr'))
if border is not None:title_ppr_direct.remove(border)
doc.save(OUT/'railroad_crossing_permit_due_diligence.docx')
print(f"candidate rows={len(candidates)} exact records={sum(x['exact_geometry_intersection']=='Yes' for x in candidates)} near rows={sum(x['exact_geometry_intersection']=='No' for x in candidates)} intersection station rows={len(crossings)}")
