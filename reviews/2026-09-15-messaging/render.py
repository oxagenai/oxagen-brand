"""Render the review and its launch-copy companion using Python's standard library."""
import base64
import html
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
d = json.loads((HERE / 'findings.json').read_text())
esc = html.escape
base = f"https://github.com/oxagenai/oxagen-brand/blob/{d['commit']}/"
def source_url(s):
    return f"{base}{s['path']}#L{s['line']}"
def refs(f):
    return ' · '.join(f'<a href="{source_url(s)}">{esc(s["path"])}:{s["line"]}</a>' for s in f['sources'])

intro = '''# Adversarial review of Oxagen launch messaging

## Recommendation

Lead with Mission Control for operators managing an autonomous agent workforce. Show how they assign identity and authority, equip agents with tools and skills, and review governed activity. Define completion for bounded tasks where a finish line exists. Keep the senior-engineer voice, the concrete demo sequence, and the single-record story. Replace blanket outcome promises with claims whose scope the buyer can inspect.

## Scope and method

This review follows the launch-state brief: the proposed customer copy assumes the intended launch capabilities are available, including completion checks and independent verdict recomputation. Existing held status is a coordination issue, not an objection to writing launch copy.

Reviewed the positioning, voice, vocabulary, examples, branding skill, message bank, README, ad recipes, and playbook source. The review covers messaging in the repository, not every rendered asset pixel or the live product. Source links are pinned to the reviewed commit. No product runtime, customer interviews, competitor survey, savings benchmark, or commercial figures were verified. Buyer objections and predicted effects are editorial hypotheses, not measured conversion results.

P1 means a claim could create a materially false expectation and should be resolved before publication. P2 means positioning, comprehension, or content-maintenance work. Priorities are editorial judgments, not security severity ratings.

## What to preserve

The request → rule → recorded answer sequence explains a mechanism a buyer can inspect. The mandate gives accountable teams a common object. The demo’s denied request and human approval are stronger evidence than a category-ownership claim. Keep the plain voice and its distinction between recorded, enforced, and independently checked results.

## Proposed message hierarchy

1. Mission Control: operate the autonomous agent workforce.
2. Identity and authority: assign agent identities and govern permitted actions.
3. Equipment: manage tools, skills, and permitted knowledge.
4. Operations and evidence: review requests, activity, budgets, and recorded decisions.
5. Completion: set criteria for bounded work and review the results.

The primary audience is operators and platform teams accountable for an autonomous agent workforce, following the founder’s stated vision. Finance and security get separate entry points into the same control plane. Validate buyer language through interviews. See launch-copy.md for the full candidate copy set.
'''
md = intro + f"\nReviewed commit: `{d['commit']}`.\n\n## Findings\n"
cards = []
for f in d['findings']:
    md += f"\n### {f['id']} · {f['priority']} · {f['title']}\n\nBuyer: {f['buyer']}\n\nCurrent wording: {f['quote']}\n"
    for label,key in [('Skeptical objection','objection'),('Why it matters','impact'),('Suggested copy','rewrite'),('Suggested change','action'),('Launch evidence and owner','proof')]:
        md += f"\n**{label}:** {f[key]}\n"
    md += '\nSources:\n\n' + '\n'.join(f'- [{s["path"]}:{s["line"]}]({source_url(s)})' for s in f['sources']) + '\n'
    cards.append(f'''<article class="finding" data-priority="{f['priority']}" id="finding-{f['id']}">
    <p class="meta">{f['id']} / {f['priority']} / {esc(f['buyer'])}</p><h3>{esc(f['title'])}</h3>
    <div class="pair"><div><p class="label">Current wording</p><blockquote>{esc(f['quote'])}</blockquote></div><div><p class="label">Buyer objection</p><p>{esc(f['objection'])}</p></div></div>
    <p>{esc(f['impact'])}</p><div class="rewrite"><p class="label">Suggested copy</p><p>{esc(f['rewrite'])}</p></div>
    <p><strong>Change:</strong> {esc(f['action'])}</p><p><strong>Launch evidence:</strong> {esc(f['proof'])}</p>
    <details><summary>Source evidence ({len(f['sources'])})</summary><ul>{''.join(f'<li><a href="{source_url(s)}">{esc(s["path"])}:{s["line"]}</a><p>{esc(s["excerpt"])}</p></li>' for s in f['sources'])}</ul></details></article>''')
