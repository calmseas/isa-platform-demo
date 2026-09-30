# Tasks: cash ISA sub-limit

_Example / fallback. One task per cleared window._

1. Write `tests/test_isa_limit.py` covering acceptance criteria 1–3.
   Check: the new tests exist and fail for the right reason (sub-limit not enforced).
2. Add the cash sub-limit branch to `check_contribution` in `app/isa_rules.py`.
   Check: `pytest tests/test_isa_limit.py` passes.
3. Run the full suite and confirm nothing else broke.
   Check: `make test` is green (after the separate /goal fee fix, if done).
