"""
Utility functions and classes for Deep Researcher Agent.
"""

import time
import json
import csv
from pathlib import Path
from typing import List, Dict, Any
from collections import defaultdict
import numpy as np

# Import core classes (these should be in core.py)
from .core import DeepResearcher, ResearchReport, QualityAnalyzer


class InteractiveResearcher:
    """Enhanced interactive research interface."""
    
    def __init__(self, base_researcher: DeepResearcher):
        self.researcher = base_researcher
        self.session_history = []
        self.current_context = ""
    
    def start_research_session(self, initial_query: str):
        """Start an interactive research session."""
        print(f"Starting research session: {initial_query}")
        report = self.researcher.research(initial_query)
        self.session_history.append(report)
        return report
    
    def ask_followup(self, followup_query: str):
        """Ask follow-up questions using previous context."""
        context = self._build_context_from_history()
        enhanced_query = f"{context} {followup_query}"
        
        report = self.researcher.research(enhanced_query)
        self.session_history.append(report)
        return report
    
    def _build_context_from_history(self) -> str:
        """Build context from previous research steps."""
        context_parts = []
        for report in self.session_history[-2:]:
            if report.steps:
                best_findings = []
                for step in report.steps:
                    if step.results and step.confidence > 0.5:
                        best_result = max(step.results, key=lambda x: x.relevance_score)
                        best_findings.append(best_result.chunk[:100])
                context_parts.extend(best_findings[:3])
        return " ".join(context_parts)


def create_sample_documents():
    """Create sample documents for testing."""
    return [
        {
            'id': 'ai_overview',
            'title': 'Introduction to Artificial Intelligence',
            'content': """
            Artificial Intelligence (AI) refers to the simulation of human intelligence in machines 
            that are programmed to think and learn like humans. Machine learning is a subset 
            of artificial intelligence that provides machines with the ability to automatically learn 
            and improve from experience without being explicitly programmed.
            
            Applications of AI include expert systems, natural language processing, speech recognition 
            and machine vision. AI is being used across various industries including healthcare, 
            finance, transportation, and entertainment.
            """,
            'metadata': {'category': 'technology', 'date': '2024-01-15'}
        },
        {
            'id': 'climate_change',
            'title': 'Climate Change and Global Warming',
            'content': """
            Climate change refers to long-term shifts in global temperatures and weather patterns. 
            The primary cause is the increased emission of greenhouse gases, particularly carbon dioxide 
            from burning fossil fuels. These gases trap heat in Earth's atmosphere, leading to global 
            warming. Effects include rising sea levels, melting ice caps, extreme weather events, 
            and ecosystem disruption.
            
            Mitigation strategies include transitioning to renewable energy sources, improving energy 
            efficiency, protecting forests, and developing carbon capture technologies.
            """,
            'metadata': {'category': 'environment', 'date': '2024-01-10'}
        }
    ]


def load_text_files(directory_path: str) -> List[Dict[str, Any]]:
    """Load text files from a directory as documents."""
    docs = []
    directory = Path(directory_path)
    
    for file_path in directory.glob("*.txt"):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            docs.append({
                'id': file_path.stem,
                'title': file_path.name,
                'content': content,
                'metadata': {'source': str(file_path)}
            })
        except Exception as e:
            print(f"Error loading {file_path}: {e}")
    
    return docs


# Placeholder classes - implement these based on your needs
class BatchProcessor:
    def __init__(self, researcher):
        self.researcher = researcher
    
    def process_query_batch(self, queries):
        results = {}
        for query in queries:
            try:
                results[query] = self.researcher.research(query)
            except Exception as e:
                results[query] = None
        return results


class PerformanceMonitor:
    def __init__(self):
        self.metrics = {}
    
    def get_performance_report(self):
        return self.metrics
