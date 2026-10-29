from pathlib import Path
import json, math, textwrap, importlib.util
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle
from matplotlib.font_manager import FontProperties
from matplotlib.textpath import TextToPath

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('data', ROOT/'work/model-data.py')
data = importlib.util.module_from_spec(spec); spec.loader.exec_module(data)
M=data.MODEL
OUT=ROOT/'output'; OUT.mkdir(exist_ok=True)
QA=ROOT/'work/rendered'; QA.mkdir(parents=True,exist_ok=True)
W,H=595.28,841.89
INK='#18333E'; MUTED='#51616B'; TEAL='#087E83'; PALE='#EAF4F3'; LINE='#CFD9DC'; AMBER='#8D5725'; AMBERPALE='#FBF1E4'
BODY=10.2
ttp=TextToPath(); widthcache={}
def tw(s,size,weight='normal'):
    key=(s,size,weight)
    if key not in widthcache:
        widthcache[key]=ttp.get_text_width_height_descent(s,FontProperties(family='DejaVu Sans',size=size,weight=weight),False)[0]
    return widthcache[key]

def wrap(s,width,size=BODY,weight='normal'):
    result=[]
    for para in str(s).split('\n'):
        words=para.split(); line=''
        for word in words:
            candidate=(line+' '+word).strip()
            if line and tw(candidate,size,weight)>width:
                result.append(line);line=word
            else:line=candidate
        result.append(line)
    return result

pages=[]; lows=[]; bounds={}; fig=ax=None; number=0
def page(title,kicker,subtitle=None,landscape=False):
    global fig,ax,number,W,H
    if fig is not None: finish()
    W,H=(841.89,595.28) if landscape else (595.28,841.89)
    number+=1
    bounds[number]=H-52
    fig=plt.figure(figsize=(W/72,H/72),dpi=130,facecolor='white')
    ax=fig.add_axes([0,0,1,1]);ax.set_xlim(0,W);ax.set_ylim(H,0);ax.axis('off')
    ax.text(44,28,'LEGIBLE / SYSTEMIC IMPACT MODEL',color=TEAL,fontsize=8.4,weight='bold',va='top')
    ax.text(W-44,28,'v0.2 · 28 OCT 2026',color=MUTED,fontsize=8.4,ha='right',va='top')
    title_end=text(44,62,title,W-88,size=24,weight='bold',leading=29)
    kicker_y=max(101,title_end+10)
    text(44,kicker_y,kicker,W-88,size=10.2,color=TEAL,weight='bold')
    y=kicker_y+25
    if subtitle:y=text(44,y,subtitle,W-88,size=10.2,color=MUTED)+13
    ax.plot([44,W-44],[H-43,H-43],color=LINE,lw=.7)
    ax.text(44,H-30,'Definitions aligned · causal effects conditional',fontsize=8,color=MUTED,va='center')
    ax.text(W-44,H-30,f'{number:02d}',fontsize=9,color=INK,ha='right',va='center')
    return y

def text(x,y,s,width,size=BODY,color=INK,weight='normal',leading=None):
    leading=leading or size*1.38
    lines=wrap(s,width,size,weight)
    for n,line in enumerate(lines):
        ax.text(x,y+n*leading,line,fontsize=size,fontfamily='DejaVu Sans',color=color,weight=weight,va='top')
    end=y+len(lines)*leading
    lows.append((number,end,s[:70]))
    return end

def para(y,s,size=BODY):return text(44,y,s,W-88,size=size)+10
def label(y,title,s):
    y=text(44,y,title,W-88,size=11.1,weight='bold')+3
    return text(44,y,s,W-88)+12
def rule(y):ax.plot([44,W-44],[y,y],color=LINE,lw=.65)
def box(y,title,s,color=PALE):
    lines=wrap(s,W-114,BODY)
    height=36+len(lines)*14
    ax.add_patch(Rectangle((44,y),W-88,height,facecolor=color,edgecolor='none'))
    text(57,y+11,title,W-114,size=10.5,weight='bold')
    text(57,y+31,s,W-114,size=BODY)
    return y+height+14

