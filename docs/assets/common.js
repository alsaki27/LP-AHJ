window.$=(s,r)=> (r||document).querySelector(s);window.$$=(s,r)=>[...(r||document).querySelectorAll(s)];
window.esc=s=>String(s==null?'':s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
window.fmt=n=>Math.round(n).toLocaleString('en-US');
window.SEGS={Segment0:'Segment 0',Segment1:'Segment 1',Spurs:'Chicago spurs'};
window.CLS_COL={'State DOT':'#c0262d','State DOT (limited access)':'#7b0f16','State route in city':'#e8590c','County':'#1f6feb','County-numbered, in city':'#7048e8','County-numbered road, city maintains':'#7048e8','County-numbered road, shared / unresolved':'#e03131','Municipal street':'#2a8f5c','Township':'#a0762c','Off-road / no public road':'#888'};
window.LAND_COL={'Mapped / presumptive public ROW':'#2a8f5c','Private parcel':'#d6336c','Public-owner parcel':'#1098ad','Parcel (owner not published)':'#e8a317','Unparceled (public ROW / water / rail)':'#868e96'};
window.SEV_COL={Critical:'#c0262d',High:'#e07b00',Medium:'#c9a400'};
window.nav=function(active){
 const items=[['index.html','Director Brief'],['map.html','Engineering map'],['water.html','Water crossings'],['report.html','Jurisdiction report'],['construction.html','Project risks'],['jdx.html','Requirements & contacts'],['research.html','Research & proof']];
 $('#nav').setAttribute('role','navigation');
 $('#nav').setAttribute('aria-label','Atlas pages');
 $('#nav').innerHTML='<b>Lightpath AHJ Atlas</b>'+items.map(([href,label])=>
   `<a href="${href}"${href===active?' class="on" aria-current="page"':''}">${label}</a>`
 ).join('')+'<span class="sp"></span><small>Baseline · '+LP.built+'</small>';
};
window.csv=function(rows,name){const keys=Object.keys(rows[0]||{});const q=v=>'"'+String(v==null?'':Array.isArray(v)?v.join('; '):v).replace(/"/g,'""')+'"';
 const t=keys.join(',')+'\n'+rows.map(r=>keys.map(k=>q(r[k])).join(',')).join('\n');const a=document.createElement('a');a.href=URL.createObjectURL(new Blob([t],{type:'text/csv'}));a.download=name;a.click();};
window.lightbox=function(src,cap){let l=$('#lightbox');if(!l){l=document.createElement('div');l.id='lightbox';l.innerHTML='<img><div class="cap"></div>';l.onclick=()=>l.style.display='none';document.body.appendChild(l);}
 $('img',l).src=src;$('.cap',l).textContent=cap||'';l.style.display='flex';};
window.sortable=function(tbl){$$('th',tbl).forEach((th,i)=>th.onclick=()=>{const tb=tbl.tBodies[0];const rows=[...tb.rows];const asc=th.dataset.asc!=='1';th.dataset.asc=asc?'1':'0';
 rows.sort((a,b)=>{const x=a.cells[i].dataset.v??a.cells[i].textContent,y=b.cells[i].dataset.v??b.cells[i].textContent;const nx=parseFloat(String(x).replace(/,/g,'')),ny=parseFloat(String(y).replace(/,/g,''));
  const r=(!isNaN(nx)&&!isNaN(ny))?nx-ny:String(x).localeCompare(String(y));return asc?r:-r;});rows.forEach(r=>tb.appendChild(r));});};
