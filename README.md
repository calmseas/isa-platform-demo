# ISA Platform — demo repo

Training material for the **Advanced Claude Code** session (Frontier Practice
Advisory, for Hargreaves). A small, fictional FastAPI service for ISA accounts,
contributions and transfers, built to exercise the techniques in the deck.

> Fictional. No real customers, systems or client code. Safe to clone and share
> within the training.

## Quick start

```bash
uv sync                                 # fastapi, uvicorn + dev tools (pytest, ruff, black, httpx)
uv run pytest                           # one test fails on purpose — see PRESENTER.md
uv run uvicorn app.main:app --reload    # http://localhost:8000/docs
```

## Layout

```
app/                FastAPI service
  routes/           one router per resource
  isa_rules.py      allowance logic (capstone feature lands here)
  fees.py           platform fees (has a planted rounding bug)
tests/              pytest suite
docs/               long handbook + incident log (bulk-reading demos)
.claude/            settings, status line, new-endpoint skill, security-reviewer agent
.claude-plugin/     marketplace manifest → plugins/isa-tools
plugins/isa-tools/  installable plugin (command + agent)
specs/              spec-driven development artefacts + fallback examples
security/           invisible-Unicode skill-poisoning demo + detector
exercises/          the eight "try this" tasks from the deck
PRESENTER.md        the run-sheet, the planted faults, and reset instructions
```

## For the session

Follow **PRESENTER.md**. It lists every demo, what to type, the planted faults and
where they live, and how to reset between runs.
