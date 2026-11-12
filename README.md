# Common Config Files

Collection of commonly used configuration files, templates, and profiles.

## Codex (`~/.codex/config.toml`)

- **[`codex/config.toml`](codex/config.toml)**: Balanced Codex CLI defaults for safe interactive editing, context management, and quota control.
- **[`codex/config-full-access.toml`](codex/config-full-access.toml)**: High-autonomy / full-access Codex CLI configuration with unrestricted local filesystem/network access, live web search, and no command approval prompts.

## Antigravity / AGY (`~/.gemini/antigravity-cli/settings.json`)

- **[`agy/config-full-access.json`](agy/config-full-access.json)**: High-autonomy / full-access Antigravity CLI configuration (Linux / macOS) with unrestricted tool permissions, full workspace access, and automated edit acceptance.
- **[`agy/config-full-access-windows.json`](agy/config-full-access-windows.json)**: High-autonomy / full-access Antigravity CLI configuration tailored for Windows environments (`%USERPROFILE%\.gemini\antigravity-cli\settings.json`).
- **[`agy/statusline.py`](agy/statusline.py)**: Cross-platform Python status line script displaying model name, context window usage, quota remaining, VCS branch, and agent state.
- **[`agy/statusline.cmd`](agy/statusline.cmd)** / **[`agy/statusline.bat`](agy/statusline.bat)**: Windows batch wrappers to execute the statusline script seamlessly from `cmd.exe`.
- **[`agy/statusline.sh`](agy/statusline.sh)**: Shell script wrapper (Linux / macOS / Git Bash) with automatic fallback between `python` and `python3`.
