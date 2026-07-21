import os
import pickle
import faiss
import numpy as np


class FAISSStore:


    def __init__(self):

        self.indexes = {}

        self.texts = {}



    # =====================================
    # CREATE POLICY INDEX
    # =====================================

    def create_doc(self, doc_id, dim=384):

        self.indexes[doc_id] = faiss.IndexFlatL2(dim)

        self.texts[doc_id] = []



    # =====================================
    # ADD POLICY CHUNKS
    # =====================================

    def add(self, doc_id, vectors, chunks):

        vectors = np.asarray(vectors).astype("float32")


        self.indexes[doc_id].add(vectors)


        self.texts[doc_id].extend(chunks)



    # =====================================
    # SEARCH POLICY
    # =====================================

    def search(self, doc_id, vector, k=5):


        if doc_id not in self.indexes:

            return []


        D, I = self.indexes[doc_id].search(

            np.asarray([vector]).astype("float32"),

            k

        )


        results = []


        for idx in I[0]:

            if idx != -1:

                results.append(
                    self.texts[doc_id][idx]
                )


        return results



    # =====================================
    # DELETE POLICY
    # =====================================

    def delete(self, doc_id):

        self.indexes.pop(doc_id, None)

        self.texts.pop(doc_id, None)



    # =====================================
    # SAVE POLICY INDEX
    # =====================================

    def save_doc(self, doc_id, folder):


        os.makedirs(folder, exist_ok=True)



        faiss.write_index(

            self.indexes[doc_id],

            os.path.join(

                folder,

                f"{doc_id}.faiss"

            )

        )



        with open(

            os.path.join(

                folder,

                f"{doc_id}_chunks.pkl"

            ),

            "wb"

        ) as f:


            pickle.dump(

                self.texts[doc_id],

                f

            )



    # =====================================
    # LOAD POLICY INDEX
    # =====================================

    def load_doc(self, doc_id, folder):


        self.indexes[doc_id] = faiss.read_index(

            os.path.join(

                folder,

                f"{doc_id}.faiss"

            )

        )



        with open(

            os.path.join(

                folder,

                f"{doc_id}_chunks.pkl"

            ),

            "rb"

        ) as f:


            self.texts[doc_id] = pickle.load(f)