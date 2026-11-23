from pathlib import Path
import zipfile, shutil, xml.etree.ElementTree as ET
root=Path(r'C:\Users\sakis\Documents\ChatGPT\LP')
old=root/'Vendor_EDPA_Full_Analysis_Package.zip'
new=root/'Vendor_EDPA_Full_Analysis_Package_v2.zip'
tracker=root/'outputs'/'01a1d0df-91d1-7421-8469-140e4d7272a9'/'AHJ_Permit_Readiness_Tracker.xlsx'
playbook=root/'edpa_workup'/'permit_readiness_playbook.md'
readme=root/'edpa_workup'/'README_FULL_ANALYSIS.md'
with zipfile.ZipFile(old,'r') as zin, zipfile.ZipFile(new,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as zout:
    seen=set()
    for info in zin.infolist():
        name=info.filename
        if info.is_dir():
            zout.writestr(info,b''); seen.add(name); continue
        disk=root.joinpath(*Path(name).parts)
        data=disk.read_bytes() if disk.is_file() else zin.read(name)
        zout.writestr(name,data); seen.add(name)
    for p in sorted((root/'edpa_workup').rglob('*')):
        if not p.is_file(): continue
        name=p.relative_to(root).as_posix()
        if name not in seen:
            zout.write(p,name); seen.add(name)
    zout.write(tracker,'permit_readiness/AHJ_Permit_Readiness_Tracker.xlsx')
# Verify workbook container and sheet count
with zipfile.ZipFile(tracker) as z:
    bad=z.testzip()
    wb=ET.fromstring(z.read('xl/workbook.xml'))
    sheets=wb.find('{http://schemas.openxmlformats.org/spreadsheetml/2006/main}sheets')
    sheet_names=[s.attrib['name'] for s in sheets]
    assert bad is None, bad
    assert len(sheet_names)==8, sheet_names
# Verify full package CRC
with zipfile.ZipFile(new) as z:
    bad=z.testzip()
    assert bad is None, bad
    print(f'Workbook sheets: {sheet_names}')
    print(f'Package entries: {len(z.namelist())}; package bytes: {new.stat().st_size}; CRC: OK')
print(f'Playbook chars: {len(playbook.read_text(encoding="utf-8-sig"))}; tracker bytes: {tracker.stat().st_size}')

