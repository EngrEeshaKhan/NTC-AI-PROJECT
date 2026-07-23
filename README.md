# NTC AI Platform

An Enterprise AI Platform built for the National Telecommunication Corporation (NTC) that enables intelligent document understanding, Retrieval-Augmented Generation (RAG), compliance analysis, and AI-assisted knowledge retrieval.

The platform combines semantic search, Large Language Models (LLMs), vector databases, and compliance intelligence into a unified web application.

---

# Overview

NTC AI Platform is designed to help organizations interact with internal documents using natural language while also providing automated compliance analysis against organizational policies.

Instead of manually searching hundreds of pages of policy documents, users can:

- Upload documents
- Ask questions in natural language
- Retrieve accurate answers using Retrieval-Augmented Generation (RAG)
- Upload complaints
- Compare complaints against organizational policies
- Detect possible policy violations
- Ask follow-up questions regarding compliance decisions

---

# Core Modules

## 1. AI Document Intelligence

Document management system for organizational knowledge.

Features

- Upload PDF documents
- Automatic text extraction
- Semantic chunking
- Embedding generation
- FAISS vector indexing
- Natural language querying
- AI-generated responses
- Document deletion

---

## 2. AI Assistant

Enterprise conversational assistant powered by Retrieval-Augmented Generation.

Capabilities

- Question answering
- Context-aware retrieval
- Document-specific chat
- Semantic search
- Hallucination reduction using retrieved context
- Multi-document knowledge retrieval

---

## 3. Compliance Intelligence

Compliance Intelligence is a specialized AI workflow built on top of the RAG engine.

The workflow allows users to upload:

- Organizational policies
- Security policies
- Email policies
- SOPs
- HR policies
- Complaint documents

The system automatically:

- Extracts complaint information
- Searches all uploaded policies
- Finds relevant policy clauses
- Matches complaint content against policies
- Detects possible violations
- Explains why a policy is violated
- Generates recommendations

Users can continue asking questions after analysis, allowing interactive compliance investigation.

Example

Complaint

Employee shared confidential information externally.

System Result

Relevant Policy:
Information Security Policy

Matching Clause:
Confidential company information must not be disclosed outside the organization.

Compliance Status

Violation Detected

Recommendation

Escalate to Information Security Team and initiate incident response.

---

# RAG Pipeline

The assistant uses a custom Retrieval-Augmented Generation (RAG) pipeline implemented without LangChain.

Pipeline

PDF Upload

↓

Text Extraction

↓

Chunking

↓

Embedding Generation

↓

FAISS Vector Store

↓

Semantic Retrieval

↓

Prompt Construction

↓

LLM Response

---

# Compliance Workflow

Policy Upload

↓

Policy Parsing

↓

Embedding Generation

↓

Vector Database

↓

Complaint Upload

↓

Complaint Parsing

↓

Semantic Matching

↓

Relevant Policy Retrieval

↓

LLM Compliance Analysis

↓

Recommendations

↓

Interactive Compliance Chat

---

# Project Architecture

```
Frontend (HTML/CSS/JavaScript)

        │

        ▼

FastAPI Backend

        │

 ┌──────────────┐
 │ API Routes   │
 └──────────────┘

        │

 ┌──────────────────────────┐
 │ Document AI              │
 │ Compliance AI            │
 │ Security AI (Future)     │
 │ Tender AI (Future)       │
 └──────────────────────────┘

        │

 ┌──────────────────────────┐
 │ RAG Pipeline             │
 │ Chunking                 │
 │ Embeddings               │
 │ Retrieval                │
 │ FAISS                    │
 │ LLM                      │
 └──────────────────────────┘

        │

Data Storage
```

---

# Technology Stack

## Backend

- Python
- FastAPI
- FAISS
- Sentence Transformers
- Ollama
- PyPDF
- NumPy

## Frontend

- HTML
- CSS
- JavaScript

## AI

- Retrieval-Augmented Generation (RAG)
- Sentence Embeddings
- Semantic Search
- FAISS Vector Database
- Large Language Models (LLMs)

---

# Backend Structure

```
backend/

api/
├── document_routes.py
├── compliance_routes.py
├── auth_routes.py
├── security_routes.py
└── tender_routes.py

rag/
├── chunking/
├── embeddings/
├── ingestion/
├── retrieval/
├── vectorstore/
├── llm/
└── pipeline.py

compliance/
├── analyzer.py
├── complaint_manager.py
├── policy_manager.py
└── prompts.py

services/
├── document_ai/
├── compliance_ai/
├── security_ai/
└── tender_ai
```

---

# Frontend

Dashboard

- Platform overview
- Navigation
- Quick actions

Documents

- Upload documents
- Delete documents
- View uploaded files

Assistant

- Select uploaded document
- Chat with AI
- Natural language search

Compliance

- Upload multiple policy documents
- Upload complaint
- Compliance analysis
- Interactive compliance chat

---

# API Endpoints

## Documents

POST

```
/api/upload
```

Upload a document.

---

GET

```
/api/docs
```

Returns uploaded documents.

---

DELETE

```
/api/docs/{id}
```

Deletes a document.

---

POST

```
/api/ask
```

Ask a question using the RAG pipeline.

---

## Compliance

Upload policies

```
POST /compliance/upload-policy
```

Upload complaint

```
POST /compliance/upload-complaint
```

Analyze complaint

```
POST /compliance/analyze
```

Compliance chat

```
POST /compliance/chat
```

---

# Data Storage

```
data/

uploads/
documents/
policies/
complaints/

vectors/
compliance_index/

reports/
logs/
```

---

# Current Features

- Document upload
- Document management
- PDF parsing
- Semantic chunking
- Embedding generation
- FAISS vector indexing
- Retrieval-Augmented Generation
- AI Assistant
- Compliance analysis
- Complaint vs Policy matching
- Multi-policy search
- Compliance recommendations
- Interactive compliance chat

---

# Planned Enterprise Modules

The project architecture has been designed to support additional enterprise AI services.

Future modules include:

- Security Intelligence
- Tender Intelligence
- Audit Assistant
- Alerts Engine
- Analytics Dashboard
- User & Role Management
- Authentication
- Logging
- Notification Engine
- Risk Scoring
- Asset Impact Analysis
- Policy Versioning
- Compliance Reporting

---

# Future Vision

The platform is designed to evolve into an Enterprise AI Governance System capable of:

- Enterprise knowledge management
- AI-assisted compliance monitoring
- Organizational policy intelligence
- Security advisory analysis
- Asset impact assessment
- Risk identification
- Intelligent auditing
- Enterprise decision support

---

# License

Academic / Research Project
