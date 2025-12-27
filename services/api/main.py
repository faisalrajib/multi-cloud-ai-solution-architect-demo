from fastapi import FastAPI
from services.llm.rag_pipeline import run_rag

app = FastAPI()

@app.post("/query")
def query_knowledge_base(payload: dict):
    question = payload.get("question")
    answer = run_rag(question)
    return {"answer": answer}
