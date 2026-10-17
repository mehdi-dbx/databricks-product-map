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
const SLABEL={PrivPreview:'PPR'};   // label shown on a status chip, when it differs from the status value
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
  node._h=Math.max(node._depth===2?FEATH:SUBH, node._nh||0);
  node._y=cur.y; cur.y+=node._h+VGAP;
  if(!node.collapsed && node.children) node.children.forEach(ch=>place(ch,colX,cur));
}
function layout(){
  const pillars=DATA.children; let maxB=0;
  const pillH=Math.max(PILLH, ...pillars.map(p=>p._nh||0));   // one height for the row, so the pillars stay aligned
  pillars.forEach((p,i)=>{
    const colX=MARGIN+i*COLW;
    p._depth=1; p._x=colX; p._y=PILLY; p._w=COLW-GAP; p._h=pillH;
    const cur={y:PILLY+pillH+VGAP};
    if(!p.collapsed && p.children) p.children.forEach(ch=>place(ch,colX,cur));
    p._bottom=cur.y; if(p._bottom>maxB) maxB=p._bottom;
  });
  DATA._depth=0; DATA._w=ROOTW; DATA._h=ROOTH;
  const firstX=pillars[0]._x, lastX=pillars[pillars.length-1]._x+(COLW-GAP);
  DATA._x=(firstX+lastX)/2-ROOTW/2; DATA._y=MARGIN;
  return {w:MARGIN+pillars.length*COLW, h:Math.max(maxB,PILLY+180)+MARGIN};
}
function visibleNodes(){ const out=[]; (function rec(n){ out.push(n); if(!n.collapsed && n.children) n.children.forEach(rec); })(DATA); return out; }

