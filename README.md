# Codex Skills

Reusable Codex skills for strategy, analytics, and project-based work.

These skills are packaged as folder-based Codex skills so teammates can clone this repo and copy the folders they want into their local Codex skills directory.

## Included Skills

| Skill | Slug | Folder |
|-------|------|--------|
| Strategy Project | `strategy-project` | [`strategy-project/`](strategy-project/) |
| Spreadsheet | `spreadsheet` | [`spreadsheet/`](spreadsheet/) |
| Analyze | `analyze` | [`analyze/`](analyze/) |
| Build Dashboard | `build-dashboard` | [`build-dashboard/`](build-dashboard/) |
| Create Viz | `create-viz` | [`create-viz/`](create-viz/) |
| Data Visualization | `data-visualization` | [`data-visualization/`](data-visualization/) |
| Data Context Extractor | `data-context-extractor` | [`data-context-extractor/`](data-context-extractor/) |
| Explore Data | `explore-data` | [`explore-data/`](explore-data/) |
| Statistical Analysis | `statistical-analysis` | [`statistical-analysis/`](statistical-analysis/) |
| Validate Data | `validate-data` | [`validate-data/`](validate-data/) |

## Install In Codex Desktop

1. Clone or download this repo.
2. Copy the skill folders you want into your Codex skills directory.
3. Restart Codex Desktop.

On Windows, the target directory is usually:

```text
C:\Users\<your-user>\.codex\skills
```

If `CODEX_HOME` is set, use:

```text
%CODEX_HOME%\skills
```

Example PowerShell install:

```powershell
git clone https://github.com/kongaharsha/claude-skills.git
Copy-Item .\claude-skills\strategy-project "$HOME\.codex\skills\" -Recurse
Copy-Item .\claude-skills\spreadsheet "$HOME\.codex\skills\" -Recurse
```

To install everything in this repo:

```powershell
git clone https://github.com/kongaharsha/claude-skills.git
@(
  'strategy-project',
  'spreadsheet',
  'analyze',
  'build-dashboard',
  'create-viz',
  'data-visualization',
  'data-context-extractor',
  'explore-data',
  'statistical-analysis',
  'validate-data'
) | ForEach-Object {
  Copy-Item ".\claude-skills\$_" "$HOME\.codex\skills\" -Recurse
}
```

## Notes

- Each skill should end up as `...\skills\<slug>\SKILL.md`.
- If a folder already exists locally, copying may overwrite that skill.
- A full Codex Desktop restart is usually required before new skills appear.
