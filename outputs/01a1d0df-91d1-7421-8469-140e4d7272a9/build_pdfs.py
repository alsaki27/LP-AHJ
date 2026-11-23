from pathlib import Path
import re, html
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT, TA_RIGHT
from reportlab.lib.pagesizes import landscape, letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, LongTable, TableStyle, KeepTogether
from reportlab.pdfbase.pdfmetrics import stringWidth

root=Path(r'C:\Users\sakis\Documents\ChatGPT\LP')
out=root/'outputs'/'01a1d0df-91d1-7421-8469-140e4d7272a9'/'vendor_reports'
reports=[('Segment 0','segment0_vendor_submission_report.md','Segment_0_Vendor_EDPA_Report.pdf'),('Segment 1','segment1_vendor_submission_report.md','Segment_1_Vendor_EDPA_Report.pdf'),('Chicago Spurs','spurs_vendor_submission_report.md','Chicago_Spurs_Vendor_EDPA_Report.pdf')]
styles=getSampleStyleSheet()
styles.add(ParagraphStyle(name='CoverTitle',parent=styles['Title'],fontName='Helvetica-Bold',fontSize=20,leading=24,textColor=colors.HexColor('#17365D'),spaceAfter=10,keepWithNext=True))
styles.add(ParagraphStyle(name='H2Custom',parent=styles['Heading2'],fontName='Helvetica-Bold',fontSize=14,leading=17,textColor=colors.HexColor('#17365D'),spaceBefore=13,spaceAfter=6,keepWithNext=True))
styles.add(ParagraphStyle(name='H3Custom',parent=styles['Heading3'],fontName='Helvetica-Bold',fontSize=11.5,leading=14,textColor=colors.HexColor('#1F4E78'),spaceBefore=9,spaceAfter=5,keepWithNext=True))
styles.add(ParagraphStyle(name='H4Custom',parent=styles['Heading4'],fontName='Helvetica-Bold',fontSize=10.2,leading=12,textColor=colors.HexColor('#365F91'),spaceBefore=7,spaceAfter=4,keepWithNext=True))
styles.add(ParagraphStyle(name='BodyCustom',parent=styles['BodyText'],fontName='Helvetica',fontSize=9.3,leading=12.2,spaceAfter=5,textColor=colors.HexColor('#243447'),allowWidows=0,allowOrphans=0))
styles.add(ParagraphStyle(name='BulletCustom',parent=styles['BodyCustom'],leftIndent=14,firstLineIndent=-9,spaceAfter=3))
styles.add(ParagraphStyle(name='TableCellCustom',fontName='Helvetica',fontSize=7.5,leading=9.1,textColor=colors.HexColor('#243447'),spaceAfter=0,wordWrap='CJK'))
styles.add(ParagraphStyle(name='TableHeaderCustom',fontName='Helvetica-Bold',fontSize=7.6,leading=9.2,textColor=colors.white,spaceAfter=0,wordWrap='CJK'))
styles.add(ParagraphStyle(name='SmallCustom',parent=styles['BodyCustom'],fontSize=8.2,leading=10.2,textColor=colors.HexColor('#536273')))

def inl(s):
    s=html.escape(s,quote=False)
    s=re.sub(r'\[([^\]]+)\]\((https?://[^)]+)\)',lambda m:f'<link href="{html.escape(m.group(2),quote=True)}" color="#0563C1"><u>{m.group(1)}</u></link>',s)
    s=re.sub(r'\[([^\]]+)\]\(([^)]+)\)',lambda m:f'<i>{m.group(1)}</i>',s)
    s=re.sub(r'\*\*(.+?)\*\*',r'<b>\1</b>',s)
    s=re.sub(r'(?<!\*)\*([^*]+)\*(?!\*)',r'<i>\1</i>',s)
    s=re.sub(r'`([^`]+)`',r'<font name="Courier" size="7.6">\1</font>',s)
    return s

def splitrow(line):
    s=line.strip()
    if s.startswith('|'):s=s[1:]
    if s.endswith('|'):s=s[:-1]
    return [x.strip().replace('\\|','|') for x in re.split(r'(?<!\\)\|',s)]
def width_matrix(rows,avail):
    n=len(rows[0]); weights=[]
    for c in range(n):
        vals=[r[c] if c<len(r) else '' for r in rows[:min(len(rows),9)]]
        maxlen=max([len(v) for v in vals]+[8])
        w=1+min(maxlen,72)/34
        head=vals[0].lower()
        if any(k in head for k in ('station','priority','risk','status','date','length','fee','duration','county','feature')):w=min(w,1.35)
        weights.append(w)
    floor=min(70,avail/n*.65)
    widths=[max(floor,avail*w/sum(weights)) for w in weights]
    scale=avail/sum(widths)
    return [x*scale for x in widths]
