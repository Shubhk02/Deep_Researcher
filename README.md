# 🧠 Deep Researcher Agent

A powerful, local research agent that can search, analyze, and synthesize information from large-scale data sources without relying on external APIs. The system handles local embedding generation, multi-step reasoning, and intelligent information synthesis entirely offline.

[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)


## ✨ Features

- **Local Embedding Generation**: Custom TF-IDF based embeddings - no external APIs needed
- **Multi-Step Reasoning**: Automatically breaks down complex queries into manageable sub-questions
- **Intelligent Synthesis**: Combines findings from multiple sources into coherent research reports
- **Confidence Scoring**: Provides reliability metrics for all research findings
- **Interactive Research Sessions**: Follow-up questions with context awareness
- **Batch Processing**: Handle multiple research queries efficiently
- **Multiple Export Formats**: Markdown, JSON, and structured reports
- **Offline Operation**: No internet connection required after setup

## 🚀 Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Run interactive demo
python examples/interactive_demo.py
```

## 📚 Basic Usage

```python
from deep_researcher import DeepResearcher

# Initialize and add documents
researcher = DeepResearcher()
documents = [{
    'id': 'doc1', 
    'title': 'Your Document',
    'content': 'Your content here...'
}]
researcher.add_documents(documents)

# Research and get results
report = researcher.research("Your research question")
print(f"Confidence: {report.confidence_score:.2f}")
print(report.synthesis)
```

## 📖 Documentation

- [Installation Guide](docs/installation.md)
- [Usage Examples](examples/)
- [API Reference](docs/api_reference.md)

## 🤝 Contributing

Contributions welcome! Please feel free to submit a Pull Request.

