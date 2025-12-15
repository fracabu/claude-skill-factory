# Claude Skill Factory

**Production-ready framework for generating Claude Code Agent Skills at scale**

[English](#english) | [Italiano](#italiano)

---

## English

### Overview

A production-ready framework for generating [Claude Code Agent Skills](https://code.claude.com/docs/en/skills) at scale. Transform your domain expertise into reusable, shareable AI capabilities that Claude autonomously invokes when relevant to your requests.

### Key Features

- **Skill Generation at Scale** - Create multiple skills from a single mega-prompt
- **Multi-Platform Support** - Works in both Claude Code CLI and browser
- **Team Collaboration** - Share expertise across teams via git
- **Composable Skills** - Combine multiple skills for complex workflows
- **Browser Import** - ZIP packages ready for direct browser upload

### What Are Agent Skills?

Agent Skills are modular capabilities that extend Claude's functionality. Each skill packages expertise into a discoverable format that Claude autonomously invokes when relevant.

**Benefits:**
- Reduce repetitive prompting
- Share expertise across teams via git
- Compose multiple skills for complex workflows

### Tech Stack

- **Claude Code** - AI agent runtime
- **YAML Frontmatter** - Skill metadata specification
- **Python** - Optional helper scripts
- **ZIP Packaging** - Browser import format

### Quick Start

```yaml
# 1. Define your requirements
BUSINESS_DOMAIN: "E-commerce"

USE_CASES:
  - "Analyze product reviews for sentiment"
  - "Generate SEO-optimized product descriptions"
  - "Calculate conversion rate metrics"

NUM_SKILLS: 3
OVERLAP_PREFERENCE: "complementary"
COMPLEXITY_LEVEL: "intermediate"
```

```bash
# 2. Generate skills
Use SKILL_FACTORY_PROMPT.md to generate skills for the above requirements

# 3. Install generated skills
# Personal (available in all projects)
cp -r generated_skills/my-skill ~/.claude/skills/

# Project-specific (shared via git)
cp -r generated_skills/my-skill .claude/skills/
```

### Skill Anatomy

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
```

| Field | Requirements |
|-------|-------------|
| `name` | kebab-case, max 64 chars, lowercase letters/numbers/hyphens only |
| `description` | Max 1024 chars. Must explain **what** AND **when** to use |
| `allowed-tools` | Optional. Restricts which tools Claude can use |

### Complexity Levels

| Level | Output |
|-------|--------|
| `basic` | SKILL.md only, simple prompts |
| `intermediate` | SKILL.md + 1-2 Python scripts |
| `advanced` | Multi-file with reference docs, validation, complex logic |

### Example Skills Included

- **blog-post-outline-generator** - SEO-optimized blog outlines
- **social-media-caption-writer** - Platform-specific captions
- **presentation-generator** - Structured slide decks
- **vacation-rental-seller** - Listing optimization
- **kids-learning-creator** - Age-appropriate educational content

### Project Structure

```
claude-skill-factory/
├── SKILL_FACTORY_PROMPT.md
├── claude_skill_instructions.md
├── claude_skills_examples.md/
│   ├── analyzing-financial-statements.md
│   ├── applying-brand-guidelines.md
│   └── *.py
└── generated_skills/
    └── {skill-name}/
        ├── SKILL.md
        ├── sample_prompt.md
        └── {skill-name}.zip
```

### License

MIT License

---

## Italiano

### Panoramica

Un framework production-ready per generare [Claude Code Agent Skills](https://code.claude.com/docs/en/skills) su larga scala. Trasforma la tua competenza di dominio in capacita AI riutilizzabili e condivisibili che Claude invoca autonomamente quando rilevanti per le tue richieste.

### Funzionalita Principali

- **Generazione Skill su Scala** - Crea multiple skill da un singolo mega-prompt
- **Supporto Multi-Piattaforma** - Funziona sia in Claude Code CLI che nel browser
- **Collaborazione Team** - Condividi competenze tra team via git
- **Skill Componibili** - Combina multiple skill per workflow complessi
- **Import Browser** - Pacchetti ZIP pronti per upload diretto nel browser

### Cosa Sono le Agent Skills?

Le Agent Skills sono capacita modulari che estendono le funzionalita di Claude. Ogni skill impacchetta competenze in un formato scopribile che Claude invoca autonomamente quando rilevante.

**Benefici:**
- Riduci i prompt ripetitivi
- Condividi competenze tra team via git
- Componi multiple skill per workflow complessi

### Stack Tecnologico

- **Claude Code** - Runtime agenti AI
- **YAML Frontmatter** - Specifica metadati skill
- **Python** - Script helper opzionali
- **ZIP Packaging** - Formato import browser

### Avvio Rapido

```yaml
# 1. Definisci i requisiti
BUSINESS_DOMAIN: "E-commerce"

USE_CASES:
  - "Analizza recensioni prodotti per sentiment"
  - "Genera descrizioni prodotto SEO-ottimizzate"
  - "Calcola metriche tasso di conversione"

NUM_SKILLS: 3
OVERLAP_PREFERENCE: "complementary"
COMPLEXITY_LEVEL: "intermediate"
```

```bash
# 2. Genera le skill
Usa SKILL_FACTORY_PROMPT.md per generare skill per i requisiti sopra

# 3. Installa le skill generate
# Personali (disponibili in tutti i progetti)
cp -r generated_skills/my-skill ~/.claude/skills/

# Specifiche progetto (condivise via git)
cp -r generated_skills/my-skill .claude/skills/
```

### Anatomia di una Skill

Ogni skill richiede un file `SKILL.md` con frontmatter YAML:

```yaml
---
name: my-skill-name
description: Cosa fa questa skill e QUANDO Claude dovrebbe usarla
allowed-tools: Read, Grep, Glob  # Restrizioni tool opzionali
---

# Nome Skill

## Capacita
- Cosa puo fare la skill

## Istruzioni
1. Guida passo-passo per Claude
```

| Campo | Requisiti |
|-------|-----------|
| `name` | kebab-case, max 64 caratteri, solo lettere minuscole/numeri/trattini |
| `description` | Max 1024 caratteri. Deve spiegare **cosa** E **quando** usare |
| `allowed-tools` | Opzionale. Limita quali tool Claude puo usare |

### Livelli di Complessita

| Livello | Output |
|---------|--------|
| `basic` | Solo SKILL.md, prompt semplici |
| `intermediate` | SKILL.md + 1-2 script Python |
| `advanced` | Multi-file con docs di riferimento, validazione, logica complessa |

### Skill di Esempio Incluse

- **blog-post-outline-generator** - Outline blog SEO-ottimizzati
- **social-media-caption-writer** - Caption specifiche per piattaforma
- **presentation-generator** - Slide deck strutturati
- **vacation-rental-seller** - Ottimizzazione annunci
- **kids-learning-creator** - Contenuti educativi per eta

### Struttura Progetto

```
claude-skill-factory/
├── SKILL_FACTORY_PROMPT.md
├── claude_skill_instructions.md
├── claude_skills_examples.md/
│   ├── analyzing-financial-statements.md
│   ├── applying-brand-guidelines.md
│   └── *.py
└── generated_skills/
    └── {skill-name}/
        ├── SKILL.md
        ├── sample_prompt.md
        └── {skill-name}.zip
```

### Licenza

MIT License