plan='''## Rollout and validation

First, product and brand owners agree on agent identity, authority, equipment assignment, and the distinction between ongoing responsibilities and bounded work. Define a passing check, a recomputed verdict, and a witness result where completion applies. Confirm scope for mediated requests, supported agent integrations, and recorded cost. Use those answers to select final launch copy.

Second, put the selected copy into one registry and update the positioning, examples, voice samples, message bank, ad recipes, and playbook together. Regenerate paired SVG and PNG assets. Then use the monorepo’s documented sync process for the vendored skill. This PR provides proposals; it does not alter the approved source files or generated campaigns.

Third, build the destinations promised by the actions: a Mission Control walkthrough covering identity, authority, tools, skills, ongoing work, and bounded work, plus a request decision and itemized cost example. Document setup requirements and control boundaries at the point where a buyer needs them.

Test comprehension with 5 to 8 people in each priority buyer group as an initial qualitative study, not a statistically representative result. Ask them what Oxagen does, what it controls, what a verdict establishes, and what they would do next. Revise any copy that produces a broad correctness guarantee or universal agent coverage interpretation.

After comprehension testing, compare the workforce-led homepage with an operator-task-led alternative using the same traffic segment and matched destinations. Track qualified walkthrough completion and qualified conversations, plus setup abandonment. Define the sample and decision rule before running the test. Click-through rate alone does not establish better positioning.

## Acceptance for the messaging change

Every public claim has a named owner, defined scope, and supporting evidence. Each action leads to the promised experience. Proof terminology stays consistent across Oxagen and Stella. Campaign short forms preserve the qualifications of their longer versions. Customer quotes and traction metrics have dated substantiation. A coordinated launch transition updates every approved surface.
'''
md += '\n'+plan
(HERE/'review.md').write_text(md)

def prose(text):
    out=[]
    for block in text.strip().split('\n\n'):
        if block.startswith('# '): out.append('<h3>'+esc(block[2:])+'</h3>')
        elif block.startswith('## '): out.append('<h3>'+esc(block[3:])+'</h3>')
        else: out.append('<p>'+esc(block).replace('\n','<br>')+'</p>')
    return '\n'.join(out)
