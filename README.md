# Kupe Status

Status page for [kupe.cloud](https://kupe.cloud), powered by
[Upptime](https://github.com/upptime/upptime).

<!-- toc -->

* [Overview](#overview)
* [Workflows](#workflows)
* [Related](#related)
* [Branding](#branding)

<!-- Regenerate with "pre-commit run -a markdown-toc" -->

<!-- tocstop -->

## Overview

Upptime runs on a schedule via GitHub Actions, pings each configured
endpoint, and persists response times to the `history/` directory.
The generated status page is published to GitHub Pages; a custom
domain redirect is managed in the `cloudflare` repo.

Monitored endpoints and notification channels are defined in
`.upptimerc.yml`.

## Workflows

All scheduling is GitHub-Actions driven:

All workflows also support `repository_dispatch` and manual
`workflow_dispatch` triggers.

| Workflow            | Schedule                    | Purpose                        |
| ------------------- | --------------------------- | ------------------------------ |
| `uptime.yml`        | every 5 min                 | endpoint ping & history update |
| `response-time.yml` | daily                       | response-time rollup           |
| `summary.yml`       | daily                       | README status summary          |
| `graphs.yml`        | daily                       | SVG response-time graphs       |
| `site.yml`          | daily / dispatch            | publish the static status site |
| `setup.yml`         | on push to `.upptimerc.yml` | one-time bootstrap             |
| `updates.yml`       | dispatch only               | no-op stub; bumps are manual   |

Note: `upptime/updates` is now an upstream no-op, so `updates.yml` does
nothing; template upgrades are prepared on a feature branch and merged through a reviewed PR.
`update-template.yml` now provides that guidance without mutating the repository.

## Related

- [cloudflare](../cloudflare) — domain routing for `status.kupe.cloud`
- [docs-public](../docs-public) — public docs site hosted alongside

## Branding

The status site shares the canonical geometric K and lowercase kupe. wordmark
with the Kupe site, documentation, console and portal. Editable sources and
rendered assets live in `assets/brand/`. The configured logo and favicon use
new paths under `/brand/` to avoid cached legacy assets during the cutover;
the legacy PNG paths remain available. Dark surfaces use near-black and navy,
with mint actions and readable ink text in both normal and hover states.
Typography uses local Arial/Helvetica/system fonts. Branding is configured in
`.upptimerc.yml`; monitoring endpoints, schedules and incident history are
independent of the visual configuration.

Production publishing is restricted to main, including manual dispatches. Setup
no longer runs Upptime's push-capable template generator: that generator rewrites
and pushes the workflow files, removing branch guards. Local workflow files are
maintained through reviewed PRs. Setup and asset publishing share one deployment
queue; the policy is checked by `python3 -m unittest discover -s tests -v`.

Upptime generates `history/summary.json` as compact JSON. It remains covered by
JSON validation; only the authored-text final-newline rule excludes this file.
