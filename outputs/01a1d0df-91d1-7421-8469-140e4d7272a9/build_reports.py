from pathlib import Path
import re
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.section import WD_ORIENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_CELL_VERTICAL_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

root=Path(r'C:\Users\sakis\Documents\ChatGPT\LP')
out=root/'outputs'/'01a1d0df-91d1-7421-8469-140e4d7272a9'/'vendor_reports'
reports=[
 ('Segment 0','segment0_vendor_submission_report.md','Segment_0_Vendor_EDPA_Report.docx'),
 ('Segment 1','segment1_vendor_submission_report.md','Segment_1_Vendor_EDPA_Report.docx'),
 ('Chicago Spurs','spurs_vendor_submission_report.md','Chicago_Spurs_Vendor_EDPA_Report.docx'),
]

def set_cell_shading(cell, fill):
    tcPr=cell._tc.get_or_add_tcPr(); shd=OxmlElement('w:shd'); shd.set(qn('w:fill'),fill); tcPr.append(shd)
def set_cell_margins(cell, top=80, start=90, bottom=80, end=90):
    tc=cell._tc; tcPr=tc.get_or_add_tcPr(); mar=OxmlElement('w:tcMar')
    for m,v in [('top',top),('start',start),('bottom',bottom),('end',end)]:
        node=OxmlElement('w:'+m); node.set(qn('w:w'),str(v)); node.set(qn('w:type'),'dxa'); mar.append(node)
    tcPr.append(mar)
def repeat_header(row):
    trPr=row._tr.get_or_add_trPr(); el=OxmlElement('w:tblHeader'); el.set(qn('w:val'),'true'); trPr.append(el)
def add_hyperlink(paragraph,text,url):
    part=paragraph.part; rel=part.relate_to(url,'http://schemas.openxmlformats.org/officeDocument/2006/relationships/hyperlink',is_external=True)
    h=OxmlElement('w:hyperlink'); h.set(qn('r:id'),rel)
    run=OxmlElement('w:r'); rPr=OxmlElement('w:rPr')
    color=OxmlElement('w:color'); color.set(qn('w:val'),'0563C1'); rPr.append(color)
    under=OxmlElement('w:u'); under.set(qn('w:val'),'single'); rPr.append(under)
    run.append(rPr); t=OxmlElement('w:t'); t.text=text; run.append(t); h.append(run); paragraph._p.append(h)
def inline(paragraph,text):
    pat=re.compile(r'(\*\*.*?\*\*|\*[^*]+\*|`[^`]+`|\[[^\]]+\]\([^)]+\))')
    pos=0
    for m in pat.finditer(text):
        if m.start()>pos: paragraph.add_run(text[pos:m.start()])
        tok=m.group(0)
        if tok.startswith('**'):
            rr=paragraph.add_run(tok[2:-2]); rr.bold=True
        elif tok.startswith('*'):
            rr=paragraph.add_run(tok[1:-1]); rr.italic=True
        elif tok.startswith('`'):
            rr=paragraph.add_run(tok[1:-1]); rr.font.name='Consolas'; rr.font.size=Pt(8)
        else:
            mm=re.match(r'\[([^\]]+)\]\(([^)]+)\)',tok)
            if mm:
                label,url=mm.groups()
                if url.startswith('http://') or url.startswith('https://'): add_hyperlink(paragraph,label,url)
                else:
                    rr=paragraph.add_run(label); rr.italic=True
        pos=m.end()
    if pos<len(text): paragraph.add_run(text[pos:])
def split_row(line):
    s=line.strip()
    if s.startswith('|'): s=s[1:]
    if s.endswith('|'): s=s[:-1]
    cells=re.split(r'(?<!\\)\|',s)
    return [c.strip().replace('\\|','|') for c in cells]
