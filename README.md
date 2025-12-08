# Claude Skill Factory

A production-ready framework for generating [Claude Code Agent Skills](https://code.claude.com/docs/en/skills) at scale. Transform your domain expertise into reusable, shareable AI capabilities.

## What Are Agent Skills?

Agent Skills are modular capabilities that extend Claude's functionality. Each skill packages expertise into a discoverable format that Claude autonomously invokes when relevant to your request.

**Key benefits:**
- Reduce repetitive prompting
- Share expertise across teams via git
- Compose multiple skills for complex workflows
- Works in both Claude Code CLI and browser

## Quick Start

### 1. Generate New Skills

Provide your requirements using the mega-prompt:

```yaml
BUSINESS_DOMAIN: "E-commerce"

USE_CASES:
  - "Analyze product reviews for sentiment"
  - "Generate SEO-optimized product descriptions"
  - "Calculate conversion rate metrics"

NUM_SKILLS: 3
OVERLAP_PREFERENCE: "complementary"
COMPLEXITY_LEVEL: "intermediate"
```

Then run:
```
Use SKILL_FACTORY_PROMPT.md to generate skills for the above requirements
```

### 2. Install Generated Skills

```bash
# Personal (available in all projects)
cp -r generated_skills/my-skill ~/.claude/skills/

# Project-specific (shared via git)
cp -r generated_skills/my-skill .claude/skills/

# Browser import
# Upload the {skill-name}.zip file directly
```

## Repository Structure

```
├── SKILL_FACTORY_PROMPT.md          # Mega-prompt for skill generation
├── claude_skill_insrtuctions.md     # Official Skills documentation
├── claude_skills_examples.md/       # Reference examples
│   ├── analyzing-financial-statements.md
│   ├── applying-brand-guidelines.md
│   ├── creating-financial-models.md
│   └── *.py                         # Python helper scripts
└── generated_skills/                # Your generated skills
    └── {skill-name}/
        ├── SKILL.md                 # Main skill file (required)
        ├── sample_prompt.md         # Usage example
        ├── {skill-name}.zip         # Browser import package
        ├── *.py                     # Optional Python scripts
        └── test_data/               # Sample data for testing
```

## Skill Anatomy

Every skill requires a `SKILL.md` file with YAML frontmatter:

```yaml
---
name: my-skill-name
description: What this skill does and WHEN Claude should use it
allowed-tools: Read, Grep, Glob  # Optional tool restrictions
---

# My Skill Name

## Capabilities
- What the skill can do

## Instructions
1. Step-by-step guidance for Claude

## Examples
Concrete usage examples
```

### Frontmatter Rules

| Field | Requirements |
|-------|-------------|
| `name` | kebab-case, max 64 chars, lowercase letters/numbers/hyphens only |
| `description` | Max 1024 chars. Must explain **what** AND **when** to use |
| `allowed-tools` | Optional. Restricts which tools Claude can use |

## Example Skills Included

### Content Marketing
- **blog-post-outline-generator** - SEO-optimized blog outlines with heading structure
- **social-media-caption-writer** - Platform-specific captions with hashtags
- **content-performance-analyzer** - Metrics analysis and recommendations

### Business
- **presentation-generator** - Structured slide decks from topics
- **vacation-rental-seller** - Listing optimization for rental properties

### Education
- **kids-learning-creator** - Age-appropriate educational content in Italian

## Configuration Options

### Complexity Levels

| Level | Output |
|-------|--------|
| `basic` | SKILL.md only, simple prompts |
| `intermediate` | SKILL.md + 1-2 Python scripts |
| `advanced` | Multi-file with reference docs, validation, complex logic |

### Overlap Preferences

| Type | Description |
|------|-------------|
| `exclusive` | Each skill has distinct scope, no overlap |
| `complementary` | Skills integrate and share context |
| `hierarchical` | Base skills + advanced extensions |

## Best Practices

1. **Specific descriptions** - "Analyze Excel spreadsheets and create pivot tables" not "Helps with data"
2. **Focused scope** - One skill = one capability
3. **Minimal test data** - 5-10 rows CSV, 1-2 paragraphs text
4. **Forward slashes** - Use `scripts/helper.py` in paths, even on Windows

## Creating Browser Import ZIP

The ZIP must contain **only** SKILL.md:

```powershell
# Windows
Compress-Archive -Path "SKILL.md" -DestinationPath "my-skill.zip" -Force
```

```bash
# macOS/Linux
zip my-skill.zip SKILL.md
```

## Resources

- [Claude Code Skills Documentation](https://code.claude.com/docs/en/skills)
- [Skills Best Practices](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/best-practices)
- [Engineering Blog: Equipping Agents with Skills](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)

## License

MIT License - See [LICENSE](LICENSE) for details.

---

Built for [Claude Code](https://claude.ai/code) by Anthropic
