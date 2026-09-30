# Exercises — try this before the next session

One per technique from the deck. None needs anything installed beyond this repo.

1. **Measure context.** Run `/context`. Then ask Claude to read `docs/ops-handbook.md`
   and run `/context` again. Note the jump.
2. **Hand off.** Start a change, then: ask for `HANDOFF.md`, `/clear`, and resume with
   `@HANDOFF.md`. Undo something with `Esc Esc`.
3. **Delegate.** "Use a subagent to find every allowance calculation and report
   file:line." Compare `/context` before and after.
4. **Workflow.** "Use a workflow to audit every route under app/routes for missing
   auth, then have fresh agents refute each finding." Only one real gap should survive.
5. **Skill.** Move endpoint conventions into a skill (see `.claude/skills/new-endpoint`),
   then in a fresh session ask for a new endpoint and watch it load.
6. **Plugin.** `/plugin marketplace add .` then install `isa-tools`; run `/context` to
   see the footprint; disable it.
7. **Reviewer.** Ask Claude to run the `security-reviewer` agent on your latest diff.
8. **Spec to tasks.** Take the cash-ISA sub-limit from spec → plan → tasks, one task
   per cleared window, with a `/goal` per task.

Bring what you found — which `/context` category dominated, how the handoff felt,
whether the reviewer caught the export bug — to the next session.
