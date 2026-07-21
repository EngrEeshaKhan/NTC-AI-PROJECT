import os
import uuid
import pickle

from backend.rag.ingestion.loader import load_pdf
from backend.rag.chunking.chunker import chunk_text
from backend.rag.embeddings.embedder import embed
from backend.rag.vectorstore.faiss_store import FAISSStore


POLICY_FOLDER = "data/policies"
INDEX_FOLDER = "data/compliance_index"

os.makedirs(POLICY_FOLDER, exist_ok=True)
os.makedirs(INDEX_FOLDER, exist_ok=True)


class PolicyManager:

    def __init__(self):

        self.store = FAISSStore()

        self.policies = {}


    async def upload(self, files):

        uploaded = []


        for file in files:

            policy_id = str(uuid.uuid4())


            filename = (
                f"{policy_id}_{file.filename}"
            )


            path = os.path.join(
                POLICY_FOLDER,
                filename
            )


            content = await file.read()


            with open(path, "wb") as f:
                f.write(content)



            text = load_pdf(path)


            chunks = chunk_text(text)


            vectors = embed(chunks)



            self.store.create_doc(
                policy_id,
                dim=len(vectors[0])
            )


            self.store.add(
                policy_id,
                vectors,
                chunks
            )


            self.store.save_doc(
                policy_id,
                INDEX_FOLDER
            )


            metadata = {

                "policy_id": policy_id,

                "filename": file.filename,

                "path": path,

                "chunks": len(chunks)

            }


            with open(
                os.path.join(
                    INDEX_FOLDER,
                    f"{policy_id}.pkl"
                ),
                "wb"
            ) as f:

                pickle.dump(
                    metadata,
                    f
                )


            self.policies[policy_id] = metadata


            uploaded.append(metadata)



        return uploaded



    def get_all(self):

        return self.policies



    def search_policy(
        self,
        policy_id,
        vector
    ):

        return self.store.search(
            policy_id,
            vector
        )