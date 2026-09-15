# Launch messaging review

Open `index.html` for the standalone report. It embeds its font and styles, supports light and dark themes, filters findings by priority, and prints all findings. Source citations link to the reviewed GitHub commit.

- `review.md`: adversarial findings and rollout plan for PR review.
- `launch-copy.md`: proposed homepage, product sections, audience entry points, announcement, emails, and ad copy.
- `findings.json`: structured findings with pinned source evidence.
- `render.py`: standard-library generator for the Markdown review and HTML report.

Regenerate from the repository root:

```sh
python3 reviews/2026-09-15-messaging/render.py
```

The launch-state brief assumes intended capabilities are available. Evidence requirements are readiness checks. This proposal does not change the approved branding skill or generated campaigns.
