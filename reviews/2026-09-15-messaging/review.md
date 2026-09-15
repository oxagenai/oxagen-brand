# Adversarial review of Oxagen launch messaging

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

Reviewed commit: `5090ebd4cf12132f78c44991f718e648846d7ceb`.

## Findings

### 01 · P1 · Completion dominates a product that also manages ongoing work

Buyer: Engineering / procurement

Current wording: The agent doesn’t get to decide it’s done.

**Skeptical objection:** Our agents have ongoing responsibilities. Does every agent need a finish line? What does a passing verdict establish?

**Why it matters:** The proof-heavy examples center bounded coding tasks. The founder’s launch vision is broader: operators manage an autonomous workforce, including work without a terminal definition of done. Treating completion as the defining feature narrows the product and still leaves the meaning of proof unclear.

**Suggested copy:** Mission Control for your autonomous agents. Set their authority, equip them for work, and define completion when the work has an endpoint.

**Suggested change:** Lead with workforce operations. Present completion checks as an optional control for bounded tasks. Show ongoing work with authority, budgets, and operator review. Define passing checks, recomputed verdicts, and witness results separately.

**Launch evidence and owner:** Launch acceptance: demonstrate both an ongoing responsibility and a bounded task. Show check failure, retry limits, human review, and verdict recomputation for the latter. Do not imply that passing specified checks establishes universal correctness.

Sources:

