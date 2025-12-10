import os
import json
from dotenv import load_dotenv
from groq import Groq

# Load environment variables
load_dotenv()

# Create Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

PROMPT_TEMPLATE = """
You are a senior QA engineer.

Generate COMPLETE test cases for the following module/page:

MODULE:
{module}

Cover:
- Functional test cases
- Negative test cases
- Boundary cases
- Validation checks
- Basic security cases

Return STRICT JSON only in this format:

{{
  "module": "{module}",
  "total_test_cases": number,
  "test_cases": [
    {{
      "id": "TC-001",
      "scenario": "",
      "type": "Functional | Negative | Boundary | Security",
      "steps": [],
      "expected_result": ""
    }}
  ]
}}

Rules:
- ONLY JSON
- No explanation text
- Must be valid JSON
"""

def generate_test_cases(module: str):
    """Generate test cases using Groq LLM"""
    
    prompt = PROMPT_TEMPLATE.format(module=module)

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",  # More capable model
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )

    text = response.choices[0].message.content.strip()

    try:
        return json.loads(text)
    except json.JSONDecodeError:
        return {
            "error": "Invalid JSON generated",
            "raw_response": text
        }


def export_to_excel(test_cases: dict, filename: str = "test_cases.xlsx"):
    """Export test cases to Excel (Tester-friendly format)"""

    import pandas as pd

    rows = []
    for tc in test_cases.get("test_cases", []):
        rows.append({
            "Test Case ID": tc.get("id", ""),
            "Scenario": tc.get("scenario", ""),
            "Type": tc.get("type", ""),
            "Steps": " | ".join(tc.get("steps", [])),
            "Expected Result": tc.get("expected_result", ""),
            "Tested? (Yes/No)": "",
            "Pass/Fail": ""
        })

    df = pd.DataFrame(rows)
    df.to_excel(filename, index=False)
    return filename
