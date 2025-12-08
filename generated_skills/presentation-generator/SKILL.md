---
name: presentation-generator
description: Creates complete PowerPoint presentations from a topic or brief. Generates slide structure, compelling content, speaker notes, and image suggestions/prompts. Use when you need to create business presentations, pitch decks, educational slides, or any visual presentation quickly.
---

# Presentation Generator

Transform any topic into a professional, visually compelling presentation with structured content, speaker notes, and image recommendations.

## Capabilities

- Generate complete presentation structure (10-20 slides)
- Write compelling headlines and bullet points
- Create detailed speaker notes for each slide
- Suggest images with AI generation prompts (DALL-E, Midjourney)
- Recommend stock photo search terms
- Apply consistent visual themes
- Export to PowerPoint (.pptx) via Python script
- Support multiple presentation styles

## Presentation Types Supported

| Type | Slides | Focus | Best For |
|------|--------|-------|----------|
| **Pitch Deck** | 10-12 | Problem → Solution → Traction | Investors, stakeholders |
| **Business Report** | 15-20 | Data, insights, recommendations | Quarterly reviews |
| **Educational** | 12-15 | Concepts, examples, exercises | Training, workshops |
| **Sales Presentation** | 8-12 | Benefits, proof, CTA | Client meetings |
| **Keynote** | 15-25 | Story, vision, inspiration | Conferences |
| **Project Update** | 8-10 | Status, milestones, next steps | Team meetings |

## Instructions

### Step 1: Gather Information
Collect from user:
- **Topic/Title**: Main subject of presentation
- **Audience**: Who will view this?
- **Goal**: Inform, persuade, educate, inspire?
- **Duration**: How long is the presentation?
- **Style**: Formal, casual, creative, minimal?
- **Slides count**: Approximate number needed

### Step 2: Generate Structure
Create outline with:
1. Title slide
2. Agenda/Overview
3. Core content sections (3-5 main sections)
4. Supporting slides per section
5. Summary/Key takeaways
6. Call to action / Next steps
7. Q&A / Contact slide

### Step 3: Write Content
For each slide provide:
- **Headline**: Compelling, action-oriented title (max 8 words)
- **Body**: 3-5 bullet points OR single powerful statement
- **Speaker Notes**: What to say (2-3 paragraphs)
- **Visual Direction**: Image description or data viz suggestion

### Step 4: Image Recommendations
For each slide suggest ONE of:
- **AI Image Prompt**: Ready for DALL-E/Midjourney
- **Stock Photo Keywords**: For Unsplash/Pexels/Shutterstock
- **Icon Suggestion**: For minimal/corporate style
- **Chart/Graph Type**: For data slides

## Input Format

```yaml
topic: "Your presentation topic"
audience: "Who will watch"
goal: "inform | persuade | educate | inspire"
duration: "10 min | 20 min | 30 min | 45 min"
style: "corporate | creative | minimal | bold"
slides: 12  # approximate
key_points:  # optional
  - "Point you must include"
  - "Another important point"
brand_colors:  # optional
  primary: "#0066CC"
  secondary: "#003366"
```

## Output Format

```markdown
# [Presentation Title]

**Audience**: [target] | **Duration**: [time] | **Slides**: [count]

---

## Slide 1: Title Slide
**Type**: Title

### Content
# [Main Title]
## [Subtitle]
[Presenter Name] | [Date]

### Visual Direction
🎨 **Background**: [description]
📸 **Image Prompt**: "[DALL-E/Midjourney prompt]"

### Speaker Notes
[What to say when this slide appears]

---

## Slide 2: [Slide Title]
**Type**: Content | Data | Quote | Image | Section Divider

### Content
**Headline**: [Compelling headline]
- Bullet point 1
- Bullet point 2
- Bullet point 3

### Visual Direction
📸 **Stock Search**: "[keywords for stock photo]"
OR
🎨 **AI Prompt**: "[detailed image generation prompt]"
OR
📊 **Chart**: [Bar chart showing X vs Y]

### Speaker Notes
[Detailed talking points - 2-3 paragraphs]

---
[Continue for all slides...]
```

## Example Usage

**Input**:
```yaml
topic: "Introduction to Artificial Intelligence for Business Leaders"
audience: "C-suite executives with limited technical background"
goal: "educate"
duration: "20 min"
style: "corporate"
slides: 12
```

**Output**: Complete 12-slide presentation with:
- Title slide with professional AI visual
- "Why AI Matters Now" with business impact data
- "AI Basics Explained Simply" with clear analogies
- "Real Business Applications" with case studies
- "Getting Started" with actionable steps
- Each slide includes speaker notes and image suggestions

## Slide Design Principles

### Headlines
- ✅ "AI Reduces Costs by 40%" (specific, impactful)
- ❌ "Cost Reduction" (vague, boring)

### Bullet Points
- Maximum 5 per slide
- Start with action verbs
- Keep under 10 words each
- One idea per bullet

### Visual Balance
- 60% visual / 40% text for engagement
- One key message per slide
- Consistent alignment and spacing

## Image Prompt Best Practices

### For AI Generation (DALL-E/Midjourney)
```
"Professional [subject], [style] style, [color scheme],
[composition], high quality, presentation slide background"
```

**Example**:
```
"Professional team collaboration in modern office, corporate style,
blue and white color scheme, wide angle, high quality, clean background
suitable for presentation slide"
```

### For Stock Photos
Use 3-5 keywords: `"business team collaboration meeting modern"`

## Python Export

The accompanying `presentation_builder.py` script can:
1. Parse the markdown output
2. Generate `.pptx` file using python-pptx
3. Apply consistent styling
4. Insert placeholder images (replace with your own)

```bash
pip install python-pptx Pillow requests
python presentation_builder.py output.md --style corporate
```

## Limitations

- Cannot generate actual images (provides prompts instead)
- Stock photo suggestions require manual download
- Complex animations not supported
- Custom fonts require manual setup
- Charts are described, not generated (use Excel/Python separately)

## Tips for Best Results

1. **Be specific about audience**: "Marketing managers at tech startups" > "Business people"
2. **Include key points**: Mention must-have content upfront
3. **Specify data**: If you have stats, include them in the request
4. **Brand guidelines**: Share colors and tone preferences
5. **Examples**: Reference presentations you like
