"""
Social Media Caption Generator Module.
Creates platform-optimized captions with hashtags and CTAs.
"""

from typing import Dict, List, Optional
from dataclasses import dataclass, field
from enum import Enum
import random


class Platform(Enum):
    """Supported social media platforms."""
    INSTAGRAM = "instagram"
    LINKEDIN = "linkedin"
    TWITTER = "twitter"
    FACEBOOK = "facebook"
    TIKTOK = "tiktok"


class Tone(Enum):
    """Caption tone options."""
    PROFESSIONAL = "professional"
    CASUAL = "casual"
    PLAYFUL = "playful"
    INSPIRATIONAL = "inspirational"
    EDUCATIONAL = "educational"


class Goal(Enum):
    """Content goals."""
    ENGAGEMENT = "engagement"
    TRAFFIC = "traffic"
    AWARENESS = "awareness"
    CONVERSION = "conversion"


@dataclass
class PlatformConfig:
    """Platform-specific configuration."""
    max_length: int
    hashtag_count: tuple  # (min, max)
    emoji_friendly: bool
    line_breaks: bool
    best_times: List[str]


@dataclass
class Caption:
    """Generated caption structure."""
    platform: Platform
    text: str
    hashtags: List[str]
    cta: str
    character_count: int
    best_posting_time: str


