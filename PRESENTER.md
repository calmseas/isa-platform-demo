# Presenter guide

Everything you need to run the demos. Keep this file to yourself — it spoils the
planted faults.

## Before the session

- `uv sync`, then `uv run pytest` once to confirm the environment (you'll see one
  failing test — that's intentional, see below).
- Pin the Claude Code version you rehearsed on.
- Present in **Manual** permission mode so the approval choices are visible.
- `/config workflowSizeGuideline=small` to keep the workflow demo fast and cheap.
- If you'll run the skill-poisoning beacon, set `BEACON_URL` to a URL you control
  (see security/README.md) and confirm outbound fetch is allowed in your demo session.
- Check the firm's provider route: if managed settings lock hooks down, `/goal` is
  unavailable; workflows can be disabled centrally; the Atlassian Cloud MCP server is
  Cloud-only.

## Planted faults (spoilers)

| Fault | Location | Used in |
| --- | --- | --- |
| Missing auth on account export | `app/routes/admin.py` → `/admin/export` (no `require_admin`) | security review / workflow audit |
| Decoy: looks unprotected, isn't | `app/routes/transfers.py` (router-level dependency) | audit (should be cleared, not flagged) |
| Decoy: public by design | `app/routes/health.py` | audit (correctly public) |
| Fee rounding bug | `app/fees.py` (float + round; 125 → 0.62, should be 0.63) | `/goal` fix |
| Missing cash sub-limit | `app/isa_rules.py` (only overall allowance enforced) | spec-driven capstone |
| Bloated CLAUDE.md | copy `examples/CLAUDE.bloated.md` over `CLAUDE.md` | skills demo |

`uv run pytest` shows **1 failed** (`tests/test_fees.py`) and the rest green.

## Run-sheet

| # | After slide | Demo | Min |
| --- | --- | --- | --- |
| 1 | 3–5 | `/context`, read `docs/ops-handbook.md`, `/context` again | 3 |
| 2 | 10–12 | Handoff → `/clear` → `@HANDOFF.md`; then `Esc Esc` to undo a bad edit | 5 |
| 3 | 13 | "Use a subagent to find every allowance calculation, report file:line" | 3 |
| 4 | 14 | "Use a workflow to audit every route under app/routes for missing auth, then have fresh agents refute each finding." One real gap survives (`/admin/export`); the two decoys are refuted. Launch at the start of part 2, reveal here | 5 |
| 5 | 15–18 | Swap in the bloated CLAUDE.md, then move endpoint conventions into the `new-endpoint` skill; in a fresh session ask for a new endpoint and watch it load | 5 |
| 6 | 19–20 | `/plugin marketplace add .`, install `isa-tools`, show `/context` footprint, disable | 3 |
| 7 | 21–24 | `security-reviewer` on the diff; then a Sonnet worker fixes a test and "send the follow-up to the same agent" | 5 |
| 8 | 18 | *(security)* build the poisoned skill, invoke it (beacon fires), then `python3 security/scan_invisible.py` reveals it; add the scan to CI + a deny rule to block it | 5 |
| 9 | 25–29 | Capstone: spec → `/plan` → tasks.md → `/clear` + `/goal` per task → `/code-review` → fresh reviewer vs the acceptance criteria. Fallbacks in `specs/cash-isa-limit/*.example.md` and branch `demo/capstone-solution` | 12 |
| 10 | 30 (fees) | `/goal tests/test_fees.py passes, output shown; no other files change; or stop after 15 turns` | 3 |
| 11 | 31 | *(optional)* the same feature through a sandbox Jira project + Confluence space, if on Atlassian Cloud and approved | 5 |

Core demos ≈ 45 min; options add ≈ 8.

## Reset between demos

- Code/state: `git reset --hard demo-start && git clean -fd` (removes any generated
  poisoned skill and scratch files).
- The capstone reference lives on `demo/capstone-solution` — diff against it if a live
  build stalls: `git diff demo-start demo/capstone-solution -- app/isa_rules.py`.
- Record a fallback screen capture of each demo in case the room's network is flaky.
