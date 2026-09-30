# Plan: cash ISA sub-limit

_Example / fallback._

## Approach
Add the sub-limit check to `check_contribution` in `app/isa_rules.py`, after the
overall-allowance check. Gate it on `account.age < 65` and `kind == "cash"`.

## Files touched
- `app/config.py` — reuse `CASH_SUBLIMIT_UNDER_65` (already defined).
- `app/isa_rules.py` — add the cash sub-limit branch.
- `tests/test_isa_limit.py` — new test file for the acceptance criteria.

## Risks
- Off-by-one on the age boundary (under 65 means age < 65).
- Applying the cash cap to stocks by mistake.
- Breaking the existing overall-allowance test.
