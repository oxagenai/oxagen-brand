# Proposed launch messaging

Launch vision: Oxagen is Mission Control for operators who design and manage an autonomous agent workforce. This proposed copy assumes the intended launch capabilities are available. Evidence requirements belong to launch acceptance, separate from the customer-facing story.

## The positioning decision

Lead with the operator’s job: define an agent’s identity and authority, equip it for its work, and oversee what it does. Use Mission Control as the experience and agent control plane as the technical category. The workforce may include bounded tasks and ongoing responsibilities. Completion criteria are optional controls for work with a defined endpoint.

Primary audience: operators and platform teams accountable for an autonomous agent workforce. Security governs authority and identity. Engineering manages tools and skills. Finance manages budgets. These responsibilities can belong to one person or several teams; the copy should not require a particular org chart.

## Homepage hero

Eyebrow: The control plane for your agent workforce

Headline: Mission Control for your autonomous agents.

Supporting copy: Give each agent an identity. Set its authority, budget, tools, and skills. Define completion when the work has an endpoint, and oversee ongoing work through its requests, activity, and spend. Oxagen keeps the record of the actions it governs.

Primary action: Explore Mission Control

Under the action: Follow an agent from its assigned authority to a recorded action.

Destination: A product walkthrough showing agent identity, mandate, tool and skill assignment, an allowed action, a request for approval, and the resulting record. Include an ongoing agent and a bounded task with completion criteria.

## One-sentence pitch

Oxagen is Mission Control for an autonomous agent workforce: assign identities, set authority, equip agents with tools and skills, and oversee their work through a shared control plane.

## Short pitch

Your operators decide what each agent is responsible for, what it may do, and what it needs to work. Oxagen gives those decisions a home: an agent identity, a mandate for authority and budget, assigned tools and skills, and a record of governed activity. For bounded work, define completion before it starts. For ongoing work, manage the agent’s authority, requests, and spend as it operates.

## The authority section

Heading: Set the authority behind each action.

Copy: Give each agent its own identity in your identity and access management system. Set which actions it may request and which resources it may reach. For actions handled through Oxagen, rules allow the request, deny it, or route it to a person. The record connects the decision to the agent and the person responsible for its work.

Detail-page requirement: Name the supported identity systems and explain provisioning, delegation, revocation, and enforcement boundaries. “IAM identity” must describe the implemented relationship, not merely an internal agent ID.

## The equipment section

Heading: Give each agent the tools and skills its work requires.

Copy: Manage the tools and skills available to your workforce, then assign them through each agent’s mandate. Pair the equipment with the authority to use it and the business context the agent is permitted to read.

Detail-page requirement: Show how an operator changes an assignment, which version an agent receives, and when the change takes effect. Do not promise centralized revocation or version pinning without demonstrated behavior.

## The work section

Heading: Define completion when the work has an endpoint.

Copy: For a bounded task, set the checks and human decisions that determine completion before the agent starts. Oxagen locks those criteria into the run and records the results. For an ongoing responsibility, set the authority, budget, and review points that keep the work accountable over time.

Supporting note: A passing verdict means the specified checks held. Your team decides whether those checks are sufficient for the task. When checks fail, the record should show the reasons and whether the agent continued, waited for a person, or reached its retry limit.

## The operations section

Heading: Manage the workforce from Mission Control.

Copy: See the agents enrolled in Oxagen, the mandates they work under, their open requests, and their recorded activity and spend. Answer an approval request, change an assignment, or adjust a budget from the operator’s view. Use the hold and stop controls supported by each integration.

Supporting note: Agents run in their supported environments. Oxagen is the control plane that governs their work. Describe what a control changes and when it takes effect.

## The audit section

Heading: Follow the action back to its authority.

Copy: Review which agent requested an action, on whose behalf, which rule answered, and who approved it when a person was required. Inspect the recorded result and cost alongside that decision.

Supporting copy: For runs with completion checks, export the record so another person can recompute the recorded verdict without an Oxagen account or network connection.

Editorial decision: Auditability describes the evidence available for review. An exported verdict does not establish that every requirement was captured or that every action was correct. Use “proven” only beside a defined witness result and its scope.

