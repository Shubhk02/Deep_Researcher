#!/usr/bin/env python3
"""
Basic usage example for Deep Researcher Agent
"""

import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.append(str(Path(__file__).parent.parent))

def main():
    """Demonstrate basic usage of Deep Researcher."""
    try:
        from deep_researcher import DeepResearcher, create_sample_documents
        
        print("🧠 Deep Researcher - Basic Usage Example")
        print("=" * 45)
        
        # 1. Initialize researcher
        print("\n1. Initializing researcher...")
        researcher = DeepResearcher()
        
        # 2. Add documents
        print("2. Adding sample documents...")
        documents = create_sample_documents()
        researcher.add_documents(documents)
        print(f"   Added {len(documents)} documents")
        
        # 3. Conduct research
        print("3. Conducting research...")
        query = "What is artificial intelligence and how is it used?"
        report = researcher.research(query)
        
        # 4. Display results
        print("\n4. Results:")
        print(f"   Query: {query}")
        print(f"   Confidence: {report.confidence_score:.2f}")
        print(f"   Sources: {len(report.sources_used)}")
        print(f"   Research steps: {len(report.steps)}")
        
        print("\n5. Research synthesis:")
        print("-" * 40)
        print(report.synthesis[:500] + "..." if len(report.synthesis) > 500 else report.synthesis)
        print("-" * 40)
        
        # 6. Export report
        print("\n6. Exporting report...")
        markdown_report = researcher.export_report(report, 'markdown')
        
        with open('basic_example_report.md', 'w', encoding='utf-8') as f:
            f.write(markdown_report)
        
        print("   Report saved to: basic_example_report.md")
        print("\n✅ Example completed successfully!")
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return 1
    except Exception as e:
        print(f"❌ Error: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