def onpage(canvas,doc,title):
    canvas.saveState(); w,h=landscape(letter)
    canvas.setStrokeColor(colors.HexColor('#C7D3DF'));canvas.setLineWidth(.4)
    canvas.line(.58*inch,h-.42*inch,w-.58*inch,h-.42*inch)
    canvas.setFont('Helvetica',7.7);canvas.setFillColor(colors.HexColor('#657487'))
    canvas.drawString(.6*inch,h-.32*inch,'VENDOR EDPA RESPONSE  |  '+title)
    canvas.line(.58*inch,.38*inch,w-.58*inch,.38*inch)
    canvas.drawString(.6*inch,.22*inch,'Public-record desktop assessment  |  Route and parcel records are screening evidence')
    canvas.drawRightString(w-.6*inch,.22*inch,f'Page {doc.page}')
    canvas.restoreState()

def build(mdpath,pdfpath,title):
    text=mdpath.read_text(encoding='utf-8-sig'); lines=text.splitlines(); story=[]; i=0
    doc=SimpleDocTemplate(str(pdfpath),pagesize=landscape(letter),rightMargin=.58*inch,leftMargin=.58*inch,topMargin=.6*inch,bottomMargin=.56*inch,title=title,author='Vendor EDPA')
    while i<len(lines):
        line=lines[i].rstrip()
        if not line.strip():i+=1;continue
        if line.strip().startswith('|') and i+1<len(lines) and lines[i+1].strip().startswith('|'):
            raw=[]
            while i<len(lines) and lines[i].strip().startswith('|'):
                raw.append(splitrow(lines[i]));i+=1
            raw=[r for r in raw if not all(re.fullmatch(r':?-{3,}:?',x.replace(' ','')) for x in r)]
            if len(raw)<2:continue
            n=len(raw[0]); norm=[]
            for row in raw:
                if len(row)>n:row=row[:n-1]+[' | '.join(row[n-1:])]
                elif len(row)<n:row += ['']*(n-len(row))
                norm.append(row)
            data=[]
            for ri,row in enumerate(norm):data.append([Paragraph(inl(v),styles['TableHeaderCustom' if ri==0 else 'TableCellCustom']) for v in row])
            avail=landscape(letter)[0]-.58*inch*2
            tbl=LongTable(data,colWidths=width_matrix(norm,avail),repeatRows=1,hAlign='LEFT',splitByRow=1)
            cmd=[('BACKGROUND',(0,0),(-1,0),colors.HexColor('#1F4E78')),('TEXTCOLOR',(0,0),(-1,0),colors.white),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),5),('RIGHTPADDING',(0,0),(-1,-1),5),('TOPPADDING',(0,0),(-1,-1),4),('BOTTOMPADDING',(0,0),(-1,-1),4),('LINEBELOW',(0,0),(-1,0),.7,colors.HexColor('#FFFFFF')),('LINEBELOW',(0,1),(-1,-1),.25,colors.HexColor('#D5DEE7'))]
            for ri in range(2,len(data),2):cmd.append(('BACKGROUND',(0,ri),(-1,ri),colors.HexColor('#EEF3F8')))
            tbl.setStyle(TableStyle(cmd));story.extend([Spacer(1,4),tbl,Spacer(1,9)]);continue
        h=re.match(r'^(#{1,6})\s+(.*)$',line)
        if h:
            level=len(h.group(1)); txt=inl(h.group(2).strip())
            style=styles['CoverTitle'] if level==1 else styles['H2Custom'] if level==2 else styles['H3Custom'] if level==3 else styles['H4Custom']
            story.append(Paragraph(txt,style));i+=1;continue
        if re.match(r'^\s*[-*]\s+',line):
            txt=re.sub(r'^\s*[-*]\s+','',line).strip();story.append(Paragraph('-&nbsp; '+inl(txt),styles['BulletCustom']));i+=1;continue
        if re.match(r'^\s*\d+[.)]\s+',line):
            m=re.match(r'^\s*(\d+)[.)]\s+(.*)$',line);story.append(Paragraph(f'{m.group(1)}.&nbsp; '+inl(m.group(2)),styles['BulletCustom']));i+=1;continue
        if re.fullmatch(r'\s*[-*_]{3,}\s*',line):i+=1;continue
        story.append(Paragraph(inl(line.strip()),styles['BodyCustom']));i+=1
    doc.build(story,onFirstPage=lambda c,d:onpage(c,d,title),onLaterPages=lambda c,d:onpage(c,d,title))
for area,md,pdf in reports:
    build(root/'edpa_workup'/md,out/pdf,title=f'{area} Vendor EDPA Report')
    print(out/pdf)