## Security and SOC 2 messaging

Proposed security-page headline: Identity, authority, and a record you can inspect.

Copy: Review how agent identities map to your access controls, how Oxagen handles connection credentials, and what each governed action records. Inspect the supported deployment and integration boundaries before granting authority.

SOC 2 publication rule: State an actual completed examination, report type, covered entity and system, examination period or date, and report-access process only when supported by the report. If the intended launch status is readiness work or support for customer controls, describe that specific status and scope. Do not turn “auditable” or the founder’s SOC 2 ambition into an unverified attestation claim. This review has not inspected a SOC 2 report.

Credential copy: For mediated connections, Oxagen uses the connection credential on the agent’s behalf without giving that credential to the agent. The agent’s own identity and authentication are separate from the downstream credential held for a connection.

## Finance entry point

Headline: See which agent spent what, and on whose behalf.

Copy: Review recorded costs by person, agent, and run. Inspect the usage and rate behind a charge, then use that record to decide where to change a budget.

Action: Inspect workforce spend

Destination: Show the budget, recorded cost, attribution, rate source, exclusions, and the relationship to provider invoices. Claim savings only for measured workloads and conditions.

## Knowledge entry point

Headline: Give agents the business context their work requires.

Copy: Put approved business context within the agent’s permitted knowledge scope. Define which sources it can use and review those sources as the business changes.

Editorial decision: Explain retrieval and updates. Avoid universal recall or the promise that every subsequent run costs less.

## Launch announcement

An autonomous agent workforce needs operators who can decide what each agent may do, equip it for the work, and inspect what happens. Oxagen is Mission Control for that workforce.

Give each agent an identity. Set its authority and budget, assign tools and skills, and review requests that need a person’s decision. The record connects governed actions to the agent, the rule, and the person responsible.

Some work has a finish line. Define its completion criteria before the agent starts and review the recorded results afterward. Other work continues. Keep its authority, activity, and spend in view as it runs.

Explore Mission Control to follow an agent from its assigned mandate to a recorded action.

## Sales email for operators

Subject: Who sets the authority for your agents?

When your team adds an autonomous agent, where do you set its identity, authority, tools, skills, and budget? Where do you review the actions it takes?

Oxagen brings those decisions into Mission Control. A walkthrough follows one agent from its mandate through an approval request and the resulting record. It also shows how an operator defines completion for a bounded task and manages an ongoing responsibility.

Explore Mission Control.

## Sales email for security

Subject: Which identity and rule authorized that agent action?

When an agent requests an action, can your team connect it to the agent’s identity, the authority it was assigned, and the person responsible?

Oxagen applies your rules to requests handled through the platform and records the decision. A walkthrough shows the agent’s mandate, a denied request, one routed to a person, and the record each leaves.

Inspect an agent’s authority.

## Ad directions

Primary: “Mission Control for your autonomous agents.” Support: “Set identity, authority, tools, and skills. Oversee the work.” Action: “Explore Mission Control.”

Authority: “Which agent can do what?” Support: “Set authority and review the decisions behind governed actions.” Action: “Inspect agent authority.”

Equipment: “Equip each agent for its work.” Support: “Manage tools and skills through the agent’s mandate.” Action: “Explore agent equipment.”

Completion: “Define the finish line before work starts.” Support: “For bounded tasks, set completion checks and review their results.” Action: “See a checked run.”

Finance: “See which agent spent what.” Support: “Inspect recorded costs by person, agent, and run.” Action: “Inspect workforce spend.”

Use these as candidate replacements, not additional approved taglines or measured winners. The primary campaign introduces the control plane; the others explain a particular operator decision.

## Oxagen and Stella

The repository describes Stella as an open-source agent and Oxagen as the control plane. Proposed relationship line, subject to confirming the launch integration: “Stella is an agent. Oxagen is Mission Control for the workforce.”

Show Stella as one supported agent where that is accurate. Keep the platform story broad enough for other supported agents. Shared branding does not establish shared proof mechanisms or identical capabilities.
