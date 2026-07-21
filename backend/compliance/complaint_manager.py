import os
import uuid
import json

from backend.rag.ingestion.loader import load_pdf



COMPLAINT_FOLDER="data/complaints"

STATE_FILE="data/current_complaint.json"


os.makedirs(
    COMPLAINT_FOLDER,
    exist_ok=True
)



class ComplaintManager:


    def __init__(self):

        self.current_text=""

        self.current_file=""

        self.current_path=""



    async def upload(self,file):


        complaint_id=str(uuid.uuid4())


        filename=f"{complaint_id}_{file.filename}"


        path=os.path.join(
            COMPLAINT_FOLDER,
            filename
        )


        content=await file.read()


        with open(path,"wb") as f:

            f.write(content)



        text=load_pdf(path)



        self.current_text=text

        self.current_file=file.filename

        self.current_path=path



        with open(
            STATE_FILE,
            "w"
        ) as f:

            json.dump(
                {
                "file":file.filename,
                "path":path
                },
                f
            )



        return {

            "filename":file.filename,

            "path":path,

            "characters":len(text)

        }



    def get_text(self):

        return self.current_text