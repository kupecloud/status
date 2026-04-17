# Kupe Status

Status page for [kupe.cloud](https://kupe.cloud), powered by
[Upptime](https://github.com/upptime/upptime).

<!-- toc -->

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

| Workflow            | Schedule          | Purpose                        |
| ------------------- | ----------------- | ------------------------------ |
| `uptime.yml`        | every 5 min       | endpoint ping & history update |
| `response-time.yml` | hourly            | response-time rollup           |
| `summary.yml`       | hourly            | README status summary          |
| `graphs.yml`        | daily             | SVG response-time graphs       |
| `site.yml`          | on push to `main` | publish the Astro status site  |
| `setup.yml`         | manual            | one-time bootstrap             |
| `updates.yml`       | weekly            | Upptime version bumps          |

## Related

- [cloudflare](../cloudflare) — domain routing for `status.kupe.cloud`
- [docs-public](../docs-public) — public docs site hosted alongside
