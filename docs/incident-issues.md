# Incident issues & the `GH_PAT` requirement

The Upptime workflows in this repo open and close **incident issues** on status
changes and regenerate the generated `.github/workflows/*` from `.upptimerc.yml`.
Both need more than the default `GITHUB_TOKEN` can provide.

## Why the default token is not enough

- The workflows set `permissions: contents: write` (plus `issues: write` /
  `actions: write`, added 2026-07-03). With those, the default `GITHUB_TOKEN`
  can create/close incident issues and dispatch sibling workflows.
- **But** Setup CI (`setup.yml`) regenerates and pushes `.github/workflows/*`.
  GitHub refuses to let `GITHUB_TOKEN` push workflow files (that needs the
  `workflow` scope, which `GITHUB_TOKEN` never has). So changes to
  `.upptimerc.yml` never propagate to the generated workflows without a PAT.
- Assigning incident issues to a user (`issues.addAssignees`) also needs a token
  that represents a real account.

## Required operator action

Create a **fine-grained PAT** scoped to **this repository only**, with:

- Contents: **Read and write**
- Issues: **Read and write**
- Actions: **Read and write**
- Workflows: **Read and write**

Add it as the repository secret **`GH_PAT`** (Settings → Secrets and variables →
Actions). The workflows already reference it as
`GH_PAT: ${{ secrets.GH_PAT || github.token }}` — when the secret exists it is
used directly and bypasses the `permissions:` block above; when absent, the
workflows fall back to the (more limited) default token.

## After adding the PAT

1. Manually run **Setup CI** (`workflow_dispatch` on `setup.yml`) to backfill the
   monitors added since the last successful run and regenerate the workflow
   files.
2. Confirm the published page at status.kupe.cloud shows fresh check data (the
   Node-24 pin bump on 2026-07-03 fixed the crash that had frozen it since
   2026-06-16 — but a fresh run must complete to republish).
3. Trigger a deliberate down/up on a throwaway monitor and confirm an incident
   issue opens and auto-closes.
