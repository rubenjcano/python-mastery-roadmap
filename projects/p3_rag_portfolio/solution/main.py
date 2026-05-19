"""
P3 — RAG Portfolio Chatbot — SOLUTION
"""
import os
from pathlib import Path
from dotenv import load_dotenv
import streamlit as st
import chromadb
import anthropic

load_dotenv()


def load_documents(docs_dir: str = "docs/") -> list[dict]:
    docs = []
    for path in Path(docs_dir).rglob("*"):
        if path.suffix in (".txt", ".md") and path.is_file():
            docs.append({"content": path.read_text(encoding="utf-8"), "source": str(path)})
    return docs


def chunk_text(text: str, chunk_size: int = 500, overlap: int = 50) -> list[str]:
    chunks, step = [], chunk_size - overlap
    for i in range(0, len(text), step):
        chunk = text[i:i + chunk_size]
        if chunk.strip():
            chunks.append(chunk)
    return chunks


@st.cache_resource
def build_vector_store():
    client_db = chromadb.Client()
    collection = client_db.get_or_create_collection("portfolio")
    docs = load_documents()
    all_chunks, all_ids, all_meta = [], [], []
    for doc in docs:
        chunks = chunk_text(doc["content"])
        for i, chunk in enumerate(chunks):
            all_chunks.append(chunk)
            all_ids.append(f"{doc['source']}_{i}")
            all_meta.append({"source": doc["source"]})
    if all_chunks:
        collection.add(documents=all_chunks, ids=all_ids, metadatas=all_meta)
    return collection


def retrieve(collection, query: str, n_results: int = 3) -> list[str]:
    results = collection.query(query_texts=[query], n_results=n_results)
    return results["documents"][0] if results["documents"] else []


def generate_answer(context_chunks: list[str], question: str) -> str:
    context = "\n\n---\n\n".join(context_chunks)
    prompt = (
        f"Answer the question based ONLY on the context below.\n"
        f"If the answer is not in the context, say \'I don\'t have that information.\'.\n\n"
        f"Context:\n{context}\n\nQuestion: {question}"
    )
    client = anthropic.Anthropic()
    msg = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=512,
        messages=[{"role": "user", "content": prompt}],
    )
    return msg.content[0].text


def main():
    st.title("📄 Portfolio Chatbot")
    st.caption("Ask me anything about my background and projects.")

    collection = build_vector_store()

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

    if question := st.chat_input("Ask a question..."):
        st.session_state.messages.append({"role": "user", "content": question})
        with st.chat_message("user"):
            st.write(question)
        context = retrieve(collection, question)
        answer = generate_answer(context, question)
        st.session_state.messages.append({"role": "assistant", "content": answer})
        with st.chat_message("assistant"):
            st.write(answer)


if __name__ == "__main__":
    main()