def table(y,headers,rows,widths,size=9.3,pad=7):
    x=44
    hh=max(len(wrap(h,w-2*pad,size,'bold')) for h,w in zip(headers,widths))*size*1.35+2*pad
    ax.add_patch(Rectangle((44,y),sum(widths),hh,facecolor=PALE,edgecolor='none'))
    for h,w in zip(headers,widths):text(x+pad,y+pad,h,w-2*pad,size=size,weight='bold');x+=w
    y+=hh
    for row in rows:
        rh=max(len(wrap(c,w-2*pad,size)) for c,w in zip(row,widths))*size*1.38+2*pad
        x=44
        for i,(c,w) in enumerate(zip(row,widths)):
            text(x+pad,y+pad,c,w-2*pad,size=size,weight='bold' if i==0 else 'normal');x+=w
        y+=rh;rule(y)
    return y+12

def node(x,y,w,h,s,color=PALE,size=9.6):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0,rounding_size=4',facecolor=color,edgecolor=LINE,lw=.75))
    ls=wrap(s,w-12,size)
    yy=y+(h-len(ls)*size*1.2)/2
    for line in ls:
        ax.text(x+w/2,yy,line,fontsize=size,ha='center',va='top',color=INK);yy+=size*1.2

def arrow(a,b,sign=None,rad=0):
    ax.add_patch(FancyArrowPatch(a,b,arrowstyle='-|>',mutation_scale=9,lw=1,color=MUTED,connectionstyle=f'arc3,rad={rad}'))
    if sign:ax.text((a[0]+b[0])/2,(a[1]+b[1])/2-5,sign,fontsize=10,color=TEAL,ha='center',va='center',bbox=dict(facecolor='white',edgecolor='none',pad=.5))

def finish():
    if fig is None:return
    pages.append(fig)
    fig.savefig(QA/f'page-{number:02d}.png',dpi=120)

# 1 - Synthesis
y=page('Quality emerges from the system','A causal model of the 18 artefact classes on fdurieux.github.io')
y=para(y,'Tools affect outcomes through the defects they reveal, the decisions people make, and the way work flows. The same gate can prevent rework or create a bottleneck. Its net effect depends on precision, ownership, timing, adoption and independent validation.',11)
y=box(y,'Four connected lenses; an explicit cascade','The four layers are distinct, not independent. Wrong or missing upstream intent can be inherited by models, code and tests, with consequences for users and delivery. Page 3 makes propagation, shared-error blindness and containment visible. Your supplied definitions now anchor the model.',PALE)
top=y+5
node(44,top,153,49,'Relevant, effective\ncheck use')
node(221,top,153,49,'Evidence understood\nand acted on')
node(398,top,153,49,'Valid intent and\ncurrent shared knowledge')
arrow((197,top+24),(221,top+24),'+');arrow((374,top+24),(398,top+24),'+')
node(398,top+92,153,49,'Implementation, tests\nand runtime behaviour')
node(221,top+92,153,49,'Product quality and\nescaped defect burden')
node(44,top+92,153,49,'Delivery flow and\nfive DORA metrics')
arrow((474,top+49),(474,top+92),'+');arrow((398,top+116),(374,top+116));arrow((221,top+116),(197,top+116))
text(44,top+153,'Mediated paths, not a direct tool-to-DORA conversion. Precise signs and conditions are in the graph data.',507,size=8.9,color=MUTED)
y=top+189
y=label(y,'The central reinforcing loop','Effective checking → validated correction → reliable shared knowledge → fewer escaped defects → less reactive work → more capacity for prevention. The last step requires an explicit allocation decision.')
y=label(y,'The competing failure loop','Stricter controls → greater gate burden → longer waits → larger batches → more failed changes → pressure for still stricter controls. A more comprehensive gate can make the system perform worse.')
y=label(y,'The purpose and boundary','Follow one application or service from hypothesis or technical-change need through production use and learning. Optimize useful, safe outcomes and sustainable change capability. Keep suppliers, platform constraints and release policy visible.')
y=para(y,'Model contents: 18 artefact mappings · your 9 quality elements · 5 delivery metrics · 8 closed feedback loops · an explicit defect cascade · stocks, interventions and a measurement design.',9.5)

