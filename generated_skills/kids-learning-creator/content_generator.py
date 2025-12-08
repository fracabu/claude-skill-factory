"""
Kids Learning Content Generator Module.
Creates interactive educational content for children aged 6-12.
"""

from typing import Dict, List, Any, Optional
from dataclasses import dataclass, field
from enum import Enum
import random


class Subject(Enum):
    """Educational subjects."""
    SCIENCE = "science"
    HISTORY = "history"
    GEOGRAPHY = "geography"
    MATH = "math"
    ART = "art"
    TECHNOLOGY = "technology"
    NATURE = "nature"
    SPACE = "space"
    BODY = "body"


class ContentLevel(Enum):
    """Complexity levels."""
    BASIC = "basic"
    INTERMEDIATE = "intermediate"
    ADVANCED = "advanced"


class QuizType(Enum):
    """Types of quiz questions."""
    MULTIPLE_CHOICE = "multiple_choice"
    TRUE_FALSE = "true_false"
    FILL_BLANK = "fill_blank"
    MATCHING = "matching"


@dataclass
class QuizQuestion:
    """A quiz question structure."""
    question: str
    quiz_type: QuizType
    options: List[str]
    correct_answer: str
    explanation: str
    emoji: str = "🤔"


@dataclass
class Experiment:
    """A hands-on experiment structure."""
    title: str
    materials: List[str]
    steps: List[str]
    what_happens: str
    science_behind: str
    safety_notes: List[str] = field(default_factory=list)
    image_prompt: str = ""


@dataclass
class FunFact:
    """A surprising fun fact."""
    fact: str
    emoji: str
    source_topic: str


@dataclass
class VocabularyItem:
    """A vocabulary word with kid-friendly definition."""
    word: str
    definition: str
    example: str
    emoji: str = "📚"


@dataclass
class LearningContent:
    """Complete learning content structure."""
    title: str
    subject: Subject
    target_age: int
    level: ContentLevel
    introduction: str
    main_explanation: str
    analogy: str
    fun_facts: List[FunFact]
    quiz_questions: List[QuizQuestion]
    experiment: Optional[Experiment]
    vocabulary: List[VocabularyItem]
    activities: List[str]
    image_prompts: Dict[str, str]
    challenge: str
    resources: List[str]


