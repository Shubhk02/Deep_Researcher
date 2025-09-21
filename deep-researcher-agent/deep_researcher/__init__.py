"""
Deep Researcher Agent - A powerful, local research agent.
"""

__version__ = "1.0.0"

# Core imports - these will be available when you do: from deep_researcher import *
from .core import (
    DeepResearcher,
    Document,
    QueryResult,
    ResearchStep,
    ResearchReport,
    LocalEmbeddingGenerator,
    DocumentProcessor,
    VectorStore,
    QueryDecomposer,
    ReasoningEngine,
    SynthesisEngine,
)

from .utils import (
    InteractiveResearcher,
    BatchProcessor,
    QualityAnalyzer,
    PerformanceMonitor,
    create_sample_documents,
)

__all__ = [
    "DeepResearcher", "Document", "QueryResult", "ResearchStep", "ResearchReport",
    "LocalEmbeddingGenerator", "DocumentProcessor", "VectorStore", 
    "QueryDecomposer", "ReasoningEngine", "SynthesisEngine",
    "InteractiveResearcher", "BatchProcessor", "QualityAnalyzer", 
    "PerformanceMonitor", "create_sample_documents"
]