# 2 - quality
y=page('What “quality” means here','Your nine quality elements, in the supplied order [S9]', 'Software quality concerns meeting users’ needs, behaving under real conditions and remaining maintainable over time. The meanings below reproduce your definitions; the indicators are proposed measurements.')
rows=[[q[0]+' '+q[1],q[2],q[3]] for q in M['quality']]
y=table(y,['Quality category','Operational meaning','Observe independently'],rows,[131,178,198],size=9.1,pad=6)
y=label(y,'Keep four connected lenses distinct','Artefact quality concerns what is written; product quality, what is built; quality in use, what people experience; DORA, how changes are delivered. Defects can cross these boundaries. Distinguishing the lenses lets us test each link instead of assuming it.')
y=para(y,'Use measurable, product-specific acceptance criteria. Technical debt is deferred work and future change burden. A gate score or delivery metric does not establish the nine quality elements.',9.8)

# Explicit cross-layer cascade: landscape preserves the branching and left-to-right dependency view.
y=page('How defects cascade','One upstream defect can be reproduced, hidden and exposed downstream',
       'Arrows show conditional causal paths, not a mandatory lifecycle. “+” increases the named defect or consequence; “−” reduces it. Every path can be interrupted.',landscape=True)
for x,w,label_ in [(44,350,'ARTEFACT QUALITY'),(422,176,'PRODUCT QUALITY'),(622,176,'QUALITY IN USE')]:
    ax.add_patch(Rectangle((x,156),w,195,facecolor=PALE,edgecolor='none',alpha=.42))
    text(x+8,163,label_,w-16,size=9,weight='bold',color=TEAL)
node(55,233,141,58,'Unresolved intent defects\nwrong / missing / stale',color=AMBERPALE)
node(243,191,139,49,'Defects in models\nand contracts',color=AMBERPALE)
node(243,289,139,49,'Tests inherit the\nsame wrong premise',color=AMBERPALE)
node(430,191,160,49,'Faulty implementation\nbehaviour / data / controls',color=AMBERPALE)
node(430,289,160,49,'Undetected / escaped\nproduct defects',color=AMBERPALE)
node(630,191,160,49,'Operational exposure\nusers / transactions / time')
node(630,289,160,49,'Adverse outcomes\nfor users and operators',color=AMBERPALE)
arrow((196,247),(243,215),'+');arrow((196,278),(243,313),'+')
arrow((382,215),(430,215),'+');arrow((382,313),(430,313),'+')
arrow((510,240),(510,289),'+');arrow((590,313),(630,313),'+')
arrow((710,240),(710,289),'+')
text(285,366,'Tests and code can agree\nwhile both are wrong.',120,size=9.3,color=AMBER)
ax.add_patch(Rectangle((422,386),376,92,facecolor=PALE,edgecolor='none',alpha=.42))
text(630,396,'DELIVERY PERFORMANCE',160,size=8.5,weight='bold',color=TEAL)
node(430,416,160,50,'Rework and\nincident workload',color=AMBERPALE)
node(630,416,160,50,'DORA outcomes\nsee per-metric conditions')
arrow((510,338),(510,416),'+');arrow((590,441),(630,441))
node(44,416,174,50,'Independent intent and\noutcome validation',color=PALE)
arrow((119,416),(119,291),'−')
arrow((218,416),(243,338),'−')
text(44,486,'Amplifiers: dependent reach · shared-oracle blindness · late discovery and repair scope · operational exposure.',754,size=10,weight='bold')
text(44,507,'Evidence: model-to-code transfer has bounded experimental support [S3]. The full cascade and DORA effects are hypotheses; dependency and change-impact guidance is in [S11]. More downstream impact is possible, not inevitable.',754,size=9.4,color=MUTED)
fig.savefig(OUT/'legible-defect-cascade.png',dpi=180)

