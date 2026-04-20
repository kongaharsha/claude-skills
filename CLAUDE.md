# claude-skills development

## Purpose

This repo is a shared skill library for Claude Code and Codex, focused on strategy, analytics, and project-based work.

When working in this repo:

- treat it as a distribution repo for reusable skills
- preserve folder-based skill packaging
- keep host compatibility in mind for both Claude and Codex
- optimize for clarity of installation, examples, and teammate adoption

## What matters most

1. Every skill folder should remain installable as `.../skills/<slug>/SKILL.md`
2. Do not break sibling-file dependencies inside a skill
3. Prefer sharing whole skill folders, not single-file fragments, when a skill depends on examples, references, scripts, or instructions
4. Keep README guidance aligned with the real install flow
5. Keep Claude and Codex compatibility explicit when the workflow differs

## Repo conventions

- Root `README.md` is the product-style landing page for the repo
- Each skill folder should contain its own `SKILL.md`
- If a skill needs support files, keep them adjacent inside that skill folder
- Example project instruction files belong under the relevant skill's `examples/` folder
- Root `AGENTS.md` and `CLAUDE.md` are for contributors working on this repo, not for end-user installation

## Compatibility rules

- Codex convention uses `AGENTS.md`
- Claude convention uses `CLAUDE.md`
- If a skill defaults to one host's convention, document the equivalent for the other host
- Do not imply that `SKILL.md` alone is enough when the skill requires sibling files

## Before changing docs

Check that:

- install steps only copy actual skill folders
- paths are accurate for the host being described
- examples and references mentioned in docs actually exist
- the README does not promise automatic discovery unless the skills are copied into the host skills directory

## Before changing skills

Check that:

- frontmatter still makes sense
- any referenced paths still exist
- example files match the documented behavior
- host-specific wording is intentional, not accidental

## Editing guidance

- Prefer small, high-signal documentation
- Preserve the repo's role as a reusable library, not a one-off project
- When adding new skills, update the root README table and install guidance if needed
- When changing `strategy-project`, keep both Claude and Codex reference examples up to date

## Good contributor behavior

- Explain packaging and compatibility clearly
- Avoid unnecessary churn in copied skill files
- Keep the repo friendly to teammates who will install by copying folders
- If something is only an example, label it as an example
