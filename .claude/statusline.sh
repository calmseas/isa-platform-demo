#!/usr/bin/env bash
# Demo status line: shows the model and how full the context window is.
# Claude Code pipes a JSON status object on stdin (context_window.used_percentage).
input=$(cat)
python3 - "$input" <<'PY'
import json, sys
try:
    d = json.loads(sys.argv[1] or "{}")
except Exception:
    d = {}
model = d.get("model", {}).get("display_name", "claude")
pct = d.get("context_window", {}).get("used_percentage")
cwd = d.get("workspace", {}).get("current_dir", "")
folder = cwd.rsplit("/", 1)[-1] if cwd else ""
if isinstance(pct, (int, float)):
    filled = min(10, int(pct // 10))
    bar = "[" + "#" * filled + "-" * (10 - filled) + f"] {pct:.0f}% ctx"
else:
    bar = "[----------] ??% ctx"
print(f"{model}  {bar}  {folder}".rstrip())
PY
