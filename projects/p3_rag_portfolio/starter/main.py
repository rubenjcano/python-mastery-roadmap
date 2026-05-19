"""
P3 — RAG Portfolio Chatbot — STARTER
======================================
Fill in all the TODOs to build a working RAG system.

Run: streamlit run main.py
"""
import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()


# ── Step 1: Document Loading ──────────────────────────────────────────────
def load_documents(docs_dir: str = "docs/") -> list[dict]:
    """Load all .txt and .md files from docs_dir.
    Return list of {"content": str, "source": str} dicts.
    """
    # TODO: use pathlib to find all .txt and .md files
    # Read each file and return list of dicts
    ...


# ── Step 2: Chunking ──────────────────────────────────────────────────────
def chunk_text(text: str, chunk_size: int = 500, overlap: int = 50) -> list[str]:
    """Split text into overlapping chunks.
    
    Hint: use a sliding window with step = chunk_size - overlap
    """
    # TODO
    ...


# ── Step 3: Embedding + Storing ───────────────────────────────────────────
def build_vector_store(chunks: list[str], sources: list[str]):
    """Embed chunks and store in ChromaDB.
    
    Hint:
        import chromadb
        client = chromadb.Client()
        collection = client.create_collection("portfolio")
        collection.add(documents=chunks, ids=[...], metadatas=[...])
    """
    # TODO
    ...


# ── Step 4: Retrieval ─────────────────────────────────────────────────────
def retrieve(collection, query: str, n_results: int = 3) -> list[str]:
    """Query the collection and return top n_results document chunks."""
    # TODO: collection.query(query_texts=[query], n_results=n_results)
    ...


# ── Step 5: Generation ────────────────────────────────────────────────────
def generate_answer(context_chunks: list[str], question: str) -> str:
    """Generate an answer using Claude with retrieved context.
    
    Build a prompt that includes the context and asks Claude to answer
    based only on the provided information.
    """
    import anthropic
    client = anthropic.Anthropic()
    # TODO: build prompt with context, call Claude, return answer
    ...


# ── Step 6: Streamlit UI ──────────────────────────────────────────────────
def main():
    import streamlit as st
    st.title("📄 Portfolio Chatbot")
    st.caption("Ask me anything about my background and projects.")

    # TODO:
    # 1. Load docs and build vector store (cache with @st.cache_resource)
    # 2. Show a chat input
    # 3. On submit: retrieve context, generate answer, display it
    ...


if __name__ == "__main__":
    main()
