# ISA platform (demo) — the bloated version

> Demo prop for the skills module. Copy this over CLAUDE.md to show a too-large,
> always-loaded instruction file, then move the situational parts into a skill.

FastAPI service for ISA accounts, contributions and transfers.

## Commands
- Install: `uv sync`
- Test: `uv run pytest`
- Run: `uv run uvicorn app.main:app --reload`

## Full endpoint-authoring procedure (belongs in a skill, not here)
When adding an endpoint: create a router in app/routes/<resource>.py with
APIRouter(prefix=..., tags=[...]); register it in app/main.py; decide auth (admin
routes take Depends(require_admin), put it on the router for admin-wide access);
define request bodies as Pydantic models in app/models.py with Field(gt=0) for
money; raise HTTPException(404) for missing records and HTTPException(422) for rule
violations with a human-readable detail; keep allowance logic in app/isa_rules.py;
write tests/test_<resource>.py covering the happy path, the auth failure and a rule
violation using the client and admin_headers fixtures; run uv run pytest and show output.

## Full release procedure (belongs in a runbook)
Cut a release branch; run the full suite; run ruff and black; update the changelog;
tag the release; get a second reviewer; deploy to staging; smoke test the health
endpoint; check the dashboards; deploy to production in a controlled window; watch
error rates for 30 minutes; record the release in the audit log.

## Full incident procedure (belongs in a runbook)
Detect via alert; declare severity; engage on-call; open an incident channel; post
comms every 30 minutes; mitigate (often a config rollback); confirm recovery; write
the post-incident review within 48 hours; add a regression test; update the spec.

## Coding style notes, tax-year notes, data-store notes, monitoring notes ...
(...pages more of situational detail that is paid for on every request...)