# 3 - metrics
y=page('How the paths reach DORA','Five current delivery metrics; all effects here are conditional', 'Use the same application or service over time. A causal path is a hypothesis to test; no percentage improvement or tool-specific coefficient is assumed. [S4]')
rows=[[r[0]+' · '+r[1],r[2],r[3]+' '+r[4]] for r in M['metrics']]
y=table(y,['Metric','Definition / direction','Proposed path and condition'],rows,[106,161,240],size=9.2,pad=6)
y=label(y,'The upstream measurement blind spot','Change lead time starts at the code commit. Earlier clarification can reduce total delivery time without moving CLT; mandatory pre-commit preparation can improve CLT while making the whole journey slower. Capture both clocks.')
y=para(y,'Track timestamps for hypothesis, first relevant code commit, production deployment, user release and validated outcome. These are event landmarks, not an assumption that discovery and delivery happen in non-overlapping phases. Deployment and release can be separate.',9.7)
y=box(y,'Additional guardrails','User task success; SLO attainment and incident impact; security and safety outcomes; performance; accessibility; debt trend; staff workload. DORA alone cannot tell whether a useful, safe product was built.')

# 4-6 - inventory
for start,end in [(0,5),(5,10),(10,14),(14,18)]:
    y=page(f'Artefact pathways {start+1:02d}–{end:02d}','All 18 inventory rows retained; site states are preserved [S1]', '“Covered” means that checks exist for some properties. “Planned” and “open” are not credited as deployed capability. Quality and metric codes are defined in the preceding sections.')
    for r in M['inventory'][start:end]:
        y=text(44,y,r['id']+'  '+r['artefact'],395,size=11.2,weight='bold')+2
        ax.text(551,y-16,r['state'].upper(),fontsize=8.1,color=TEAL,ha='right',va='top')
        y=text(44,y,r['tools'],507,size=9.0,color=MUTED)+4
        y=text(44,y,'Mechanism: '+r['mechanism'],507,size=9.35)+3
        y=text(44,y,'Quality: '+', '.join(r['quality'])+'. '+r['route'],507,size=9.35)+3
        y=text(44,y,'Limit: '+r['limit'],507,size=9.05,color=AMBER)+7
        rule(y);y+=9
    if end==18:
        y=label(y,'Coverage is uneven; tool effects are not additive','The clearest proposed paths concern correctness, compatibility and maintainability. Performance, usability, security and other properties need their own verification. Overlapping tools do not create additive benefits; shared assumptions can create common-mode failure.')

# 7-8 - loops
names={n['id']:n['label'] for n in M['nodes']}
short={
'check':'Effective check use','early':'Validated early correction','knowledge':'Current validated knowledge','fidelity':'Implementation correctness','escape':'Escaped defect burden','reactive':'Reactive workload','capacity':'Improvement capacity','pressure':'Delivery pressure','bypass':'Check bypass','severity':'Control strictness','gateburden':'Gate burden','waiting':'Waiting time','batch':'Batch size','cfr':'Change fail rate','repair':'Score-driven repair','green':'Apparent gate success','confidence':'Unwarranted confidence','validation':'Independent validation','unknown':'Unresolved / invented intent','drift':'Artefact-to-reality drift','discrepancy':'Confirmed discrepancies','learning':'Validated learning'}
short.update(updef='Unresolved upstream defects',deriveddef='Defects in derived artefacts',codedef='Implementation defects',harm='Adverse outcomes in use')
def drawloop(y,L):
    y=text(44,y,L['id']+'  '+L['title'],507,size=12,weight='bold')+6
    ids=L['nodes']; nt=math.ceil(len(ids)/2); nb=len(ids)-nt
    xs=[52+i*(491-100)/(nt-1) for i in range(nt)] if nt>1 else [247]
    bxs=[52+i*(491-100)/(nb-1) for i in range(nb)] if nb>1 else [247]
    coords=[(x,y) for x in xs]+[(x,y+64) for x in reversed(bxs)]
    for n,(x,yy) in zip(ids,coords):node(x,yy,100,38,short[n],size=8.5)
    for i,ei in enumerate(L['edges']):
        e=next(e for e in M['edges'] if e['id']==ei)
        a=coords[i];b=coords[(i+1)%len(ids)]
        if abs(a[1]-b[1])<1:
            forward=b[0]>a[0];p=(a[0]+(100 if forward else 0),a[1]+19);q=(b[0]+(0 if forward else 100),b[1]+19)
        else:
            down=b[1]>a[1];p=(a[0]+50,a[1]+(38 if down else 0));q=(b[0]+50,b[1]+(0 if down else 38))
        arrow(p,q,e['polarity'])
    y+=112
    y=text(44,y,L['reading']+' '+L['leverage'],507,size=9.5)+5
    y=text(44,y,'Evidence: '+L['evidence']+'.',507,size=8.6,color=MUTED)+16
    return y