font=base64.b64encode((ROOT/'fonts/space-grotesk-latin-400.woff2').read_bytes()).decode()
tokens=(ROOT/'tokens/house-tokens.css').read_text()
css='''
@font-face{font-family:Review;src:url(data:font/woff2;base64,FONT) format('woff2');font-weight:400;font-display:swap}
:root{color-scheme:dark;--bg:var(--ox-ink);--fg:var(--ox-text);--muted:var(--ox-muted);--panel:var(--ox-panel);--border:var(--ox-rule)}
[data-theme=light]{color-scheme:light;--bg:var(--ox-paper);--fg:var(--ox-text-ink);--muted:var(--ox-muted-ink);--panel:var(--ox-paper-panel);--border:var(--ox-paper-rule)}
*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;background:var(--bg);color:var(--fg);font:16px/1.65 Review,Arial,sans-serif}main,header,footer{max-width:1120px;margin:auto;padding:24px}header{display:flex;justify-content:space-between;align-items:center;gap:20px}.brand{font-size:25px;letter-spacing:-1px}.brand span{color:var(--ox-gold)}h1,h2,h3{line-height:1.17;letter-spacing:-.025em}h1{font-size:clamp(34px,5vw,58px);max-width:850px;margin:20px 0}h2{font-size:30px}h3{font-size:23px}p{max-width:85ch}a{color:inherit;text-underline-offset:4px;overflow-wrap:anywhere}.meta,.label{font-size:12px;letter-spacing:.08em;text-transform:uppercase;color:var(--muted)}.lead{font-size:21px;max-width:800px}.hero{padding:32px 0 44px}.note{border-left:3px solid var(--border);padding:8px 20px;color:var(--muted)}nav{display:flex;gap:22px;flex-wrap:wrap;border-block:1px solid var(--border);padding:16px 0}section{padding:35px 0;border-bottom:1px solid var(--border);scroll-margin-top:15px}.pair{display:grid;grid-template-columns:1fr 1fr;gap:24px}.finding{padding:30px 0;border-top:1px solid var(--border)}.finding:first-of-type{border-top:0}blockquote{margin:0;font-size:20px;line-height:1.5}.rewrite{background:var(--panel);border:1px solid var(--border);border-radius:12px;padding:16px 22px}.rewrite p:last-child{font-size:20px;margin:4px 0}.toolbar{display:flex;gap:10px;flex-wrap:wrap;align-items:center}button{font:inherit;background:var(--panel);border:1px solid var(--border);border-radius:8px;padding:8px 14px;color:var(--fg);cursor:pointer}button[aria-pressed=true]{border:3px double var(--fg);padding:6px 12px}button:focus-visible,a:focus-visible,summary:focus-visible{outline:2px solid var(--fg);outline-offset:4px}details{border:1px dashed var(--border);border-radius:12px;padding:12px 16px;margin-top:20px}summary{cursor:pointer}details li{padding:8px 0}details p{font-size:14px;overflow-wrap:anywhere;color:var(--muted)}.copy h3{margin-top:36px}.copy{max-width:880px}footer{color:var(--muted);font-size:13px}[hidden]{display:none!important}.skip{position:absolute;left:-9999px}.skip:focus{left:20px;top:15px;background:var(--bg);padding:15px;z-index:9}@media(max-width:650px){.pair{grid-template-columns:1fr;gap:12px}header,main,footer{padding:18px}h2{font-size:26px}.lead{font-size:18px}header{align-items:flex-start}}@media(prefers-reduced-motion:reduce){html{scroll-behavior:auto}}@media print{body{--bg:white;--fg:black;--muted:#444;--panel:white;--border:#bbb;color-scheme:light;font-size:11pt}header button,.toolbar,nav,.skip{display:none}article{break-inside:avoid}.finding[hidden]{display:block!important}details{display:block}h1{font-size:30pt}section{padding:20px 0}}
'''.replace('FONT',font)
page=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Oxagen · Adversarial launch messaging review</title><style>{tokens}{css}</style></head><body>
<a class="skip" href="#main">Skip to review</a><header><div class="brand">o<span>x</span>agen <small> / messaging review</small></div><button id="theme" type="button">Switch to light</button></header>
<main id="main"><div class="hero"><p class="meta">Launch preparation / 15 September 2026</p><h1>Mission Control needs a workforce story.</h1><p class="lead">Put the operator in charge of identity, authority, tools, and skills. Define completion when it applies. Make the governed work inspectable.</p><p class="note">Launch-state brief: proposed copy assumes the intended launch capabilities are available. Readiness checks are separate from the customer-facing story.</p><p>10 findings · 5 claim priorities · 5 positioning and consistency priorities</p></div>
<nav aria-label="Report sections"><a href="#decision">Recommendation</a><a href="#findings">Findings</a><a href="#copy">Proposed launch copy</a><a href="#plan">Rollout</a><a href="#scope">Scope</a></nav>
<section id="decision"><p class="meta">The decision</p><h2>One launch story, distinct buyer entry points.</h2><div class="pair"><div><h3>Keep the concrete mechanism</h3><p>Start with the agent’s identity and mandate, show its assigned tools and skills, then follow a request through a rule to the recorded answer. That sequence makes the control plane tangible.</p></div><div><h3>Define what the evidence establishes</h3><p>Ongoing agents need authority and oversight even when their work has no finish line. Bounded tasks can add completion checks. Keep IAM identity, credential custody, and SOC 2 status precise.</p></div></div><div class="rewrite"><p class="label">Proposed homepage headline</p><p>Mission Control for your autonomous agents.</p></div><p>Use workforce operations as the lead, identity and authority for security, and cost attribution for finance. These are proposed directions to test, not measured winners.</p></section>
<section id="findings"><p class="meta">The skeptical buyer’s case</p><h2>Ten findings and concrete replacements</h2><p>P1: resolve material claim expectations before publication. P2: improve positioning, comprehension, and consistency.</p><div class="toolbar" aria-label="Filter findings"><button data-filter="all" aria-pressed="true">All findings</button><button data-filter="P1" aria-pressed="false">P1 · Claims</button><button data-filter="P2" aria-pressed="false">P2 · Positioning</button><span id="count" role="status">10 findings shown</span></div>{''.join(cards)}</section>
<section id="copy"><p class="meta">Ready for editorial selection</p><h2>The proposed launch copy set</h2><div class="copy">{prose((HERE/'launch-copy.md').read_text())}</div></section>
<section id="plan"><p class="meta">From recommendation to release</p><h2>Rollout and validation</h2>{prose(plan)}</section>
<section id="scope"><h2>Evidence and limits</h2><p>Reviewed positioning, voice, vocabulary, examples, the branding skill, message bank, README, ad recipes, and playbook source. Findings cite the repository at commit <code>{d['commit'][:12]}</code>. Source links require access to the repository; the report itself works offline.</p><p>Product runtime, buyer interviews, competitor coverage, savings, and traction were not independently verified. Objections and predicted effects are editorial hypotheses. This report does not certify implementation readiness. The approved source copy remains unchanged in this proposal PR.</p><p>Keep: the plain voice, the common mandate, the recorded-request demo, and the distinction between recorded and enforced behavior.</p></section></main><footer>Oxagen launch messaging review · Proposed copy for review · Generated from findings.json and launch-copy.md</footer>
<script>
const theme=document.querySelector('#theme');function setTheme(light){{document.documentElement.dataset.theme=light?'light':'dark';theme.textContent=light?'Switch to dark':'Switch to light'}}setTheme(matchMedia('(prefers-color-scheme: light)').matches);theme.addEventListener('click',()=>setTheme(document.documentElement.dataset.theme!=='light'));
for(const button of document.querySelectorAll('[data-filter]'))button.addEventListener('click',()=>{{let count=0;for(const item of document.querySelectorAll('.finding')){{item.hidden=button.dataset.filter!=='all'&&item.dataset.priority!==button.dataset.filter;if(!item.hidden)count++}}for(const other of document.querySelectorAll('[data-filter]'))other.setAttribute('aria-pressed',String(other===button));document.querySelector('#count').textContent=count+' findings shown'}});
</script></body></html>'''
(HERE/'index.html').write_text(page)
print('Rendered review.md and index.html')
