# AI Test Case Generator

Generate comprehensive test cases automatically using AI (Groq + LLaMA) with a beautiful Streamlit interface.

## Features

- **AI-Powered Generation**: Uses Groq's LLaMA model to generate comprehensive test cases
- **Multiple Test Types**: Functional, Negative, Boundary, and Security test cases
- **Export Formats**: JSON, CSV, Excel, and Text
- **IP Address Restriction**: Built-in security to restrict access by IP address
- **Beautiful UI**: Modern Streamlit interface with multiple view modes

## Prerequisites

- Python 3.8+
- Groq API Key ([Get it here](https://console.groq.com))

## Installation

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd ai-testcase-generator
```

### 2. Set up Python environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Configure API Key

Create a `.env` file in the root directory:

```bash
cp .env.example .env
```

Edit `.env` and add your Groq API key:

```
GROQ_API_KEY=your_actual_api_key_here
```

## Usage

### Streamlit UI

```bash
streamlit run ui.py
```

Open your browser at `http://localhost:8501`

**Features:**
- Beautiful gradient UI
- Multiple view modes (Table, Detailed, JSON)
- Download buttons for all formats (JSON, CSV, Excel, Text)
- Real-time generation
- Session state management
- IP address restriction for security

### Flask API (Optional)

If you want to use the REST API separately:

```bash
python api.py
```

This starts the Flask API server on `http://localhost:5000`

**API Endpoints:**
- `POST /api/generate` - Generate test cases
- `POST /api/export/json` - Export as JSON
- `POST /api/export/csv` - Export as CSV
- `POST /api/export/excel` - Export as Excel
- `GET /api/health` - Health check

All endpoints are protected with IP address restriction.

## Security - IP Address Restriction

Both the Streamlit UI and Flask API are configured with IP address restrictions for security.

**Configure Allowed IPs:**

Edit `ALLOWED_IPS` in [ui.py](ui.py) and [api.py](api.py):

```python
ALLOWED_IPS = [
    '125.21.51.10',  # Your IP address
]
```

Unauthorized IP addresses will be blocked from accessing the application.

## Export Formats

### 1. JSON
Complete test case data in JSON format with full structure

### 2. CSV
Comma-separated values file with columns:
- ID
- Title
- Scenario
- Type
- Steps (semicolon-separated)
- Expected Result
- Status

### 3. Excel
Formatted Excel workbook with:
- Headers
- Auto-adjusted column widths
- Color-coded status (Pending, Passed, Failed)
- Clean formatting

### 4. Text
Human-readable text file with:
- Module information
- Detailed test case descriptions
- Formatted steps
- Clear separators

## Project Structure

```
ai-testcase-generator/
├── app.py                 # Core logic and export functions
├── ui.py                  # Streamlit UI with IP restriction
├── api.py                 # Flask REST API with IP restriction
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables (create this)
├── .env.example           # Example environment file
├── .gitignore            # Git ignore rules
└── README.md              # This file
```

## Examples

### Example Input

```
Login page with email, password, remember me checkbox, and forgot password link
```

### Example Output

The AI will generate comprehensive test cases including:
- Valid login scenarios
- Invalid credential tests
- Email format validation
- Password strength checks
- Remember me functionality
- Forgot password flow
- Security test cases
- Boundary conditions

## Customization

### Changing the AI Model

Edit [app.py](app.py:58) to use a different model:

```python
model="llama-3.1-8b-instant",  # Fast (default)
# model="llama-3.1-70b-versatile",  # More accurate
# model="llama3-70b-8192",  # Alternative
```

### Adjusting Temperature

Edit [app.py](app.py:62) to change creativity:

```python
temperature=0.2  # Lower = more deterministic, Higher = more creative
```

### Adding More Allowed IPs

Edit [ui.py](ui.py:10-14) and [api.py](api.py:14-18):

```python
ALLOWED_IPS = [
    '127.0.0.1',
    '::1',
    '192.168.1.150',  # Your current IP
    '192.168.1.200',  # Additional IP
]
```

## Troubleshooting

### Streamlit Issues

```bash
# If streamlit command not found
python -m streamlit run ui.py
```

### IP Address Changes

If your IP address changes (e.g., different WiFi network), update the `ALLOWED_IPS` list in both [ui.py](ui.py) and [api.py](api.py).

### Module Import Errors

```bash
# Make sure you're in the virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt
```

## Contributing

Feel free to submit issues and enhancement requests!

## License

MIT License

## Credits

- Built with [Streamlit](https://streamlit.io/)
- Powered by [Groq](https://groq.com/)
- AI Model: LLaMA 3.1

---

Made with ❤️ for the QA community

## Quick Start Command

```bash
streamlit run ui.py
```
