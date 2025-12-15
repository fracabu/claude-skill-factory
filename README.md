<h1 align="center">Claude Skill Factory</h1>
<h3 align="center">Generate Claude Code Agent Skills at scale</h3>

<p align="center">
  <em>Transform domain expertise into reusable, shareable AI capabilities</em>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Claude_Code-8B5CF6?style=flat-square&logo=anthropic&logoColor=white" alt="Claude Code" />
  <img src="https://img.shields.io/badge/Skills-Framework-blue?style=flat-square" alt="Skills" />
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python" />
</p>

<p align="center">
  :gb: <a href="#english">English</a> | :it: <a href="#italiano">Italiano</a>
</p>

---

<a name="english"></a>
## :gb: English

### Overview

A production-ready framework for generating [Claude Code Agent Skills](https://code.claude.com/docs/en/skills) at scale. Skills are modular capabilities that Claude autonomously invokes when relevant to your requests.

### Features

- **Skill Generation at Scale** - Create multiple skills from a single mega-prompt
- **Multi-Platform Support** - Works in Claude Code CLI and browser
- **Team Collaboration** - Share expertise across teams via git
- **Composable Skills** - Combine multiple skills for complex workflows
- **Browser Import** - ZIP packages ready for direct upload

### Quick Start

```yaml
# 1. Define requirements
BUSINESS_DOMAIN: "E-commerce"
USE_CASES:
  - "Analyze product reviews for sentiment"
  - "Generate SEO-optimized descriptions"
NUM_SKILLS: 3
COMPLEXITY_LEVEL: "intermediate"
```

```bash
# 2. Generate skills
Use SKILL_FACTORY_PROMPT.md to generate skills

# 3. Install
cp -r generated_skills/my-skill ~/.claude/skills/     # Personal
cp -r generated_skills/my-skill .claude/skills/       # Project
```

### Skill Anatomy

```yaml
---
name: my-skill-name
description: What this skill does and WHEN to use it
allowed-tools: Read, Grep, Glob
---

# My Skill Name

## Capabilities
- What the skill can do

## Instructions
1. Step-by-step guidance
```

### Complexity Levels

| Level | Output |
|-------|--------|
| `basic` | SKILL.md only |
| `intermediate` | SKILL.md + Python scripts |
| `advanced` | Multi-file with validation |

---

<a name="italiano"></a>
## :it: Italiano

### Panoramica

Un framework production-ready per generare [Claude Code Agent Skills](https://code.claude.com/docs/en/skills) su larga scala. Le Skills sono capacita modulari che Claude invoca autonomamente quando rilevanti.

### Funzionalita

- **Generazione Skill su Scala** - Crea multiple skill da un singolo mega-prompt
- **Supporto Multi-Piattaforma** - Funziona in Claude Code CLI e browser
- **Collaborazione Team** - Condividi competenze via git
- **Skill Componibili** - Combina skill per workflow complessi
- **Import Browser** - Pacchetti ZIP pronti per upload

### Avvio Rapido

```yaml
# 1. Definisci requisiti
BUSINESS_DOMAIN: "E-commerce"
USE_CASES:
  - "Analizza recensioni per sentiment"
  - "Genera descrizioni SEO-ottimizzate"
NUM_SKILLS: 3
COMPLEXITY_LEVEL: "intermediate"
```

```bash
# 2. Genera skill
Usa SKILL_FACTORY_PROMPT.md per generare skill

# 3. Installa
cp -r generated_skills/my-skill ~/.claude/skills/     # Personale
cp -r generated_skills/my-skill .claude/skills/       # Progetto
```

### Livelli Complessita

| Livello | Output |
|---------|--------|
| `basic` | Solo SKILL.md |
| `intermediate` | SKILL.md + script Python |
| `advanced` | Multi-file con validazione |

---

## License

MIT

---

<p align="center">
  <a href="https://github.com/fracabu">
    <img src="https://img.shields.io/badge/Made_by-fracabu-8B5CF6?style=flat-square" alt="Made by fracabu" />
  </a>
</p>
