# Technical Documentation
## AI Test Case Generator

**Version:** 1.0.0
**Last Updated:** December 2025
**Technology Stack:** Python, Streamlit, Flask, Groq AI (LLaMA 3.1)

---

## Table of Contents

1. [System Architecture](#system-architecture)
2. [Technology Stack](#technology-stack)
3. [Installation & Setup](#installation--setup)
4. [Core Components](#core-components)
5. [API Documentation](#api-documentation)
6. [Security Implementation](#security-implementation)
7. [Data Flow](#data-flow)
8. [Configuration](#configuration)
9. [Error Handling](#error-handling)
10. [Performance Optimization](#performance-optimization)
11. [Testing](#testing)
12. [Deployment](#deployment)
13. [Troubleshooting](#troubleshooting)

---

## System Architecture

### Overview

The AI Test Case Generator is a web-based application that uses Large Language Models (LLMs) to automatically generate comprehensive test cases for software modules, APIs, and pages.

### Architecture Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                        User Layer                            │
│  ┌──────────────┐              ┌──────────────┐             │
│  │  Streamlit   │              │  External    │             │
│  │  Web UI      │              │  API Clients │             │
│  └──────┬───────┘              └──────┬───────┘             │
└─────────┼───────────────────────────────┼──────────────────┘
          │                               │
          │                               │
┌─────────┼───────────────────────────────┼──────────────────┐
│         │     Application Layer         │                   │
│  ┌──────▼───────┐              ┌────────▼──────┐           │
│  │  ui.py       │              │  api.py       │           │
│  │  (Streamlit) │              │  (Flask REST) │           │
│  └──────┬───────┘              └────────┬──────┘           │
│         │                               │                   │
│         └───────────────┬───────────────┘                   │
│                         │                                   │
│                  ┌──────▼──────┐                            │
│                  │  app.py     │                            │
│                  │  (Core      │                            │
│                  │   Logic)    │                            │
│                  └──────┬──────┘                            │
└─────────────────────────┼────────────────────────────────┘
                          │
                          │
┌─────────────────────────┼────────────────────────────────┐
│         External Services Layer                           │
│                  ┌──────▼──────┐                          │
│                  │  Groq API   │                          │
│                  │  (LLaMA 3.1)│                          │
│                  └─────────────┘                          │
└──────────────────────────────────────────────────────────┘
```

### Design Patterns

1. **MVC Pattern**: Separation of UI (View), Business Logic (Controller), and Data (Model)
2. **Decorator Pattern**: IP address restriction using function decorators
3. **Strategy Pattern**: Multiple export formats (JSON, CSV, Excel, Text)
4. **Singleton Pattern**: Session state management in Streamlit

---

## Technology Stack

### Backend

| Technology | Version | Purpose |
|------------|---------|---------|
| Python | 3.8+ | Core programming language |
| Flask | 3.0.0+ | REST API framework |
| Streamlit | 1.28.0+ | Web UI framework |
| Groq SDK | 0.4.0+ | AI model integration |
| Pandas | 2.0.0+ | Data manipulation |
| OpenPyXL | 3.1.0+ | Excel file generation |

### AI/ML

| Component | Description |
|-----------|-------------|
| Groq API | Cloud-based inference engine |
| LLaMA 3.1 8B Instant | Fast, efficient model |
| LLaMA 3.1 70B Versatile | Higher accuracy model (optional) |

### Frontend

| Technology | Purpose |
|------------|---------|
| Streamlit | Web interface |
| HTML/CSS | Custom styling |
| JavaScript | (via Streamlit components) |

---

## Installation & Setup

### Prerequisites

```bash
# System Requirements
- Python 3.8 or higher
- pip package manager
- 2GB RAM minimum
- Internet connection for API calls
```

### Step 1: Clone Repository

```bash
git clone <repository-url>
cd ai-testcase-generator
```

### Step 2: Create Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Environment Configuration

Create `.env` file:

```bash
cp .env.example .env
```

Edit `.env`:

```env
GROQ_API_KEY=gsk_your_actual_api_key_here
```

### Step 5: Configure IP Restrictions

Edit `ui.py` and `api.py`:

```python
ALLOWED_IPS = [
    '127.0.0.1',        # localhost
    '::1',              # localhost IPv6
    '192.168.1.150',    # Your IP address
]
```

---

## Core Components

### 1. app.py - Core Business Logic

**Purpose**: Contains the main test case generation logic and export functions.

#### Key Functions

##### `generate_test_cases(module: str) -> dict`

Generates test cases using AI.

**Parameters:**
- `module` (str): Description of the module/page/API to test

**Returns:**
- dict: JSON object containing generated test cases

**Algorithm:**
1. Format prompt using predefined template
2. Call Groq API with LLaMA model
3. Parse JSON response
4. Validate and return structured data

**Example:**

```python
from app import generate_test_cases

result = generate_test_cases("Login page with email and password")

# Returns:
{
    "module": "Login page with email and password",
    "total_test_cases": 15,
    "test_cases": [
        {
            "id": "TC-001",
            "title": "Valid login test",
            "scenario": "User logs in with valid credentials",
            "type": "Functional",
            "steps": ["Navigate to login page", "Enter valid email", ...],
            "expected_result": "User successfully logged in",
            "status": "Pending"
        },
        ...
    ]
}
```

##### `export_to_excel(test_cases: dict, filename: str) -> dict`

Exports test cases to Excel with formatting.

**Features:**
- Auto-adjusted column widths
- Color-coded status cells
- Professional formatting

##### `export_to_csv(test_cases: dict, filename: str) -> dict`

Exports to CSV format.

##### `export_to_text(test_cases: dict, filename: str) -> dict`

Exports to human-readable text format.

---

### 2. api.py - REST API Server

**Purpose**: Provides REST API endpoints for external integrations.

**Base URL**: `http://localhost:5000`

#### Endpoints

##### POST /api/generate

Generates test cases.

**Request:**
```json
{
    "module": "Login page with email and password"
}
```

**Response:**
```json
{
    "module": "Login page...",
    "total_test_cases": 15,
    "test_cases": [...]
}
```

**Status Codes:**
- 200: Success
- 400: Invalid request
- 403: IP not whitelisted
- 500: Server error

##### POST /api/export/json

Exports as JSON.

##### POST /api/export/csv

Exports as CSV.

##### POST /api/export/excel

Exports as Excel file (returns binary).

##### GET /api/health

Health check endpoint.

**Response:**
```json
{
    "status": "healthy"
}
```

---

### 3. ui.py - Streamlit Web Interface

**Purpose**: Provides interactive web UI.

#### Key Features

1. **IP Address Restriction**
   ```python
   def check_ip_access():
       headers = st.context.headers
       client_ip = headers.get("X-Forwarded-For", ...)
       return client_ip, client_ip in ALLOWED_IPS
   ```

2. **Session State Management**
   ```python
   st.session_state['test_cases'] = result
   ```

3. **Dynamic Metrics**
   - Real-time test case count
   - Type-based categorization
   - Statistics in sidebar

4. **Multiple Views**
   - Table View: Dataframe display
   - Detailed View: Expandable cards
   - JSON View: Raw data

---

## API Documentation

### Authentication

IP-based whitelisting (no token required for whitelisted IPs).

### Rate Limiting

Currently no rate limiting implemented. Consider adding for production:

```python
from flask_limiter import Limiter

limiter = Limiter(
    app,
    key_func=lambda: request.remote_addr,
    default_limits=["100 per hour"]
)
```

### Error Responses

All errors follow this format:

```json
{
    "error": "Error type",
    "message": "Detailed error message"
}
```

---

## Security Implementation

### 1. IP Whitelisting

**Location**: `ui.py:16-34`, `api.py:20-34`

**Mechanism**:
- Checks `X-Forwarded-For` header
- Fallback to `request.remote_addr`
- Returns 403 for unauthorized IPs

**Flask Implementation:**

```python
def require_ip_whitelist(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        client_ip = request.remote_addr
        if client_ip not in ALLOWED_IPS:
            return jsonify({"error": "Access denied"}), 403
        return f(*args, **kwargs)
    return decorated_function
```

**Streamlit Implementation:**

```python
client_ip, is_allowed = check_ip_access()
if not is_allowed:
    st.error("Access Denied")
    st.stop()
```

### 2. Environment Variables

- API keys stored in `.env` (not in version control)
- `.env` added to `.gitignore`

### 3. Input Validation

- Module description required
- JSON validation on AI responses
- Type checking on exports

### 4. CORS Configuration

```python
CORS(app)  # Currently allows all origins
```

**Production Recommendation:**

```python
CORS(app, resources={
    r"/api/*": {
        "origins": ["https://yourdomain.com"],
        "methods": ["GET", "POST"],
        "allow_headers": ["Content-Type"]
    }
})
```

---

## Data Flow

### Test Case Generation Flow

```
1. User Input
   ↓
2. Input Validation
   ↓
3. Prompt Construction
   ↓
4. Groq API Call (LLaMA)
   ↓
5. Response Parsing
   ↓
6. JSON Validation
   ↓
7. Session Storage
   ↓
8. UI Rendering
```

### Export Flow

```
1. Select Export Format
   ↓
2. Retrieve from Session
   ↓
3. Format Conversion
   ↓
4. File Generation
   ↓
5. Download Trigger
```

---

## Configuration

### Model Configuration

**File**: `app.py:58-62`

```python
model="llama-3.1-8b-instant",  # Fast model
# model="llama-3.1-70b-versatile",  # Accurate model
temperature=0.2  # Creativity (0.0-1.0)
```

**Temperature Guidelines:**
- 0.0-0.3: Deterministic, consistent
- 0.3-0.7: Balanced
- 0.7-1.0: Creative, varied

### Prompt Configuration

**File**: `app.py:11-50`

Customize test case types, format, and rules in `PROMPT_TEMPLATE`.

---

## Error Handling

### Application-Level Errors

```python
try:
    result = generate_test_cases(module)
except Exception as e:
    return {"error": str(e)}
```

### API Errors

```python
try:
    # Process request
except Exception as e:
    return jsonify({"error": str(e)}), 500
```

### Common Error Scenarios

| Error | Cause | Solution |
|-------|-------|----------|
| Invalid JSON | AI response malformed | Retry generation |
| API Key Error | Missing/invalid GROQ_API_KEY | Check .env file |
| Import Error | Missing dependencies | Run `pip install -r requirements.txt` |
| IP Denied | IP not in whitelist | Add IP to ALLOWED_IPS |

---

## Performance Optimization

### 1. Model Selection

- **Development**: `llama-3.1-8b-instant` (faster)
- **Production**: `llama-3.1-70b-versatile` (more accurate)

### 2. Caching

Streamlit auto-caching:

```python
@st.cache_data
def cached_generation(module):
    return generate_test_cases(module)
```

### 3. Async Processing

For multiple requests:

```python
import asyncio

async def generate_multiple(modules):
    tasks = [generate_test_cases(m) for m in modules]
    return await asyncio.gather(*tasks)
```

---

## Testing

### Unit Tests

Create `tests/test_app.py`:

```python
import pytest
from app import generate_test_cases

def test_generate_test_cases():
    result = generate_test_cases("Login page")
    assert "test_cases" in result
    assert result["total_test_cases"] > 0

def test_invalid_input():
    result = generate_test_cases("")
    # Should handle gracefully
```

### API Tests

```python
def test_api_health():
    response = client.get('/api/health')
    assert response.status_code == 200
    assert response.json["status"] == "healthy"
```

### Run Tests

```bash
pytest tests/ -v
```

---

## Deployment

### Local Development

```bash
# Streamlit UI
streamlit run ui.py

# Flask API
python api.py
```

### Production Deployment

#### Option 1: Streamlit Cloud

```bash
# Push to GitHub
git add .
git commit -m "Deploy"
git push

# Deploy on Streamlit Cloud
# Add GROQ_API_KEY in secrets
```

#### Option 2: Docker

Create `Dockerfile`:

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "ui.py", "--server.address=0.0.0.0"]
```

Build and run:

```bash
docker build -t ai-testcase-generator .
docker run -p 8501:8501 --env-file .env ai-testcase-generator
```

#### Option 3: AWS/Azure/GCP

Use Streamlit Cloud or deploy as containerized app.

---

## Troubleshooting

### Issue: Deprecation Warning

**Problem**: `_get_websocket_headers is deprecated`

**Solution**: Updated to `st.context.headers` (already implemented)

### Issue: IP Not Detected

**Problem**: Running behind proxy

**Solution**: Check `X-Forwarded-For` header configuration

### Issue: Slow Generation

**Problem**: Large prompts or slow API

**Solutions**:
1. Use faster model (`llama-3.1-8b-instant`)
2. Reduce prompt complexity
3. Check network latency

### Issue: Excel Export Fails

**Problem**: `openpyxl` not installed

**Solution**:
```bash
pip install openpyxl
```

---

## API Rate Limits

### Groq API Limits

- Requests per minute: Varies by plan
- Tokens per request: Model-dependent

**Monitoring**:

```python
response = client.chat.completions.create(...)
print(response.usage)  # Check token usage
```

---

## Contributing

### Code Style

- Follow PEP 8
- Use type hints
- Add docstrings
- Write tests

### Pull Request Process

1. Fork repository
2. Create feature branch
3. Make changes
4. Add tests
5. Submit PR

---

## License

MIT License

---

## Support

For technical issues:
- GitHub Issues: [repository-url]/issues
- Email: support@example.com

---

## Changelog

### Version 1.0.0 (December 2025)
- Initial release
- IP address restriction
- Professional UI design
- Multiple export formats
- REST API implementation

---

## Appendix

### A. Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| GROQ_API_KEY | Yes | Groq API authentication key |

### B. File Structure

```
ai-testcase-generator/
├── app.py                      # Core logic
├── api.py                      # Flask REST API
├── ui.py                       # Streamlit UI
├── requirements.txt            # Dependencies
├── .env                        # Environment variables (create this)
├── .env.example                # Example environment file
├── .gitignore                  # Git ignore rules
├── README.md                   # User guide
├── TECHNICAL_DOCUMENTATION.md  # This file
└── FUNCTIONAL_DOCUMENTATION.md # User documentation
```

### C. Dependencies

See `requirements.txt` for complete list.

---

**Document Version**: 1.0.0
**Last Updated**: December 10, 2025
**Author**: Development Team
