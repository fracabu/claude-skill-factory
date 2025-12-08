"""
Vacation Rental Optimizer for Rome.
Provides pricing suggestions, gap analysis, and content generation.
"""

from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from enum import Enum
import calendar


class Season(Enum):
    """Roman tourism seasons."""
    LOW = "low"           # Gen-Feb
    SHOULDER = "shoulder"  # Mar, Nov
    HIGH = "high"         # Apr-Giu, Set-Ott
    PEAK = "peak"         # Pasqua, Natale, Giubileo events


class GuestType(Enum):
    """Target guest segments."""
    COUPLE = "couple"
    FAMILY = "family"
    BUSINESS = "business"
    SOLO = "solo"
    GROUP = "group"


@dataclass
class RomeEvent:
    """Special event in Rome affecting pricing."""
    name: str
    start_date: str
    end_date: str
    impact_multiplier: float
    target_guests: List[GuestType]


@dataclass
class Property:
    """Vacation rental property details."""
    name: str
    zona: str
    tipologia: str
    camere: int
    bagni: int
    max_ospiti: int
    base_price: float
    punti_forza: List[str] = field(default_factory=list)
    distanza_metro: str = ""
    attrazioni_vicine: Dict[str, str] = field(default_factory=dict)


@dataclass
class GapPeriod:
    """Unfilled period in calendar."""
    start_date: datetime
    end_date: datetime
    nights: int
    days_until: int
    suggested_discount: float
    target_segment: GuestType
    urgency: str  # low, medium, high, critical