class KidsContentGenerator:
    """Generate educational content for kids."""

    # Age-appropriate emoji sets
    EMOJI_SETS = {
        "science": ["🔬", "🧪", "⚗️", "🔭", "🧲", "💡", "⚡"],
        "nature": ["🌿", "🌳", "🦋", "🐝", "🌸", "🍃", "🌍"],
        "space": ["🚀", "🌙", "⭐", "🪐", "🌌", "☄️", "👨‍🚀"],
        "history": ["🏛️", "⚔️", "👑", "📜", "🗿", "🏰", "🎭"],
        "math": ["🔢", "📐", "📊", "➕", "✖️", "🎯", "🧩"],
        "body": ["❤️", "🧠", "👁️", "🦴", "💪", "🫁", "🦷"],
        "general": ["🎯", "✨", "🎉", "🌟", "💫", "🎁", "🏆"],
    }

    # Encouraging phrases for kids
    ENCOURAGEMENTS = [
        "Fantastico! 🌟",
        "Bravissimo! 🏆",
        "Wow, che scoperta! ✨",
        "Sei un vero scienziato! 🔬",
        "Incredibile! 🎉",
        "Continua così! 💪",
        "Ottimo lavoro! 🌈",
    ]

    # Image style suffix for kid-friendly images
    IMAGE_STYLE_SUFFIX = (
        "children's book illustration style, colorful, friendly, "
        "educational, simple shapes, warm colors, suitable for 10-year-old, "
        "cute cartoon style, white background"
    )

    def __init__(self, target_age: int = 10, language: str = "it"):
        """
        Initialize content generator.

        Args:
            target_age: Target age for content (6-12)
            language: Content language (it, en)
        """
        self.target_age = max(6, min(12, target_age))
        self.language = language
        self.content: Optional[LearningContent] = None

    def get_complexity_level(self) -> ContentLevel:
        """Determine complexity based on age."""
        if self.target_age <= 7:
            return ContentLevel.BASIC
        elif self.target_age <= 9:
            return ContentLevel.INTERMEDIATE
        else:
            return ContentLevel.ADVANCED

    def generate_image_prompt(self, subject: str, context: str) -> str:
        """Generate a kid-friendly image prompt."""
        base_prompt = f"{subject}, {context}"
        return f"{base_prompt}, {self.IMAGE_STYLE_SUFFIX}"

    def create_quiz_question(
        self,
        question: str,
        correct_answer: str,
        wrong_answers: List[str],
        explanation: str,
        quiz_type: QuizType = QuizType.MULTIPLE_CHOICE,
    ) -> QuizQuestion:
        """Create a quiz question with shuffled options."""
        options = [correct_answer] + wrong_answers
        random.shuffle(options)

        return QuizQuestion(
            question=question,
            quiz_type=quiz_type,
            options=options,
            correct_answer=correct_answer,
            explanation=explanation,
            emoji=random.choice(self.EMOJI_SETS["general"]),
        )

    def create_true_false(
        self,
        statement: str,
        is_true: bool,
        explanation: str,
    ) -> QuizQuestion:
        """Create a true/false question."""
        return QuizQuestion(
            question=statement,
            quiz_type=QuizType.TRUE_FALSE,
            options=["Vero", "Falso"],
            correct_answer="Vero" if is_true else "Falso",
            explanation=explanation,
            emoji="🤔",
        )

    def create_experiment(
        self,
        title: str,
        materials: List[str],
        steps: List[str],
        result: str,
        science: str,
        safety: Optional[List[str]] = None,
    ) -> Experiment:
        """Create an experiment structure."""
        return Experiment(
            title=title,
            materials=materials,
            steps=steps,
            what_happens=result,
            science_behind=science,
            safety_notes=safety or ["Chiedi aiuto a un adulto!"],
            image_prompt=self.generate_image_prompt(
                f"science experiment {title}",
                "step by step illustration, materials shown"
            ),
        )

    def get_random_encouragement(self) -> str:
        """Get a random encouraging phrase."""
        return random.choice(self.ENCOURAGEMENTS)

    def format_quiz_markdown(self, quiz: QuizQuestion, number: int) -> str:
        """Format a quiz question as markdown."""
        lines = [
            f"### Domanda {number}: {quiz.question}",
            "",
        ]

        if quiz.quiz_type == QuizType.MULTIPLE_CHOICE:
            for i, option in enumerate(quiz.options):
                letter = chr(65 + i)  # A, B, C, D...
                lines.append(f"{letter}) {option}")
        else:
            lines.append("- Vero")
            lines.append("- Falso")

        lines.extend([
            "",
            "<details>",
            "<summary>👀 Vedi la risposta</summary>",
            "",
            f"✅ **{quiz.correct_answer}**",
            "",
            quiz.explanation,
            "",
            self.get_random_encouragement(),
            "",
            "</details>",
            "",
        ])

        return "\n".join(lines)

    def format_experiment_markdown(self, exp: Experiment) -> str:
        """Format an experiment as markdown."""
        lines = [
            f"## 🔬 Esperimento: {exp.title}",
            "",
            "### 🧪 Cosa Ti Serve",
        ]

        for material in exp.materials:
            lines.append(f"- {material}")

        lines.extend([
            "",
            "### 📝 Procedimento",
        ])

        for i, step in enumerate(exp.steps, 1):
            lines.append(f"{i}. {step}")

        lines.extend([
            "",
            "### 🎉 Cosa Succede?",
            exp.what_happens,
            "",
            "### 🧠 La Scienza Dietro",
            exp.science_behind,
            "",
        ])

        if exp.safety_notes:
            lines.append("### ⚠️ Sicurezza")
            for note in exp.safety_notes:
                lines.append(f"- {note}")
            lines.append("")

        lines.extend([
            f"🖼️ **Immagine AI**: \"{exp.image_prompt}\"",
            "",
        ])

        return "\n".join(lines)

    def format_vocabulary_markdown(self, vocabulary: List[VocabularyItem]) -> str:
        """Format vocabulary as markdown table."""
        lines = [
            "## 📝 Vocabolario",
            "",
            "| Parola | Cosa Significa | Esempio |",
            "|--------|----------------|---------|",
        ]

        for item in vocabulary:
            lines.append(
                f"| {item.emoji} **{item.word}** | {item.definition} | {item.example} |"
            )

        lines.append("")
        return "\n".join(lines)


