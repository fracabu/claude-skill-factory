# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Purpose

A **Skill Factory** for creating Claude Code Agent Skills. Contains reference documentation, examples, and a mega-prompt for generating production-ready skills.

## How to Generate New Skills

Use `SKILL_FACTORY_PROMPT.md` - a mega-prompt that guides skill generation. Provide these variables:

```yaml
BUSINESS_DOMAIN: "your domain (Finance, Marketing, HR, etc.)"
USE_CASES:
  - "use case 1"
  - "use case 2"
NUM_SKILLS: 3
OVERLAP_PREFERENCE: "exclusive|complementary|hierarchical"
COMPLEXITY_LEVEL: "basic|intermediate|advanced"
```

Generated skills go in `generated_skills/{skill-name}/`.

## Creating ZIP Files for Browser Import

After generating a skill, create the ZIP file containing **only** SKILL.md:

```powershell
# Windows PowerShell
Compress-Archive -Path "generated_skills\my-skill\SKILL.md" -DestinationPath "generated_skills\my-skill\my-skill.zip" -Force
```

## Skill File Format

SKILL.md requires YAML frontmatter:
```yaml
---
name: kebab-case-name          # max 64 chars, lowercase letters/numbers/hyphens only
description: What + WHEN       # max 1024 chars, critical for discovery
allowed-tools: Read, Grep      # optional tool restrictions
---
```

**Critical**: The `description` must explain both what the skill does AND when Claude should use it. Vague descriptions like "Helps with documents" will not trigger properly.

## SKILL.md Content Structure

Each SKILL.md should include these sections:
1. **Capabilities** - What the skill can do
2. **Instructions** - Step-by-step guidance for Claude
3. **Input Format** - What inputs are accepted
4. **Output Format** - Expected output structure
5. **Examples** - 1-2 concrete usage examples
6. **Best Practices** - Domain-specific guidelines
7. **Limitations** - What the skill cannot do

## Generated Skill Checklist

Each generated skill must include:
- [ ] `SKILL.md` with valid YAML frontmatter (opening/closing `---`, no tabs)
- [ ] `sample_prompt.md` with copy-paste example
- [ ] `{skill-name}.zip` containing **only** SKILL.md (for browser import)
- [ ] Optional: Python scripts with type hints, test_data/ with minimal samples

## Key Conventions

- Skill names: kebab-case only (e.g., `blog-post-outline-generator`)
- Python scripts: type hints, dataclasses, `if __name__ == "__main__":` blocks
- Reference files via relative links: `[reference.md](reference.md)`
- Test data: minimal but functional (5-10 rows CSV, 1-2 paragraph TXT)
- Use forward slashes in paths within SKILL.md: `scripts/helper.py` not `scripts\helper.py`

## Installing Generated Skills

```bash
# Personal (all projects)
cp -r generated_skills/my-skill ~/.claude/skills/

# Project-specific
cp -r generated_skills/my-skill .claude/skills/

# Browser import
# Upload the {skill-name}.zip file directly
```

## Reference Documentation

- `claude_skill_insrtuctions.md` - Official Skills docs from code.claude.com
- `claude_skills_examples.md/` - Example skills (finance, branding) with Python scripts