y=page('Feedback that compounds','R = reinforcing: it can amplify improvement or deterioration', '+ means same direction; − means opposite direction, with other factors held comparable. The loop sign comes from the product of its link signs. Delays and edge conditions are explicit in the JSON model.')
for L in M['loops'][:3]:y=drawloop(y,L)
y=para(y,'Reinvestment is a decision: saved time can instead become extra demand. That rebound increases WIP and waiting, eroding the intended benefit.',9.4)

y=page('False assurance and correction','R4 is a failure loop; B1 and B2 counter a discrepancy', 'The existence of a balancing loop does not guarantee a good outcome. Delay, weak evidence, overload or an incorrect target can prevent effective correction.')
for L in M['loops'][3:6]:y=drawloop(y,L)

y=page('Why downstream effects can grow','Propagation and amplification are different mechanisms',
       'The root error need not become more wrong. Its reach, persistence, repair burden or consequences can increase. Independent evidence, containment and early correction can attenuate the cascade.')
for L in M['loops'][6:]:y=drawloop(y,L)
y=label(y,'What “worse downstream” can mean','Spread: more dependent artefacts and components carry consequences. Concealment: shared assumptions delay discovery. Entrenchment: more decisions, data and commitments must be unwound. Exposure: more users or transactions experience the fault. These are separate variables, not a universal cost multiplier.')
y=label(y,'What to measure','Link each confirmed root defect to the downstream items actually affected. Record detection stage and delay, escapes, independent checks that stopped it, repair scope and effort, and user impact. Do not count every copy as an independent root cause.')

# 9 - stocks and delays
y=page('Stocks, delays and bottlenecks','A dynamic structure, without invented numerical coefficients')
y=table(y,['Stock','Additions / removals','What the measure does not mean'],[[r[0]+' · '+r[1]+'\n'+r[2],r[3],r[4]] for r in M['stocks']],[146,202,159],size=9.6,pad=7)
y=label(y,'Conservation statements','U(next) = U + introduced defects − validated corrections.\nT(next) = T + newly deferred effort + re-estimated drift burden − retired effort.\nK(next) = K + validated knowledge − invalidated or stale knowledge.\nW(next) = W + admitted changes − completed changes − abandoned changes.')
y=para(y,'Use consistent units and periods. A future simulation needs locally estimated rates, delays and capacity constraints, with stocks bounded at zero. These are bookkeeping structures, not fitted equations.',9.8)
y=label(y,'Three relevant delays','Minutes to a change: check feedback, triage and author corrections. Days to weeks: altered implementation and escaped-defect observations. Weeks to months: confidence, skills, debt repayment and rule maintenance. These time bands are assumptions to check locally.')
y=label(y,'Why the effect is nonlinear','Coverage saturates: the next rule can add little value. Low precision consumes scarce attention. As demand approaches available review capacity, waiting can rise sharply. Better upstream information may not improve delivery if release policy or deployment infrastructure remains the bottleneck.')

