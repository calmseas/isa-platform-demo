# ISA platform (demo)

FastAPI service for ISA accounts, contributions and transfers. Training material.

## Commands
- Install: `make install`
- Test: `make test` (pytest)
- Run: `make run` (uvicorn on :8000)

## Conventions
- Routes live in `app/routes/<resource>.py`, one router per resource, registered in `app/main.py`.
- Allowance rules live in `app/isa_rules.py`, never inline in routes.
- Admin routes require `Depends(require_admin)` from `app/auth.py`.
- Money amounts are floats validated with Pydantic `Field(gt=0)`.
- Adding an endpoint? Use the `new-endpoint` skill.

## Notes
- This repo ships with intentional faults for a training session; see PRESENTER.md.
- No real customer data. Do not add any.
