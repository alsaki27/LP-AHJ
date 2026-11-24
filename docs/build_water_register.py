"""Build the offline crossing data from the GIS evidence and decision register."""

import csv
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent / 'data'
SOURCE_LINKS = {
    'dupage': ('DuPage Highway Permits', 'https://www.dupagecounty.gov/government/departments/transportation/doing_business/permits/construction_permits.php'),
    'itasca': ('Itasca utility plan requirements', 'https://www.itasca.com/DocumentCenter/View/16622/Utility-Permit-projects-Requirmentspdf'),
    'devonproof': ('Devon drainage investigation', 'research.html#proof-CHI-W01'),
    'devonplan': ('IDOT 63055 drainage plan and profile, sheet 32', 'https://apps.dot.illinois.gov/eplan/desenv/110708/63055-064/Plans/110708-63055-064-094-032-11x17.pdf'),
    'devonstudy': ('Itasca hydraulic study, March 2025 packet pp. 24–26 and 33–34', 'https://www.itasca.com/AgendaCenter/ViewFile/Agenda/_03182025-1164?packet=true#page=24'),
    'cook': ('Cook DoTH utility permit intake', 'https://www.cookcountyil.gov/service/constructionmaintenance-permits'),
    'idotbridge': ('IDOT structure inventory', 'https://gis1.dot.illinois.gov/arcgis/rest/services/TrafficSafety/cis_LocationTool2026/MapServer/4'),
    'idnr': ('IDNR waterway permits', 'https://dnr.illinois.gov/waterresources/permitprograms.html'),
    'mwrd': ('MWRD permit determinations', 'https://www.mwrd.org/doing-business/watershed-management-ordinance-and-infiltrationinflow/watershed-management-ordinance-wmo-and-technical-guidance-manual-tgm/watershed-management-ordinance-wmo-frequently-asked-questions-faqs'),
    'elk': ('Elk Grove Village utility code', 'https://codelibrary.amlegal.com/codes/elkgrovevillageil/latest/elkgrovevillage_il/0-0-0-6645'),
    'licking': ('Licking County Engineer utility permit', 'https://lickingcounty.gov/depts/engineer/permits.htm'),
    'newalbany': ('New Albany ROW application and checklist', 'https://newalbanyohio.org/right-of-way/'),
    'franklin': ('Franklin County Engineer utility application', 'https://www.franklincountyengineer.org/wp-content/uploads/2016/04/Application-for-permit-pdf.pdf'),
    'odot': ('ODOT ROW permit intake', 'https://www.transportation.ohio.gov/business/permits/row-permits'),
    'rose': ('New Albany Rose Run project', 'https://newalbanyohio.org/news/2026/10/rose-run-phase-two-update-s-high-st-lane-closure-through-nov-25/'),
    'columbus': ('Columbus Chapter 903 utility ROW rules', 'https://columbus.legistar.com/LegislationDetail.aspx?FullText=1&GUID=3522B4CF-33A3-4278-A9E9-EED1F2325E6E&ID=7480234'),
    'sancus': ('Columbus Sancus Boulevard improvements', 'https://engage.columbus.gov/sancusboulevardimprovements'),
    'highbanks': ('Highbanks Metro Park', 'https://www.metroparks.net/parks-and-trails/highbanks/'),
    'delaware': ('Delaware County utility and ROW permits', 'https://engineer.co.delaware.oh.us/permits/'),
    'home315': ('Home Road bridge and SR 315 project', 'https://engineer.co.delaware.oh.us/projects/home315/'),
    'scenic': ('ODNR Olentangy Scenic River', 'https://ohiodnr.gov/go-and-do/plan-a-visit/find-a-property/olentangy-scenic-river'),
    'liberty': ('County and Liberty Township permit assignments', 'https://engineer.co.delaware.oh.us/permits/'),
    'concord': ('County and Concord Township permit assignments', 'https://engineer.co.delaware.oh.us/permits/'),
    'powell': ('Powell ROW ordinance', 'https://www.cityofpowell.us/files/assets/city/v/1/city-council/documents/ordinances/2022/ordinance-2022-11.pdf'),
    'countyagreement': ('Delaware–Columbus agreement, Resolution 01-957', 'https://co.delaware.oh.us/wp-content/uploads/commissioners/journal/2001/jnlaug27.pdf'),
    'watershed': ('Columbus Watershed Management', 'https://www.columbus.gov/Services/Columbus-Water-Power/About-Columbus-Water-Power/The-Division-of-Water/Reservoir-Land-Stewardship-Program/About-the-Columbus-Watershed-Management-Section'),
    'roundabout': ('Home Road and SR 745 County project', 'https://engineer.co.delaware.oh.us/home-road-sr-745-intersection-improvements/'),
    'union': ('Union County April 2026 utility requirements', 'https://www.unioncountyohio.gov/media/Officials/Engineer/road-bridge/workwithinrwrequirements_2026_04_01.pdf'),
    'marysville': ('Marysville Chapter 901', 'https://www.marysvilleohio.org/documentview.aspx?did=303'),
    'watkinswater': ('Marysville Scottslawn–US 42 water main', 'https://www.marysvilleohio.org/803/Scottslawn-To-US-42-Water-Main-Extension'),
}


def evidence_key(feature, station):
    return feature, round(float(station), 1)


def build():
    with (ROOT / 'water_crossing_point_evidence.csv').open(encoding='utf-8-sig', newline='') as stream:
        evidence = {evidence_key(row['feature'], row['station_ft']): row for row in csv.DictReader(stream)}

    crossings = []
    for line in (ROOT / 'water_decisions.txt').read_text(encoding='utf-8').splitlines():
        if not line or line.startswith('#'):
            continue
        (identifier, feature, station, name, priority, method, blocker, lead,
         conditional, submit, fallback, sources) = line.split('|')
        point = evidence.pop(evidence_key(feature, station))
        crossings.append({
            'id': identifier, 'segment': point['segment'], 'feature': feature,
            'station': float(station), 'name': name, 'priority': priority,
            'method': method, 'blocker': blocker, 'lead': lead,
            'conditional': conditional, 'submit': submit, 'fallback': fallback,
            'lat': float(point['latitude']), 'lon': float(point['longitude']),
            'evidence': point,
            'sources': [SOURCE_LINKS[key] for key in sources.split(',')] + [
                ('Official flowline layer', point['source_layer'])
            ],
        })
    if evidence:
        raise ValueError(f'Unmatched mapped points: {sorted(evidence)}')
    if len({row['id'] for row in crossings}) != len(crossings):
        raise ValueError('Crossing IDs must be unique')
    (ROOT / 'water.js').write_text(
        'window.WATER_CROSSINGS = ' + json.dumps(crossings, ensure_ascii=False, indent=2) + ';\n',
        encoding='utf-8',
    )


if __name__ == '__main__':
    build()