class RomePricingEngine:
    """Dynamic pricing engine for Rome vacation rentals."""

    # 2025 Events Calendar
    EVENTS_2025 = [
        RomeEvent("Capodanno", "2024-12-30", "2025-01-02", 1.6, [GuestType.COUPLE, GuestType.GROUP]),
        RomeEvent("Giubileo Opening", "2025-01-01", "2025-01-15", 1.5, [GuestType.FAMILY, GuestType.COUPLE]),
        RomeEvent("San Valentino", "2025-02-13", "2025-02-16", 1.4, [GuestType.COUPLE]),
        RomeEvent("Maratona Roma", "2025-03-15", "2025-03-17", 1.3, [GuestType.SOLO, GuestType.GROUP]),
        RomeEvent("Pasqua", "2025-04-18", "2025-04-22", 1.7, [GuestType.FAMILY, GuestType.COUPLE]),
        RomeEvent("1 Maggio", "2025-04-30", "2025-05-04", 1.4, [GuestType.COUPLE, GuestType.GROUP]),
        RomeEvent("Estate Romana", "2025-06-15", "2025-08-31", 1.2, [GuestType.FAMILY, GuestType.COUPLE]),
        RomeEvent("Ferragosto", "2025-08-14", "2025-08-17", 1.3, [GuestType.FAMILY]),
        RomeEvent("Festival Cinema", "2025-10-15", "2025-10-26", 1.3, [GuestType.COUPLE, GuestType.SOLO]),
        RomeEvent("Ponte Ognissanti", "2025-10-31", "2025-11-03", 1.4, [GuestType.COUPLE, GuestType.FAMILY]),
        RomeEvent("Immacolata", "2025-12-06", "2025-12-09", 1.4, [GuestType.FAMILY, GuestType.COUPLE]),
        RomeEvent("Natale", "2025-12-22", "2025-12-28", 1.6, [GuestType.FAMILY]),
        RomeEvent("Capodanno 2026", "2025-12-29", "2026-01-02", 1.7, [GuestType.COUPLE, GuestType.GROUP]),
    ]

    # Seasonal multipliers
    SEASONAL_MULTIPLIERS = {
        1: 0.8,   # Gennaio - bassa
        2: 0.8,   # Febbraio - bassa
        3: 1.1,   # Marzo - shoulder
        4: 1.3,   # Aprile - alta
        5: 1.3,   # Maggio - alta
        6: 1.2,   # Giugno - alta
        7: 1.0,   # Luglio - media (caldo)
        8: 0.95,  # Agosto - media (caldo, romani via)
        9: 1.25,  # Settembre - alta
        10: 1.3,  # Ottobre - alta
        11: 1.0,  # Novembre - shoulder
        12: 1.2,  # Dicembre - alta (Natale)
    }

    # Day of week multipliers
    DOW_MULTIPLIERS = {
        0: 0.9,   # Lunedì
        1: 0.9,   # Martedì
        2: 0.95,  # Mercoledì
        3: 1.0,   # Giovedì
        4: 1.15,  # Venerdì
        5: 1.2,   # Sabato
        6: 1.0,   # Domenica
    }

    def __init__(self, property_data: Property):
        """Initialize pricing engine with property data."""
        self.property = property_data

    def get_season(self, date: datetime) -> Season:
        """Determine season for a given date."""
        month = date.month
        if month in [1, 2]:
            return Season.LOW
        elif month in [3, 11]:
            return Season.SHOULDER
        elif month in [4, 5, 6, 9, 10, 12]:
            return Season.HIGH
        else:
            return Season.SHOULDER

    def check_events(self, date: datetime) -> List[RomeEvent]:
        """Check if date falls within any special events."""
        events = []
        for event in self.EVENTS_2025:
            start = datetime.strptime(event.start_date, "%Y-%m-%d")
            end = datetime.strptime(event.end_date, "%Y-%m-%d")
            if start <= date <= end:
                events.append(event)
        return events

    def calculate_price(self, date: datetime) -> Dict[str, Any]:
        """
        Calculate suggested price for a specific date.

        Returns dict with price and factors.
        """
        base = self.property.base_price

        # Seasonal adjustment
        seasonal = self.SEASONAL_MULTIPLIERS.get(date.month, 1.0)

        # Day of week adjustment
        dow = self.DOW_MULTIPLIERS.get(date.weekday(), 1.0)

        # Event adjustment
        events = self.check_events(date)
        event_multiplier = max([e.impact_multiplier for e in events]) if events else 1.0

        # Calculate final price
        final_price = base * seasonal * dow * event_multiplier

        return {
            "date": date.strftime("%Y-%m-%d"),
            "base_price": base,
            "seasonal_multiplier": seasonal,
            "dow_multiplier": dow,
            "event_multiplier": event_multiplier,
            "events": [e.name for e in events],
            "suggested_price": round(final_price, 0),
            "min_price": round(final_price * 0.85, 0),
            "max_price": round(final_price * 1.15, 0),
        }

    def analyze_gap(
        self,
        start_date: datetime,
        end_date: datetime
    ) -> GapPeriod:
        """Analyze a calendar gap and suggest strategy."""
        nights = (end_date - start_date).days
        days_until = (start_date - datetime.now()).days

        # Calculate urgency
        if days_until <= 2:
            urgency = "critical"
            discount = 0.30
        elif days_until <= 7:
            urgency = "high"
            discount = 0.20
        elif days_until <= 14:
            urgency = "medium"
            discount = 0.15
        else:
            urgency = "low"
            discount = 0.10

        # Determine target segment based on days
        weekday_start = start_date.weekday()
        if weekday_start in [4, 5]:  # Fri-Sat
            target = GuestType.COUPLE
        elif weekday_start in [0, 1, 2, 3]:  # Mon-Thu
            target = GuestType.BUSINESS
        else:
            target = GuestType.FAMILY if nights >= 4 else GuestType.COUPLE

        return GapPeriod(
            start_date=start_date,
            end_date=end_date,
            nights=nights,
            days_until=days_until,
            suggested_discount=discount,
            target_segment=target,
            urgency=urgency,
        )

    def generate_gap_promo(self, gap: GapPeriod) -> Dict[str, str]:
        """Generate promotional content for a gap period."""

        discounted_price = self.property.base_price * (1 - gap.suggested_discount)

        # Instagram post
        instagram = f"""🚨 LAST MINUTE ROMA 🚨

📅 {gap.start_date.strftime('%d/%m')} - {gap.end_date.strftime('%d/%m')} disponibile!
💰 €{discounted_price:.0f}/notte (invece di €{self.property.base_price:.0f})
📍 {self.property.zona}

{self.property.punti_forza[0] if self.property.punti_forza else 'Appartamento nel cuore di Roma'}

✨ Solo {gap.nights} notti rimaste!
👉 Link in bio per prenotare

#Roma #LastMinute #WeekendRoma #{self.property.zona.replace(' ', '')}
#RomeApartment #VisitRome #ItalyTravel #Giubileo2025"""

        # Email to past guests
        email = f"""Oggetto: 🏠 Offerta Esclusiva: Torna a Roma!

Ciao!

Il nostro appartamento a {self.property.zona} ha una disponibilità
last-minute che vogliamo offrirti in esclusiva:

📅 Date: {gap.start_date.strftime('%d %B')} - {gap.end_date.strftime('%d %B')}
💰 Prezzo speciale: €{discounted_price:.0f}/notte (-{gap.suggested_discount*100:.0f}%)

Come nostro ospite passato, hai la priorità di prenotazione!

Rispondi a questa email per bloccare le date.

A presto a Roma!
"""

        # Airbnb message
        airbnb_title = f"⚡ -{gap.suggested_discount*100:.0f}% {self.property.zona} | {gap.nights} notti disponibili"

        return {
            "instagram_post": instagram,
            "email_template": email,
            "airbnb_title": airbnb_title,
            "discount_percent": f"{gap.suggested_discount*100:.0f}%",
            "discounted_price": f"€{discounted_price:.0f}",
            "urgency": gap.urgency,
            "target": gap.target_segment.value,
        }


