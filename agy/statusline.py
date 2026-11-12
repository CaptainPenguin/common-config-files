import json, sys

try:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    d = json.load(sys.stdin)
    if not isinstance(d, dict):
        d = {}
except Exception:
    d = {}

def tokens(n):
    if n is None:
        return "?"
    try:
        n = float(n)
    except (ValueError, TypeError):
        return "?"
    if n >= 1_000_000:
        return f"{n/1_000_000:.1f}M"
    if n >= 1_000:
        return f"{n/1_000:.1f}k"
    return str(int(n) if n.is_integer() else n)

model_info = d.get("model")
if isinstance(model_info, dict):
    model = model_info.get("display_name") or model_info.get("name") or "?"
elif isinstance(model_info, str):
    model = model_info
else:
    model = "?"

ctx = d.get("context_window")
if not isinstance(ctx, dict):
    ctx = {}

used_in = ctx.get("total_input_tokens") or 0
used_out = ctx.get("total_output_tokens") or 0
try:
    used = float(used_in) + float(used_out)
except (ValueError, TypeError):
    used = 0

limit = ctx.get("context_window_size")
pct = ctx.get("used_percentage")

ctx_text = f"ctx {tokens(used)}/{tokens(limit)}"
if pct is not None:
    try:
        ctx_text += f" ({float(pct):.0f}%)"
    except (ValueError, TypeError):
        pass

quota_items = []
quota_info = d.get("quota")
if isinstance(quota_info, dict):
    for name, q in quota_info.items():
        if not isinstance(q, dict):
            continue
        remaining = q.get("remaining_fraction")
        if remaining is not None:
            try:
                quota_items.append(f"{name} {float(remaining)*100:.0f}%")
            except (ValueError, TypeError):
                pass

quota_text = "quota " + ",".join(quota_items) if quota_items else "quota ?"

vcs = d.get("vcs")
if not isinstance(vcs, dict):
    vcs = {}
branch = vcs.get("branch")
if branch and vcs.get("dirty"):
    branch = f"{branch}*"

parts = [
    f"◈ {model}",
    ctx_text,
    quota_text,
]

if branch:
    parts.append(str(branch))

tasks = d.get("task_count")
if tasks:
    parts.append(f"tasks {tasks}")

state = d.get("agent_state")
if state:
    parts.append(str(state))

print(" | ".join(parts))
