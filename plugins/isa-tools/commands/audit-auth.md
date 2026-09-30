---
description: Audit the API routes for missing authentication or data-exposure issues.
---

Review every router under `app/routes/` for authentication and authorization gaps.

For each route, state whether it is protected (by a handler dependency OR a
router-level `dependencies=[Depends(require_admin)]`) and whether it exposes
account or balance data. Remember that a router-level dependency guards every
route in that router. Report each real gap as file:line, severity, and the
smallest fix. Report gaps, not style. Do not edit files.
