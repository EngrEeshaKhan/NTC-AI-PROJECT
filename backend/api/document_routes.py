from fastapi import APIRouter, UploadFile, File
from backend.rag.pipeline import Pipeline

router = APIRouter()
rag = Pipeline()


@router.post("/upload")
async def upload(file: UploadFile = File(...)):
    return await rag.upload(file)


@router.get("/docs")
def docs():
    return rag.list_docs()


@router.delete("/docs/{doc_id}")
def delete(doc_id: str):
    return rag.delete_doc(doc_id)


@router.post("/ask")
def ask(data: dict):
    print("ASK HIT:", data)

    result = rag.ask(data["doc_id"], data["question"])

    print("FINAL RESULT:", result)

    return {"answer": result}