class ListingOptimizer:
    """Optimize vacation rental listings for conversions."""

    # Power words for titles
    POWER_WORDS = {
        "location": ["Central", "Walking Distance", "Heart of", "Steps from", "View of"],
        "emotion": ["Charming", "Stunning", "Cozy", "Elegant", "Romantic", "Magical"],
        "features": ["Terrace", "Balcony", "A/C", "Modern", "Renovated", "Quiet"],
        "trust": ["Superhost", "★", "5-Star", "Top Rated"],
    }

    ROME_ZONES = {
        "Trastevere": {
            "vibe": "bohemian, romantic, nightlife",
            "highlights": ["authentic Roman neighborhood", "cobblestone streets", "best restaurants"],
            "nearby": ["Vatican 15min", "Colosseum 20min", "Campo de' Fiori 10min"],
        },
        "Centro Storico": {
            "vibe": "historic, walkable, iconic",
            "highlights": ["Pantheon", "Piazza Navona", "Trevi Fountain"],
            "nearby": ["Everything walkable", "Spanish Steps 10min"],
        },
        "Monti": {
            "vibe": "trendy, local, artsy",
            "highlights": ["vintage shops", "local bars", "Colosseum views"],
            "nearby": ["Colosseum 5min", "Roman Forum 5min", "Termini 10min"],
        },
        "Testaccio": {
            "vibe": "authentic, foodie, nightlife",
            "highlights": ["best food market", "real Roman life", "clubs"],
            "nearby": ["Piramide metro", "Aventine Hill 10min"],
        },
        "Prati": {
            "vibe": "elegant, quiet, Vatican",
            "highlights": ["Vatican walking distance", "upscale shopping", "residential"],
            "nearby": ["St. Peter's 5min", "Castel Sant'Angelo 10min"],
        },
    }

    def generate_titles(self, property_data: Property, count: int = 5) -> List[str]:
        """Generate optimized listing titles."""
        zona_info = self.ROME_ZONES.get(property_data.zona, {})

        templates = [
            f"★ {property_data.zona} Gem | {property_data.punti_forza[0] if property_data.punti_forza else 'Central Location'} | {property_data.distanza_metro}",
            f"Stunning {property_data.tipologia} in {property_data.zona} ★ Walk to Everything",
            f"{property_data.zona} Hideaway | {property_data.camere}BR | Colosseo {property_data.attrazioni_vicine.get('Colosseo', '15min')}",
            f"Romantic {property_data.zona} ★ {property_data.punti_forza[0] if property_data.punti_forza else 'Authentic Rome'}",
            f"⭐ Superhost | {property_data.zona} | Modern {property_data.camere}BR with A/C",
        ]

        return templates[:count]

    def generate_description(
        self,
        property_data: Property,
        language: str = "it"
    ) -> str:
        """Generate optimized listing description."""

        zona_info = self.ROME_ZONES.get(property_data.zona, {
            "vibe": "central, authentic",
            "highlights": ["great location"],
            "nearby": ["city center"],
        })

        if language == "it":
            description = f"""🏠 BENVENUTI NEL CUORE DI ROMA

Scopri il nostro {property_data.tipologia} nel quartiere più {zona_info['vibe'].split(',')[0]} di Roma: {property_data.zona}.

📍 POSIZIONE IMBATTIBILE
{property_data.distanza_metro} dalla metro, a pochi passi da:
"""
            for attrazione, distanza in property_data.attrazioni_vicine.items():
                description += f"• {attrazione}: {distanza}\n"

            description += f"""
✨ COSA RENDE SPECIALE IL NOSTRO APPARTAMENTO
"""
            for punto in property_data.punti_forza:
                description += f"• {punto}\n"

            description += f"""
🛏️ SPAZI
• {property_data.camere} camera/e da letto
• {property_data.bagni} bagno/i
• Ideale per {property_data.max_ospiti} ospiti

🎁 INCLUSO
• WiFi veloce (100+ Mbps)
• Aria condizionata
• Cucina attrezzata
• Biancheria e asciugamani
• Kit di benvenuto romano

📱 CHECK-IN FLESSIBILE
Self check-in disponibile 24/7

👋 SIAMO QUI PER VOI
Superhost con 5 stelle - rispondiamo in meno di un'ora!

Prenota ora per vivere Roma come un vero romano! 🇮🇹
"""
        else:  # English
            description = f"""🏠 WELCOME TO THE HEART OF ROME

Discover our {property_data.tipologia} in Rome's most {zona_info['vibe'].split(',')[0]} neighborhood: {property_data.zona}.

📍 UNBEATABLE LOCATION
{property_data.distanza_metro} from metro, steps away from:
"""
            for attrazione, distanza in property_data.attrazioni_vicine.items():
                description += f"• {attrazione}: {distanza}\n"

            description += f"""
✨ WHAT MAKES OUR PLACE SPECIAL
"""
            for punto in property_data.punti_forza:
                description += f"• {punto}\n"

            description += f"""
🛏️ THE SPACE
• {property_data.camere} bedroom(s)
• {property_data.bagni} bathroom(s)
• Perfect for up to {property_data.max_ospiti} guests

🎁 INCLUDED
• Fast WiFi (100+ Mbps)
• Air conditioning
• Fully equipped kitchen
• Linens and towels
• Roman welcome kit

📱 FLEXIBLE CHECK-IN
Self check-in available 24/7

👋 WE'RE HERE FOR YOU
Superhost with 5 stars - we respond within the hour!

Book now to experience Rome like a true local! 🇮🇹
"""

        return description


