# ⚡ Week 1: Resilient Local RAG Backend Engine

A production-grade, zero-dependency Retrieval-Augmented Generation (RAG) backend API built with FastAPI, PostgreSQL (`pgvector`), and Ollama.

## 🏗️ Tech Stack
* **FastAPI:** Asynchronous API layer with streaming responses.
* **pgvector:** HNSW vector index in PostgreSQL for sub-10ms similarity search.
* **Ollama:** Self-hosted open-weight model serving (`llama3.2`).
* **Tenacity:** Exponential backoff retry logic for inference resilience.

## 🚀 Quickstart

1. **Spin up local infrastructure:**
   ```bash
   docker compose up -d
   docker exec -it rag_ollama ollama pull llama3.2
   docker exec -it rag_ollama ollama pull mxbai-embed-large