class TopicExamples:
    """Pre-built examples for common topics."""

    @staticmethod
    def get_volcano_content() -> Dict[str, Any]:
        """Get volcano topic content structure."""
        return {
            "title": "🌋 I Vulcani: Montagne che Sputano Fuoco!",
            "subject": Subject.SCIENCE,
            "introduction": (
                "Ti sei mai chiesto perché alcune montagne... ESPLODONO? 💥\n"
                "Oggi scopriremo il segreto dei vulcani!"
            ),
            "analogy": (
                "La Terra è come una ENORME pesca! 🍑\n"
                "La buccia è la crosta, la polpa è il mantello caldissimo, "
                "e il nocciolo è il nucleo super caldo!"
            ),
            "fun_facts": [
                FunFact(
                    "Il vulcano più alto del Sistema Solare è su Marte!",
                    "🚀",
                    "space"
                ),
                FunFact(
                    "La lava può raggiungere i 1.200°C!",
                    "🔥",
                    "science"
                ),
            ],
            "experiment": {
                "title": "Vulcano in Cucina",
                "materials": [
                    "Bottiglia di plastica",
                    "Bicarbonato (3 cucchiai)",
                    "Aceto (mezzo bicchiere)",
                    "Colorante rosso",
                    "Detersivo (1 goccia)",
                ],
                "steps": [
                    "Metti la bottiglia su un vassoio",
                    "Aggiungi bicarbonato e colorante",
                    "Versa l'aceto e... BOOM!",
                ],
                "result": "La 'lava' esce dalla bottiglia!",
                "science": "Aceto + bicarbonato = gas che spinge fuori tutto!",
            },
        }

    @staticmethod
    def get_solar_system_content() -> Dict[str, Any]:
        """Get solar system topic content structure."""
        return {
            "title": "🚀 Il Sistema Solare: La Famiglia del Sole!",
            "subject": Subject.SPACE,
            "introduction": (
                "Sai che viviamo su una palla che gira intorno a una stella? "
                "Scopriamo i nostri vicini di spazio!"
            ),
            "analogy": (
                "Il Sistema Solare è come una grande famiglia!\n"
                "Il Sole è il papà al centro, e i pianeti sono i figli "
                "che gli girano intorno!"
            ),
            "fun_facts": [
                FunFact(
                    "Giove è così grande che ci starebbero 1.300 Terre!",
                    "🪐",
                    "space"
                ),
                FunFact(
                    "Un giorno su Venere dura più di un anno su Venere!",
                    "😵",
                    "space"
                ),
            ],
        }


# Example usage
if __name__ == "__main__":
    generator = KidsContentGenerator(target_age=10, language="it")

    # Create a sample quiz
    quiz = generator.create_quiz_question(
        question="Cosa esce da un vulcano quando erutta?",
        correct_answer="Lava, cenere e gas",
        wrong_answers=["Ghiaccio e neve", "Acqua e pesci"],
        explanation="La lava è roccia fusa caldissima!",
    )

    print("Quiz Question:")
    print(generator.format_quiz_markdown(quiz, 1))

    # Create a sample experiment
    exp = generator.create_experiment(
        title="Vulcano in Cucina",
        materials=["Bottiglia", "Bicarbonato", "Aceto", "Colorante rosso"],
        steps=[
            "Metti la bottiglia sul vassoio",
            "Aggiungi bicarbonato e colorante",
            "Versa l'aceto velocemente",
        ],
        result="La schiuma rossa esce come lava!",
        science="Il bicarbonato e l'aceto reagiscono creando gas CO2",
    )

    print("\nExperiment:")
    print(generator.format_experiment_markdown(exp))

    # Sample image prompt
    print("\nSample Image Prompt:")
    print(generator.generate_image_prompt(
        "volcano erupting",
        "cross-section showing lava chamber"
    ))
