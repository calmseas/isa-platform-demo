# Specs

Spec-driven development artefacts live here, one folder per feature.

- `cash-isa-limit/` — the capstone feature for the session. On a fresh checkout the
  `*.example.md` files are a fallback you can fall back to if a live demo step
  stalls; the point of the demo is to generate `spec.md`, `plan.md` and `tasks.md`
  yourself with Claude.
- `plans/` — where Claude Code writes plan files (`plansDirectory` in
  `.claude/settings.json`), so approved plans land in the repo rather than in your
  home directory.

A working reference implementation of the capstone is on the branch
`demo/capstone-solution`.
