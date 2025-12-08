"""
Blog Post Outline Generator Module.
Provides structured outline generation with SEO optimization.
"""

from typing import Dict, List, Any, Optional
from dataclasses import dataclass, field
from enum import Enum


class ContentGoal(Enum):
    """Content goals for blog posts."""
    INFORM = "inform"
    CONVERT = "convert"
    ENTERTAIN = "entertain"
    EDUCATE = "educate"


class ContentLength(Enum):
    """Standard content length targets."""
    SHORT = 800
    MEDIUM = 1500
    LONG = 2500
    PILLAR = 4000


@dataclass
class Section:
    """Represents a section in the blog outline."""
    heading: str
    level: int  # 1=H1, 2=H2, 3=H3
    word_count: int
    key_points: List[str] = field(default_factory=list)
    internal_link_opportunity: Optional[str] = None
    cta: Optional[str] = None


@dataclass
class BlogOutline:
    """Complete blog post outline structure."""
    title: str
    primary_keyword: str
    target_audience: str
    total_word_count: int
    reading_time_minutes: int
    sections: List[Section] = field(default_factory=list)
    meta_description: str = ""
    secondary_keywords: List[str] = field(default_factory=list)


class OutlineGenerator:
    """Generate structured blog post outlines."""

    # Section templates by content goal
    SECTION_TEMPLATES = {
        ContentGoal.INFORM: [
            "What is {topic}",
            "Why {topic} Matters",
            "Key Facts About {topic}",
            "Common Misconceptions",
            "Expert Insights",
        ],
        ContentGoal.EDUCATE: [
            "Understanding {topic}",
            "Step-by-Step Guide",
            "Best Practices",
            "Common Mistakes to Avoid",
            "Tools and Resources",
        ],
        ContentGoal.CONVERT: [
            "The Problem with {topic}",
            "Why Traditional Solutions Fail",
            "A Better Approach",
            "How It Works",
            "Getting Started",
        ],
        ContentGoal.ENTERTAIN: [
            "The Surprising Truth About {topic}",
            "What Nobody Tells You",
            "Real Stories",
            "The Fun Side",
            "What's Next",
        ],
    }

    def __init__(self):
        """Initialize the outline generator."""
        self.outline: Optional[BlogOutline] = None

    def calculate_reading_time(self, word_count: int) -> int:
        """Calculate estimated reading time in minutes."""
        words_per_minute = 200
        return max(1, round(word_count / words_per_minute))

    def distribute_word_count(
        self, total_words: int, num_sections: int
    ) -> Dict[str, int]:
        """Distribute word count across sections."""
        intro_words = int(total_words * 0.10)  # 10% for intro
        conclusion_words = int(total_words * 0.10)  # 10% for conclusion
        body_words = total_words - intro_words - conclusion_words
        section_words = body_words // num_sections

        return {
            "introduction": intro_words,
            "section": section_words,
            "conclusion": conclusion_words,
        }

    def generate_section_headings(
        self, topic: str, goal: ContentGoal, num_sections: int = 5
    ) -> List[str]:
        """Generate section headings based on topic and goal."""
        templates = self.SECTION_TEMPLATES.get(goal, self.SECTION_TEMPLATES[ContentGoal.INFORM])
        headings = [t.format(topic=topic) for t in templates[:num_sections]]
        return headings

    def create_outline(
        self,
        topic: str,
        target_audience: str,
        primary_keyword: str,
        word_count: int = 1500,
        goal: ContentGoal = ContentGoal.EDUCATE,
    ) -> BlogOutline:
        """
        Create a complete blog post outline.

        Args:
            topic: Main subject of the blog post
            target_audience: Intended readers
            primary_keyword: Main SEO keyword
            word_count: Target word count
            goal: Content goal (inform, educate, convert, entertain)

        Returns:
            Complete BlogOutline object
        """
        # Determine number of sections based on length
        if word_count <= 800:
            num_body_sections = 3
        elif word_count <= 1500:
            num_body_sections = 5
        elif word_count <= 2500:
            num_body_sections = 7
        else:
            num_body_sections = 9

        # Distribute word counts
        distribution = self.distribute_word_count(word_count, num_body_sections)

        # Generate sections
        sections = []

        # Introduction
        sections.append(Section(
            heading="Introduction",
            level=2,
            word_count=distribution["introduction"],
            key_points=[
                f"Hook: Start with compelling statistic or question about {topic}",
                f"Context: Why {target_audience} should care",
                "Promise: What the reader will learn/gain",
            ],
        ))

        # Body sections
        headings = self.generate_section_headings(topic, goal, num_body_sections)
        for i, heading in enumerate(headings):
            section = Section(
                heading=heading,
                level=2,
                word_count=distribution["section"],
                key_points=[
                    "Main concept explanation",
                    "Supporting evidence or example",
                    "Practical application or tip",
                ],
            )
            if i == 1:  # Add internal link to second section
                section.internal_link_opportunity = f"Link to related content about {topic}"
            if i == len(headings) - 1:  # Add CTA to last body section
                section.cta = "Soft CTA encouraging engagement"
            sections.append(section)

        # Conclusion
        sections.append(Section(
            heading="Conclusion",
            level=2,
            word_count=distribution["conclusion"],
            key_points=[
                "Summarize 3 key takeaways",
                "Reinforce main benefit for reader",
                "Clear call-to-action",
            ],
            cta="Primary CTA (subscribe, download, contact)",
        ))

        # Create outline
        self.outline = BlogOutline(
            title=f"{primary_keyword.title()}: Complete Guide for {target_audience}",
            primary_keyword=primary_keyword,
            target_audience=target_audience,
            total_word_count=word_count,
            reading_time_minutes=self.calculate_reading_time(word_count),
            sections=sections,
            meta_description=f"Discover everything about {topic} in this comprehensive guide. "
                           f"Learn key strategies and tips for {target_audience}.",
            secondary_keywords=[
                f"{primary_keyword} tips",
                f"{primary_keyword} guide",
                f"best {primary_keyword}",
                f"how to {primary_keyword}",
            ],
        )

        return self.outline

    def to_markdown(self) -> str:
        """Convert outline to markdown format."""
        if not self.outline:
            return "No outline generated yet."

        lines = [
            f"# {self.outline.title}",
            "",
            f"**Target Length**: {self.outline.total_word_count} words | "
            f"**Reading Time**: {self.outline.reading_time_minutes} min | "
            f"**Keyword**: {self.outline.primary_keyword}",
            "",
            f"**Target Audience**: {self.outline.target_audience}",
            "",
            "---",
            "",
        ]

        for section in self.outline.sections:
            prefix = "#" * (section.level + 1)
            lines.append(f"{prefix} {section.heading} ({section.word_count} words)")
            lines.append("")

            for point in section.key_points:
                lines.append(f"- {point}")

            if section.internal_link_opportunity:
                lines.append(f"- 🔗 {section.internal_link_opportunity}")

            if section.cta:
                lines.append(f"- 📣 CTA: {section.cta}")

            lines.append("")

        # SEO Notes
        lines.extend([
            "---",
            "",
            "## SEO Notes",
            "",
            f"**Meta Description**: {self.outline.meta_description}",
            "",
            "**Secondary Keywords**:",
        ])

        for kw in self.outline.secondary_keywords:
            lines.append(f"- {kw}")

        return "\n".join(lines)


# Example usage
if __name__ == "__main__":
    generator = OutlineGenerator()

    outline = generator.create_outline(
        topic="Remote Work Productivity",
        target_audience="Corporate professionals",
        primary_keyword="remote work productivity tips",
        word_count=1500,
        goal=ContentGoal.EDUCATE,
    )

    print(generator.to_markdown())
