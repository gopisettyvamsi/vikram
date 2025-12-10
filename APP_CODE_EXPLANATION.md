# app.py - Code Explanation

## Overview
This file contains the core logic for an AI-powered test case generator. It uses the Groq API with the Llama model to automatically generate comprehensive test cases based on module descriptions.

---

## Imports Section

### Line 1: `import os`
- **Purpose**: Import the `os` module to interact with the operating system
- **Usage**: Used to access environment variables (like API keys)

### Line 2: `import json`
- **Purpose**: Import the `json` module for JSON parsing and manipulation
- **Usage**: Used to parse the AI-generated response as JSON and handle JSON decode errors

### Line 3: `from dotenv import load_dotenv`
- **Purpose**: Import the `load_dotenv` function from the `python-dotenv` package
- **Usage**: Loads environment variables from a `.env` file into the application

### Line 4: `from groq import Groq`
- **Purpose**: Import the `Groq` class from the `groq` SDK
- **Usage**: Creates an API client to communicate with the Groq LLM service

---

## Environment Setup

### Line 7: `load_dotenv()`
- **Purpose**: Loads environment variables from a `.env` file in the project directory
- **Why**: Keeps sensitive data (like API keys) out of the source code
- **Execution**: Should be called early, before any API keys are accessed

### Line 10: `client = Groq(api_key=os.getenv("GROQ_API_KEY"))`
- **Purpose**: Creates a Groq API client object
- **Details**:
  - `os.getenv("GROQ_API_KEY")` retrieves the API key from environment variables
  - `Groq()` initializes the client with this key
  - The client is stored in a module-level variable for reuse across functions

---

## PROMPT_TEMPLATE (Lines 12-46)

### What it is:
A multi-line string (template) that defines the instructions for the AI model

### Key Components:

1. **Role Definition** (Line 13):
   - `"You are a senior QA engineer."` - Sets the context/persona for the AI

2. **Task Description** (Lines 15-16):
   - Tells the AI to generate "COMPLETE test cases"
   - Indicates the input will be a module/page description

3. **Test Case Coverage Areas** (Lines 18-23):
   - **Functional test cases**: Normal, happy-path scenarios
   - **Negative test cases**: Invalid inputs, error conditions
   - **Boundary cases**: Edge values (min/max, empty, null, etc.)
   - **Validation checks**: Input validation and data integrity
   - **Basic security cases**: Authentication, authorization, injection attacks

4. **Output Format** (Lines 25-40):
   - Specifies strict JSON structure with:
     - `module`: Name of the module
     - `total_test_cases`: Count of test cases
     - `test_cases`: Array of individual test case objects
   - Each test case has: `id`, `scenario`, `type`, `steps` (array), `expected_result`

5. **Rules** (Lines 42-46):
   - Forces JSON-only output (no explanatory text)
   - Ensures response is valid JSON (parseable)
   - No extra formatting or explanation

---

## Function 1: `generate_test_cases(module: str)`

### Function Definition (Line 48):
```python
def generate_test_cases(module: str):
```
- **Parameters**: Takes a string `module` describing a feature/page
- **Returns**: Dictionary containing either test cases or error information

### Line 50-51: Prompt Customization
```python
prompt = PROMPT_TEMPLATE.format(module=module)
```
- **Purpose**: Replaces `{module}` placeholder in the template with the actual module description
- **Example**: If `module="login form"`, the prompt will include "MODULE: login form"

### Lines 53-57: API Call
```python
response = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[{"role": "user", "content": prompt}],
    temperature=0.2
)
```
- **`client.chat.completions.create()`**: Sends request to Groq API
- **`model`**: Uses the Llama 3.1 8B instant model (fast, smaller model)
- **`messages`**: Formatted as chat message with role "user" and prompt content
- **`temperature=0.2`**: Low temperature (0-1) means deterministic, consistent output
  - Low values = more focused, less creative
  - High values = more random, creative
  - 0.2 is good for structured output like JSON

### Line 59: Extract Response Text
```python
text = response.choices[0].message.content.strip()
```
- **`response.choices[0]`**: Gets the first (and usually only) response choice
- **`.message.content`**: Extracts the text content from the response
- **`.strip()`**: Removes leading/trailing whitespace

### Lines 61-65: Parse JSON & Error Handling
```python
try:
    return json.loads(text)
except json.JSONDecodeError:
    return {
        "error": "Invalid JSON generated",
        "raw_response": text
    }
```
- **`json.loads(text)`**: Parses the text string into a Python dictionary
- **Try-Except**: If parsing fails, returns an error object with the raw response for debugging

---

## Function 2: `export_to_excel(test_cases: dict, filename: str = "test_cases.xlsx")`

### Function Definition (Line 68):
```python
def export_to_excel(test_cases: dict, filename: str = "test_cases.xlsx"):
```
- **Parameters**:
  - `test_cases`: Dictionary containing test case data
  - `filename`: Output filename (default: "test_cases.xlsx")
- **Returns**: The filename of the created Excel file

### Line 71: Import pandas
```python
import pandas as pd
```
- **Purpose**: Imports pandas library for DataFrame and Excel export functionality
- **Why here**: Only imported when this function is called (lazy import)

### Lines 73-83: Build Data Rows
```python
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
```
- **`test_cases.get("test_cases", [])`**: Safely gets the test_cases array (defaults to empty list)
- **Loop**: Iterates through each test case
- **Dictionary creation**: For each test case, creates a row with:
  - ID, Scenario, Type from the original test case
  - **Steps**: Joins the steps array into a pipe-separated string: `"Step 1 | Step 2 | Step 3"`
  - **Empty columns**: "Tested? (Yes/No)" and "Pass/Fail" for testers to fill in manually

### Line 85: Create DataFrame
```python
df = pd.DataFrame(rows)
```
- Converts the list of dictionaries into a pandas DataFrame (table structure)

### Line 86: Export to Excel
```python
df.to_excel(filename, index=False)
```
- **`.to_excel()`**: Writes DataFrame to an Excel file
- **`index=False`**: Doesn't include row numbers in the output

### Line 87: Return Filename
```python
return filename
```
- Returns the filename so the caller knows what file was created

---

## Summary of Data Flow

```
User Input (Module Description)
         ↓
    [generate_test_cases()]
         ↓
    Groq API Call (with Llama model)
         ↓
    AI generates JSON test cases
         ↓
    JSON parsing
         ↓
    Dictionary returned to UI
         ↓
    [export_to_excel()] (optional)
         ↓
    Excel file created for testers
```

---

## Key Technologies Used

| Technology | Purpose |
|-----------|---------|
| **Groq API** | Access to Llama LLM for AI test case generation |
| **python-dotenv** | Environment variable management |
| **pandas** | Data manipulation and Excel export |
| **JSON** | Structured data format for test cases |

---

## Notes for Developers

1. **API Key**: Must have a valid `GROQ_API_KEY` in `.env` file
2. **Model Choice**: `llama-3.1-8b-instant` is chosen for speed vs quality balance
3. **Temperature**: Set to 0.2 for consistent, structured output
4. **Error Handling**: JSON parsing errors return raw response for debugging
5. **Excel Export**: Includes extra columns for tester annotations (Tested?, Pass/Fail)
