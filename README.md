# AI Skills For Claude And Codex

These are reusable skills for strategy, analytics, and project-based work.

The goal is simple: make Claude Code and Codex feel less like blank chat windows and more like sharp working partners with repeatable workflows. The skills here cover project setup, structured analysis, dashboard creation, visualization, spreadsheet work, and analytical QA.

They are built as folder-based skills so you can install only what you want, share them with teammates, and keep using the same workflows across both hosts.

## Why this exists

Most people are not blocked by model quality anymore. They are blocked by starting from scratch every session.

The difference between a helpful AI and a genuinely useful one is usually workflow:

- a strong starting prompt
- durable context
- a clear sequence of steps
- repeatable review habits
- examples that show the model how to behave

That is what this repo is for.

## What’s in here

| Skill | Slug | What it does |
|-------|------|--------------|
| Strategy Project | `strategy-project` | Sets up an AI-native project workspace with context files, workstreams, and session discipline |
| Spreadsheet | `spreadsheet` | Creates, edits, and analyzes spreadsheets |
| Analyze | `analyze` | Answers end-to-end data questions |
| Build Dashboard | `build-dashboard` | Creates interactive HTML dashboards |
| Create Viz | `create-viz` | Builds publication-quality charts |
| Data Visualization | `data-visualization` | Helps choose and design the right chart |
| Data Context Extractor | `data-context-extractor` | Builds company-specific data-analysis context |
| Explore Data | `explore-data` | Profiles a new dataset or table |
| Statistical Analysis | `statistical-analysis` | Applies practical statistical methods |
| Validate Data | `validate-data` | QA pass for an analysis before sharing |

## Quick start

1. Clone or download this repo.
2. Copy the skill folders you want into your host’s skills directory.
3. Restart the host.

## Install

### Codex

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

To install the full recommended pack:

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

### Claude Code

This repo is packaged and tested primarily as a Codex skill pack today. Claude compatibility is a supported design goal, but it should be treated as a reference install path unless a given skill is explicitly validated in Claude.

In practice:

- `strategy-project` is the clearest dual-host example because the workflow is mostly host-agnostic and the instruction-file difference is documented
- the analytics skills are still distributed from the same shared folders, but this repo does not yet claim full Claude-specific validation parity for every skill
- if you use Claude, prefer starting with `strategy-project` and then expand from there as you validate the others in your environment

Typical Claude location:

```text
~/.claude/skills
```

Example install:

```bash
git clone https://github.com/kongaharsha/claude-skills.git
cp -r claude-skills/strategy-project ~/.claude/skills/strategy-project
cp -r claude-skills/spreadsheet ~/.claude/skills/spreadsheet
```

If you are adopting these in Claude for a team, validate the specific skills you care about first instead of assuming the whole pack is production-ready for Claude just because it is installable as folders.

## Claude vs Codex

The repo is meant to work for both hosts, but there is one important convention difference:

- Codex uses `AGENTS.md`
- Claude uses `CLAUDE.md`

The `strategy-project` skill defaults to `AGENTS.md` because Codex is the primary packaging target in this repo, but the workflow is intentionally host-agnostic. If you are using Claude, the same structure can be adapted to `CLAUDE.md` instead.

That is why keeping both example files around is useful:

- [AGENTS example](strategy-project/examples/agents-md.md)
- [CLAUDE example](strategy-project/examples/claude-md.md)

## Best entry point

If you only try one skill first, start with [`strategy-project/`](strategy-project/).

It is the clearest example of the overall philosophy in this repo:

- durable context over blank starts
- small, maintained markdown files over giant notes
- explicit workstreams over vague project memory
- chat-first collaboration before artifact generation

Once that pattern clicks, the analytics skills become much more useful because they are operating inside a cleaner working system.

## How to share with teammates

The easiest way to share these skills internally is:

1. Keep this repo as the source of truth.
2. Ask teammates to copy the skill folders they want into their local host skills directory.
3. Restart Claude or Codex.

If you want a one-step distribution flow for teammates, package the selected skill folders into a zip or a separate bundle repo and keep the folder names unchanged.

## Notes

- Each installed skill should end up as `.../skills/<slug>/SKILL.md`.
- If a folder already exists locally, copying may overwrite that skill.
- A full restart is usually required before new skills appear.
- Some skills are self-contained; others, like `strategy-project`, depend on sibling reference files and examples, so share the whole folder rather than only `SKILL.md`.

## Contributing

These are patterns, not sacred artifacts. If you find a better workflow, a missing skill, a clearer example, or a cleaner host-compatibility pattern, open a PR.