# Example usage
if __name__ == "__main__":
    # Create sample property
    property_data = Property(
        name="Casa Trastevere",
        zona="Trastevere",
        tipologia="Appartamento",
        camere=2,
        bagni=1,
        max_ospiti=4,
        base_price=120,
        punti_forza=[
            "Terrazza panoramica con vista cupole",
            "Appena ristrutturato 2024",
            "Silenzioso nonostante la posizione centrale",
        ],
        distanza_metro="8 min a piedi da Trastevere station",
        attrazioni_vicine={
            "Piazza Santa Maria": "3 min",
            "Colosseo": "15 min bus",
            "Vaticano": "20 min tram",
            "Campo de' Fiori": "10 min a piedi",
        },
    )

    # Initialize engines
    pricing = RomePricingEngine(property_data)
    optimizer = ListingOptimizer()

    # Test pricing for a date
    test_date = datetime(2025, 4, 19)  # Pasqua
    price_info = pricing.calculate_price(test_date)
    print("Pricing Analysis:")
    print(f"  Date: {price_info['date']}")
    print(f"  Events: {price_info['events']}")
    print(f"  Suggested: €{price_info['suggested_price']}")
    print(f"  Range: €{price_info['min_price']} - €{price_info['max_price']}")

    # Test gap analysis
    gap_start = datetime(2025, 1, 15)
    gap_end = datetime(2025, 1, 18)
    gap = pricing.analyze_gap(gap_start, gap_end)
    promo = pricing.generate_gap_promo(gap)

    print("\nGap Promo:")
    print(f"  Urgency: {promo['urgency']}")
    print(f"  Discount: {promo['discount_percent']}")
    print(f"  Target: {promo['target']}")

    # Generate titles
    titles = optimizer.generate_titles(property_data)
    print("\nOptimized Titles:")
    for i, title in enumerate(titles, 1):
        print(f"  {i}. {title}")
