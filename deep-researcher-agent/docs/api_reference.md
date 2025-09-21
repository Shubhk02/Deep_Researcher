# API Reference

## Core Classes

### DeepResearcher

The main orchestrator class that coordinates the entire research process.

#### Constructor
```python
DeepResearcher(storage_path: str = "research_data")
```

**Parameters:**
- `storage_path` (str): Directory path for storing embeddings and data

**Example:**
```python
researcher = DeepResearcher(storage_path="my_research_data")
```

#### Methods

##### add_documents(documents)
Add documents to the knowledge base.

```python
add_documents(documents: List[Dict[str, Any]]) -> None
```

**Parameters:**
- `documents`: List of document dictionaries with keys:
  - `id` (str): Unique document identifier
  - `title` (str): Document title
  - `content` (str): Document text content
  - `metadata` (dict, optional): Additional metadata

**Example:**
```python
docs = [
    {
        'id': 'doc1',
        'title': 'AI Overview',
        'content': 'Artificial intelligence is...',
        'metadata': {'author': 'John Doe', 'year': 2024}
    }
]
researcher.add_documents(docs)
```

##### research(query, max_steps)
Conduct comprehensive research on a query.

```python
research(query: str, max_steps: int = 5) -> ResearchReport
```

**Parameters:**
- `query` (str): Research question or topic
- `max_steps` (int): Maximum number of reasoning steps

**Returns:**
- `ResearchReport`: Comprehensive research results

**Example:**
```python
report = researcher.research("What are the benefits of renewable energy?", max_steps=3)
print(f"Confidence: {report.confidence_score:.2f}")
```

##### export_report(report, format)
Export research report in specified format.

```python
export_report(report: ResearchReport, format: str = 'markdown') -> str
```

**Parameters:**
- `report` (ResearchReport): Research report to export
- `format` (str): Export format ('markdown' or 'json')

**Returns:**
- `str`: Formatted report content

**Example:**
```python
markdown_text = researcher.export_report(report, 'markdown')
json_text = researcher.export_report(report, 'json')
```

##### refine_query(original_query, feedback)
Refine query based on user feedback.

```python
refine_query(original_query: str, feedback: str) -> str
```

**Parameters:**
- `original_query` (str): Original research query
- `feedback` (str): User feedback ('more specific', 'broader', 'examples', etc.)

**Returns:**
- `str`: Refined query

**Example:**
```python
refined = researcher.refine_query("AI applications", "more specific")
# Returns: "Provide detailed analysis of AI applications"
```

---

### LocalEmbeddingGenerator

Generates embeddings using local TF-IDF computation.

#### Constructor
```python
LocalEmbeddingGenerator()
```

#### Methods

##### fit(documents)
Train the embedding model on document collection.

```python
fit(documents: List[str]) -> None
```

##### embed(text)
Generate embedding vector for text.

```python
embed(text: str) -> np.ndarray
```

##### embed_batch(texts)
Generate embeddings for multiple texts.

```python
embed_batch(texts: List[str]) -> List[np.ndarray]
```

---

### DocumentProcessor

Handles document chunking and preprocessing.

#### Constructor
```python
DocumentProcessor(chunk_size: int = 500, overlap: int = 50)
```

**Parameters:**
- `chunk_size` (int): Maximum words per chunk
- `overlap` (int): Overlapping words between chunks

#### Methods

##### process_document(doc_id, title, content, metadata)
Process a document into chunks with metadata.

```python
process_document(
    doc_id: str, 
    title: str, 
    content: str, 
    metadata: Dict[str, Any] = None
) -> Document
```

##### chunk_text(text)
Split text into overlapping chunks.

```python
chunk_text(text: str) -> List[str]
```

---

### VectorStore

Manages document storage and similarity search.

#### Constructor
```python
VectorStore(storage_path: str = "vector_store")
```

#### Methods

##### add_document(document, embeddings)
Add document with embeddings to the store.

```python
add_document(document: Document, embeddings: List[np.ndarray]) -> None
```

##### similarity_search(query_embedding, top_k)
Find most similar document chunks.

```python
similarity_search(
    query_embedding: np.ndarray, 
    top_k: int = 10
) -> List[QueryResult]
```

##### save() / load()
Persist vector store to disk.

```python
save() -> None
load() -> None
```

---

### ReasoningEngine

Handles multi-step reasoning and query analysis.

#### Constructor
```python
ReasoningEngine(vector_store: VectorStore, embedding_generator: LocalEmbeddingGenerator)
```

#### Methods

##### analyze_query_complexity(query)
Analyze complexity of query (0-1 scale).

```python
analyze_query_complexity(query: str) -> float
```

##### execute_reasoning_step(query, context)
Execute a single reasoning step.

```python
execute_reasoning_step(query: str, context: str = "") -> ResearchStep
```

---

### SynthesisEngine

Synthesizes information into coherent reports.

#### Constructor
```python
SynthesisEngine()
```

#### Methods

##### synthesize_research(original_query, steps)
Synthesize research steps into comprehensive report.

```python
synthesize_research(
    original_query: str, 
    steps: List[ResearchStep]
) -> ResearchReport
```

---

