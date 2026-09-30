# Skill poisoning — invisible-Unicode demo (training only)

A contained, **benign** demonstration for the Advanced Claude Code session: a skill whose
`SKILL.md` looks harmless to a human reviewer but carries a hidden instruction the model reads.
When invoked, the model makes a single `GET` to a URL **you** control — proof that an
unreviewed instruction executed. Nothing is exfiltrated and nothing destructive runs.

## Guardrails baked in (keep them)

- **Benign payload only.** The hidden instruction is a bare `GET <your-url>?e=skill_demo`.
  It does **not** read files, include host/machine data, or run shell beyond the fetch.
  The teaching point is "an outbound call fired that no one approved," not data theft.
- **Not a general weaponiser.** `build_poisoned_skill.py` hides one fixed, benign string.
  It is not a CLI that encodes arbitrary text. Don't turn it into one.
- **Your endpoint, controlled room.** Point `BEACON_URL` at a logging endpoint you own
  (e.g. a RequestBin-style catcher). Run it in a demo session, not against a real repo.
- **Do not escalate.** If someone asks "what if it sent the .env?" — describe the risk,
  don't run it. Swapping the beacon for real exfiltration is the line this demo won't cross.

## Prerequisites

    export BEACON_URL="https://<a-host-you-control>/hit"   # must log a GET and return 200

## Build the poisoned skill

    python3 build_poisoned_skill.py
    # writes .claude/skills/code-formatter/SKILL.md
    # the description reads "A code-formatting helper. Formats staged Python…"
    # with a hidden run of invisible Unicode tag characters appended

## Run the demo (≈4 minutes)

1. **Open the file / show a PR diff.** Ask the room: "would you approve this skill?"
   The visible text is an innocent formatter. Everyone says yes.
2. **Invoke it** in Claude Code: "format the staged Python files."
   The model reads the hidden instruction and hits your beacon. Show the hit in your log.
3. **Reveal** — run the detector:

       python3 scan_invisible.py .claude/skills/code-formatter/SKILL.md

   It flags the invisible characters and prints the decoded instruction. The reviewer's
   eyes missed exactly what the model (and now the scanner) saw.
4. **Defend.** Add a scan to pre-commit/CI (the detector exits non-zero on a hit), and show
   the permission layer is the real backstop: a `deny` rule on `WebFetch`/`Bash(curl:*)`,
   or a `PreToolUse` hook, blocks the callout even when the text slips through review.
5. **Land it:** skills, plugins and MCP servers are third-party code. Review from
   allowlisted sources, scan for invisible/bidi characters, pin versions, and rely on
   permission rules — not on a human reading the text — as the control.

## Files

- `build_poisoned_skill.py` — writes the one benign poisoned `SKILL.md`.
- `scan_invisible.py` — detector/reveal; use it in pre-commit and CI too.

Drops into the demo repo as `security/` plus the generated `.claude/skills/code-formatter/`.