- [skills/oxagen-branding/references/positioning.md:88](https://github.com/oxagenai/oxagen-brand/blob/5090ebd4cf12132f78c44991f718e648846d7ceb/skills/oxagen-branding/references/positioning.md#L88)
- [skills/oxagen-branding/references/examples.md:71](https://github.com/oxagenai/oxagen-brand/blob/5090ebd4cf12132f78c44991f718e648846d7ceb/skills/oxagen-branding/references/examples.md#L71)
- [skills/oxagen-branding/references/examples.md:109](https://github.com/oxagenai/oxagen-brand/blob/5090ebd4cf12132f78c44991f718e648846d7ceb/skills/oxagen-branding/references/examples.md#L109)
- [build/build.py:335](https://github.com/oxagenai/oxagen-brand/blob/5090ebd4cf12132f78c44991f718e648846d7ceb/build/build.py#L335)
- [skills/oxagen-branding/references/positioning.md:137](https://github.com/oxagenai/oxagen-brand/blob/5090ebd4cf12132f78c44991f718e648846d7ceb/skills/oxagen-branding/references/positioning.md#L137)
- [skills/oxagen-branding/references/examples.md:33](https://github.com/oxagenai/oxagen-brand/blob/5090ebd4cf12132f78c44991f718e648846d7ceb/skills/oxagen-branding/references/examples.md#L33)

### 02 · P1 · A lower bill is promised without a boundary

Buyer: Finance

Current wording: Oxagen learns from every run, and the next one costs less.

**Skeptical objection:** Does every next run cost less, even when its task or model changes? What do you mean by the same answer?

**Why it matters:** The ad makes an unconditional outcome promise. Cost attribution alone does not establish savings or equal answer quality. The compact ad strengthens the claim further.

**Suggested copy:** See what each recorded run costs.

**Suggested change:** Separate the cost visibility claim from the cost reduction claim. For launch, use savings language only with the workload and conditions actually measured.

**Launch evidence and owner:** FinOps and engineering: provide a reproducible baseline, task set, model and rate versions, sample size, quality measure, and costs including retries and Oxagen fees. Report the distribution and exceptions, not only an average.

Sources:

- [build/build.py:328](https://github.com/oxagenai/oxagen-brand/blob/5090ebd4cf12132f78c44991f718e648846d7ceb/build/build.py#L328)
- [build/build.py:329](https://github.com/oxagenai/oxagen-brand/blob/5090ebd4cf12132f78c44991f718e648846d7ceb/build/build.py#L329)
- [skills/oxagen-branding/references/positioning.md:69](https://github.com/oxagenai/oxagen-brand/blob/5090ebd4cf12132f78c44991f718e648846d7ceb/skills/oxagen-branding/references/positioning.md#L69)

### 03 · P1 · Enforcement language exceeds its stated scope

Buyer: Security / platform

Current wording: enforced on every call

**Skeptical objection:** What happens with an unwrapped agent, a direct tool call, observe mode, or a workspace with no rules?

**Why it matters:** The repo itself distinguishes recording from enforcement and describes identity-only behavior without rules. Universal copy hides those distinctions. This is a messaging scope finding, not a finding that a specific bypass exists.

**Suggested copy:** For actions routed through Oxagen, teams can set access and budget rules and review the recorded decisions.

**Suggested change:** State the enrollment and enforcement boundary next to the claim. Document supported adapters, the default when no rule matches, outage behavior, and what hold or stop can affect.

**Launch evidence and owner:** Platform owner: demonstrate allow, deny, approval, missing-rule, observe-mode, and outage cases for each supported integration. Identify requests outside that boundary.

Sources:

- [skills/oxagen-branding/references/positioning.md:13](https://github.com/oxagenai/oxagen-brand/blob/5090ebd4cf12132f78c44991f718e648846d7ceb/skills/oxagen-branding/references/positioning.md#L13)
- [skills/oxagen-branding/references/voice.md:17](https://github.com/oxagenai/oxagen-brand/blob/5090ebd4cf12132f78c44991f718e648846d7ceb/skills/oxagen-branding/references/voice.md#L17)
- [skills/oxagen-branding/references/examples.md:133](https://github.com/oxagenai/oxagen-brand/blob/5090ebd4cf12132f78c44991f718e648846d7ceb/skills/oxagen-branding/references/examples.md#L133)

### 04 · P1 · Identity, connection credentials, and assurance need distinct claims

Buyer: Security

Current wording: there is no key to hand over, so there is nothing for the agent to leak

**Skeptical objection:** Does the agent have a real IAM identity? Which credential stays in Oxagen? What exactly is covered by the SOC 2 claim?

**Why it matters:** The vision requires real identity and access management identities, while the copy emphasizes agents holding no token. An agent’s own authentication and downstream connection credentials need distinct explanations. The broad leak promise exceeds credential custody, and auditability alone does not substantiate a SOC 2 examination.

**Suggested copy:** Give each agent its own identity. For mediated connections, Oxagen uses the connection credential on the agent’s behalf and records the governed action.

**Suggested change:** Separate agent identity, downstream credential custody, authorization, and audit evidence. Name supported identity systems and lifecycle behavior. Keep any SOC 2 statement specific to the actual report or readiness status; no report was inspected in this review.

**Launch evidence and owner:** Security owner: demonstrate provisioning, delegation, revocation, credential handling, and audit coverage. Before an attestation claim, verify the report type, entity, system scope, period, and access process against the actual report.

Sources:

- [skills/oxagen-branding/references/positioning.md:47](https://github.com/oxagenai/oxagen-brand/blob/5090ebd4cf12132f78c44991f718e648846d7ceb/skills/oxagen-branding/references/positioning.md#L47)
- [skills/oxagen-branding/references/positioning.md:40](https://github.com/oxagenai/oxagen-brand/blob/5090ebd4cf12132f78c44991f718e648846d7ceb/skills/oxagen-branding/references/positioning.md#L40)
- [skills/oxagen-branding/references/voice.md:79](https://github.com/oxagenai/oxagen-brand/blob/5090ebd4cf12132f78c44991f718e648846d7ceb/skills/oxagen-branding/references/voice.md#L79)

### 05 · P1 · Memory promises conflict with scoped knowledge

Buyer: Engineering / security

Current wording: Teach Oxagen your business once. Every agent you run has it.

**Skeptical objection:** Does every agent get the same information? How do updates, permissions, and stale knowledge work?

**Why it matters:** “Every agent” suggests universal distribution while the mandate promises restricted data scope. “Never” also violates the kit’s own restriction on outcome absolutes.

**Suggested copy:** Give agents the business context their work requires.

**Suggested change:** Explain approved context, permitted scope, and updates. Keep claims about reuse conditional on supported agents and configured knowledge sources. Avoid implying that storing context guarantees accurate recall.

**Launch evidence and owner:** Knowledge owner: demonstrate scoped retrieval, source attribution, corrections, deletion, and an agent denied access to another scope before claiming reuse across agents.

Sources:

- [build/build.py:317](https://github.com/oxagenai/oxagen-brand/blob/5090ebd4cf12132f78c44991f718e648846d7ceb/build/build.py#L317)
- [skills/oxagen-branding/references/positioning.md:70](https://github.com/oxagenai/oxagen-brand/blob/5090ebd4cf12132f78c44991f718e648846d7ceb/skills/oxagen-branding/references/positioning.md#L70)
- [skills/oxagen-branding/references/positioning.md:27](https://github.com/oxagenai/oxagen-brand/blob/5090ebd4cf12132f78c44991f718e648846d7ceb/skills/oxagen-branding/references/positioning.md#L27)

### 06 · P2 · The bill headline argues about providers

Buyer: Finance / platform

Current wording: Can you explain your AI bill? Neither can your provider.

**Skeptical objection:** My provider gives me usage reports. What does Oxagen add to those?

**Why it matters:** The second sentence creates an unsupported universal comparison. It also shifts attention away from the more useful question of attribution to a person, agent, and run. This review has not surveyed providers.

**Suggested copy:** See which agent spent what, and on whose behalf.

**Suggested change:** Keep cost attribution as the finance entry point. Lead the launch page with Mission Control for the autonomous workforce. Replace provider and category-wide dismissal with a concrete demonstration of agent identity, authority, equipment, and recorded activity.

**Launch evidence and owner:** Finance owner: show a sample cost row, rate source, attribution fields, exclusions, and reconciliation to billed totals. Use an explicit comparison set before making comparative claims.

Sources:

- [skills/oxagen-branding/references/positioning.md:68](https://github.com/oxagenai/oxagen-brand/blob/5090ebd4cf12132f78c44991f718e648846d7ceb/skills/oxagen-branding/references/positioning.md#L68)
- [skills/oxagen-branding/references/examples.md:7](https://github.com/oxagenai/oxagen-brand/blob/5090ebd4cf12132f78c44991f718e648846d7ceb/skills/oxagen-branding/references/examples.md#L7)

### 07 · P2 · The operator’s full job is missing from the lead

Buyer: Platform buyer

Current wording: The category has two names and Oxagen owns both

**Skeptical objection:** Where do I design authority and assign tools and skills? Is this a workforce control plane or a page for watching agents?

**Why it matters:** The current bill-led hero underrepresents the founder’s Mission Control vision. The mandate contains equipment, but tools, skills, and real agent identity do little work in the headline or first action. Multiple category claims compete with the operator’s actual job.

**Suggested copy:** Oxagen is Mission Control for an autonomous agent workforce: assign identities, set authority, equip agents with tools and skills, and oversee their work through a shared control plane.

**Suggested change:** Use Mission Control as the experience and agent control plane as the technical category. Demonstrate the full operator loop from agent identity and mandate to equipment assignment, governed action, and review. Make completion optional for bounded work.

**Launch evidence and owner:** Product owner: provide a launch walkthrough with identity, authority, tool and skill assignment, a recorded action, an ongoing agent, and a task with completion criteria. Document supported environments and control boundaries.

Sources:

- [skills/oxagen-branding/SKILL.md:41](https://github.com/oxagenai/oxagen-brand/blob/5090ebd4cf12132f78c44991f718e648846d7ceb/skills/oxagen-branding/SKILL.md#L41)
- [skills/oxagen-branding/references/positioning.md:13](https://github.com/oxagenai/oxagen-brand/blob/5090ebd4cf12132f78c44991f718e648846d7ceb/skills/oxagen-branding/references/positioning.md#L13)
- [skills/oxagen-branding/references/examples.md:11](https://github.com/oxagenai/oxagen-brand/blob/5090ebd4cf12132f78c44991f718e648846d7ceb/skills/oxagen-branding/references/examples.md#L11)
- [skills/oxagen-branding/references/examples.md:13](https://github.com/oxagenai/oxagen-brand/blob/5090ebd4cf12132f78c44991f718e648846d7ceb/skills/oxagen-branding/references/examples.md#L13)

### 08 · P2 · Sales copy presumes incompetence and hides proof status

Buyer: Security / engineering

Current wording: Your coding agents run with a GitHub token that can push to every repo

**Skeptical objection:** You have not seen our access setup. Are those buyer quotes actual testimonials? Are the traction numbers current?

**Why it matters:** The email asserts an unknown prospect configuration. Aspirational buyer statements look like testimonials when copied out of context. Time-sensitive traction and setup claims lack dated evidence in these examples.

**Suggested copy:** When an agent requests a repository action, can your team see which rule allowed it and who approved it? A walkthrough can show a denied request, an approval request, and the resulting record.

**Suggested change:** Use a diagnostic question instead of asserting the prospect’s setup. Label buyer statements as hypothetical. Keep traction and setup-duration claims out of launch copy until an owner provides dated evidence and publication approval.

**Launch evidence and owner:** Sales owner: confirm the demo exists. Founder: date and substantiate partner counts. Customer owner: obtain attribution permission before publishing an actual testimonial. Do not promise the demo on a prospect’s repositories without agreed setup.

Sources:

- [skills/oxagen-branding/references/examples.md:103](https://github.com/oxagenai/oxagen-brand/blob/5090ebd4cf12132f78c44991f718e648846d7ceb/skills/oxagen-branding/references/examples.md#L103)
- [skills/oxagen-branding/references/positioning.md:117](https://github.com/oxagenai/oxagen-brand/blob/5090ebd4cf12132f78c44991f718e648846d7ceb/skills/oxagen-branding/references/positioning.md#L117)
- [skills/oxagen-branding/references/examples.md:111](https://github.com/oxagenai/oxagen-brand/blob/5090ebd4cf12132f78c44991f718e648846d7ceb/skills/oxagen-branding/references/examples.md#L111)

### 09 · P2 · The approved message bank has already drifted

Buyer: Content operations

Current wording: Four live lines. Do not write a fifth.

**Skeptical objection:** Which approved file should I trust when the HTML, skill, and ads disagree?

**Why it matters:** The positioning has five live lead lines, the message bank lists four, and the ad recipe includes a proof headline outside those live lines. The declared source-of-truth rule has no demonstrated synchronization guarantee here.

**Suggested copy:** Approved messages, with release status and supporting evidence.

**Suggested change:** Create one message registry with ID, audience, long and short copy, release status, evidence, owner, and review date. Generate the message bank and ad copy from it. Apply one coordinated launch transition to approved entries. Avoid manually maintained line counts.

**Launch evidence and owner:** Brand engineering: add a build check that every published headline maps to a launch-approved registry entry and its evidence. Regenerate SVG and PNG assets together. Sync the vendored skill after approved source changes.

Sources:

- [message-bank.html:143](https://github.com/oxagenai/oxagen-brand/blob/5090ebd4cf12132f78c44991f718e648846d7ceb/message-bank.html#L143)
- [skills/oxagen-branding/references/positioning.md:72](https://github.com/oxagenai/oxagen-brand/blob/5090ebd4cf12132f78c44991f718e648846d7ceb/skills/oxagen-branding/references/positioning.md#L72)
- [message-bank.html:246](https://github.com/oxagenai/oxagen-brand/blob/5090ebd4cf12132f78c44991f718e648846d7ceb/message-bank.html#L246)
- [build/build.py:335](https://github.com/oxagenai/oxagen-brand/blob/5090ebd4cf12132f78c44991f718e648846d7ceb/build/build.py#L335)

### 10 · P2 · The glossary makes the first explanation harder

Buyer: New technical buyer

Current wording: Use each word exactly as defined and never a synonym.

**Skeptical objection:** What is a mandate, and why do I need to learn frames, witnesses, and verdicts before I understand the product?

**Why it matters:** Precise vocabulary helps operators, but the initial pitch bundles internal concepts before explaining a familiar task. A reader can mistake local definitions such as “proven” for broader guarantees.

**Suggested copy:** Set an agent’s authority, budget, tools, and skills in its mandate. Review the record of the work Oxagen governs.

**Suggested change:** Define mandate once beside the task. Keep run, request, rule, check, and cost in initial copy. Introduce frames and witness verdicts in detail pages with explicit definitions. Permit familiar explanatory language around exact UI labels.

**Launch evidence and owner:** Design owner: run a comprehension test with new buyers. Ask what the product does, which actions it controls, and what the next step requires. Track misconceptions, not just headline preference.

Sources:

- [skills/oxagen-branding/references/words.md:5](https://github.com/oxagenai/oxagen-brand/blob/5090ebd4cf12132f78c44991f718e648846d7ceb/skills/oxagen-branding/references/words.md#L5)
- [skills/oxagen-branding/references/words.md:31](https://github.com/oxagenai/oxagen-brand/blob/5090ebd4cf12132f78c44991f718e648846d7ceb/skills/oxagen-branding/references/words.md#L31)
- [skills/oxagen-branding/references/words.md:24](https://github.com/oxagenai/oxagen-brand/blob/5090ebd4cf12132f78c44991f718e648846d7ceb/skills/oxagen-branding/references/words.md#L24)
- [skills/oxagen-branding/references/positioning.md:96](https://github.com/oxagenai/oxagen-brand/blob/5090ebd4cf12132f78c44991f718e648846d7ceb/skills/oxagen-branding/references/positioning.md#L96)

## Rollout and validation

First, product and brand owners agree on agent identity, authority, equipment assignment, and the distinction between ongoing responsibilities and bounded work. Define a passing check, a recomputed verdict, and a witness result where completion applies. Confirm scope for mediated requests, supported agent integrations, and recorded cost. Use those answers to select final launch copy.

Second, put the selected copy into one registry and update the positioning, examples, voice samples, message bank, ad recipes, and playbook together. Regenerate paired SVG and PNG assets. Then use the monorepo’s documented sync process for the vendored skill. This PR provides proposals; it does not alter the approved source files or generated campaigns.

Third, build the destinations promised by the actions: a Mission Control walkthrough covering identity, authority, tools, skills, ongoing work, and bounded work, plus a request decision and itemized cost example. Document setup requirements and control boundaries at the point where a buyer needs them.

Test comprehension with 5 to 8 people in each priority buyer group as an initial qualitative study, not a statistically representative result. Ask them what Oxagen does, what it controls, what a verdict establishes, and what they would do next. Revise any copy that produces a broad correctness guarantee or universal agent coverage interpretation.

After comprehension testing, compare the workforce-led homepage with an operator-task-led alternative using the same traffic segment and matched destinations. Track qualified walkthrough completion and qualified conversations, plus setup abandonment. Define the sample and decision rule before running the test. Click-through rate alone does not establish better positioning.

## Acceptance for the messaging change

Every public claim has a named owner, defined scope, and supporting evidence. Each action leads to the promised experience. Proof terminology stays consistent across Oxagen and Stella. Campaign short forms preserve the qualifications of their longer versions. Customer quotes and traction metrics have dated substantiation. A coordinated launch transition updates every approved surface.
