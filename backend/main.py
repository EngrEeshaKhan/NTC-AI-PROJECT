from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.api.document_routes import router as rag_router

app = FastAPI()

# ---------------------------
# CORS
# ---------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------------------
# AUTH (KEEP FOR NOW)
# ---------------------------
@app.post("/api/auth/login")
def login(data: dict):
    email = data.get("email")
    password = data.get("password")

    if email == "admin@test.com" and password == "12345678":
        return {"token": "demo-token"}

    return {"error": "wrong credentials"}

# ---------------------------
# RAG ROUTES
# ---------------------------
app.include_router(rag_router, prefix="/api")