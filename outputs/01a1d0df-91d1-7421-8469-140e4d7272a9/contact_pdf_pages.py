from pathlib import Path
from PIL import Image,ImageOps,ImageDraw
base=Path(r'C:\Users\sakis\Documents\ChatGPT\LP\outputs\01a1d0df-91d1-7421-8469-140e4d7272a9\vendor_reports')
for tag in ['s0','s1','spurs']:
 files=sorted((base/f'qa_{tag}').glob('page-*.png'))
 pages=[Image.open(f).convert('RGB') for f in files]
 for start in range(0,len(pages),4):
  group=pages[start:start+4]
  thumbs=[]
  for idx,im in enumerate(group,start+1):
   im.thumbnail((850,660))
   canvas=Image.new('RGB',(870,690),'white');canvas.paste(im,((870-im.width)//2,22))
   ImageDraw.Draw(canvas).text((12,5),f'{tag} page {idx}',fill='black'); thumbs.append(canvas)
  sheet=Image.new('RGB',(1740,1380),'#d8dee7')
  for j,im in enumerate(thumbs):sheet.paste(im,((j%2)*870,(j//2)*690))
  sheet.save(base/f'contact_{tag}_{start//4+1}.png')
 print(tag,'pages',len(files))
