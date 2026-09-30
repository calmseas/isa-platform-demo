"""Runtime configuration for the demo app."""
import os

# Overall ISA subscription allowance for the tax year (unchanged from 2027).
OVERALL_ALLOWANCE = 20_000.00

# Cash ISA sub-limit for under-65s, effective 6 April 2027.
# NOTE: not yet enforced in app/isa_rules.py — this is the capstone feature.
CASH_SUBLIMIT_UNDER_65 = 12_000.00

# Demo admin key. Training only; never a real secret.
ADMIN_KEY = os.environ.get("ISA_DEMO_ADMIN_KEY", "demo-admin-key")