# 10 - actors and lifecycle
y=page('People, power and lifecycle','Tools are actants; people retain decisions and accountability')
y=table(y,['Actor','Decision / leverage','Needed feedback or safeguard'],M['actors'],[130,155,222],size=9.1,pad=6)
y=label(y,'Anchor the causal network in the SAFe delivery wheel','Continuous Exploration: Hypothesize; Collaborate & Research; Architect; Synthesize.\nContinuous Integration: Develop; Build; Test End-to-End; Stage.\nContinuous Deployment: Deploy; Verify; Monitor; Respond.\nRelease on Demand: Release; Stabilize; Measure; Learn.')
y=para(y,'The inventory acts mainly on exploration and integration. Deployment and release outcomes are mediated by runtime practices. This model adds the return path from user and operational evidence to upstream decisions; it does not extend the tool catalogue’s coverage by assertion. [S1]',9.5)
y=box(y,'A change in incentives is a stronger intervention than a score target','Reward resolution of real uncertainty and verified outcomes. Do not rank individuals by DORA, finding count, diagram maturity or number of links. Allow teams to challenge a bad rule and make exceptions visible, owned and temporary.')

# 11 - practices and leverage
y=page('Interventions that change the loops','Use the six gate-contract properties as a system, with intent validation')
for p in M['practices']:
    y=text(44,y,p[0]+'  '+p[1],507,size=11,weight='bold')+2
    y=text(44,y,p[2]+'. '+p[3],507,size=9.8)+11
y=label(y,'Suggested order of leverage','1. Fix the purpose: useful, safe outcomes rather than passing scores.\n2. Clarify decision rights: who resolves missing intent and accepts residual risk.\n3. Shorten information feedback: author-local checks and usable incident evidence.\n4. Adjust flow and rules: precision, thresholds, ratchets and WIP limits.\n5. Add tool coverage only where an observed defect class justifies it.')
y=para(y,'This is a design proposal, not an empirical ranking. Co-design with authors, users, responders and gate maintainers. Their perspectives and power differ; participation is proposed here, not claimed to have occurred. Reframe the model as experiments reveal new dynamics.',9.5)

# 12 - predictions and pilot
y=page('Make the model testable','A small service-level pilot; no assumed DORA effect size')
for h in M['hypotheses']:
    y=text(44,y,h[0]+'  '+h[1],507,size=11,weight='bold')+2
    y=text(44,y,h[2],507,size=9.7)+3
    y=text(44,y,'Prediction: '+h[3],507,size=9.7)+3
    y=text(44,y,'Challenge: '+h[4],507,size=9.5,color=AMBER)+12
y=label(y,'Prospective use: choose one causal path','Pick one service, one real defect class and the applicable artefacts. Establish observation before enforcing a gate. Agree check scope, finding review, time budget and independent correctness evidence. Run advisory first, then enforce only validated high-precision rules.')
y=label(y,'Diagnostic use: work backward from the outcome','If CLT worsens, locate the waiting stage before adding rules. If incidents persist despite green artefacts, inspect semantic validity, coverage, drift and downstream use. If FDRT is unchanged, check whether responders use the model and whether diagnosis is the limiting step.')
y=para(y,'Suggested cadence: a baseline window, then a staged pilot and follow-up spanning several delivery cycles. Choose duration from deployment frequency and event counts; a fixed calendar window cannot guarantee enough failures to infer an effect.',9.5)

# 13 - measurement and evidence
y=page('Measure mechanisms before outcomes','A falsifiable learning plan, with evidence limits attached')
y=table(y,['Record','Why it matters'],[
['Relevant check exposure','Eligible artefacts and changes; rule/version/config; whether run and consumed. Separate tool installation from effective use.'],
['Finding usefulness','Independently adjudicated actionable findings; samples of missed defects; duplicate/noise rate; time to action. Findings rising initially can mean better detection.'],
['Costs and behaviour','Triage hours, execution delay, approval wait, bypasses, suppressions, baseline updates, batch size, WIP and reactive work share.'],
['Downstream outcomes','Covered defect escape classes, independent acceptance, user/SLO/security outcomes, debt trend, all five DORA metrics and both delivery clocks.'],
['Context and provenance','Service, change ID, risk/size, team and platform changes, deployment and incident IDs, artefact versions, authorship and unresolved decisions.']
],[137,370],size=9.6,pad=7)
y=label(y,'Evaluate direction and trade-offs, not a vanity score','Define acceptable gate burden and the targeted quality improvement before enforcement. Compare similar change cohorts or use a phased introduction with a credible comparison service. Inspect pre-existing trends and changes in staffing, demand, release policy, test coverage and incident reporting.')
y=para(y,'Show deployment counts and failure/rework counts alongside rates. For CLT and recovery, show distributions and event counts; fewer incidents can change which failures remain. If no failed deployments occur, report no observed recovery-time sample, not zero recovery time. No single-service before/after result proves causality.',9.8)
y=box(y,'What is actually measured in pumllint','The author-less repair experiment raised the low-maturity tier’s gate results while executed pass rate fell 5.9 percentage points relative to its degraded baseline. This supports a specific “green but wrong” failure mode on that instrument. It does not estimate a DORA effect or establish the same effect for every artefact class. [S3]')
y=label(y,'Evidence status of this whole model','M: bounded local experiment. R: related primary capability research. H: proposed causal mechanism. I: site inventory. All tool-to-production-DORA paths remain hypotheses here; no production intervention dataset was supplied.')

