from services.data.vector_store import search_documents
from services.llm.llm_provider import generate_response

def run_rag(query: str) -> str:
    docs = search_documents(query)
    context = "\n".join(docs)

    prompt = f"""
    Use the context below to answer the question.

    Context:
    {context}

    Question:
    {query}
    """

    return generate_response(prompt)
