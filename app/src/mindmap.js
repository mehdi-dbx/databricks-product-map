// ---- state holders (DATA is swapped per tab via loadTree) ----
let DATA = TREES.ai, _id=0, byId={};
function initTree(){
  _id=0; byId={};
  (function walk(n,parent,depth){ n.id='n'+(_id++); n._p=parent; n._depth=depth; byId[n.id]=n; (n.children||[]).forEach(c=>walk(c,n,depth+1)); })(DATA,null,0);
}

const COLW=300, GAP=18, INDENT=22, ROOTW=280, ROOTH=56, PILLH=50, FEATH=42, SUBH=32, PILLY=140, VGAP=9, MARGIN=24;
let lastSize={w:1200,h:640};
const SC={GA:'#1B3139',PuP:'#2272B4',Beta:'#B06A00',PrivPreview:'#8a9aa1',Announced:'#b4b9bc',Legacy:'#a05a5a'};
let selNode=null;
let state={tx:28,ty:28,k:1, newOnly:false, hideVerify:false, q:''};
const vp=document.getElementById('viewport');
const svg=document.getElementById('svg');
const stage=document.getElementById('stage');
const panelEl=document.getElementById('panel');
const panelTab=document.getElementById('panelTab');

function esc(s){return (s||'').replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');}
// display names without dates; the JSON keeps the full name
const MON='(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|June?|July?|Aug(?:ust)?|Sep(?:t(?:ember)?)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)';
const DATE_RE=new RegExp('\\b'+MON+'\\b|\\b20\\d\\d\\b','i');
const TRAIL_DATE_RE=new RegExp('\\s+(?:through|until|as of)\\s+'+MON+'\\b.*$','i');
function dn(s){
  return (s||'').replace(/\s*\(([^()]*)\)/g,(m,inner)=>DATE_RE.test(inner)?'':m).replace(TRAIL_DATE_RE,'').trim();
}
function shortDoc(u){ try{ const x=new URL(u); const seg=x.pathname.split('/').filter(Boolean).pop()||x.hostname; return seg.replace(/[-_]/g,' ').slice(0,30); }catch(e){ return 'link'; } }

// ---- layout: pillars across the top, each a vertical indented file-tree ----
function place(node,colX,cur){
  node._x=colX+(node._depth-1)*INDENT;
  node._w=(COLW-GAP)-(node._depth-1)*INDENT;
  node._h=(node._depth===2?FEATH:SUBH);
  node._y=cur.y; cur.y+=node._h+VGAP;
  if(!node.collapsed && node.children) node.children.forEach(ch=>place(ch,colX,cur));
}
function layout(){
  const pillars=DATA.children; let maxB=0;
  pillars.forEach((p,i)=>{
    const colX=MARGIN+i*COLW;
    p._depth=1; p._x=colX; p._y=PILLY; p._w=COLW-GAP; p._h=PILLH;
    const cur={y:PILLY+PILLH+VGAP};
    if(!p.collapsed && p.children) p.children.forEach(ch=>place(ch,colX,cur));
    p._bottom=cur.y; if(p._bottom>maxB) maxB=p._bottom;
  });
  DATA._depth=0; DATA._w=ROOTW; DATA._h=ROOTH;
  const firstX=pillars[0]._x, lastX=pillars[pillars.length-1]._x+(COLW-GAP);
  DATA._x=(firstX+lastX)/2-ROOTW/2; DATA._y=MARGIN;
  return {w:MARGIN+pillars.length*COLW, h:Math.max(maxB,PILLY+180)+MARGIN};
}
function visibleNodes(){ const out=[]; (function rec(n){ out.push(n); if(!n.collapsed && n.children) n.children.forEach(rec); })(DATA); return out; }

function computeFlags(nodes){
  const q=state.q.trim().toLowerCase();
  nodes.forEach(n=>{n._hit=false;n._dim=false;});
  nodes.forEach(n=>{
    if(q){ const hay=(n.n+' '+(n.note||'')).toLowerCase(); if(hay.includes(q)) n._hit=true; }
    if(n._depth>=2){
      if(state.newOnly && !n.new) n._dim=true;
      if(state.hideVerify && n.c==='verify') n._dim=true;
    }
  });
  if(q){ nodes.forEach(n=>{ if(n._depth>0 && !n._hit) n._dim=true; }); }
}

function render(){
  lastSize=layout();
  const nodes=visibleNodes();
  computeFlags(nodes);
  svg.setAttribute('viewBox',`0 0 ${stage.clientWidth} ${stage.clientHeight}`);

  let links='';
  // root → pillars (curved fan)
  const rb={x:DATA._x+DATA._w/2, y:DATA._y+DATA._h};
  DATA.children.forEach(p=>{ const pt={x:p._x+14, y:p._y}, my=(rb.y+pt.y)/2;
    links+=`<path class="link" d="M${rb.x},${rb.y} C${rb.x},${my} ${pt.x},${my} ${pt.x},${pt.y}"/>`; });
  // in-column file-tree spines (pillar→feature, feature→sub)
  nodes.forEach(n=>{
    if(n._depth>=1 && !n.collapsed && n.children && n.children.length){
      const spineX=n._x+12, top=n._y+n._h, last=n.children[n.children.length-1], bottom=last._y+last._h/2;
      links+=`<path class="link" d="M${spineX},${top} L${spineX},${bottom}"/>`;
      n.children.forEach(c=>{ const cy=c._y+c._h/2; links+=`<path class="link${c.c==='verify'?' toverify':''}" d="M${spineX},${cy} L${c._x},${cy}"/>`; });
    }
  });

  let fo='';
  nodes.forEach(n=>{
    const hasKids=!!(n.children&&n.children.length);
    const cls=`node d${n._depth}${n._hit?' hit':''}${n._dim?' dim':''}${n===selNode?' sel':''}`;
    const dot = hasKids ? '<span class="ddot"></span>' : '';
    const warn = n.c==='verify' ? '<span class="flag warn">⚠</span>' : '';
    let inner='';
    if(n._depth===0){
      inner=`<div class="nm">${esc(dn(n.n))}</div>`;
    } else if(n._depth===1){
      const tog=hasKids?`<span class="ptoggle">${n.collapsed?'▸':'▾'}</span>`:'';
      inner=`<div class="nm">${tog}${esc(dn(n.n))}</div>`+
            `<div class="meta">${n.sub?`<span class="sub">${esc(n.sub)}</span>`:''}<span class="count">${(n.children||[]).length} items</span>${dot}</div>`;
    } else if(n._depth===2){
      const tog=hasKids?`<span class="ptoggle">${n.collapsed?'▸':'▾'}</span>`:'';
      inner=`<div class="nm">${tog}${esc(dn(n.n))}</div>`+
            `<div class="meta">${n.s?`<span class="chip s-${n.s}">${n.s}</span>`:''}${warn}${dot}</div>`;
    } else {
      inner=`<div class="nm">${esc(dn(n.n))}</div>`+
            `<div class="meta">${n.s?`<span class="chip s-${n.s}">${n.s}</span>`:''}${warn}${dot}</div>`;
    }
    fo+=`<foreignObject class="${cls}" x="${n._x}" y="${n._y}" width="${n._w}" height="${n._h}" data-id="${n.id}">`+
        `<div xmlns="http://www.w3.org/1999/xhtml" class="nodebox d${n._depth}${n.c==='verify'?' verify':''}">${inner}</div>`+
        `</foreignObject>`;
  });

  vp.innerHTML=links+fo;
  applyTransform();
}

function applyTransform(){ vp.setAttribute('transform',`translate(${state.tx},${state.ty}) scale(${state.k})`); }
function fitView(){
  const vw=stage.clientWidth, vh=stage.clientHeight;
  const k=Math.min(1.1,(vw-40)/lastSize.w,(vh-40)/lastSize.h);
  state.k=Math.max(0.2,k);
  state.tx=Math.max(10,(vw-lastSize.w*state.k)/2);
  state.ty=18;
  applyTransform();
}

// ---- interactions ----
vp.addEventListener('click',e=>{
  const fo=e.target.closest('foreignObject'); if(!fo) return;
  const n=byId[fo.dataset.id]; if(!n) return;
  if(n.children&&n.children.length&&n._depth>=1){ n.collapsed=!n.collapsed; }
  showPanel(n);
  render();
});

// ---- panel helpers ----
function mdBold(s){ return esc(s).replace(/\*\*(.+?)\*\*/g,'<b>$1</b>'); }
const RANK={ga:4,beta:3,partial:2,unverified:1,none:0};
const WINLBL={home:'DATABRICKS',field:'FIELD',parity:'PARITY'};
let APPMODE='customer';
function dbxLosesRow(cap,homeId){
  const h=RANK[(cap.cells[homeId]||{}).status]??0;
  return Object.entries(cap.cells).some(([id,c])=>id!==homeId && (RANK[c.status]??0)>h);
}
function docsFor(n){
  let docs=(n.docs&&n.docs.length)?n.docs:[];
  if(!docs.length){ let p=n._p; while(p){ if(p.docs&&p.docs.length){ docs=p.docs; break; } p=p._p; } }
  return docs;
}
function docsHTML(n){
  const docs=docsFor(n);
  return docs.length?`<div class="pdocs">`+docs.map(u=>`<a href="${u}" target="_blank" rel="noopener">↗ ${esc(shortDoc(u))}</a>`).join('')+`</div>`:'';
}
function metaFor(n){
  let m='';
  const par=(n._p&&n._p._depth>=1)?n._p:null;
  if(par){ const PLBL={1:'Pillar',2:'Capsule',3:'Feature',4:'Group',5:'Group'}; m+=`<div class="pmeta"><b>${PLBL[par._depth]||'Parent'}:</b> ${esc(dn(par.n))}</div>`; }
  if(n.deck) m+=`<div class="pdeck">Deck · ${esc(n.deck)}</div>`;
  return m;
}
function solveBlockHTML(n){
  const rows=n.solves.map(s=>
    `<div class="solverow"><div class="solvecell sc-prob">${mdBold(s.problem)}</div>`+
    `<div class="solvecell sc-axis">${esc(s.axis)}</div>`+
    `<div class="solvecell sc-sol">${mdBold(s.solution)}</div></div>`).join('');
  return `<div class="toggrow"><label class="ptoggleswitch"><input type="checkbox" id="solveTg"><span class="ptrack"></span><span class="pknob"></span></label>`+
         `<span class="toghint" id="solveHint">without the tool</span></div>`+
         `<div class="solveblock off" id="solveBlock">${rows}</div>`;
}
function matrixHTML(m){
  const comps=m.competitors, n=comps.length+1, homeId=m.home, internal=(APPMODE==='internal');
  const lg='<div class="mx-legend">'+Object.entries(m.legend).map(([k,v])=>`<span><b class="st-${k}">${v.symbol}</b> ${esc(v.label)}</span>`).join('')+'</div>';
  const head='<tr><th class="mcap">Capability</th>'+comps.map(c=>`<th class="${c.home?'mhome':''}">${esc(c.name)}</th>`).join('')+'</tr>';
  let body='';
  m.groups.forEach(g=>{
    const caps=g.capabilities.filter(cap=> internal || !dbxLosesRow(cap,homeId));
    if(!caps.length) return;
    body+=`<tr class="grp"><td colspan="${n}">${esc(g.label)}</td></tr>`;
    caps.forEach(cap=>{
      const lose=dbxLosesRow(cap,homeId);
      const tag=(internal&&lose)?'<span class="fieldwin-tag">field leads</span>':'';
      body+=`<tr class="${internal&&lose?'lose':''}"><td class="mcap">${esc(cap.label)}${tag}</td>`+comps.map(c=>{
        const cell=cap.cells[c.id]||{status:'unverified'};
        const sym=(m.legend[cell.status]||{symbol:'?'}).symbol;
        const note=cell.note?`<span class="cnote">${esc(cell.note)}</span>`:'';
        return `<td class="${c.home?'mhome ':''}${cell.emphasis?'emph':''}"><span class="st-${cell.status}">${sym}</span>${note}</td>`;
      }).join('')+'</tr>';
    });
  });
  const foot=m.sources?`<div class="mx-foot">sources ${esc(m.sources)}</div>`:'';
  let verd='';
  const vs=(m.verdicts||[]).filter(v=> internal || v.winner!=='field');
  if(vs.length){
    verd='<div class="mx-verdicts">'+vs.map(v=>
      `<div class="vrow"><span class="vwin ${v.winner}">${WINLBL[v.winner]||esc(v.winner)}</span><span><span class="vdim">${esc(v.dimension)}</span><br><span class="vtxt">DATABRICKS: ${esc(v.home||'')} · field: ${esc(v.field||'')}</span></span></div>`
    ).join('')+'</div>';
  }
  return lg+'<div class="mx-wrap"><table class="mx"><thead>'+head+'</thead><tbody>'+body+'</tbody></table></div>'+foot+verd;
}
function renderLandscape(n){ document.getElementById('pane-landscape').innerHTML = n&&n.matrix ? matrixHTML(n.matrix) : ''; if(typeof sizePanel==='function') sizePanel(); }

function showPanel(n){
  if(n._depth===0){ return; }
  selNode=n;
  document.getElementById('btnFocus').disabled=false;
  document.getElementById('pname').textContent=dn(n.n);
  panelEl.style.borderTopColor=(n.s&&SC[n.s])?SC[n.s]:'var(--red)';
  let r='';
  if(n.s) r+=`<span class="chip s-${n.s}">${n.s}</span>`;
  if(n.c==='verify') r+=`<span class="conf verify">⚠ to verify</span>`;
  if(n.new) r+=`<span style="color:var(--red);font-weight:700;font-size:0.8rem">✦ DAIS</span>`;
  document.getElementById('prow').innerHTML=r;

  // overview pane: intro sentence + doc links (always above the fold) + (optional) problem/solution block + meta
  let ov=`<div class="pintro">${esc(n.note||n.sub||'')}</div>`+docsHTML(n);
  if(n.solves&&n.solves.length) ov+=solveBlockHTML(n);
  const meta=metaFor(n);
  if(meta) ov+=`<div class="ppillar">${meta}</div>`;
  document.getElementById('pane-overview').innerHTML=ov;

  // wire the problem/solution toggle if present
  const tg=document.getElementById('solveTg');
  if(tg){ const blk=document.getElementById('solveBlock'), hint=document.getElementById('solveHint');
    tg.onchange=()=>{ blk.classList.toggle('on',tg.checked); blk.classList.toggle('off',!tg.checked); hint.textContent=tg.checked?('with '+dn(n.n)):'without the tool'; }; }

  // landscape pane: only when a compete matrix exists
  const hasMx=!!(n.matrix&&n.matrix.groups&&n.matrix.groups.length);
  document.getElementById('ptabLandscape').hidden=!hasMx;
  renderLandscape(hasMx?n:null);
  setPane('overview');

  panelEl.classList.add('open'); panelTab.classList.remove('show'); document.body.classList.add('panel-open');
}
function setPane(name){
  document.querySelectorAll('.ptab').forEach(t=>t.classList.toggle('active',t.dataset.pane===name));
  document.querySelectorAll('.ppane').forEach(p=>p.classList.toggle('active',p.id==='pane-'+name));
  sizePanel();
}
// panel height follows its content, capped at 70% of the window; the tree area above follows the panel
function sizePanel(){
  const h=Math.min(panelEl.scrollHeight, Math.round(window.innerHeight*0.7));
  document.documentElement.style.setProperty('--panel-h', h+'px');
}
document.querySelectorAll('.ptab').forEach(t=>t.onclick=()=>{ if(!t.hidden) setPane(t.dataset.pane); });
document.getElementById('modeTg').onchange=e=>{ APPMODE=e.target.checked?'internal':'customer'; renderLandscape(selNode); };
function collapsePanel(){ panelEl.classList.remove('open'); document.body.classList.remove('panel-open'); if(selNode) panelTab.classList.add('show'); }
function reopenPanel(){ if(selNode){ panelEl.classList.add('open'); panelTab.classList.remove('show'); document.body.classList.add('panel-open'); } }
document.getElementById('pclose').onclick=collapsePanel;
panelTab.onclick=reopenPanel;
// after the panel opens or closes, refit; when arriving from the Story, focus the target instead
let pendingFocus=false;
stage.addEventListener('transitionend',e=>{ if(e.propertyName==='bottom'){ render(); if(pendingFocus){ pendingFocus=false; focusSelected(); } else fitView(); } });

// pan
let drag=null;
stage.addEventListener('mousedown',e=>{ if(e.target.closest('foreignObject'))return; drag={x:e.clientX,y:e.clientY,tx:state.tx,ty:state.ty}; stage.classList.add('grabbing'); });
window.addEventListener('mousemove',e=>{ if(!drag)return; state.tx=drag.tx+(e.clientX-drag.x); state.ty=drag.ty+(e.clientY-drag.y); applyTransform(); });
window.addEventListener('mouseup',()=>{ drag=null; stage.classList.remove('grabbing'); });

// zoom
stage.addEventListener('wheel',e=>{
  e.preventDefault();
  const r=svg.getBoundingClientRect();
  const vb=svg.viewBox.baseVal, sx=vb.width/r.width, sy=vb.height/r.height;
  const mx=(e.clientX-r.left)*sx, my=(e.clientY-r.top)*sy;
  const f=e.deltaY<0?1.12:1/1.12, nk=Math.min(2.4,Math.max(0.25,state.k*f));
  state.tx=mx-(mx-state.tx)*(nk/state.k);
  state.ty=my-(my-state.ty)*(nk/state.k);
  state.k=nk; applyTransform();
},{passive:false});

// toolbar
document.getElementById('search').addEventListener('input',e=>{
  if(document.body.classList.contains('story-mode')){ storyFind(e.target.value); return; }
  state.q=e.target.value;
  if(state.q.trim()){
    const q=state.q.trim().toLowerCase();
    (function w(n){ (n.children||[]).forEach(w);
      if((n.n+' '+(n.note||'')).toLowerCase().includes(q)){ let p=n._p; while(p){p.collapsed=false;p=p._p;} }
    })(DATA);
  }
  render();
});
document.getElementById('btnNew').onclick=e=>{ state.newOnly=!state.newOnly; e.currentTarget.classList.toggle('on',state.newOnly); if(state.newOnly){ expandLevel=maxDepth; applyLevel(); } render(); };
document.getElementById('btnVerify').onclick=e=>{ state.hideVerify=!state.hideVerify; e.currentTarget.classList.toggle('on',state.hideVerify); render(); };
function expandAll(){ (function w(n){ if(n.children){n.collapsed=false; n.children.forEach(w);} })(DATA); }
function collapseAll(){ DATA.children.forEach(p=>p.collapsed=true); }
const btnToggle=document.getElementById('btnToggle');
const ICON_LAYERS='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12.83 2.18a2 2 0 0 0-1.66 0L2.6 6.08a1 1 0 0 0 0 1.83l8.58 3.91a2 2 0 0 0 1.66 0l8.58-3.9a1 1 0 0 0 0-1.84Z"/><path d="M2 12a1 1 0 0 0 .58.91l8.6 3.91a2 2 0 0 0 1.65 0l8.58-3.9A1 1 0 0 0 22 12"/><path d="M2 17a1 1 0 0 0 .58.91l8.6 3.91a2 2 0 0 0 1.65 0l8.58-3.9A1 1 0 0 0 22 17"/></svg>';
let maxDepth=3, expandLevel=2;
function computeMaxDepth(){ let m=1; for(const id in byId){ const d=byId[id]._depth; if(d>m) m=d; } return m; }
function applyLevel(){
  for(const id in byId){ const n=byId[id]; if(n.children&&n.children.length) n.collapsed=(n._depth>=expandLevel); }
  btnToggle.innerHTML=ICON_LAYERS+`<span class="lvl">${expandLevel}</span>`;
  btnToggle.setAttribute('data-tip', expandLevel>=maxDepth?`Depth ${expandLevel}/${maxDepth} · click to collapse`:`Depth ${expandLevel}/${maxDepth} · click to expand deeper`);
  btnToggle.classList.toggle('on', expandLevel>=maxDepth);
}
btnToggle.onclick=()=>{ expandLevel=(expandLevel>=maxDepth)?1:expandLevel+1; applyLevel(); render(); fitView(); };
document.getElementById('btnReset').onclick=()=>{ fitView(); };
// zoom buttons: fixed steps around the stage centre (the trackpad is too coarse)
function zoomBy(f){
  const mx=stage.clientWidth/2, my=stage.clientHeight/2;
  const nk=Math.min(2.4,Math.max(0.25,state.k*f));
  state.tx=mx-(mx-state.tx)*(nk/state.k);
  state.ty=my-(my-state.ty)*(nk/state.k);
  state.k=nk; applyTransform();
}
document.getElementById('btnZoomIn').onclick=()=>zoomBy(1.2);
document.getElementById('btnZoomOut').onclick=()=>zoomBy(1/1.2);
// focus: center and zoom on the selected block and its visible sub-blocks
const btnFocus=document.getElementById('btnFocus');
function focusSelected(){
  if(!selNode) return;
  let p=selNode._p, opened=false;
  while(p){ if(p.collapsed){ p.collapsed=false; opened=true; } p=p._p; }
  if(opened) render();
  let x0=selNode._x, y0=selNode._y, x1=x0+selNode._w, y1=y0+selNode._h;
  (function rec(n){ if(n.collapsed||!n.children) return;
    n.children.forEach(c=>{ x0=Math.min(x0,c._x); y0=Math.min(y0,c._y); x1=Math.max(x1,c._x+c._w); y1=Math.max(y1,c._y+c._h); rec(c); }); })(selNode);
  const vw=stage.clientWidth, vh=stage.clientHeight, pad=60, bw=x1-x0, bh=y1-y0;
  const k=Math.min(1.8,Math.max(0.25,Math.min((vw-2*pad)/bw,(vh-2*pad)/bh)));
  state.k=k; state.tx=vw/2-(x0+bw/2)*k; state.ty=vh/2-(y0+bh/2)*k; applyTransform();
}
btnFocus.onclick=focusSelected;
window.addEventListener('resize',()=>{ sizePanel(); render(); });

// ---- tabs: swap the active tree ----
function loadTree(key){
  DATA = TREES[key] || TREES.ai;
  initTree();
  selNode=null; state.q=''; state.newOnly=false; state.hideVerify=false;
  btnFocus.disabled=true;
  const s=document.getElementById('search'); if(s) s.value='';
  document.getElementById('btnNew').classList.remove('on');
  document.getElementById('btnVerify').classList.remove('on');
  panelEl.classList.remove('open'); document.body.classList.remove('panel-open'); panelTab.classList.remove('show');
  maxDepth=computeMaxDepth(); expandLevel=Math.min(2,maxDepth); applyLevel();
  render(); fitView();
}
function setActiveTab(key){
  document.querySelectorAll('.navtab').forEach(x=>x.classList.toggle('active',x.dataset.tree===key));
}
document.querySelectorAll('.navtab').forEach(b=>{ b.onclick=()=>{
  storyReturn=null; btnBack.hidden=true;   // a manual tab change cancels the way back
  setActiveTab(b.dataset.tree);
  document.body.classList.toggle('decks-mode', b.dataset.tree==='decks');
  if(b.dataset.tree==='story'){ showStory(); }
  else if(b.dataset.tree==='decks'){ hideStory(); }
  else { hideStory(); loadTree(b.dataset.tree); }
}; });

// ---- Story tab: chapters as slides, capsule cards pulled from the trees ----
const storyView=document.getElementById('storyView');
let storyBuilt=false;
function nodeByPath(tree,path){
  let n=TREES[tree]; if(!n||n.n!==path[0]) return null;
  for(let i=1;i<path.length;i++){ n=(n.children||[]).find(c=>c.n===path[i]); if(!n) return null; }
  return n;
}
function capCard(ref,key){
  const n=nodeByPath(ref.tree,ref.path); if(!n) return '';
  const chip=n.s?`<span class="chip s-${n.s}">${n.s}</span>`:'';
  return `<button class="scap" data-ref="${key}">`+
    `<div class="sct"><span class="stree">${ref.tree.toUpperCase()}</span><span>${esc(dn(n.n))}</span>${chip}</div>`+
    `<div class="scn">${esc(n.note||'')}</div><div class="scgo">See in tree →</div></button>`;
}
function buildStory(){
  const chs=STORY.chapters;
  const rail=`<div class="srail"><div class="srail-t">Chapters</div>`+
    chs.map(c=>`<a href="#sch-${c.num}" data-ch="${c.num}"><b>${c.num}</b><span>${esc(c.title)}</span></a>`).join('')+`</div>`;
  const body=chs.map((c,ci)=>
    `<section class="schap" id="sch-${c.num}" data-ch="${c.num}">`+
    `<div class="schap-h"><span class="schap-n">${c.num}</span><h2 class="schap-t">${esc(c.title)}</h2></div>`+
    c.points.map((p,pi)=>
      `<article class="sslide" data-ci="${ci}" data-pi="${pi}"><h3>${esc(p.title)}</h3>`+
      (p.lead?`<p class="slead">${esc(p.lead)}</p>`:'')+
      `<ul class="sbul">${p.bullets.map(b=>`<li>${esc(b)}</li>`).join('')}</ul>`+
      (p.refs.length?`<div class="scaps">${p.refs.map((r,ri)=>capCard(r,`${ci}-${pi}-${ri}`)).join('')}</div>`:'')+
      `</article>`).join('')+
    (c.handoff?`<p class="shand">${esc(c.handoff)}</p>`:'')+
    `</section>`).join('');
  storyView.innerHTML=`<div class="story">${rail}<div class="sbody">${body}</div></div>`;
  // rail: highlight the chapter being read
  const links=[...storyView.querySelectorAll('.srail a')];
  const obs=new IntersectionObserver(es=>{ es.forEach(e=>{ if(e.isIntersecting){
    links.forEach(a=>a.classList.toggle('on',a.dataset.ch===e.target.dataset.ch)); } }); },
    {root:storyView, rootMargin:'0px 0px -70% 0px'});
  storyView.querySelectorAll('.schap').forEach(s=>obs.observe(s));
  links.forEach(a=>a.onclick=e=>{ e.preventDefault(); storyView.querySelector(a.getAttribute('href')).scrollIntoView({behavior:'smooth'}); });
}
// previous / next arrows: one stop per slide; a chapter's first stop is its header
const storyPrev=document.getElementById('storyPrev'), storyNext=document.getElementById('storyNext');
function storyStops(){
  const top=storyView.getBoundingClientRect().top, st=storyView.scrollTop, stops=[];
  storyView.querySelectorAll('.schap').forEach(sec=>{
    const slides=[...sec.querySelectorAll('.sslide')];
    [sec, ...slides.slice(1)].forEach(el=>stops.push(el.getBoundingClientRect().top-top+st-16));
  });
  return stops;
}
function storyStep(dir){
  const st=storyView.scrollTop, stops=storyStops();
  const target = dir>0 ? stops.find(y=>y>st+20) : [...stops].reverse().find(y=>y<st-20);
  if(target!==undefined) storyView.scrollTo({top:Math.max(0,target),behavior:'smooth'});
}
function updateStoryNav(){
  const st=storyView.scrollTop;
  storyPrev.disabled = st<=2;
  storyNext.disabled = st+storyView.clientHeight>=storyView.scrollHeight-2;
}
storyPrev.onclick=()=>storyStep(-1);
storyNext.onclick=()=>storyStep(1);
// keyboard ↑ / ↓ do the same as the arrow buttons, in the Story only
document.addEventListener('keydown',e=>{
  if(!document.body.classList.contains('story-mode')) return;
  if(e.target.closest('input,textarea,select,[contenteditable]')) return;
  if(e.key==='ArrowDown'){ e.preventDefault(); storyStep(1); }
  else if(e.key==='ArrowUp'){ e.preventDefault(); storyStep(-1); }
});
storyView.addEventListener('scroll',updateStoryNav,{passive:true});
function showStory(){
  document.body.classList.add('story-mode');
  if(!storyBuilt){ buildStory(); storyBuilt=true; }
  searchEl.placeholder='Search the story…'; searchEl.value=storyQ;
  updateStoryNav();
}
function hideStory(){ document.body.classList.remove('story-mode'); searchEl.placeholder='Search features…'; storyResults.hidden=true; }
// ---- Story search: find as you type, list the sections and slides where the word appears ----
const searchEl=document.getElementById('search'), storyResults=document.getElementById('storyResults');
let storyQ='', storyRes=[], storyResIdx=0;
function hl(raw,q){
  if(!q) return esc(raw);
  const re=new RegExp('('+q.replace(/[.*+?^${}()|[\]\\]/g,'\\$&')+')','ig');
  return raw.split(re).map((part,i)=>i%2?`<mark>${esc(part)}</mark>`:esc(part)).join('');
}
function snippet(text,q){
  const i=text.toLowerCase().indexOf(q); if(i<0) return '';
  const a=Math.max(0,i-40), b=Math.min(text.length,i+q.length+60);
  return (a>0?'…':'')+hl(text.slice(a,b),q)+(b<text.length?'…':'');
}
function slideTexts(p){
  const t=[p.title,p.lead,...p.bullets];
  p.refs.forEach(r=>{ const n=nodeByPath(r.tree,r.path); if(n) t.push(dn(n.n), n.note||''); });
  return t.filter(Boolean);
}
function storyFind(value){
  storyQ=value; const q=value.trim().toLowerCase(); storyRes=[]; storyResIdx=0;
  if(q) STORY.chapters.forEach((c,ci)=>{
    const ct=[c.title,c.handoff||''].find(s=>s.toLowerCase().includes(q));
    if(ct) storyRes.push({ci,pi:-1,snip:snippet(ct,q)});
    c.points.forEach((p,pi)=>{ const hit=slideTexts(p).find(s=>s.toLowerCase().includes(q)); if(hit) storyRes.push({ci,pi,snip:snippet(hit,q)}); });
  });
  renderStoryResults(q);
}
function renderStoryResults(q){
  if(!q){ storyResults.hidden=true; storyResults.innerHTML=''; return; }
  storyResults.innerHTML = storyRes.length
    ? storyRes.map((r,i)=>{ const c=STORY.chapters[r.ci], title=r.pi<0?c.title:c.points[r.pi].title;
        return `<button class="sres${i===storyResIdx?' on':''}" data-i="${i}">`+
          `<div class="sres-crumb">${c.num} · ${esc(c.title)}${r.pi<0?' · chapter':''}</div>`+
          `<div class="sres-t">${hl(title,q)}</div><div class="sres-snip">${r.snip}</div></button>`; }).join('')
    : `<div class="sres-none">No match</div>`;
  storyResults.hidden=false;
}
function storyGoRes(i){
  const r=storyRes[i]; if(!r) return;
  storyResults.hidden=true;
  const el = r.pi<0 ? storyView.querySelector(`#sch-${STORY.chapters[r.ci].num}`)
                    : storyView.querySelector(`.sslide[data-ci="${r.ci}"][data-pi="${r.pi}"]`);
  if(!el) return;
  const top=el.getBoundingClientRect().top-storyView.getBoundingClientRect().top+storyView.scrollTop-16;
  storyView.scrollTo({top:Math.max(0,top),behavior:'smooth'});
  if(r.pi>=0){ el.classList.remove('sflash'); void el.offsetWidth; el.classList.add('sflash'); }
}
// mousedown (not click) so the choice lands before the input loses focus
storyResults.addEventListener('mousedown',e=>{ const b=e.target.closest('.sres'); if(!b) return; e.preventDefault(); storyGoRes(+b.dataset.i); });
searchEl.addEventListener('keydown',e=>{
  if(!document.body.classList.contains('story-mode')) return;
  if(e.key==='ArrowDown'||e.key==='ArrowUp'){
    if(!storyRes.length) return; e.preventDefault();
    storyResIdx=(storyResIdx+(e.key==='ArrowDown'?1:-1)+storyRes.length)%storyRes.length;
    renderStoryResults(storyQ.trim().toLowerCase());
    const on=storyResults.querySelector('.sres.on'); if(on) on.scrollIntoView({block:'nearest'});
  }
  else if(e.key==='Enter'){ e.preventDefault(); storyGoRes(storyResIdx); }
  else if(e.key==='Escape'){ storyResults.hidden=true; }
});
searchEl.addEventListener('focus',()=>{ if(document.body.classList.contains('story-mode') && storyQ.trim()) renderStoryResults(storyQ.trim().toLowerCase()); });
searchEl.addEventListener('blur',()=>{ storyResults.hidden=true; });
// "See in tree": switch to the capsule's tree, select it, center on it
function gotoNode(tree,path){
  setActiveTab(tree); hideStory(); loadTree(tree);
  const n=nodeByPath(tree,path); if(!n) return;
  let p=n._p; while(p){ p.collapsed=false; p=p._p; }
  render(); showPanel(n); render();
  focusSelected();
  // focus again once the panel has opened (transitionend), or after its duration if no transition ran
  pendingFocus=true; setTimeout(()=>{ if(pendingFocus){ pendingFocus=false; focusSelected(); } },320);
}
storyView.addEventListener('click',e=>{
  const b=e.target.closest('.scap'); if(!b) return;
  const [ci,pi,ri]=b.dataset.ref.split('-').map(Number);
  const ref=STORY.chapters[ci].points[pi].refs[ri];
  storyReturn={scroll:storyView.scrollTop, key:b.dataset.ref};
  document.getElementById('btsCh').textContent=STORY.chapters[ci].title;
  btnBack.hidden=false;
  history.pushState({fromStory:true},'');
  gotoNode(ref.tree, ref.path);
});
// way back to the Story: the pill, Esc, or the browser / trackpad back gesture
const btnBack=document.getElementById('backToStory');
let storyReturn=null;                       // {scroll, key} of the slide we left
function backToStory(){
  if(!storyReturn) return;
  const {scroll,key}=storyReturn; storyReturn=null; btnBack.hidden=true;
  setActiveTab('story'); showStory();
  storyView.scrollTop=scroll;
  const card=storyView.querySelector(`.scap[data-ref="${key}"]`);
  if(card){ card.classList.remove('flash'); void card.offsetWidth; card.classList.add('flash'); }
}
btnBack.onclick=backToStory;
document.addEventListener('keydown',e=>{ if(e.key==='Escape' && storyReturn && !document.body.classList.contains('story-mode')) backToStory(); });
window.addEventListener('popstate',()=>{ if(storyReturn) backToStory(); });
loadTree('ai');
