"""
Content Performance Analyzer Module.
Analyzes content marketing metrics and generates insights.
"""

import csv
from typing import Dict, List, Any, Optional
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
import statistics


class ContentType(Enum):
    """Types of content."""
    BLOG_POST = "blog_post"
    SOCIAL_MEDIA = "social_media"
    VIDEO = "video"
    NEWSLETTER = "newsletter"
    INFOGRAPHIC = "infographic"
    CASE_STUDY = "case_study"


@dataclass
class ContentItem:
    """Single content piece with metrics."""
    content_id: str
    title: str
    publish_date: str
    content_type: str
    views: int
    engagement: int
    clicks: int
    channel: str = ""
    category: str = ""
    word_count: int = 0
    time_on_page: float = 0.0
    conversions: int = 0
    shares: int = 0
    comments: int = 0

    @property
    def engagement_rate(self) -> float:
        """Calculate engagement rate."""
        if self.views == 0:
            return 0.0
        return (self.engagement / self.views) * 100

    @property
    def click_through_rate(self) -> float:
        """Calculate CTR."""
        if self.views == 0:
            return 0.0
        return (self.clicks / self.views) * 100

    @property
    def conversion_rate(self) -> float:
        """Calculate conversion rate."""
        if self.clicks == 0:
            return 0.0
        return (self.conversions / self.clicks) * 100


@dataclass
class PerformanceReport:
    """Complete performance analysis report."""
    total_content: int
    date_range: tuple
    avg_views: float
    avg_engagement_rate: float
    avg_ctr: float
    top_performers: List[ContentItem]
    worst_performers: List[ContentItem]
    by_category: Dict[str, Dict[str, float]]
    by_content_type: Dict[str, Dict[str, float]]
    trends: List[str]
    recommendations: List[str]


