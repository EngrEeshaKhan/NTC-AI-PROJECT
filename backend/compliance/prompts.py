COMPLIANCE_PROMPT = """
You are an expert Compliance Officer.

Analyze the complaint against the provided company policies.

Complaint:
{complaint}

Relevant Policy Sections:
{policies}

Return your response in this format:

Compliance Score:
(0-100)

Violations:
- Policy Name
- Clause
- Severity
- Explanation

Risk Level:

Recommendations:
- Suggest corrections
- Suggest preventive actions

Final Verdict:
"""