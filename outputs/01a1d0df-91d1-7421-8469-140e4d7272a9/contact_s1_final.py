from pathlib import Path
from PIL import Image,ImageDraw
base=Path(r'C:\Users\sakis\Documents\ChatGPT\LP\outputs\01a1d0df-91d1-7421-8469-140e4d7272a9\vendor_reports\qa3_s1')
files=sorted(base.glob('page-*.png'),key=lambda p:int(p.stem.split('-')[-1]))
pages=[Image.open(f).convert('RGB') for f in files]
group=pages[8:]
sheet=Image.new('RGB',(1740,1380),'#d8dee7')
for j,im in enumerate(group):
 im.thumbnail((850,660)); c=Image.new('RGB',(870,690),'white'); c.paste(im,((870-im.width)//2,22)); ImageDraw.Draw(c).text((12,5),f'S1 page {j+9}',fill='black'); sheet.paste(c,((j%2)*870,(j//2)*690))
sheet.save(Path(r'C:\Users\sakis\Documents\ChatGPT\LP\outputs\01a1d0df-91d1-7421-8469-140e4d7272a9\vendor_reports\contact_s1_final.png'))
