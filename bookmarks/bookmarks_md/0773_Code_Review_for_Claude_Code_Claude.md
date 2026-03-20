# Bringing Code Review to Claude Code

March 9, 2026 · Claude Blog

Claude Code now has a thorough, agent team-based review system, modeled on the one we run at Anthropic. Available in research preview.

## Managing the review bottleneck

Code output per Anthropic engineer has grown 200% in the last year. Code review has become a bottleneck, and we hear the same from customers every week. Developers are stretched thin, and many PRs get skims rather than deep reads.

Code Review is the result: deep, multi-agent reviews that catch bugs human reviewers often miss themselves. It's a more thorough (and more expensive) option than the existing Claude Code GitHub Action, which remains open source and available.

We run Code Review on nearly every PR at Anthropic. Before, 16% of PRs got substantive review comments. Now 54% do. It won't approve PRs — that's still a human call — but it closes the gap so reviewers can actually cover what's shipping.

## How it works

When a PR is opened, Code Review dispatches a team of agents. The agents:
- Look for bugs in parallel
- Verify bugs to filter out false positives
- Rank bugs by severity

The result lands on the PR as a single high-signal overview comment, plus in-line comments for specific bugs. Reviews scale with the PR. Large or complex changes get more agents and a deeper read; trivial ones get a lightweight pass. The average review takes around 20 minutes.

## Code Review in action

Internal results:
- On large PRs (over 1,000 lines changed): 84% get findings, averaging 7.5 issues
- On small PRs under 50 lines: 31% get findings, averaging 0.5 issues
- Less than 1% of findings are marked incorrect by engineers

In one case, a one-line change to a production service looked routine. But Code Review flagged it as critical — the change would have broken authentication for the service, a failure mode that's easy to read past in the diff but obvious once pointed out.

On a ZFS encryption refactor in TrueNAS's open-source middleware, Code Review surfaced a pre-existing bug: a type mismatch silently wiping the encryption key cache on every sync.

## Cost and control

Reviews are billed on token usage and generally average $15–25, scaling with PR size and complexity.

Admin controls:
- Analytics dashboard: Track PRs reviewed, acceptance rate, and total review costs
- Repository-level control: Enable reviews only on chosen repositories
- Monthly organization caps: Define total monthly spend

## Getting started

Code Review is available now as a research preview in beta for Team and Enterprise plans.

- For developers: Reviews run automatically on new PRs once enabled. No configuration needed.
- For admins: Enable in Claude Code settings, install the GitHub App, and select repositories.

[Explore the docs](http://code.claude.com/docs/en/code-review) for more information.

---
Source: https://claude.com/blog/code-review