# 14 - provenance and next use
y=page('Sources and model maintenance','Readable report plus a machine-readable causal graph')
for s in M['sources']:
    y=text(44,y,s['id']+'  '+s['title'],507,size=10.5,weight='bold')+2
    # Short display labels are clickable and kept legible.
    display=s['url'].replace('https://','')
    if 'chatgpt.com/library' in display:display='systemic-impact-model-task.md — supplied definitions'
    if '/blob/' in display:
        pre,post=display.split('/blob/',1);sha,path=post.split('/',1);display=pre+'/blob/'+sha[:7]+'/'+path
    # URL may contain long tokens; use deliberate wrap at slashes for legibility.
    lines=textwrap.wrap(display,width=87,break_long_words=True,break_on_hyphens=False)
    for line in lines:
        ax.text(44,y,line,fontsize=8.5,color=TEAL,va='top',url=s['url']);y+=12
    y=text(44,y,s['scope'],507,size=9.2,color=MUTED)+9
y=label(y,'Source discipline','The tool inventory is the site’s dated snapshot, not a new exhaustive tool audit. The site table labels diagram-code drift “planned”, whereas the programme roadmap records it as “open”; this model treats it as unavailable and does not assume that either status means implemented.')

finish()
overflow=[(p,round(y,1),s) for p,y,s in lows if y>bounds[p]]
if overflow:
    print(json.dumps({'layout_overflow':overflow},indent=2))
else:print('Layout bounds OK')

with PdfPages(OUT/'legible-systemic-impact-model.pdf',metadata={'Title':M['title'],'Author':'Prepared for Frederik Durieux','Subject':'Conditional causal model: defect propagation across artefacts, products, use and delivery'}) as pdf:
    for f in pages:pdf.savefig(f)
(OUT/'legible-systemic-impact-model.json').write_text(json.dumps(M,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

# Meaningful structural verification of the model.
ids={n['id'] for n in M['nodes']}; edges={e['id']:e for e in M['edges']}
assert len(M['inventory'])==18 and len({a['id'] for a in M['inventory']})==18
assert len(M['quality'])==9 and len(M['metrics'])==5
assert all(e['source'] in ids and e['target'] in ids and e['polarity'] in ('+','-') for e in M['edges'])
assert all(e['mechanism'] and e['condition'] and e['delay'] and e['evidence'] for e in M['edges'])
for L in M['loops']:
    ls=[edges[e] for e in L['edges']]
    assert all(ls[i]['target']==ls[(i+1)%len(ls)]['source'] for i in range(len(ls)))
    assert ((-1)**sum(e['polarity']=='-' for e in ls)==1)==(L['type']=='R')
assert all(q in {r[0] for r in M['quality']} for a in M['inventory'] for q in a['quality'])
assert all(s in {r['id'] for r in M['sources']} for a in M['inventory'] for s in a['source'])
(QA/'verification.json').write_text(json.dumps({'pages':len(pages),'nodes':len(ids),'edges':len(edges),'loops':len(M['loops']),'inventory_rows':len(M['inventory']),'layout_overflow':overflow},indent=2))
print(json.dumps({'pdf':str(OUT/'legible-systemic-impact-model.pdf'),'pages':len(pages),'nodes':len(ids),'edges':len(edges),'loops':len(M['loops'])}))