def add_table(doc,lines):
    parsed=[split_row(x) for x in lines]
    parsed=[r for r in parsed if not all(re.fullmatch(r':?-{3,}:?',c.replace(' ','')) for c in r)]
    if len(parsed)<2:return
    cols=len(parsed[0]); norm=[]
    for row in parsed:
        if len(row)>cols: row=row[:cols-1]+[' | '.join(row[cols-1:])]
        elif len(row)<cols: row=row+['']*(cols-len(row))
        norm.append(row)
    tbl=doc.add_table(rows=1,cols=cols)
    tbl.alignment=WD_TABLE_ALIGNMENT.CENTER; tbl.autofit=True
    try: tbl.style='Light Shading Accent 1'
    except: tbl.style='Table Grid'
    repeat_header(tbl.rows[0])
    for ri,row in enumerate(norm):
        cells=tbl.rows[0].cells if ri==0 else tbl.add_row().cells
        if ri>0:
            trPr=tbl.rows[-1]._tr.get_or_add_trPr(); cant=OxmlElement('w:cantSplit'); trPr.append(cant)
        for ci,val in enumerate(row):
            cell=cells[ci]; cell.text=''; cell.vertical_alignment=WD_CELL_VERTICAL_ALIGNMENT.CENTER; set_cell_margins(cell)
            p=cell.paragraphs[0]; p.paragraph_format.space_after=Pt(0); p.paragraph_format.line_spacing=1.0
            inline(p,val)
            for run in p.runs:
                run.font.name='Arial'; run.font.size=Pt(7.6 if cols>=5 else 8.3); run.font.color.rgb=RGBColor(35,48,62)
                if ri==0: run.bold=True; run.font.color.rgb=RGBColor(255,255,255)
            if ri==0: set_cell_shading(cell,'1F4E78')
            elif ri%2==0: set_cell_shading(cell,'EAF1F7')
    doc.add_paragraph().paragraph_format.space_after=Pt(2)

def add_page_field(p):
    p.alignment=WD_ALIGN_PARAGRAPH.RIGHT
    p.add_run('Page ')
    fld=OxmlElement('w:fldSimple'); fld.set(qn('w:instr'),'PAGE'); p._p.append(fld)

for area,mdfile,docname in reports:
    text=(root/'edpa_workup'/mdfile).read_text(encoding='utf-8-sig')
    doc=Document(); sec=doc.sections[0]; sec.orientation=WD_ORIENT.LANDSCAPE
    sec.page_width=Inches(11); sec.page_height=Inches(8.5)
    sec.left_margin=Inches(.62); sec.right_margin=Inches(.62); sec.top_margin=Inches(.62); sec.bottom_margin=Inches(.58)
    normal=doc.styles['Normal']; normal.font.name='Arial'; normal.font.size=Pt(9.5); normal.font.color.rgb=RGBColor(36,48,62)
    normal.paragraph_format.space_after=Pt(5); normal.paragraph_format.line_spacing=1.05
    for sty,size,color in [('Title',20,'17365D'),('Heading 1',14,'17365D'),('Heading 2',11.5,'1F4E78'),('Heading 3',10.5,'365F91')]:
        s=doc.styles[sty]; s.font.name='Arial'; s.font.size=Pt(size); s.font.bold=(sty!='Title' or True); s.font.color.rgb=RGBColor.from_string(color)
        s.paragraph_format.space_before=Pt(12 if sty!='Title' else 2); s.paragraph_format.space_after=Pt(5); s.paragraph_format.keep_with_next=True
    header=sec.header.paragraphs[0]; header.alignment=WD_ALIGN_PARAGRAPH.LEFT
    rr=header.add_run(f'Vendor EDPA Response  |  {area}'); rr.font.name='Arial'; rr.font.size=Pt(8); rr.font.color.rgb=RGBColor(90,102,116)
    footer=sec.footer.paragraphs[0]; rr=footer.add_run('Desktop due diligence from supplied route and public records  |  '); rr.font.name='Arial'; rr.font.size=Pt(8); rr.font.color.rgb=RGBColor(90,102,116); add_page_field(footer)
    lines=text.splitlines(); i=0; first_title=True
    while i<len(lines):
        line=lines[i].rstrip()
        if not line.strip(): i+=1; continue
        if line.strip().startswith('|') and i+1<len(lines) and lines[i+1].strip().startswith('|'):
            block=[]
            while i<len(lines) and lines[i].strip().startswith('|'):
                block.append(lines[i]);i+=1
            add_table(doc,block); continue
        hm=re.match(r'^(#{1,6})\s+(.*)$',line)
        if hm:
            level=len(hm.group(1)); title=hm.group(2).strip()
            if level==1 and first_title:
                p=doc.add_paragraph(style='Title'); inline(p,title); first_title=False
            else:
                heading_level=min(level,3); p=doc.add_paragraph(style=f'Heading {heading_level}'); inline(p,title)
            i+=1; continue
        if re.match(r'^\s*[-*]\s+',line):
            p=doc.add_paragraph(style='List Bullet'); inline(p,re.sub(r'^\s*[-*]\s+','',line)); i+=1; continue
        if re.match(r'^\s*\d+[.)]\s+',line):
            p=doc.add_paragraph(style='List Number'); inline(p,re.sub(r'^\s*\d+[.)]\s+','',line)); i+=1; continue
        if re.fullmatch(r'\s*[-*_]{3,}\s*',line): i+=1; continue
        p=doc.add_paragraph(); inline(p,line.strip()); i+=1
    path=out/docname; doc.save(path); print(path)
