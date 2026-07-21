from backend.rag.embeddings.embedder import embed
from backend.rag.llm.ollama_llm import generate


class ComplianceAnalyzer:


    def __init__(
        self,
        policy_manager,
        complaint_manager
    ):

        self.policy_manager = policy_manager

        self.complaint_manager = complaint_manager



    def analyze(self):


        complaint_text = (
            self.complaint_manager.get_text()
        )


        if not complaint_text:

            return {

                "status":"failed",

                "message":"No complaint uploaded"

            }



        # Embed complaint

        complaint_vector = embed(
            [
                complaint_text
            ]
        )[0]



        all_results = []



        # Search every policy

        for policy_id, metadata in self.policy_manager.policies.items():


            chunks = self.policy_manager.search_policy(
                policy_id,
                complaint_vector
            )


            all_results.append({

                "policy":
                    metadata["filename"],

                "clauses":
                    chunks

            })



        if not all_results:

            return {

                "status":"failed",

                "message":"No policies available"

            }



        context = ""


        for item in all_results:


            context += "\n\nPOLICY: "

            context += item["policy"]


            context += "\nRELEVANT CLAUSES:\n"


            context += "\n".join(
                item["clauses"]
            )



        prompt = f"""

You are a compliance AI assistant.

Analyze this employee complaint against company policies.

Complaint:

{complaint_text}


Policies:

{context}


Provide:

1. Violated policy name
2. Relevant clause
3. Explanation
4. Risk level
5. Recommended action

"""



        report = generate(
            context,
            prompt
        )



        return {


            "status":"success",

            "report":report

        }




    def chat(self, question):


        complaint = self.complaint_manager.get_text()


        if not complaint:

            return "No complaint uploaded."



        return generate(
            complaint,
            question
        )