## Utility Classes

### InteractiveResearcher

Enhanced interface for interactive research sessions.

#### Constructor
```python
InteractiveResearcher(base_researcher: DeepResearcher)
```

#### Methods

##### start_research_session(initial_query)
Start an interactive research session.

```python
start_research_session(initial_query: str) -> ResearchReport
```

##### ask_followup(followup_query)
Ask follow-up questions using previous context.

```python
ask_followup(followup_query: str) -> ResearchReport
```

**Example:**
```python
interactive = InteractiveResearcher(researcher)
initial_report = interactive.start_research_session("What is machine learning?")
followup_report = interactive.ask_followup("What are its applications?")
```

---

### BatchProcessor

Process multiple research queries efficiently.

#### Constructor
```python
BatchProcessor(researcher: DeepResearcher)
```

#### Methods

##### process_query_batch(queries)
Process multiple queries and return results.

```python
process_query_batch(queries: List[str]) -> Dict[str, ResearchReport]
```

##### generate_comparative_analysis(queries)
Generate comparative analysis across multiple queries.

```python
generate_comparative_analysis(queries: List[str]) -> str
```

**Example:**
```python
batch_processor = BatchProcessor(researcher)
queries = ["AI benefits", "AI risks", "AI applications"]
results = batch_processor.process_query_batch(queries)
analysis = batch_processor.generate_comparative_analysis(queries)
```

---

### QualityAnalyzer

Analyze and improve research quality.

#### Constructor
```python
QualityAnalyzer()
```

#### Methods

##### analyze_report_quality(report)
Comprehensive quality analysis of research report.

```python
analyze_report_quality(report: ResearchReport) -> Dict[str, float]
```

**Returns dictionary with metrics:**
- `coverage`: How well query was addressed (0-1)
- `diversity`: Variety of sources (0-1) 
- `confidence`: Overall reliability (0-1)
- `coherence`: How well findings connect (0-1)

##### suggest_improvements(report)
Suggest improvements based on quality analysis.

```python
suggest_improvements(report: ResearchReport) -> List[str]
```

**Example:**
```python
analyzer = QualityAnalyzer()
metrics = analyzer.analyze_report_quality(report)
improvements = analyzer.suggest_improvements(report)

print(f"Coverage: {metrics['coverage']:.2f}")
for improvement in improvements:
    print(f"• {improvement}")
```

---

### PerformanceMonitor

Monitor and optimize system performance.

#### Constructor
```python
PerformanceMonitor()
```

#### Methods

##### time_operation(operation_name)
Decorator to time operations.

```python
@time_operation("embedding_generation")
def generate_embeddings(texts):
    # Your code here
    pass
```

##### get_performance_report()
Generate performance analysis report.

```python
get_performance_report() -> Dict[str, Any]
```

---

## Data Classes

### Document
```python
@dataclass
class Document:
    id: str
    title: str
    content: str
    metadata: Dict[str, Any]
    embedding: Optional[np.ndarray] = None
    chunks: List[str] = None
    chunk_embeddings: List[np.ndarray] = None
```

### QueryResult
```python
@dataclass
class QueryResult:
    document: Document
    chunk: str
    relevance_score: float
    chunk_index: int
```

### ResearchStep
```python
@dataclass
class ResearchStep:
    query: str
    results: List[QueryResult]
    reasoning: str
    confidence: float
```

### ResearchReport
```python
@dataclass
class ResearchReport:
    original_query: str
    steps: List[ResearchStep]
    synthesis: str
    sources_used: List[str]
    confidence_score: float
    timestamp: str
```

---

## Utility Functions

### create_sample_documents()
Create sample documents for testing.

```python
create_sample_documents() -> List[Dict[str, Any]]
```

### load_text_files(directory_path)
Load text files from directory as documents.

```python
load_text_files(directory_path: str) -> List[Dict[str, Any]]
```

### load_csv_as_documents(csv_file)
Load CSV data as documents.

```python
load_csv_as_documents(csv_file: str) -> List[Dict[str, Any]]
```

### load_json_documents(json_file)
Load JSON data as documents.

```python
load_json_documents(json_file: str) -> List[Dict[str, Any]]
```

---

## Configuration Options

### Chunk Size Configuration
```python
# Smaller chunks for better precision
processor = DocumentProcessor(chunk_size=200, overlap=25)
researcher = DeepResearcher()
researcher.document_processor = processor
```

### Storage Location
```python
# Custom storage location
researcher = DeepResearcher(storage_path="/path/to/storage")
```

### Search Results Tuning
```python
# Get more results per search
results = vector_store.similarity_search(embedding, top_k=20)
```

### Confidence Thresholds
```python
# Filter low-confidence results
high_conf_results = [r for r in results if r.relevance_score > 0.5]
```

---

## Error Handling

### Common Exceptions

- `ValueError`: Raised when invalid parameters are provided
- `ImportError`: Raised when required dependencies are missing
- `FileNotFoundError`: Raised when storage files are not found

### Best Practices

```python
try:
    researcher = DeepResearcher()
    researcher.add_documents(documents)
    report = researcher.research(query)
except ValueError as e:
    print(f"Invalid input: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
```