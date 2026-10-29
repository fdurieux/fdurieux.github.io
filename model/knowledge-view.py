"""The reduced knowledge view of the systemic impact model, as an SVG generated from model.json.

Standard library only. Node ids and edge ids are the model's; the layout is this script's.
Run from the repository root:  python3 -I model/knowledge-view.py model/model.json model/knowledge-view.svg
"""
import json, sys, html

src, out = sys.argv[1], sys.argv[2]
M = json.load(open(src, encoding='utf-8'))
E = {e['id']: e for e in M['edges']}
N = {n['id']: n for n in M['nodes']}

W, H = 1280, 820
BW, BH = 212, 58
INK, MUTED, TEAL, PALE, LINE, AMBER, AMBERPALE, GREEN = '#18333E', '#51616B', '#087E83', '#EAF4F3', '#CFD9DC', '#8D5725', '#FBF1E4', '#2E7D5B'

# id -> (x, y, label lines, fill). Labels are the view's wording; ids are the model's.
nodes = {
  'tacit':       (40, 150, ['Knowledge held', 'only by people'], PALE),
  'updef':       (40, 300, ['Unresolved upstream', 'intent defects'], AMBERPALE),
  'unknown':     (40, 450, ['Unresolved or invented', 'decisions (assumptions)'], AMBERPALE),
  'validation':  (40, 700, ['Independent intent', 'validation'], PALE),
  'deriveddef':  (330, 220, ['Behaviour-carrying artefacts', 'contracts, tables, examples'], AMBERPALE),
  'explderived': (330, 320, ['Explanatory artefacts', 'models, prose'], AMBERPALE),
  'testdef':     (330, 420, ['Tests inherit the', 'same wrong premise'], AMBERPALE),
  'drift':       (330, 540, ['Artefact-to-reality', 'drift'], AMBERPALE),
  'depchange':   (620, 128, ['Platform or', 'dependency change'], PALE),
  'codedef':     (620, 220, ['Implementation', 'defects'], AMBERPALE),
  'escape':      (620, 380, ['Escaped product', 'defects'], AMBERPALE),
  'detection':   (620, 530, ['Effective independent', 'detection'], PALE),
  'confidence':  (620, 680, ['Unwarranted', 'confidence'], AMBERPALE),
  'harm':        (910, 380, ['Adverse outcomes', 'in use'], AMBERPALE),
  'dora':        (910, 530, ['Delivery performance', 'five DORA metrics'], PALE),
  'diverse':     (910, 610, ['Diverse independent', 'derivation'], PALE),
  'completeness':(910, 710, ['Completeness against', 'an inventory'], PALE),
}
# (edge id or None, source, target, label override)
edges = [
  ('E71', 'tacit', 'updef', None), ('E72', 'tacit', 'unknown', None),
  ('E50', 'updef', 'deriveddef', None), ('E75', 'updef', 'explderived', None), ('E52', 'updef', 'testdef', None),
  ('E51', 'deriveddef', 'codedef', None), ('E73', 'codedef', 'deriveddef', None), ('E76', 'explderived', 'codedef', None),
  ('E74', 'depchange', 'codedef', None), ('E55', 'codedef', 'escape', None), ('E64', 'escape', 'harm', None),
  ('E53', 'testdef', 'detection', None), ('E54', 'detection', 'escape', None),
  ('E56', 'validation', 'updef', None), ('E30', 'validation', 'unknown', None), ('E57', 'validation', 'detection', None),
  ('E77', 'drift', 'confidence', None), ('E29', 'confidence', 'validation', None),
  ('E78', 'diverse', 'detection', None), ('E79', 'completeness', 'detection', None),
  ('E17', 'escape', 'dora', 'H'),
]
levers = [  # (node, text)
  ('tacit', 'L1 · elicit (P10)'),
  ('validation', 'L2 · owner validates (P12)'),
  ('drift', 'L3 · externalise + register (P11)'),
  ('detection', 'L4 · calibrated oracle (P9)'),
]

def centre(nid):
  x, y, _, _ = nodes[nid]; return x + BW / 2, y + BH / 2

