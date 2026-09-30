# Spec: cash ISA sub-limit for under-65s

_Example / fallback. In the demo, generate this with Claude by interview._

## Why
From 6 April 2027 the cash ISA subscription limit falls to £12,000 for holders
under 65, inside the unchanged £20,000 overall ISA allowance. The platform must
reject cash contributions that would breach the sub-limit.

## Scope
- Enforce the £12,000 cash sub-limit in `app/isa_rules.py`.
- Applies to holders **under 65**. Holders 65 and over keep the full £20,000 in cash.
- The overall £20,000 allowance still applies to everyone.

## Out of scope
- Stocks & shares limits beyond the overall allowance.
- Lifetime ISA and Junior ISA rules.
- Back-dating or the anti-circumvention rules; this is the sub-limit only.

## Acceptance criteria
1. WHEN a holder under 65 makes a cash contribution that would take their cash
   subscription above £12,000, THE SYSTEM SHALL reject it with HTTP 422 and a
   message naming the cash sub-limit.
2. WHEN a holder aged 65 or over makes a cash contribution within the £20,000
   overall allowance, THE SYSTEM SHALL accept it even above £12,000 cash.
3. WHEN any holder makes a contribution that would breach the £20,000 overall
   allowance, THE SYSTEM SHALL reject it (unchanged behaviour).
4. All existing tests continue to pass.

## Verification
`pytest tests/test_isa_limit.py` passes, plus the full suite is green.