class ContentPerformanceAnalyzer:
    """Analyze content performance metrics."""

    # Engagement benchmarks by content type
    BENCHMARKS = {
        "blog_post": {"good": 2.0, "great": 5.0},
        "social_media": {"good": 1.0, "great": 5.0},
        "video": {"good": 3.0, "great": 8.0},
        "newsletter": {"good": 15.0, "great": 30.0},
        "default": {"good": 2.0, "great": 5.0},
    }

    def __init__(self):
        """Initialize analyzer."""
        self.content_items: List[ContentItem] = []
        self.report: Optional[PerformanceReport] = None

    def load_from_csv(self, filepath: str) -> int:
        """
        Load content data from CSV file.

        Args:
            filepath: Path to CSV file

        Returns:
            Number of items loaded
        """
        with open(filepath, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                item = ContentItem(
                    content_id=row.get("content_id", ""),
                    title=row.get("title", ""),
                    publish_date=row.get("publish_date", ""),
                    content_type=row.get("content_type", "blog_post"),
                    views=int(row.get("views", 0)),
                    engagement=int(row.get("engagement", 0)),
                    clicks=int(row.get("clicks", 0)),
                    channel=row.get("channel", ""),
                    category=row.get("category", ""),
                    word_count=int(row.get("word_count", 0)),
                    time_on_page=float(row.get("time_on_page", 0)),
                    conversions=int(row.get("conversions", 0)),
                    shares=int(row.get("shares", 0)),
                    comments=int(row.get("comments", 0)),
                )
                self.content_items.append(item)

        return len(self.content_items)

    def load_from_list(self, data: List[Dict[str, Any]]) -> int:
        """Load content data from list of dictionaries."""
        for row in data:
            item = ContentItem(
                content_id=row.get("content_id", ""),
                title=row.get("title", ""),
                publish_date=row.get("publish_date", ""),
                content_type=row.get("content_type", "blog_post"),
                views=int(row.get("views", 0)),
                engagement=int(row.get("engagement", 0)),
                clicks=int(row.get("clicks", 0)),
                channel=row.get("channel", ""),
                category=row.get("category", ""),
            )
            self.content_items.append(item)
        return len(self.content_items)

    def get_top_performers(self, n: int = 5, metric: str = "engagement_rate") -> List[ContentItem]:
        """Get top N performing content items."""
        sorted_items = sorted(
            self.content_items,
            key=lambda x: getattr(x, metric, 0),
            reverse=True,
        )
        return sorted_items[:n]

    def get_worst_performers(self, n: int = 5, metric: str = "engagement_rate") -> List[ContentItem]:
        """Get worst N performing content items."""
        sorted_items = sorted(
            self.content_items,
            key=lambda x: getattr(x, metric, 0),
        )
        return sorted_items[:n]

    def analyze_by_category(self) -> Dict[str, Dict[str, float]]:
        """Analyze performance grouped by category."""
        categories: Dict[str, List[ContentItem]] = {}

        for item in self.content_items:
            cat = item.category or "Uncategorized"
            if cat not in categories:
                categories[cat] = []
            categories[cat].append(item)

        results = {}
        for cat, items in categories.items():
            results[cat] = {
                "count": len(items),
                "avg_views": statistics.mean([i.views for i in items]),
                "avg_engagement_rate": statistics.mean([i.engagement_rate for i in items]),
                "avg_ctr": statistics.mean([i.click_through_rate for i in items]),
                "total_views": sum([i.views for i in items]),
            }

        return results

    def analyze_by_content_type(self) -> Dict[str, Dict[str, float]]:
        """Analyze performance grouped by content type."""
        types: Dict[str, List[ContentItem]] = {}

        for item in self.content_items:
            ct = item.content_type or "other"
            if ct not in types:
                types[ct] = []
            types[ct].append(item)

        results = {}
        for ct, items in types.items():
            benchmark = self.BENCHMARKS.get(ct, self.BENCHMARKS["default"])
            avg_engagement = statistics.mean([i.engagement_rate for i in items])

            results[ct] = {
                "count": len(items),
                "avg_views": statistics.mean([i.views for i in items]),
                "avg_engagement_rate": avg_engagement,
                "benchmark_status": (
                    "great" if avg_engagement >= benchmark["great"]
                    else "good" if avg_engagement >= benchmark["good"]
                    else "below_benchmark"
                ),
            }

        return results

    def detect_trends(self) -> List[str]:
        """Detect performance trends."""
        trends = []

        if len(self.content_items) < 3:
            return ["Insufficient data for trend analysis"]

        # Sort by date
        sorted_items = sorted(
            self.content_items,
            key=lambda x: x.publish_date,
        )

        # Calculate engagement trend
        first_half = sorted_items[: len(sorted_items) // 2]
        second_half = sorted_items[len(sorted_items) // 2:]

        first_avg = statistics.mean([i.engagement_rate for i in first_half])
        second_avg = statistics.mean([i.engagement_rate for i in second_half])

        if second_avg > first_avg * 1.1:
            trends.append(f"📈 Engagement trending UP: {first_avg:.1f}% → {second_avg:.1f}%")
        elif second_avg < first_avg * 0.9:
            trends.append(f"📉 Engagement trending DOWN: {first_avg:.1f}% → {second_avg:.1f}%")
        else:
            trends.append(f"➡️ Engagement stable: ~{statistics.mean([first_avg, second_avg]):.1f}%")

        # Find best performing day (if dates available)
        # Find content length correlation
        if any(i.word_count > 0 for i in self.content_items):
            items_with_length = [i for i in self.content_items if i.word_count > 0]
            short = [i for i in items_with_length if i.word_count < 1000]
            long = [i for i in items_with_length if i.word_count >= 1000]

            if short and long:
                short_avg = statistics.mean([i.engagement_rate for i in short])
                long_avg = statistics.mean([i.engagement_rate for i in long])

                if long_avg > short_avg * 1.2:
                    trends.append("📝 Long-form content (1000+ words) outperforms short content")
                elif short_avg > long_avg * 1.2:
                    trends.append("📝 Short-form content (<1000 words) outperforms long content")

        return trends

    def generate_recommendations(self) -> List[str]:
        """Generate actionable recommendations."""
        recommendations = []

        # Top performer analysis
        top = self.get_top_performers(3)
        if top:
            top_types = [t.content_type for t in top]
            most_common = max(set(top_types), key=top_types.count)
            recommendations.append(
                f"🎯 Quick Win: Create more {most_common} content - your top performers are this type"
            )

        # Category analysis
        by_cat = self.analyze_by_category()
        if by_cat:
            best_cat = max(by_cat.items(), key=lambda x: x[1]["avg_engagement_rate"])
            recommendations.append(
                f"📊 Strategic: Double down on '{best_cat[0]}' category "
                f"({best_cat[1]['avg_engagement_rate']:.1f}% avg engagement)"
            )

        # Underperformer analysis
        worst = self.get_worst_performers(3)
        if worst:
            avg_views = statistics.mean([w.views for w in worst])
            recommendations.append(
                f"🔬 Experiment: Test different headlines/formats for low performers "
                f"(avg {avg_views:.0f} views)"
            )

        return recommendations

    def analyze(self) -> PerformanceReport:
        """Run complete analysis and generate report."""
        if not self.content_items:
            raise ValueError("No content data loaded")

        # Calculate overall metrics
        avg_views = statistics.mean([i.views for i in self.content_items])
        avg_engagement = statistics.mean([i.engagement_rate for i in self.content_items])
        avg_ctr = statistics.mean([i.click_through_rate for i in self.content_items])

        # Get date range
        dates = [i.publish_date for i in self.content_items if i.publish_date]
        date_range = (min(dates), max(dates)) if dates else ("N/A", "N/A")

        self.report = PerformanceReport(
            total_content=len(self.content_items),
            date_range=date_range,
            avg_views=avg_views,
            avg_engagement_rate=avg_engagement,
            avg_ctr=avg_ctr,
            top_performers=self.get_top_performers(),
            worst_performers=self.get_worst_performers(),
            by_category=self.analyze_by_category(),
            by_content_type=self.analyze_by_content_type(),
            trends=self.detect_trends(),
            recommendations=self.generate_recommendations(),
        )

        return self.report

    def to_markdown(self) -> str:
        """Generate markdown report."""
        if not self.report:
            self.analyze()

        r = self.report
        lines = [
            "# Content Performance Report",
            "",
            "## Executive Summary",
            f"- **Total content analyzed**: {r.total_content}",
            f"- **Date range**: {r.date_range[0]} to {r.date_range[1]}",
            f"- **Average views**: {r.avg_views:,.0f}",
            f"- **Average engagement rate**: {r.avg_engagement_rate:.2f}%",
            f"- **Average CTR**: {r.avg_ctr:.2f}%",
            "",
            "## Top Performers",
            "",
            "| Rank | Title | Views | Engagement Rate |",
            "|------|-------|-------|-----------------|",
        ]

        for i, item in enumerate(r.top_performers, 1):
            lines.append(f"| {i} | {item.title[:40]}... | {item.views:,} | {item.engagement_rate:.2f}% |")

        lines.extend([
            "",
            "## Performance by Category",
            "",
            "| Category | Count | Avg Views | Avg Engagement |",
            "|----------|-------|-----------|----------------|",
        ])

        for cat, metrics in r.by_category.items():
            lines.append(
                f"| {cat} | {metrics['count']} | {metrics['avg_views']:,.0f} | "
                f"{metrics['avg_engagement_rate']:.2f}% |"
            )

        lines.extend([
            "",
            "## Trends Identified",
            "",
        ])
        for trend in r.trends:
            lines.append(f"- {trend}")

        lines.extend([
            "",
            "## Recommendations",
            "",
        ])
        for rec in r.recommendations:
            lines.append(f"1. {rec}")

        return "\n".join(lines)


# Example usage
if __name__ == "__main__":
    analyzer = ContentPerformanceAnalyzer()

    # Sample data
    sample_data = [
        {"content_id": "1", "title": "10 Tips for Remote Work", "publish_date": "2025-01-01",
         "content_type": "blog_post", "views": 5000, "engagement": 250, "clicks": 150, "category": "Productivity"},
        {"content_id": "2", "title": "How to Build a Morning Routine", "publish_date": "2025-01-05",
         "content_type": "blog_post", "views": 3000, "engagement": 180, "clicks": 90, "category": "Lifestyle"},
        {"content_id": "3", "title": "Marketing Trends 2025", "publish_date": "2025-01-10",
         "content_type": "blog_post", "views": 8000, "engagement": 560, "clicks": 320, "category": "Marketing"},
        {"content_id": "4", "title": "Email Templates That Convert", "publish_date": "2025-01-15",
         "content_type": "blog_post", "views": 4500, "engagement": 315, "clicks": 225, "category": "Marketing"},
        {"content_id": "5", "title": "Beginner's Guide to SEO", "publish_date": "2025-01-20",
         "content_type": "blog_post", "views": 6000, "engagement": 240, "clicks": 180, "category": "Marketing"},
    ]

    analyzer.load_from_list(sample_data)
    analyzer.analyze()
    print(analyzer.to_markdown())
