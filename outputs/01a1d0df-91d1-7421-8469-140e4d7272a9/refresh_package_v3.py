from pathlib import Path
import zipfile, xml.etree.ElementTree as ET
root=Path(r'C:\Users\sakis\Documents\ChatGPT\LP')
old=root/'Vendor_EDPA_Full_Analysis_Package_v2.zip'
new=root/'Vendor_EDPA_Full_Analysis_Package_v3.zip'
report_dir=root/'outputs'/'01a1d0df-91d1-7421-8469-140e4d7272a9'/'vendor_reports'
tracker='permit_readiness/AHJ_Permit_Readiness_Tracker.xlsx'
with zipfile.ZipFile(old,'r') as zin, zipfile.ZipFile(new,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as zout:
    seen=set()
    for info in zin.infolist():
        name=info.filename
        if info.is_dir(): zout.writestr(info,b''); seen.add(name); continue
        disk=root.joinpath(*Path(name).parts)
        data=disk.read_bytes() if disk.is_file() else zin.read(name)
        zout.writestr(name,data); seen.add(name)
    for p in sorted((root/'edpa_workup').rglob('*')):
        if not p.is_file(): continue
        name=p.relative_to(root).as_posix()
        if name not in seen: zout.write(p,name); seen.add(name)
    for pdf in sorted(report_dir.glob('*.pdf')):
        zout.write(pdf,f'vendor_reports/{pdf.name}')
with zipfile.ZipFile(root/'outputs'/'01a1d0df-91d1-7421-8469-140e4d7272a9'/'AHJ_Permit_Readiness_Tracker.xlsx') as z:
    assert z.testzip() is None
    wb=ET.fromstring(z.read('xl/workbook.xml'))
    sheets=wb.find('{http://schemas.openxmlformats.org/spreadsheetml/2006/main}sheets')
    assert len(sheets)==8
with zipfile.ZipFile(new) as z:
    assert z.testzip() is None
    names=z.namelist()
    assert len(names)==len(set(names)), 'duplicate archive paths'
    expected=['vendor_reports/Segment_0_Vendor_EDPA_Report.pdf','vendor_reports/Segment_1_Vendor_EDPA_Report.pdf','vendor_reports/Chicago_Spurs_Vendor_EDPA_Report.pdf',tracker,'edpa_workup/segment0_vendor_exhibits.kmz','edpa_workup/segment1_vendor_submission_report.md','edpa_workup/spurs_vendor_screening_exhibit.kmz']
    missing=[n for n in expected if n not in names]
    assert not missing,missing
    print(f'Package entries={len(names)} bytes={new.stat().st_size}; duplicate paths=0; CRC=OK; deliverables verified')
