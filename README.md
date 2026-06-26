# Kupe Status

Status page for [kupe.cloud](https://kupe.cloud), powered by
[Upptime](https://github.com/upptime/upptime).

<!-- toc -->

* [Overview](#overview)
* [Workflows](#workflows)
* [Related](#related)

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

| Workflow            | Schedule                         | Purpose                        |
| ------------------- | -------------------------------- | ------------------------------ |
| `uptime.yml`        | every 5 min                      | endpoint ping & history update |
| `response-time.yml` | daily                            | response-time rollup           |
| `summary.yml`       | daily                            | README status summary          |
| `graphs.yml`        | daily                            | SVG response-time graphs       |
| `site.yml`          | daily / dispatch                 | publish the static status site |
| `setup.yml`         | on push to `.upptimerc.yml`      | one-time bootstrap             |
| `updates.yml`       | daily                            | Upptime version bumps          |

## Related

- [cloudflare](../cloudflare) — domain routing for `status.kupe.cloud`
- [docs-public](../docs-public) — public docs site hosted alongside
