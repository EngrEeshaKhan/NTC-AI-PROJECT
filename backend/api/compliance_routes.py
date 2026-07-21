from fastapi import APIRouter, UploadFile, File
from typing import List


from backend.compliance.policy_manager import PolicyManager
from backend.compliance.complaint_manager import ComplaintManager
from backend.compliance.analyzer import ComplianceAnalyzer



router = APIRouter()



policy_manager = PolicyManager()

complaint_manager = ComplaintManager()

analyzer = ComplianceAnalyzer(
    policy_manager,
    complaint_manager
)




@router.post("/upload-policies")
async def upload_policies(
    files: List[UploadFile] = File(...)
):

    uploaded = await policy_manager.upload(files)


    return {

        "success": True,

        "uploaded": len(uploaded),

        "policies": uploaded

    }




@router.post("/upload-complaint")
async def upload_complaint(
    file: UploadFile = File(...)
):

    result = await complaint_manager.upload(file)


    return {

        "success": True,

        "complaint": result

    }




@router.post("/analyze")
def analyze():

    return analyzer.analyze()




@router.post("/chat")
def chat(data:dict):

    question = data.get(
        "question",
        ""
    )


    return {

        "answer":
        analyzer.chat(question)

    }