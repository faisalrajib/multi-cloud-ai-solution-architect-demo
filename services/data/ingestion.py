"""
Document ingestion pipeline for the AI Knowledge Assistant.

Responsibilities:
- Load raw documents
- Chunk content for embeddings
- Store raw data in object storage
- Index embeddings in a vector database

This module is intentionally cloud-agnostic.
"""

from typing import List
from services.data.vector_store import index_documents


def load_documents(source_path: str) -> List[str]:
    """
    Load documents from a source location.
    In production, this could be:
    - Cloud object storage
    - SharePoint / Confluence
    - Database exports
    """
    # Placeholder implementation
    with open(source_path, "r") as file:
        content = file.read()

    return [content]


def chunk_document(
    document: str,
    chunk_size: int = 500,
    overlap: int = 50
) -> List[str]:
    """
    Split document into overlapping chunks for better retrieval.
    """
    chunks = []
    start = 0

    while start < len(document):
        end = start + chunk_size
        chunk = document[start:end]
        chunks.append(chunk)
        start = end - overlap

    return chunks


def ingest(source_path: str):
    """
    End-to-end ingestion workflow.
    """
    documents = load_documents(source_path)

    all_chunks = []
    for doc in documents:
        chunks = chunk_document(doc)
        all_chunks.extend(chunks)

    index_documents(all_chunks)

    print(f"Ingested {len(all_chunks)} chunks into vector store")

