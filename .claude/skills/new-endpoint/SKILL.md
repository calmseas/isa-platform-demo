---
name: new-endpoint
description: Add a FastAPI endpoint to this ISA platform following house conventions. Use when asked to add, create or expose a new route or API endpoint.
---

# Add an endpoint

Follow these conventions for every new route in this repo:

1. **One router per resource** in `app/routes/<resource>.py`, created with
   `APIRouter(prefix="/<resource>", tags=["<resource>"])`.
2. **Register it** in `app/main.py` with `app.include_router(...)`.
3. **Auth**: any route that reads or changes more than the caller's own data takes
   `dependencies=[Depends(require_admin)]` from `app.auth`. Admin-wide routes put the
   dependency on the router, not the handler.
4. **Validation**: request bodies are Pydantic models in `app/models.py`. Money
   amounts are `float = Field(gt=0)`.
5. **Errors**: missing records raise `HTTPException(404)`; rule violations raise
   `HTTPException(422)` with a human-readable `detail`.
6. **Allowance rules** live in `app/isa_rules.py`, never inline in a route.
7. **Tests**: add a `tests/test_<resource>.py` covering the happy path, the auth
   failure, and one rule violation. Use the `client` and `admin_headers` fixtures.

Run `make test` before you finish and show the output.
