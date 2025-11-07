#!/usr/bin/env python3
"""
Skill Finder - Help AI agents find relevant skills for their tasks.

This helper analyzes tasks and recommends appropriate skills and examples.
"""

import os
import re
from pathlib import Path
from typing import List, Dict, Optional
from dataclasses import dataclass


@dataclass
class Skill:
    """Represents a skill."""
    name: str
    category: str
    file_path: str
    description: str
    keywords: List[str]
    examples: List[str]


class SkillFinder:
    """Find and recommend skills based on task requirements."""

    def __init__(self, skills_dir: str = "../skills"):
        self.skills_dir = Path(skills_dir)
        self.skills = self._load_skills()

    def _load_skills(self) -> List[Skill]:
        """Load all skills from the skills directory."""
        skills = []

        if not self.skills_dir.exists():
            return skills

        for category_dir in self.skills_dir.iterdir():
            if not category_dir.is_dir():
                continue

            category = category_dir.name

            for skill_file in category_dir.glob("*.py"):
                skill = self._parse_skill_file(skill_file, category)
                if skill:
                    skills.append(skill)

        return skills

    def _parse_skill_file(self, file_path: Path, category: str) -> Optional[Skill]:
        """Parse a skill file to extract metadata."""
        try:
            with open(file_path) as f:
                content = f.read()

            # Extract docstring
            docstring_match = re.search(r'"""(.*?)"""', content, re.DOTALL)
            if not docstring_match:
                return None

            docstring = docstring_match.group(1).strip()
            lines = docstring.split('\n')
            name = lines[0].replace("Skill:", "").strip() if lines else file_path.stem
            description = lines[1].strip() if len(lines) > 1 else ""

            # Extract keywords from content
            keywords = self._extract_keywords(content)

            # Extract example classes
            examples = re.findall(r'class (\w+App|class \w+Demo|class \w+Screen)', content)

            return Skill(
                name=name,
                category=category,
                file_path=str(file_path),
                description=description,
                keywords=keywords,
                examples=examples[:5],  # Limit to 5 examples
            )

        except Exception as e:
            print(f"Error parsing {file_path}: {e}")
            return None

    def _extract_keywords(self, content: str) -> List[str]:
        """Extract keywords from skill content."""
        keywords = []

        # Extract class names
        keywords.extend(re.findall(r'from textual\.widgets import ([\w, ]+)', content))
        keywords.extend(re.findall(r'from textual\.containers import ([\w, ]+)', content))

        # Common patterns
        patterns = [
            r'reactive\(',
            r'on_\w+',
            r'watch_\w+',
            r'compute_\w+',
            r'push_screen',
            r'pop_screen',
            r'ModalScreen',
            r'CSS =',
            r'BINDINGS =',
        ]

        for pattern in patterns:
            if re.search(pattern, content):
                keywords.append(pattern.replace('\\', '').replace('(', ''))

        return list(set(keywords))

    def find_skills(
        self,
        query: str,
        category: Optional[str] = None,
        limit: int = 5
    ) -> List[Skill]:
        """
        Find skills matching a query.

        Args:
            query: Search query
            category: Filter by category
            limit: Max results

        Returns:
            List of matching skills
        """
        query_lower = query.lower()
        results = []

        for skill in self.skills:
            if category and skill.category != category:
                continue

            score = 0

            # Check name
            if query_lower in skill.name.lower():
                score += 10

            # Check description
            if query_lower in skill.description.lower():
                score += 5

            # Check keywords
            for keyword in skill.keywords:
                if query_lower in keyword.lower():
                    score += 2

            if score > 0:
                results.append((score, skill))

        # Sort by score and return top results
        results.sort(key=lambda x: x[0], reverse=True)
        return [skill for _, skill in results[:limit]]

    def find_by_task(self, task_description: str) -> Dict[str, List[Skill]]:
        """
        Find skills based on task description.

        Args:
            task_description: Description of what to build

        Returns:
            Dictionary of recommended skills by category
        """
        recommendations = {
            "essential": [],
            "recommended": [],
            "optional": []
        }

        task_lower = task_description.lower()

        # Essential skills (always needed)
        if any(word in task_lower for word in ["app", "application", "create", "build"]):
            recommendations["essential"].extend(
                self.find_skills("getting started", limit=1)
            )

        # Widget-related
        if any(word in task_lower for word in ["button", "input", "form", "widget"]):
            recommendations["recommended"].extend(
                self.find_skills("builtin widgets", limit=1)
            )

        # Custom widgets
        if any(word in task_lower for word in ["custom widget", "reusable"]):
            recommendations["recommended"].extend(
                self.find_skills("custom widget", limit=1)
            )

        # Layout
        if any(word in task_lower for word in ["layout", "grid", "horizontal", "vertical"]):
            recommendations["recommended"].extend(
                self.find_skills("layout", limit=1)
            )

        # Styling
        if any(word in task_lower for word in ["style", "css", "theme", "color"]):
            recommendations["recommended"].extend(
                self.find_skills("css", limit=1)
            )

        # Events
        if any(word in task_lower for word in ["click", "event", "handler", "interaction"]):
            recommendations["recommended"].extend(
                self.find_skills("events", limit=1)
            )

        # Reactivity
        if any(word in task_lower for word in ["reactive", "state", "update"]):
            recommendations["recommended"].extend(
                self.find_skills("reactive", limit=1)
            )

        # Screens
        if any(word in task_lower for word in ["screen", "navigation", "modal", "dialog"]):
            recommendations["recommended"].extend(
                self.find_skills("screens", limit=1)
            )

        # Testing
        if any(word in task_lower for word in ["test", "testing"]):
            recommendations["optional"].extend(
                self.find_skills("testing", limit=1)
            )

        return recommendations

    def get_skill_guide(self, skill: Skill) -> str:
        """
        Get a quick guide for a skill.

        Args:
            skill: The skill

        Returns:
            Formatted guide text
        """
        guide = f"""
SKILL: {skill.name}
Category: {skill.category}
File: {skill.file_path}

DESCRIPTION:
{skill.description}

KEYWORDS:
{', '.join(skill.keywords)}

EXAMPLES IN FILE:
{', '.join(skill.examples) if skill.examples else 'No examples'}

USAGE:
Read the skill file at: {skill.file_path}
Look for example classes and copy/adapt the code.
"""
        return guide

    def list_all_skills(self) -> Dict[str, List[str]]:
        """List all available skills by category."""
        by_category = {}

        for skill in self.skills:
            if skill.category not in by_category:
                by_category[skill.category] = []
            by_category[skill.category].append(skill.name)

        return by_category

    def get_learning_path(self, goal: str) -> List[str]:
        """
        Suggest a learning path based on goal.

        Args:
            goal: What the user wants to learn

        Returns:
            Ordered list of skill names
        """
        goal_lower = goal.lower()

        # Beginner path
        if "beginner" in goal_lower or "start" in goal_lower:
            return [
                "Getting Started with Textual",
                "Built-in Widget Usage",
                "Layout Systems",
                "CSS Styling (TCSS)",
                "Events and Messages",
                "Snapshot Testing"
            ]

        # Form/Input path
        if "form" in goal_lower or "input" in goal_lower:
            return [
                "Getting Started with Textual",
                "Built-in Widget Usage",
                "Events and Messages",
                "Reactive Attributes",
                "Input Handling & Validation"
            ]

        # Dashboard path
        if "dashboard" in goal_lower or "data" in goal_lower:
            return [
                "Getting Started with Textual",
                "Layout Systems",
                "Built-in Widget Usage",
                "CSS Styling (TCSS)",
                "Reactive Attributes",
                "Workers & Async Operations"
            ]

        # Default: comprehensive path
        return [
            "Getting Started with Textual",
            "App Lifecycle & Structure",
            "Built-in Widget Usage",
            "Layout Systems",
            "CSS Styling (TCSS)",
            "Events and Messages",
            "Reactive Attributes",
            "Screens and Navigation",
            "Custom Widget Development",
            "Snapshot Testing"
        ]


def main():
    """Example usage."""
    finder = SkillFinder()

    print("=== All Skills ===")
    for category, skills in finder.list_all_skills().items():
        print(f"\n{category.upper()}:")
        for skill in skills:
            print(f"  - {skill}")

    print("\n\n=== Search: 'button' ===")
    results = finder.find_skills("button")
    for skill in results:
        print(f"- {skill.name} ({skill.category})")

    print("\n\n=== Task: Create a data entry form ===")
    task = "Create a data entry form with validation"
    recommendations = finder.find_by_task(task)

    for level, skills in recommendations.items():
        if skills:
            print(f"\n{level.upper()}:")
            for skill in skills:
                print(f"  - {skill.name}")

    print("\n\n=== Learning Path: Beginner ===")
    path = finder.get_learning_path("beginner")
    for i, skill_name in enumerate(path, 1):
        print(f"{i}. {skill_name}")


if __name__ == "__main__":
    main()
