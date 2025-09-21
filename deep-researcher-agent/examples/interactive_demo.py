#!/usr/bin/env python3
"""
Interactive Demo for Deep Researcher Agent
"""

import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.append(str(Path(__file__).parent.parent))

def check_dependencies():
    """Check if required packages are installed."""
    try:
        import numpy
        print("✅ All dependencies are installed!")
        return True
    except ImportError as e:
        print(f"❌ Missing dependency: {e}")
        print("Install with: pip install numpy")
        return False

def main():
    """Main demo function."""
    if not check_dependencies():
        return 1
    
    try:
        from deep_researcher import DeepResearcher, create_sample_documents
        
        print("🧠 Deep Researcher Agent - Interactive Demo")
        print("=" * 50)
        
        # Initialize system
        researcher = DeepResearcher()
        
        # Add sample documents
        docs = create_sample_documents()
        researcher.add_documents(docs)
        print(f"📚 Loaded {len(docs)} sample documents")
        
        # Interactive loop
        query_count = 0
        while True:
            try:
                query = input(f"\n🔍 Research Query #{query_count + 1} (or 'exit'): ").strip()
                
                if query.lower() == 'exit':
                    print("👋 Goodbye!")
                    break
                
                if not query:
                    continue
                
                print(f"🔍 Researching: {query}")
                report = researcher.research(query)
                
                print(f"\n📊 Results:")
                print(f"   Confidence: {report.confidence_score:.2f}")
                print(f"   Sources: {len(report.sources_used)}")
                
                # Show summary
                sentences = report.synthesis.split('.')[:2]
                print(f"\n📋 Summary:")
                for sentence in sentences:
                    if sentence.strip():
                        print(f"   • {sentence.strip()}.")
                
                query_count += 1
                
            except KeyboardInterrupt:
                print("\n👋 Interrupted by user. Goodbye!")
                break
            except Exception as e:
                print(f"❌ Error: {e}")
    
    except ImportError as e:
        print(f"❌ Import error: {e}")
        print("Make sure you have the deep_researcher package in the correct location.")
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
