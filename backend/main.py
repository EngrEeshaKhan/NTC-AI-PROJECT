from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Existing RAG
from backend.api.document_routes import router as rag_router

# New Compliance Module
from backend.api.compliance_routes import router as compliance_router

app = FastAPI(
    title="NTC AI Platform",
    version="1.0"
)

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
# HOME
# ---------------------------
@app.get("/")
def home():
    return {
        "message": "NTC AI Platform Backend Running"
    }

# ---------------------------
# EXISTING DOCUMENT RAG
# ---------------------------
app.include_router(
    rag_router,
    prefix="/api"
)

# ---------------------------
# COMPLIANCE INTELLIGENCE
# ---------------------------
app.include_router(
    compliance_router,
    prefix="/api/compliance",
    tags=["Compliance"]
)