def anchor(nid, towards):
  """Point on the node's border on the line from its centre towards a point."""
  cx, cy = centre(nid); tx, ty = towards
  dx, dy = tx - cx, ty - cy
  if dx == 0 and dy == 0: return cx, cy
  sx = (BW / 2) / abs(dx) if dx else 1e9
  sy = (BH / 2) / abs(dy) if dy else 1e9
  s = min(sx, sy)
  return cx + dx * s, cy + dy * s

def ev(e):
  return 'M' if e['evidence'].startswith('M') else 'H'

o = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="DejaVu Sans, Arial, sans-serif" font-size="13">',
     f'<rect width="{W}" height="{H}" fill="#ffffff"/>',
     '<defs><marker id="a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#51616B"/></marker></defs>',
     f'<text x="40" y="44" font-size="22" font-weight="bold" fill="{INK}">Where knowledge capture acts on quality: the reduced view of the systemic model, v{html.escape(M["version"])}</text>',
     f'<text x="40" y="68" fill="{MUTED}">Signs and evidence labels only. M = measured, bounded; H = hypothesis. Node and edge ids are the model’s (model.json). The four levers are the capture practices.</text>']
# lanes
for x, w, lab in [(20, 290, 'PEOPLE AND INTENT'), (310, 290, 'DERIVED ARTEFACTS'), (600, 290, 'PRODUCT'), (890, 290, 'USE AND DELIVERY')]:
  o.append(f'<rect x="{x}" y="100" width="{w}" height="{H-120}" fill="{PALE}" opacity="0.35"/>')
  o.append(f'<text x="{x+12}" y="124" font-size="11" font-weight="bold" fill="{TEAL}">{lab}</text>')
# edges
for eid, a, b, override in edges:
  pa = anchor(a, centre(b)); pb = anchor(b, centre(a))
  mx, my = (pa[0] + pb[0]) / 2, (pa[1] + pb[1]) / 2
  e = E.get(eid)
  sign = e['polarity'] if e else '+'
  lab = override or (ev(e) if e else 'H')
  dash = ' stroke-dasharray="6,5"' if lab == 'H' else ''
  o.append(f'<line x1="{pa[0]:.1f}" y1="{pa[1]:.1f}" x2="{pb[0]:.1f}" y2="{pb[1]:.1f}" stroke="#51616B" stroke-width="1.6" marker-end="url(#a)"{dash}/>')
  o.append(f'<rect x="{mx-19:.1f}" y="{my-10:.1f}" width="38" height="20" rx="4" fill="#ffffff" stroke="{LINE}"/>')
  o.append(f'<text x="{mx:.1f}" y="{my+4:.1f}" text-anchor="middle" font-size="11" fill="{TEAL if sign=="+" else AMBER}">{html.escape(sign)} {lab}</text>')
# nodes
for nid, (x, y, lines, fill) in nodes.items():
  o.append(f'<rect x="{x}" y="{y}" width="{BW}" height="{BH}" rx="6" fill="{fill}" stroke="{LINE}"/>')
  for i, ln in enumerate(lines):
    o.append(f'<text x="{x+BW/2}" y="{y+24+i*17}" text-anchor="middle" fill="{INK}">{html.escape(ln)}</text>')
  o.append(f'<text x="{x+6}" y="{y+BH-5}" font-size="9" fill="{MUTED}">{nid if nid in N else "metrics: cfr, drr, clt, fdrt, df"}</text>')
# levers
for nid, text in levers:
  x, y, _, _ = nodes[nid]
  o.append(f'<rect x="{x}" y="{y-24}" width="{BW}" height="20" rx="10" fill="{GREEN}"/>')
  o.append(f'<text x="{x+BW/2}" y="{y-10}" text-anchor="middle" font-size="11" fill="#ffffff">{html.escape(text)}</text>')
# notes
o.append(f'<text x="40" y="{H-28}" font-size="11" fill="{MUTED}">Reverse path E73 and dependency source E74 (review F1); explanatory artefacts attenuated by precedence E76 (F3, degradation D1); drift feeding confidence E77 (F4).</text>')
o.append(f'<text x="40" y="{H-12}" font-size="11" fill="{MUTED}">Diverse derivation E78 and completeness E79 as detection inputs (F2, F5). The people-side edges E71 and E72 and the path to delivery metrics are hypotheses until the pilot runs.</text>')
o.append('</svg>')
open(out, 'w', encoding='utf-8').write('\n'.join(o) + '\n')
print('wrote', out, 'nodes', len(nodes), 'edges', len(edges))