// a name too long for one line wraps; the node takes the height its text needs
function nodeInner(n){
  const hasKids=!!(n.children&&n.children.length);
  const dot=hasKids?'<span class="ddot"></span>':'';
  const warn=n.c==='verify'?'<span class="flag warn">⚠</span>':'';
  const tog=hasKids?`<span class="ptoggle">${n.collapsed?'▸':'▾'}</span>`:'';
  const chip=n.s?`<span class="chip s-${n.s}">${SLABEL[n.s]||n.s}</span>`:'';
  if(n._depth===0) return `<div class="nm">${esc(dn(n.n))}</div>`;
  if(n._depth===1) return `<div class="nm">${tog}${esc(dn(n.n))}</div>`+
    `<div class="meta">${n.sub?`<span class="sub">${esc(n.sub)}</span>`:''}<span class="count">${(n.children||[]).length} items</span>${dot}</div>`;
  if(n._depth===2) return `<div class="nm">${tog}${esc(dn(n.n))}</div><div class="meta">${chip}${warn}${dot}</div>`;
  return `<div class="nm">${esc(dn(n.n))}</div><div class="meta">${chip}${warn}${dot}</div>`;
}
function measureHeights(){
  const all=Object.values(byId), box=document.createElement('div');
  box.style.cssText='position:absolute;left:-99999px;top:0;visibility:hidden';
  box.innerHTML=all.map(n=>{
    const w=n._depth===0?ROOTW:(COLW-GAP)-Math.max(0,n._depth-1)*INDENT;
    return `<div class="node d${n._depth}" style="width:${w}px"><div class="nodebox d${n._depth}${n.c==='verify'?' verify':''}" style="height:auto">${nodeInner(n)}</div></div>`;
  }).join('');
  document.body.appendChild(box);
  all.forEach((n,i)=>{ n._nh=box.children[i].firstChild.offsetHeight; });
  box.remove();
}

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
    const cls=`node d${n._depth}${n._hit?' hit':''}${n._dim?' dim':''}${n===selNode?' sel':''}`;
    fo+=`<foreignObject class="${cls}" x="${n._x}" y="${n._y}" width="${n._w}" height="${n._h}" data-id="${n.id}">`+
        `<div xmlns="http://www.w3.org/1999/xhtml" class="nodebox d${n._depth}${n.c==='verify'?' verify':''}">${nodeInner(n)}</div>`+
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
function docsLinks(docs){
  return docs.length?`<div class="pdocs">`+docs.map(u=>`<a href="${u}" target="_blank" rel="noopener">↗ ${esc(shortDoc(u))}</a>`).join('')+`</div>`:'';
}
function docsHTML(n){ return docsLinks(docsFor(n)); }
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
  if(n.s) r+=`<span class="chip s-${n.s}">${SLABEL[n.s]||n.s}</span>`;
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
  const m=findMode(); if(m){ runFind(m,e.target.value); return; }
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
  initTree(); measureHeights();
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
  else if(b.dataset.tree==='decks'){ showDecks(); }
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
// the panel's docs for a Story capsule: its own, else the nearest ancestor's, found along the
// path because the capsule's tree may not be loaded (no _p links)
function pathDocs(ref){
  let n=TREES[ref.tree]; const chain=[n];
  for(let i=1;i<ref.path.length;i++){ n=(n.children||[]).find(c=>c.n===ref.path[i]); chain.push(n); }
  const d=chain.reverse().find(x=>x&&x.docs&&x.docs.length); return d?d.docs:[];
}
function capCard(ref,key){
  const n=nodeByPath(ref.tree,ref.path); if(!n) return '';
  const chip=n.s?`<span class="chip s-${n.s}">${SLABEL[n.s]||n.s}</span>`:'';
  return `<div class="scap" role="button" tabindex="0" data-ref="${key}">`+
    `<div class="sct"><span class="stree">${ref.tree.toUpperCase()}</span><span>${esc(dn(n.n))}</span>${chip}</div>`+
    `<div class="scn">${esc(n.note||'')}</div>`+
    `<div class="scfoot"><span class="scgo">See in tree →</span>${docsLinks(pathDocs(ref))}</div></div>`;
}
// ---- illustration candidates (temporary, while the illustrations are chosen) ----
// a click on an image shows it full screen; its checkbox picks or unpicks it. The picks file
// (chosen once per page load, Chrome / Edge only) is the reference: each change reads it,
// changes that one pick and writes it back. The browser keeps a copy only for display.
const PICKS=JSON.parse(localStorage.getItem('illusPicks')||'{}');
let picksFile=null, pickQueue=Promise.resolve();
const isPicked=(pid,id)=>(PICKS[pid]||[]).includes(id);
function illusRow(pid){
  const cands=ILLUS[pid]; if(!cands||!cands.length) return '';
  return `<div class="sill">`+cands.map(c=>
    `<div class="sillc${isPicked(pid,c.id)?' on':''}" data-pid="${pid}" data-id="${c.id}">`+
    `<img src="${IMG_BASE}${c.file}" alt="" loading="lazy">`+
    `<label><input type="checkbox"${isPicked(pid,c.id)?' checked':''}><span>${esc(c.source)}</span></label></div>`).join('')+`</div>`;
}
async function togglePick(pid,id){
  if(!picksFile) picksFile=await showSaveFilePicker({suggestedName:'illustration-picks.json',
    types:[{description:'JSON',accept:{'application/json':['.json']}}]});
  const text=(await (await picksFile.getFile()).text()).trim();
  let cur;
  try{ cur=text?JSON.parse(text):{}; }catch(e){ throw new Error('the picks file is not valid JSON, it was left as is'); }
  const set=new Set(cur[pid]||[]);
  if(set.has(id)) set.delete(id); else set.add(id);
  if(set.size) cur[pid]=[...set]; else delete cur[pid];
  const w=await picksFile.createWritable(); await w.write(JSON.stringify(cur,null,1)+'\n'); await w.close();
  Object.keys(PICKS).forEach(k=>delete PICKS[k]); Object.assign(PICKS,cur);
  localStorage.setItem('illusPicks',JSON.stringify(PICKS));
}
// full-screen view, with the same checkbox
const illusView=document.createElement('div');
illusView.id='illusView'; illusView.hidden=true;
illusView.innerHTML=`<img alt=""><div class="ivbar"><label><input type="checkbox"><span></span></label><a target="_blank" rel="noopener">Open the source ↗</a></div>`;
document.body.appendChild(illusView);
const ivBox=illusView.querySelector('input');
let ivCur=null;
function openIllus(pid,id){
  const c=ILLUS[pid].find(x=>x.id===id); ivCur={pid,id};
  illusView.querySelector('img').src=IMG_BASE+c.file;
  illusView.querySelector('span').textContent=c.source;
  illusView.querySelector('a').href=c.url;
  ivBox.checked=isPicked(pid,id); illusView.hidden=false;
}
function syncPicks(){
  storyView.querySelectorAll('.sillc').forEach(el=>{ const on=isPicked(el.dataset.pid,el.dataset.id);
    el.classList.toggle('on',on); el.querySelector('input').checked=on; });
  if(ivCur) ivBox.checked=isPicked(ivCur.pid,ivCur.id);
}
// changes run one after the other, so two quick clicks cannot overwrite each other
function changePick(pid,id){
  pickQueue=pickQueue.then(()=>togglePick(pid,id))
    .catch(err=>{ if(err.name!=='AbortError') alert('Pick not saved: '+err.message); })
    .finally(syncPicks);
}
storyView.addEventListener('click',e=>{ const img=e.target.closest('.sillc img'); if(img){ const c=img.closest('.sillc'); openIllus(c.dataset.pid,c.dataset.id); } });
storyView.addEventListener('change',e=>{ const c=e.target.closest('.sillc'); if(c) changePick(c.dataset.pid,c.dataset.id); });
ivBox.addEventListener('change',()=>changePick(ivCur.pid,ivCur.id));
illusView.addEventListener('click',e=>{ if(!e.target.closest('.ivbar')) illusView.hidden=true; });
document.addEventListener('keydown',e=>{ if(e.key==='Escape'&&!illusView.hidden) illusView.hidden=true; });
// "Image picks" switch in the nav (Story only): shows or hides the candidates, remembered by the browser
const illusTg=document.getElementById('illusTg');
illusTg.checked=localStorage.getItem('illusShow')!=='0';
document.body.classList.toggle('illus-off',!illusTg.checked);
illusTg.onchange=()=>{ localStorage.setItem('illusShow',illusTg.checked?'1':'0'); document.body.classList.toggle('illus-off',!illusTg.checked); };
// the Story serves as slides: a text of two or more sentences shows one bullet per sentence
const sentencesOf=t=>t?t.split(/(?<=[.!?])\s+(?=[A-Z"“(])/):[];
function bullets(items,cls){ return items&&items.length?`<ul class="${cls} slist">${items.map(x=>`<li>${mdBold(x)}</li>`).join('')}</ul>`:''; }
function prose(text,cls){ const s=sentencesOf(text); return !text?'':s.length>1?bullets(s,cls):`<p class="${cls}">${esc(text)}</p>`; }
// the first slide: the platform architecture, one block per chapter, its slides as tiles (story.json, overview)
function overviewHtml(th){
  const ov=STORY.overview; if(!ov||!ov.length) return '';
  const where={}; STORY.chapters.forEach((c,ci)=>c.points.forEach((p,pi)=>{ where[p.id]=`ss-${ci}-${pi}`; }));
  return `<section class="schap sover" id="sch-over" data-ch="over"><div class="sover-k">Overview</div>`+
    (th?`<h1 class="sover-t">${esc(th.title)}</h1>`:'')+(th&&th.overview?`<p class="sover-s">${esc(th.overview)}</p>`:'')+
    `<div class="sov-path" style="--steps:${ov.length}">${ov.map((b,bi)=>`<div class="sov-step"><div class="sov-card">`+
      `<div class="sov-h"><span class="sov-n">${bi+1}</span><span class="sov-name">${esc(b.name)}</span></div>`+
      `<div class="sov-tiles">${b.tiles.map(tl=>`<button type="button" class="sov-tile" data-go="${where[tl.id]}">${esc(tl.label)}</button>`).join('')}</div></div>`+
      (b.points.length?`<ul class="sov-pts">${b.points.map(x=>`<li>${esc(x)}</li>`).join('')}</ul>`:'')+
      `</div>`).join('')}</div></section>`;
}
// the appendix: the capability map, every slide with its features from the plan (docs/feature-tree.md)
const featureText=fs=>fs.map(f=>f.name+(f.children.length?` (${featureText(f.children)})`:'')).join(' · ');
function appendixHtml(){
  const ap=STORY.appendix; if(!ap) return '';
  const title=ap.title.charAt(0).toUpperCase()+ap.title.slice(1);
  return `<section class="schap sapp" id="sch-app" data-ch="app"><div class="schap-h"><h2 class="schap-t">Appendix: ${esc(title)}</h2></div>`+
    `<div class="sapp-map">${STORY.chapters.map((c,ci)=>`<div class="sapp-sec"><div class="sapp-h"><span>${c.num}</span>${esc(c.title)}</div>`+
      c.points.map((p,pi)=>`<div class="sapp-pt"><a href="#ss-${ci}-${pi}" class="sapp-t"><span>${esc(p.id)}</span>${esc(p.title)}</a>`+
        (p.features.length?`<ul>${p.features.map(f=>`<li>${esc(f.name)}${f.children.length?`<span>${esc(featureText(f.children))}</span>`:''}</li>`).join('')}</ul>`:'')+
        `</div>`).join('')+`</div>`).join('')}</div></section>`;
}
function buildStory(){
  const chs=STORY.chapters, th=STORY.thread;   // thread: the complete story (docs/story-cement.md)
  const over=overviewHtml(th);
  const rail=`<div class="srail"><div class="srail-t">Chapters</div>`+
    (over?`<a href="#sch-over" data-ch="over"><b>·</b><span>Overview</span></a>`:'')+
    chs.map((c,ci)=>`<a href="#sch-${c.num}" data-ch="${c.num}"><b>${c.num}</b><span>${esc(c.title)}</span></a>`+
      // sub-entries: one per slide, shown only for the chapter being read
      `<div class="srail-sub" data-ch="${c.num}">${c.points.map((p,pi)=>`<a href="#ss-${ci}-${pi}">${esc(p.title)}</a>`).join('')}</div>`).join('')+
    (th&&th.closing&&th.closing.length?`<a href="#sch-end" data-ch="end"><b>·</b><span>Closing</span></a>`:'')+
    (STORY.appendix?`<a href="#sch-app" data-ch="app"><b>·</b><span>Appendix</span></a>`:'')+`</div>`;
  // the story's title goes on the overview when there is one
  const top=th?`<div class="sthread">${over?'':`<h1 class="sthread-t">${esc(th.title)}</h1>`}${bullets(th.opening,'sopen')}</div>`:'';
  const close=th&&th.closing&&th.closing.length?`<section class="schap" id="sch-end" data-ch="end"><div class="schap-h"><h2 class="schap-t">Closing</h2></div>`+
    `${bullets(th.closing,'sintro')}</section>`:'';
  const body=chs.map((c,ci)=>
    `<section class="schap" id="sch-${c.num}" data-ch="${c.num}">`+
    `<div class="schap-h"><span class="schap-n">${c.num}</span><h2 class="schap-t">${esc(c.title)}</h2></div>`+
    bullets(c.intro,'sintro')+
    c.points.map((p,pi)=>
      `<article class="sslide" id="ss-${ci}-${pi}" data-ci="${ci}" data-pi="${pi}"><h3>${esc(p.title)}</h3>`+
      (p.effect?`<p class="seff">${esc(p.effect)}</p>`:'')+
      prose(p.lead,'slead')+
      // challenge, then the pivot that leads to the bullets (docs/story-editorial-guide.md)
      (p.challenge?`<div class="schbox"><div class="schbox-l">Challenges</div>${prose(p.challenge,'sadd schal')}</div>`:prose(p.challenge,'sadd schal'))+(p.pivot?`<p class="sadd">${mdBold(p.pivot)}</p>`:'')+
      `<ul class="sbul">${p.bullets.map(b=>`<li>${mdBold(b)}</li>`).join('')}</ul>`+
      (p.refs.length?`<div class="scaps">${p.refs.map((r,ri)=>capCard(r,`${ci}-${pi}-${ri}`)).join('')}</div>`:'')+
      illusRow(p.id)+
      `</article>`).join('')+
    prose(c.handoff,'shand')+
    `</section>`).join('');
  storyView.innerHTML=`<div class="story">${over}${rail}<div class="sbody">${top}${body}${close}${appendixHtml()}</div></div>`;
  // rail: highlight the chapter being read
  const links=[...storyView.querySelectorAll('.srail a')], subs=[...storyView.querySelectorAll('.srail-sub')];
  const obs=new IntersectionObserver(es=>{ es.forEach(e=>{ if(e.isIntersecting){
    links.forEach(a=>a.classList.toggle('on',a.dataset.ch===e.target.dataset.ch));
    subs.forEach(d=>d.classList.toggle('open',d.dataset.ch===e.target.dataset.ch)); } }); },
    {root:storyView, rootMargin:'0px 0px -70% 0px'});
  storyView.querySelectorAll('.schap').forEach(s=>obs.observe(s));
  links.forEach(a=>a.onclick=e=>{ e.preventDefault(); storyView.querySelector(a.getAttribute('href')).scrollIntoView({behavior:'smooth'}); });
}
// previous / next arrows: one stop per slide; a chapter's first stop is its header
const storyPrev=document.getElementById('storyPrev'), storyNext=document.getElementById('storyNext');
function storyStops(){
  const top=storyView.getBoundingClientRect().top, st=storyView.scrollTop, stops=[];
  storyView.querySelectorAll('.schap,.sthread').forEach(sec=>{
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
  if(!document.body.classList.contains('story-mode')||!illusView.hidden) return;
  if(e.target.closest('input,textarea,select,[contenteditable]')) return;
  if(e.key==='ArrowDown'){ e.preventDefault(); storyStep(1); }
  else if(e.key==='ArrowUp'){ e.preventDefault(); storyStep(-1); }
});
storyView.addEventListener('scroll',updateStoryNav,{passive:true});
// a tile of the overview opens its slide
storyView.addEventListener('click',e=>{ const tl=e.target.closest('.sov-tile'); if(tl) reveal(storyView,document.getElementById(tl.dataset.go),true); });
function showStory(){
  document.body.classList.add('story-mode');
  if(!storyBuilt){ buildStory(); storyBuilt=true; }
  searchEl.placeholder='Search the story…'; searchEl.value=findQ.story;
  updateStoryNav();
}
function hideStory(){ document.body.classList.remove('story-mode'); searchEl.placeholder='Search features…'; findResults.hidden=true; }
function showDecks(){ hideStory(); searchEl.placeholder='Search the decks…'; searchEl.value=findQ.decks; }
// ---- Story and Decks search: find as you type, list the places where the word appears ----
const searchEl=document.getElementById('search'), findResults=document.getElementById('findResults');
const decksView=document.getElementById('decksView');
const findQ={story:'',decks:''};   // each tab keeps its own query
let findRes=[], findResIdx=0;
function findMode(){ const c=document.body.classList; return c.contains('story-mode')?'story':c.contains('decks-mode')?'decks':null; }
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
  const t=[p.title,p.effect,p.lead,p.challenge,(p.pivot||'').replace(/\*\*/g,''),...p.bullets.map(b=>b.replace(/\*\*/g,'')),featureText(p.features||[])];
  p.refs.forEach(r=>{ const n=nodeByPath(r.tree,r.path); if(n) t.push(dn(n.n), n.note||''); });
  return t.filter(Boolean);
}
// scroll a view to el (near the top, or centered), then flash el
function reveal(view,el,flash,center){
  if(!el) return;
  const off=center?(view.clientHeight-el.offsetHeight)/2:16;
  const top=el.getBoundingClientRect().top-view.getBoundingClientRect().top+view.scrollTop-off;
  view.scrollTo({top:Math.max(0,top),behavior:'smooth'});
  if(flash){ el.classList.remove('sflash'); void el.offsetWidth; el.classList.add('sflash'); }
}
function storyFind(q){
  const th=STORY.thread;   // the opening and the closing of the complete story
  if(th) [['Opening',(th.opening||[]).join(' ').replace(/\*\*/g,''),'.sthread'],['Closing',(th.closing||[]).join(' ').replace(/\*\*/g,''),'#sch-end']].forEach(([name,text,sel])=>{
    if(text&&text.toLowerCase().includes(q)) findRes.push({crumb:`The story · ${name}`, title:th.title, snip:snippet(text,q),
      go:()=>reveal(storyView,storyView.querySelector(sel),false)}); });
  STORY.chapters.forEach((c,ci)=>{
    const ct=[c.title,(c.intro||[]).join(' ').replace(/\*\*/g,''),c.handoff||''].find(s=>s.toLowerCase().includes(q));
    if(ct) findRes.push({crumb:`${c.num} · ${c.title} · chapter`, title:c.title, snip:snippet(ct,q),
      go:()=>reveal(storyView,storyView.querySelector(`#sch-${c.num}`),false)});
    c.points.forEach((p,pi)=>{ const hit=slideTexts(p).find(s=>s.toLowerCase().includes(q));
      if(hit) findRes.push({crumb:`${c.num} · ${c.title}`, title:p.title, snip:snippet(hit,q),
        go:()=>reveal(storyView,storyView.querySelector(`.sslide[data-ci="${ci}"][data-pi="${pi}"]`),true)}); });
  });
}
// a deck hit is a section heading or a table row; a row is named by its deck link
function decksFind(q){
  let h2='', h3='';
  decksView.querySelectorAll('h2, h3, tbody tr').forEach(el=>{
    const text=el.textContent;
    if(el.tagName==='H2'){ h2=text; h3=''; }
    if(el.tagName==='H3') h3=text;
    if(el.tagName!=='TR'){
      if(text.toLowerCase().includes(q)) findRes.push({crumb:el.tagName==='H3'?`${h2} · section`:'section', title:text, snip:'', go:()=>reveal(decksView,el,false)});
      return;
    }
    const hit=[...el.cells].map(td=>td.textContent).find(s=>s.toLowerCase().includes(q));
    if(hit) findRes.push({crumb:h3?`${h2} · ${h3}`:h2, title:(el.querySelector('a')||el.cells[0]).textContent,
      snip:snippet(hit,q), go:()=>reveal(decksView,el,true,true)});
  });
}
function runFind(mode,value){
  findQ[mode]=value; const q=value.trim().toLowerCase(); findRes=[]; findResIdx=0;
  if(q) (mode==='story'?storyFind:decksFind)(q);
  renderFindResults(q);
}
function renderFindResults(q){
  if(!q){ findResults.hidden=true; findResults.innerHTML=''; return; }
  findResults.innerHTML = findRes.length
    ? findRes.map((r,i)=>`<button class="sres${i===findResIdx?' on':''}" data-i="${i}">`+
        `<div class="sres-crumb">${esc(r.crumb)}</div>`+
        `<div class="sres-t">${hl(r.title,q)}</div><div class="sres-snip">${r.snip}</div></button>`).join('')
    : `<div class="sres-none">No match</div>`;
  findResults.hidden=false;
}
function findGo(i){ const r=findRes[i]; if(!r) return; findResults.hidden=true; r.go(); }
// mousedown (not click) so the choice lands before the input loses focus
findResults.addEventListener('mousedown',e=>{ const b=e.target.closest('.sres'); if(!b) return; e.preventDefault(); findGo(+b.dataset.i); });
searchEl.addEventListener('keydown',e=>{
  const m=findMode(); if(!m) return;
  if(e.key==='ArrowDown'||e.key==='ArrowUp'){
    if(!findRes.length) return; e.preventDefault();
    findResIdx=(findResIdx+(e.key==='ArrowDown'?1:-1)+findRes.length)%findRes.length;
    renderFindResults(findQ[m].trim().toLowerCase());
    const on=findResults.querySelector('.sres.on'); if(on) on.scrollIntoView({block:'nearest'});
  }
  else if(e.key==='Enter'){ e.preventDefault(); findGo(findResIdx); }
  else if(e.key==='Escape'){ findResults.hidden=true; }
});
// on focus, list the results again for the current tab's query
searchEl.addEventListener('focus',()=>{ const m=findMode(); if(m && findQ[m].trim()) runFind(m,findQ[m]); });
searchEl.addEventListener('blur',()=>{ findResults.hidden=true; });
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
  const b=e.target.closest('.scap'); if(!b || e.target.closest('a')) return;   // a doc link opens, the card does not move
  const [ci,pi,ri]=b.dataset.ref.split('-').map(Number);
  const ref=STORY.chapters[ci].points[pi].refs[ri];
  storyReturn={scroll:storyView.scrollTop, key:b.dataset.ref};
  document.getElementById('btsCh').textContent=STORY.chapters[ci].title;
  btnBack.hidden=false;
  history.pushState({fromStory:true},'');
  gotoNode(ref.tree, ref.path);
});
// a capsule card is a div (it holds links), so Enter and Space open it like a button
storyView.addEventListener('keydown',e=>{ if(e.target.classList.contains('scap') && (e.key==='Enter'||e.key===' ')){ e.preventDefault(); e.target.click(); } });
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
document.fonts.ready.then(()=>{ measureHeights(); render(); });   // measure again once DM Sans is loaded
