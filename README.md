# CSAI 422 - Lab Assignment 6: Retrieval-Augmented Generation (RAG) System

## Overview

This project implements a complete **Retrieval-Augmented Generation (RAG)** system using open-source components. It integrates document loading, processing, local vector storage (via FAISS), and retrieval strategies to support large language models (LLMs) in generating informed answers. The system is built using documents related to AI sourced from Google Scholar.

## Project Structure

.
├── documents/ # Corpus of 5 AI-related research papers
├── processor.py # Document loading, splitting, embedding
├── retrieval.py # Similarity and MMR retrieval logic
├── ragsystem.py # Prompt engineering and RAG pipeline
├── evaluate.py # Evaluation functions for retrieval & generation
├── configuration.py # Configuration comparison framework
├── README.md # Project documentation (this file)

yaml
Copy code

> Vector store folders (`faiss_store/`, `faiss_store_l12/`) will be created automatically during embedding.

---

## Setup Instructions

### 1. Install Dependencies

Ensure you're using **Python 3.10+**. Then install the required packages:

```bash
pip install langchain sentence-transformers faiss-cpu openai python-docx PyPDF2
2. Prepare the Document Corpus
Place 5 AI-related research papers (PDF/DOCX/TXT) inside the documents/ folder.

3. Run Processing & Indexing
bash
Copy code
python processor.py
This script will:

Load and parse your documents

Split them into text chunks

Generate vector embeddings using:

all-MiniLM-L6-v2

paraphrase-MiniLM-L12-v2

Store them in FAISS vector databases (folders created automatically)

Retrieval & Generation
bash
Copy code
python retrieval.py
python ragsystem.py
Sample queries tested:

"Why do consumers prefer AI recommendations?"

"Is AI effective for learning?"

"How is AI used in healthcare?"

"Could there be an AI co-scientist?"

Supports:

Basic similarity retrieval

Maximum Marginal Relevance (MMR)

Prompt template switching

Query rewriting (bonus)

Evaluation
bash
Copy code
python evaluate.py
Performs:

Retrieval evaluation (Precision, Recall, F1)

Generation quality check (keyword-based)

System Components
Component	Tool
Load Documents	LangChain Loaders
Split Text	LangChain TextSplitter
Embeddings	SentenceTransformers
Vector Storage	FAISS (local, dynamic creation)
Retrieval	Basic + MMR
Generation	OpenAI API via LangChain
Prompting	Custom Templates
Evaluation	Keyword Matching, ID-based Scoring

Sample Evaluation Result
Query: "Why do consumers prefer AI recommendations?"
Expected Keywords: "AI recommendations", "Product type", "AI assistant", "Competence perception"

Metric	Value
Precision	0.75
Recall	0.60
F1 Score	0.666
Answer Quality	Good (4/5 concepts matched)

Strengths
Modular pipeline

Swappable embedding models

MMR retrieval

Built-in evaluation framework

Limitations
Keyword-based evaluation lacks nuance

Prompt templates are basic

No re-ranking step after retrieval

Bonus Implemented
Query Rewriting — uses LLM to rewrite vague queries for better retrieval.
Use via:

python
Copy code
run_rag("Could there be an AI co-scientist?", rewrite=True)
Run Pipeline End-to-End
bash
Copy code
# Step 1: Install dependencies
pip install -r requirements.txt

# Step 2: Embed your documents
python processor.py

# Step 3: Run retrieval and generation
python retrieval.py
python ragsystem.py

# Step 4: Run evaluation
python evaluate.py
References
Lewis et al., Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks

LangChain Docs: https://python.langchain.com/

SentenceTransformers: https://www.sbert.net/

FAISS: https://github.com/facebookresearch/faiss

The Illustrated RAG (Blog)

CSAI Textbook Chapter 9: LLM Workflows

