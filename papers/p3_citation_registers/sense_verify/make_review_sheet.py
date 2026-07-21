#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Generate the interactive A18 sense-verification review sheet (self-contained
HTML, no server/CDN) from sense_verify_items.json.

Output: review/A18_sense_verify_sheet.html (gitignored — personal review
artifact, not a repo deliverable). Votes persist in localStorage; the
"Download decisions.json" button exports
  { sheet_id, generated, decided, items: [{id, decision, note}] }
with decision null for unvoted items. Drop the file at
review/decisions.json and run apply_decisions.py.

Item id = k1_slp1 (stable natural key; survives sheet regeneration).
"""
import sys, os, json, html, datetime
sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

HERE = os.path.dirname(os.path.abspath(__file__))
OUT  = os.path.join(HERE, 'review')
os.makedirs(OUT, exist_ok=True)

items = json.load(open(os.path.join(HERE, 'sense_verify_items.json'), encoding='utf-8'))

def scan_url(pc):
    # pc like '442,3' -> Cologne MW 1899 scan page
    page = pc.split(',')[0]
    return f'https://www.sanskrit-lexicon.uni-koeln.de/scans/MWScan/2020/web/webtc/servepdf.php?page={page}'

def hl(sentence, form):
    s = html.escape(sentence)
    f = html.escape(form)
    return s.replace(f, f'<mark>{f}</mark>') if f else s

cards = []
for it in items:
    iid = it['k1_slp1']
    stratum = it['stratum']
    badge = ('<span class="badge hedge">L.-hedged</span>' if stratum == 'hedge'
             else '<span class="badge control">control (text-cited)</span>')
    links = ' · '.join(
        f'<a href="{scan_url(pc)}" target="_blank">MW scan p.{html.escape(pc)}</a>'
        for pc in it['mw_pc'])
    occ_rows = ''.join(
        f'<tr><td class="txt">{html.escape(o["text"])}</td>'
        f'<td class="ref">{html.escape(o["ref"] or "")}</td>'
        f'<td class="sent">{hl(o["sentence"], o["form"])}</td></tr>'
        for o in it['dcs_occurrences'])
    cards.append(f'''
<div class="item" data-id="{html.escape(iid)}">
 <div class="head"><span class="k1">{html.escape(iid)}</span> {badge}
   <span class="tok">{it['dcs2026_tokens']} DCS tokens</span>
   <span class="links">{links}</span></div>
 <div class="mw"><b>MW:</b> {html.escape(it['mw_entry_plain'])}
   <span class="cites">⟨{html.escape(' | '.join(it['ls_citations']))}⟩</span></div>
 <table class="occ"><thead><tr><th>DCS text</th><th>ref</th><th>sentence</th></tr></thead>
   <tbody>{occ_rows}</tbody></table>
 <div class="vote">
  <button class="b app" onclick="vote('{html.escape(iid)}','approve')">✅ sense attested</button>
  <button class="b rej" onclick="vote('{html.escape(iid)}','reject')">❌ homograph / other sense</button>
  <button class="b def" onclick="vote('{html.escape(iid)}','defer')">⏸ unsure</button>
  <input class="note" placeholder="note…" oninput="note('{html.escape(iid)}',this.value)">
 </div>
</div>''')

n_h = sum(1 for i in items if i['stratum'] == 'hedge')
n_c = len(items) - n_h
today = datetime.date.today().strftime('%d-%m-%Y')
page = f'''<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<title>A18 sense verification — {len(items)} items</title>
<style>
 body{{font-family:Segoe UI,system-ui,sans-serif;margin:0;background:#f6f6f4;color:#1a1a1a}}
 header{{position:sticky;top:0;background:#2b2b40;color:#fff;padding:10px 18px;z-index:9;display:flex;gap:18px;align-items:baseline;flex-wrap:wrap}}
 header h1{{font-size:16px;margin:0}} header .tally{{font-size:14px}}
 header button{{background:#4a7;border:0;color:#fff;padding:6px 12px;border-radius:5px;cursor:pointer;font-size:13px}}
 .wrap{{max-width:1080px;margin:14px auto;padding:0 14px}}
 .item{{background:#fff;border:1px solid #ddd;border-radius:8px;padding:12px 14px;margin-bottom:14px}}
 .item.voted-approve{{border-left:6px solid #3a9a5f}} .item.voted-reject{{border-left:6px solid #c0392b}}
 .item.voted-defer{{border-left:6px solid #c8a400}} .item.current{{outline:2px solid #5b7fd4}}
 .k1{{font-weight:700;font-size:17px}} .tok{{color:#666;font-size:12px;margin-left:8px}}
 .links{{font-size:12px;margin-left:8px}}
 .badge{{font-size:11px;padding:2px 7px;border-radius:9px;margin-left:6px;vertical-align:middle}}
 .badge.hedge{{background:#fde8c8}} .badge.control{{background:#d7e7fb}}
 .mw{{margin:8px 0;font-size:14px}} .cites{{color:#8a5a00;font-size:12px;margin-left:6px}}
 table.occ{{width:100%;border-collapse:collapse;font-size:13px;margin:6px 0}}
 table.occ th{{text-align:left;color:#666;font-weight:600;border-bottom:1px solid #ddd;padding:2px 6px}}
 table.occ td{{border-bottom:1px solid #eee;padding:3px 6px;vertical-align:top}}
 td.txt{{white-space:nowrap;color:#333;width:16%}} td.ref{{white-space:nowrap;color:#666;width:14%}}
 mark{{background:#ffe28a;padding:0 1px}}
 .vote{{display:flex;gap:8px;margin-top:8px;align-items:center;flex-wrap:wrap}}
 .b{{border:1px solid #bbb;background:#fafafa;padding:6px 10px;border-radius:6px;cursor:pointer;font-size:13px}}
 .b.app:hover{{background:#e2f4e8}} .b.rej:hover{{background:#fbe4e0}} .b.def:hover{{background:#fbf3d0}}
 .note{{flex:1;min-width:180px;border:1px solid #ccc;border-radius:6px;padding:6px 8px;font-size:13px}}
 footer{{color:#888;font-size:12px;text-align:center;margin:24px 0}}
</style></head><body>
<header>
 <h1>A18 · MW sense verification (band-3 <i>L.</i> pass)</h1>
 <span class="tally" id="tally"></span>
 <button onclick="dl()">⬇ Download decisions.json</button>
 <span style="font-size:12px;color:#cdd">Generated {today} · {len(items)} items ({n_h} hedged + {n_c} control) · keys: a approve · r reject · d defer · j/k or ↑/↓ move</span>
</header>
<div class="wrap">
<p><b>Question per item:</b> do the DCS-2026 corpus occurrences attest <i>the sense MW gives</i>?
For <b>L.-hedged</b> items MW knew no text witness — an attested sense refutes the hedge at sense level.
<b>Control</b> items are text-cited senses; they measure the method's expected ceiling.</p>
{''.join(cards)}
</div>
<footer>sheet_id a18-sense-verify-v1 · votes autosave to localStorage · export → review/decisions.json → apply_decisions.py</footer>
<script>
const SHEET='a18-sense-verify-v1';
const state=JSON.parse(localStorage.getItem(SHEET)||'{{}}');
const ids=[...document.querySelectorAll('.item')].map(e=>e.dataset.id);
let cur=0;
function paint(){{
 let t={{approve:0,reject:0,defer:0,unvoted:0}};
 document.querySelectorAll('.item').forEach(el=>{{
  const s=state[el.dataset.id]||{{}};
  el.classList.remove('voted-approve','voted-reject','voted-defer');
  if(s.decision){{el.classList.add('voted-'+s.decision);t[s.decision]++;}}else t.unvoted++;
  const n=el.querySelector('.note'); if(n && s.note!==undefined && n.value!==s.note) n.value=s.note;
 }});
 document.getElementById('tally').textContent=
  `✅ ${{t.approve}} · ❌ ${{t.reject}} · ⏸ ${{t.defer}} · ⬜ ${{t.unvoted}}`;
}}
function save(){{localStorage.setItem(SHEET,JSON.stringify(state));paint();}}
function vote(id,d){{state[id]=state[id]||{{}};state[id].decision=d;save();}}
function note(id,v){{state[id]=state[id]||{{}};state[id].note=v;save();}}
function focusItem(i){{
 cur=Math.max(0,Math.min(ids.length-1,i));
 document.querySelectorAll('.item').forEach((e,j)=>e.classList.toggle('current',j===cur));
 document.querySelectorAll('.item')[cur].scrollIntoView({{block:'center'}});
}}
document.addEventListener('keydown',e=>{{
 if(e.target.tagName==='INPUT')return;
 if(e.key==='a'){{vote(ids[cur],'approve');focusItem(cur+1);}}
 else if(e.key==='r'){{vote(ids[cur],'reject');focusItem(cur+1);}}
 else if(e.key==='d'){{vote(ids[cur],'defer');focusItem(cur+1);}}
 else if(e.key==='j'||e.key==='ArrowDown'){{focusItem(cur+1);e.preventDefault();}}
 else if(e.key==='k'||e.key==='ArrowUp'){{focusItem(cur-1);e.preventDefault();}}
}});
function dl(){{
 const out={{sheet_id:SHEET,generated:'{today}',decided:new Date().toISOString(),
  items:ids.map(id=>({{id,decision:(state[id]||{{}}).decision||null,note:(state[id]||{{}}).note||''}}))}};
 const a=document.createElement('a');
 a.href=URL.createObjectURL(new Blob([JSON.stringify(out,null,1)],{{type:'application/json'}}));
 a.download='decisions.json';a.click();
}}
paint();focusItem(0);
</script></body></html>'''

path = os.path.join(OUT, 'A18_sense_verify_sheet.html')
open(path, 'w', encoding='utf-8').write(page)
print(f'wrote {path} ({os.path.getsize(path)/1024:.0f} KB, {len(items)} items)')