class CaptionGenerator:
    """Generate social media captions for multiple platforms."""

    PLATFORM_CONFIGS = {
        Platform.INSTAGRAM: PlatformConfig(
            max_length=2200,
            hashtag_count=(5, 15),
            emoji_friendly=True,
            line_breaks=True,
            best_times=["Tuesday 11am-1pm", "Thursday 11am-1pm", "Wednesday 7pm"],
        ),
        Platform.LINKEDIN: PlatformConfig(
            max_length=3000,
            hashtag_count=(3, 5),
            emoji_friendly=False,
            line_breaks=True,
            best_times=["Tuesday 10am-12pm", "Wednesday 10am-12pm", "Thursday 9am"],
        ),
        Platform.TWITTER: PlatformConfig(
            max_length=280,
            hashtag_count=(1, 2),
            emoji_friendly=True,
            line_breaks=False,
            best_times=["Monday-Friday 8am-10am", "Lunch hours 12pm-1pm"],
        ),
        Platform.FACEBOOK: PlatformConfig(
            max_length=500,  # Recommended, not max
            hashtag_count=(1, 3),
            emoji_friendly=True,
            line_breaks=True,
            best_times=["Wednesday 11am", "Friday 10am-11am"],
        ),
        Platform.TIKTOK: PlatformConfig(
            max_length=2200,
            hashtag_count=(3, 5),
            emoji_friendly=True,
            line_breaks=False,
            best_times=["Tuesday 9am", "Thursday 12pm", "Friday 5pm"],
        ),
    }

    # CTA templates by goal
    CTA_TEMPLATES = {
        Goal.ENGAGEMENT: [
            "What do you think? 👇",
            "Drop a comment below!",
            "Tag someone who needs this",
            "Double tap if you agree!",
            "Share your thoughts",
        ],
        Goal.TRAFFIC: [
            "Link in bio",
            "Click the link to learn more",
            "Swipe up for details",
            "Visit our website",
            "Read the full story →",
        ],
        Goal.AWARENESS: [
            "Follow for more",
            "Share with your network",
            "Save this for later",
            "Turn on notifications 🔔",
            "Stay tuned for more",
        ],
        Goal.CONVERSION: [
            "Shop now - link in bio",
            "Limited time offer!",
            "Get yours today",
            "Sign up now",
            "Book your spot",
        ],
    }

    # Hashtag suggestions by category
    HASHTAG_POOLS = {
        "business": ["entrepreneur", "business", "success", "motivation", "mindset"],
        "marketing": ["marketing", "digitalmarketing", "socialmedia", "branding", "contentmarketing"],
        "tech": ["technology", "innovation", "startup", "tech", "digital"],
        "lifestyle": ["lifestyle", "inspiration", "goals", "life", "daily"],
        "education": ["learning", "education", "tips", "howto", "guide"],
    }

    def __init__(self):
        """Initialize caption generator."""
        self.generated_captions: List[Caption] = []

    def get_hashtags(
        self, platform: Platform, category: str, custom: Optional[List[str]] = None
    ) -> List[str]:
        """Generate appropriate hashtags for platform."""
        config = self.PLATFORM_CONFIGS[platform]
        min_tags, max_tags = config.hashtag_count

        pool = self.HASHTAG_POOLS.get(category, self.HASHTAG_POOLS["business"])
        selected = random.sample(pool, min(len(pool), max_tags))

        if custom:
            selected = custom[:max_tags] + selected[: max_tags - len(custom)]

        return [f"#{tag}" for tag in selected[:max_tags]]

    def get_cta(self, goal: Goal) -> str:
        """Get appropriate CTA for goal."""
        templates = self.CTA_TEMPLATES.get(goal, self.CTA_TEMPLATES[Goal.ENGAGEMENT])
        return random.choice(templates)

    def format_caption(
        self, text: str, platform: Platform, add_line_breaks: bool = True
    ) -> str:
        """Format caption according to platform best practices."""
        config = self.PLATFORM_CONFIGS[platform]

        # Truncate if needed
        if len(text) > config.max_length:
            text = text[: config.max_length - 3] + "..."

        # Add line breaks for readability
        if add_line_breaks and config.line_breaks:
            # Add breaks after sentences for longer captions
            sentences = text.split(". ")
            if len(sentences) > 2:
                formatted_parts = []
                for i, sentence in enumerate(sentences):
                    formatted_parts.append(sentence + ("." if not sentence.endswith(".") else ""))
                    if i < len(sentences) - 1 and i % 2 == 1:
                        formatted_parts.append("\n\n")
                text = "".join(formatted_parts)

        return text

    def generate_caption(
        self,
        content_description: str,
        key_message: str,
        platform: Platform,
        tone: Tone = Tone.PROFESSIONAL,
        goal: Goal = Goal.ENGAGEMENT,
        category: str = "business",
        custom_hashtags: Optional[List[str]] = None,
    ) -> Caption:
        """
        Generate a single caption for specified platform.

        Args:
            content_description: What the post is about
            key_message: Main message to convey
            platform: Target platform
            tone: Desired tone
            goal: Content goal
            category: Content category for hashtags
            custom_hashtags: Optional custom hashtags to include

        Returns:
            Caption object with text, hashtags, and CTA
        """
        config = self.PLATFORM_CONFIGS[platform]

        # Build caption based on tone
        if tone == Tone.PROFESSIONAL:
            text = f"{key_message}.\n\n{content_description}"
        elif tone == Tone.CASUAL:
            text = f"Hey! 👋 {key_message}\n\n{content_description}"
        elif tone == Tone.PLAYFUL:
            text = f"POV: {key_message} ✨\n\n{content_description}"
        elif tone == Tone.INSPIRATIONAL:
            text = f"💡 {key_message}\n\nHere's the thing: {content_description}"
        else:  # Educational
            text = f"Did you know? {key_message}\n\n{content_description}"

        # Format for platform
        text = self.format_caption(text, platform)

        # Get hashtags and CTA
        hashtags = self.get_hashtags(platform, category, custom_hashtags)
        cta = self.get_cta(goal)

        # Add CTA to text if platform supports longer content
        if config.max_length > 300:
            text = f"{text}\n\n{cta}"

        caption = Caption(
            platform=platform,
            text=text,
            hashtags=hashtags,
            cta=cta,
            character_count=len(text),
            best_posting_time=random.choice(config.best_times),
        )

        self.generated_captions.append(caption)
        return caption

    def generate_multi_platform(
        self,
        content_description: str,
        key_message: str,
        platforms: List[Platform],
        tone: Tone = Tone.PROFESSIONAL,
        goal: Goal = Goal.ENGAGEMENT,
    ) -> Dict[Platform, Caption]:
        """Generate captions for multiple platforms."""
        results = {}
        for platform in platforms:
            results[platform] = self.generate_caption(
                content_description, key_message, platform, tone, goal
            )
        return results

    def to_markdown(self, captions: Dict[Platform, Caption]) -> str:
        """Convert captions to markdown format."""
        lines = ["# Generated Social Media Captions\n"]

        for platform, caption in captions.items():
            lines.extend([
                f"## {platform.value.title()}",
                "",
                caption.text,
                "",
                f"**Hashtags**: {' '.join(caption.hashtags)}",
                f"**Character Count**: {caption.character_count}",
                f"**Best Posting Time**: {caption.best_posting_time}",
                "",
                "---",
                "",
            ])

        return "\n".join(lines)


# Example usage
if __name__ == "__main__":
    generator = CaptionGenerator()

    captions = generator.generate_multi_platform(
        content_description="Behind-the-scenes look at our team brainstorming session",
        key_message="Great ideas come from collaboration",
        platforms=[Platform.INSTAGRAM, Platform.LINKEDIN, Platform.TWITTER],
        tone=Tone.PROFESSIONAL,
        goal=Goal.ENGAGEMENT,
    )

    print(generator.to_markdown(captions))
