import streamlit as st
import json
import pandas as pd
from io import BytesIO
import base64
from app import generate_test_cases, export_to_excel, export_to_text, export_to_csv

st.set_page_config(
    page_title="AI Test Case Generator | Professional QA Tool",
    layout="wide",
    page_icon="🧪",
    initial_sidebar_state="expanded"
)

# IP Address Restriction
ALLOWED_IPS = [
    '127.0.0.1',      # localhost
    '::1',            # localhost IPv6
    '125.21.51.10',  # Your IP address
]

def check_ip_access():
    """Check if the current user's IP is allowed"""
    try:
        # Get client IP from Streamlit context (using new API)
        headers = st.context.headers
        client_ip = headers.get("X-Forwarded-For", headers.get("Host", "unknown"))

        # Handle multiple IPs in X-Forwarded-For header
        if "," in str(client_ip):
            client_ip = client_ip.split(",")[0].strip()

        # Fallback: if running locally, allow localhost
        if client_ip == "unknown" or str(client_ip).startswith("localhost"):
            client_ip = "127.0.0.1"

        # Print to console for debugging
        print(f"\n{'='*60}")
        print(f"IP ACCESS CHECK - Streamlit UI")
        print(f"{'='*60}")
        print(f"Current IP Address: {client_ip}")
        print(f"Allowed IP Addresses: {ALLOWED_IPS}")
        print(f"Access Allowed: {client_ip in ALLOWED_IPS}")
        print(f"{'='*60}\n")

        return client_ip, client_ip in ALLOWED_IPS
    except Exception as e:
        print(f"\n[ERROR] Could not determine IP: {e}")
        # If we can't determine IP, default to localhost for local dev
        return "127.0.0.1", True

# Check IP access
client_ip, is_allowed = check_ip_access()

# Load and encode logo for use in HTML
def get_base64_logo():
    """Convert logo to base64 for embedding in HTML"""
    try:
        with open("Edvenswa1logo.jpeg", "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except:
        return None

logo_base64 = get_base64_logo()

# TEMPORARILY DISABLED - Allowing all IPs
# if not is_allowed:
#     # Display detailed access denied information
#     st.error("🚫 Access Denied")
#     st.warning(f"Your IP address ({client_ip}) is not authorized to access this application.")
#     st.info("Please contact the administrator to whitelist your IP address.")

#     # Show comparison for debugging
#     st.markdown("---")
#     st.markdown("### 🔍 Access Details")
#     st.code(f"""
# Current IP Address: {client_ip}
# Allowed IP Addresses: {', '.join(ALLOWED_IPS)}
# Status: BLOCKED ❌
#     """)
#     st.stop()

# Professional Custom CSS
st.markdown("""
<style>
    /* Import Professional Font */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

    /* Global Styling */
    .main {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }

    /* Header Styling */
    .main-header {
        text-align: center;
        padding: 2rem 0 1rem 0;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 3rem;
        font-weight: 700;
        letter-spacing: -0.02em;
        margin-bottom: 0.5rem;
        animation: fadeInDown 0.8s ease-in-out;
    }

    .sub-header {
        text-align: center;
        color: #6b7280;
        font-size: 1.1rem;
        font-weight: 400;
        margin-bottom: 2rem;
        animation: fadeInUp 0.8s ease-in-out;
    }

    @keyframes fadeInDown {
        from {
            opacity: 0;
            transform: translateY(-20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    /* Card Styling */
    .info-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 12px;
        color: white;
        box-shadow: 0 10px 25px -5px rgba(102, 126, 234, 0.3), 0 10px 10px -5px rgba(118, 75, 162, 0.2);
        margin-bottom: 1rem;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }

    .info-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 15px 30px -5px rgba(102, 126, 234, 0.4), 0 15px 15px -5px rgba(118, 75, 162, 0.3);
    }

    .metric-card {
        background: white;
        padding: 1.25rem;
        border-radius: 10px;
        border: 1px solid #e5e7eb;
        box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.1);
        transition: all 0.3s ease;
    }

    .metric-card:hover {
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        transform: translateY(-2px);
    }

    .metric-value {
        font-size: 2rem;
        font-weight: 700;
        color: #667eea;
        margin-bottom: 0.25rem;
    }

    .metric-label {
        font-size: 0.875rem;
        color: #6b7280;
        font-weight: 500;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }

    /* Status Badges */
    .badge {
        display: inline-block;
        padding: 0.25rem 0.75rem;
        border-radius: 9999px;
        font-size: 0.75rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }

    .badge-functional {
        background: #dbeafe;
        color: #1e40af;
    }

    .badge-negative {
        background: #fee2e2;
        color: #991b1b;
    }

    .badge-boundary {
        background: #fef3c7;
        color: #92400e;
    }

    .badge-security {
        background: #f3e8ff;
        color: #6b21a8;
    }

    /* Success Message */
    .success-banner {
        background: linear-gradient(135deg, #10b981 0%, #059669 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 12px;
        text-align: center;
        font-size: 1.125rem;
        font-weight: 600;
        box-shadow: 0 10px 15px -3px rgba(16, 185, 129, 0.3);
        margin: 2rem 0;
    }

    /* Button Styling */
    .stDownloadButton button {
        width: 100%;
        border-radius: 8px;
        font-weight: 600;
        transition: all 0.2s ease;
    }

    .stDownloadButton button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    }

    /* Table Styling */
    .dataframe {
        border-radius: 8px;
        overflow: hidden;
    }

    /* Sidebar Styling */
    .css-1d391kg, .st-emotion-cache-1d391kg {
        background: #f9fafb;
    }

    /* Feature List */
    .feature-item {
        display: flex;
        align-items: center;
        padding: 0.5rem 0;
        color: #374151;
        font-weight: 500;
    }

    .feature-icon {
        margin-right: 0.75rem;
        font-size: 1.25rem;
    }

    /* Divider */
    hr {
        margin: 2rem 0;
        border: none;
        border-top: 2px solid #e5e7eb;
    }

    /* Footer */
    .footer {
        text-align: center;
        color: #9ca3af;
        font-size: 0.875rem;
        padding: 2rem 0;
        border-top: 1px solid #e5e7eb;
        margin-top: 3rem;
    }

    /* Expander Styling */
    .streamlit-expanderHeader {
        background-color: #f9fafb;
        border-radius: 8px;
        font-weight: 600;
    }

    /* Tab Styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 2rem;
    }

    .stTabs [data-baseweb="tab"] {
        font-weight: 600;
        padding: 0.75rem 1.5rem;
    }
</style>
""", unsafe_allow_html=True)

# Header with Professional Branding
st.markdown("""
<div style="text-align: center; padding: 2rem 0 1rem 0;">
    <h1 class="main-header">🧪 AI Test Case Generator</h1>
    <p class="sub-header">Generate comprehensive, AI-powered test cases in seconds</p>
    <div style="display: inline-block; padding: 0.5rem 1.5rem; background: linear-gradient(135deg, #667eea15 0%, #764ba215 100%); border-radius: 20px; margin-top: 0.5rem;">
        <span style="color: #667eea; font-weight: 600; font-size: 0.9rem;">⚡ Powered by Edvenswa Technology</span>
    </div>
</div>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    # Edvenswa Logo - Professional Design (Smaller size)
    if logo_base64:
        st.markdown(f"""
        <div style="text-align: center; padding: 1rem 0 0.5rem 0;">
            <img src="data:image/jpeg;base64,{logo_base64}" alt="Edvenswa Logo" style="max-width: 150px; height: auto; border-radius: 8px; display: block; margin: 0 auto;">
        </div>
        """, unsafe_allow_html=True)
    else:
        # Fallback if logo not found
        st.markdown("""
        <div style="text-align: center; padding: 1rem 0 0.5rem 0;">
            <h1 style="
                font-size: 1.5rem;
                font-weight: 700;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                margin: 0;
                letter-spacing: 0.05em;
            ">EDVENSWA</h1>
            <p style="font-size: 0.7rem; color: #6b7280; margin-top: 0.25rem; font-weight: 500;">TECHNOLOGY SOLUTIONS</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div class="info-card">
        <h2 style="margin-top: 0; font-size: 1.5rem;">ℹ️ About</h2>
        <p style="margin-bottom: 0;">Powered by <strong>Edvenswa</strong> to generate professional test cases automatically using advanced AI technology.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### ✨ Features")
    st.markdown("""
    <div class="feature-item">
        <span class="feature-icon">✅</span>
        <span>Functional Test Cases</span>
    </div>
    <div class="feature-item">
        <span class="feature-icon">❌</span>
        <span>Negative Scenarios</span>
    </div>
    <div class="feature-item">
        <span class="feature-icon">📊</span>
        <span>Boundary Testing</span>
    </div>
    <div class="feature-item">
        <span class="feature-icon">🔒</span>
        <span>Security Validation</span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    st.markdown("### 📥 Export Formats")
    formats = ["JSON", "CSV", "Excel (XLSX)", "Plain Text"]
    for fmt in formats:
        st.markdown(f"• {fmt}")

    st.markdown("---")

    # Statistics if test cases exist
    if 'test_cases' in st.session_state and st.session_state['test_cases']:
        result = st.session_state['test_cases']
        total = len(result.get('test_cases', []))

        st.markdown("### 📈 Statistics")
        st.metric("Total Test Cases", total)

        # Count by type
        types_count = {}
        for tc in result.get('test_cases', []):
            tc_type = tc.get('type', 'Unknown')
            types_count[tc_type] = types_count.get(tc_type, 0) + 1

        for tc_type, count in types_count.items():
            st.metric(tc_type, count)

    st.markdown("---")
    st.markdown(f"🔒 **IP:** {client_ip}")
    st.caption("Access Restricted")

# Main Content
st.markdown("### 📝 Describe Your Module")

module_text = st.text_area(
    label="Enter a detailed description of the module, page, or API you want to test",
    placeholder="Example: Login page with email and password fields, remember me checkbox, forgot password link, and social media login options (Google, Facebook). Include validation for email format and password strength.",
    height=150,
    key="module_input",
    label_visibility="collapsed"
)

st.markdown("<br>", unsafe_allow_html=True)

# Generate Button
col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    generate_clicked = st.button(
        "🚀 Generate Test Cases",
        type="primary",
        use_container_width=True
    )

if generate_clicked:
    if not module_text.strip():
        st.warning("⚠️ Please enter a module description to generate test cases.")
    else:
        with st.spinner("🔄 Analyzing requirements and generating comprehensive test cases..."):
            result = generate_test_cases(module_text)

        if "error" in result:
            st.error("❌ Failed to generate test cases. Please try again.")
            with st.expander("🔍 View Error Details"):
                st.code(result.get("raw", "Unknown error"))
        else:
            # Store result in session state
            st.session_state['test_cases'] = result

            # Get all test cases
            all_test_cases = result.get("test_cases", [])
            total_count = len(all_test_cases)

            # Success Banner
            st.markdown(f"""
            <div class="success-banner">
                ✅ Successfully generated {total_count} comprehensive test cases!
            </div>
            """, unsafe_allow_html=True)

            # Metrics Row
            col1, col2, col3, col4 = st.columns(4)

            types_count = {}
            for tc in all_test_cases:
                tc_type = tc.get('type', 'Unknown')
                types_count[tc_type] = types_count.get(tc_type, 0) + 1

            with col1:
                st.markdown(f"""
                <div class="metric-card">
                    <div class="metric-value">{total_count}</div>
                    <div class="metric-label">Total Cases</div>
                </div>
                """, unsafe_allow_html=True)

            with col2:
                st.markdown(f"""
                <div class="metric-card">
                    <div class="metric-value">{types_count.get('Functional', 0)}</div>
                    <div class="metric-label">Functional</div>
                </div>
                """, unsafe_allow_html=True)

            with col3:
                st.markdown(f"""
                <div class="metric-card">
                    <div class="metric-value">{types_count.get('Negative', 0)}</div>
                    <div class="metric-label">Negative</div>
                </div>
                """, unsafe_allow_html=True)

            with col4:
                st.markdown(f"""
                <div class="metric-card">
                    <div class="metric-value">{types_count.get('Security', 0) + types_count.get('Boundary', 0)}</div>
                    <div class="metric-label">Security & Boundary</div>
                </div>
                """, unsafe_allow_html=True)

            st.markdown("<br>", unsafe_allow_html=True)

            # Tabs for different views
            tab1, tab2, tab3 = st.tabs(["📊 Table View", "📄 Detailed View", "🔍 JSON View"])

            with tab1:
                st.markdown("### 📋 Test Cases Overview")
                df_data = []
                for tc in all_test_cases:
                    df_data.append({
                        "ID": tc.get("id", ""),
                        "Title": tc.get("title", ""),
                        "Type": tc.get("type", ""),
                        "Scenario": tc.get("scenario", "")[:100] + "..." if len(tc.get("scenario", "")) > 100 else tc.get("scenario", ""),
                        "Steps": str(len(tc.get("steps", []))),
                        "Status": tc.get("status", "Pending")
                    })
                df = pd.DataFrame(df_data)
                st.dataframe(
                    df,
                    use_container_width=True,
                    height=500,
                    column_config={
                        "ID": st.column_config.TextColumn("Test ID", width="small"),
                        "Title": st.column_config.TextColumn("Title", width="medium"),
                        "Type": st.column_config.TextColumn("Type", width="small"),
                        "Scenario": st.column_config.TextColumn("Scenario", width="large"),
                        "Steps": st.column_config.NumberColumn("Steps", width="small"),
                        "Status": st.column_config.TextColumn("Status", width="small"),
                    }
                )

            with tab2:
                st.markdown("### 📝 Detailed Test Cases")
                for tc in all_test_cases:
                    tc_type = tc.get('type', 'Unknown')
                    badge_class = {
                        'Functional': 'badge-functional',
                        'Negative': 'badge-negative',
                        'Boundary': 'badge-boundary',
                        'Security': 'badge-security'
                    }.get(tc_type, 'badge-functional')

                    with st.expander(f"**{tc.get('id', '')}** • {tc.get('title', '')}", expanded=False):
                        st.markdown(f'<span class="badge {badge_class}">{tc_type}</span>', unsafe_allow_html=True)
                        st.markdown(f"**Scenario:** {tc.get('scenario', '')}")
                        st.markdown(f"**Status:** {tc.get('status', 'Pending')}")
                        st.markdown("**Test Steps:**")
                        for i, step in enumerate(tc.get("steps", []), 1):
                            st.markdown(f"{i}. {step}")
                        st.markdown(f"**Expected Result:** {tc.get('expected_result', '')}")

            with tab3:
                st.markdown("### 📄 JSON Export Preview")
                st.json(result)

# Download Section
if 'test_cases' in st.session_state and st.session_state['test_cases']:
    st.markdown("---")
    st.markdown("### 💾 Export Test Cases")
    st.markdown("Download your generated test cases in your preferred format")

    result = st.session_state['test_cases']

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        # JSON download
        json_str = json.dumps(result, indent=2)
        st.download_button(
            label="📥 JSON",
            data=json_str,
            file_name="test_cases.json",
            mime="application/json",
            use_container_width=True,
            help="Download as JSON file"
        )

    with col2:
        # CSV download
        df_data = []
        for tc in result.get("test_cases", []):
            df_data.append({
                "ID": tc.get("id", ""),
                "Title": tc.get("title", ""),
                "Scenario": tc.get("scenario", ""),
                "Type": tc.get("type", ""),
                "Steps": "; ".join(tc.get("steps", [])),
                "Expected Result": tc.get("expected_result", ""),
                "Status": tc.get("status", "Pending")
            })
        df = pd.DataFrame(df_data)
        csv = df.to_csv(index=False).encode('utf-8')

        st.download_button(
            label="📥 CSV",
            data=csv,
            file_name="test_cases.csv",
            mime="text/csv",
            use_container_width=True,
            help="Download as CSV file"
        )

    with col3:
        # Excel download
        try:
            buffer = BytesIO()
            with pd.ExcelWriter(buffer, engine='openpyxl') as writer:
                df.to_excel(writer, index=False, sheet_name='Test Cases')

            st.download_button(
                label="📥 Excel",
                data=buffer.getvalue(),
                file_name="test_cases.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                use_container_width=True,
                help="Download as Excel file"
            )
        except ImportError:
            st.button("📥 Excel", disabled=True, use_container_width=True)
            st.caption("Install openpyxl to enable")

    with col4:
        # Text download
        text_content = f"AI TEST CASE GENERATOR\n"
        text_content += f"{'=' * 80}\n\n"
        text_content += f"MODULE: {result.get('module', 'N/A')}\n"
        text_content += f"TOTAL TEST CASES: {result.get('total_test_cases', 0)}\n"
        text_content += f"GENERATED: {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        text_content += f"{'=' * 80}\n\n"

        for tc in result.get("test_cases", []):
            text_content += f"[{tc.get('id', '')}] {tc.get('title', '')}\n"
            text_content += f"{'-' * 80}\n"
            text_content += f"Type: {tc.get('type', '')}\n"
            text_content += f"Scenario: {tc.get('scenario', '')}\n\n"
            text_content += "Steps:\n"
            for i, step in enumerate(tc.get("steps", []), 1):
                text_content += f"  {i}. {step}\n"
            text_content += f"\nExpected Result: {tc.get('expected_result', '')}\n"
            text_content += f"Status: {tc.get('status', 'Pending')}\n"
            text_content += f"{'=' * 80}\n\n"

        st.download_button(
            label="📥 Text",
            data=text_content,
            file_name="test_cases.txt",
            mime="text/plain",
            use_container_width=True,
            help="Download as plain text file"
        )

# Footer - Professional Branding with Logo
footer_logo = f'<img src="data:image/jpeg;base64,{logo_base64}" alt="Edvenswa Logo" style="max-width: 120px; height: auto; border-radius: 6px; opacity: 0.9;">' if logo_base64 else ''

st.markdown(f"""
<div class="footer">
    <div style="text-align: center; padding: 1.5rem 0;">
        <!-- Edvenswa Logo in Footer -->
        <div style="margin-bottom: 1rem;">
            {footer_logo}
        </div>
        <p style="font-size: 1rem; margin-bottom: 0.5rem;">
            Developed by <strong style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-size: 1.1rem;">Edvenswa</strong>
        </p>
        <p style="margin-top: 0.5rem; font-size: 0.75rem; color: #9ca3af;"> 
            AI Test Case Generator | Professional QA Automation Tool
        </p>
        <p style="margin-top: 0.75rem; font-size: 0.7rem; color: #d1d5db;">
            © 2025 Edvenswa. All rights reserved.
        </p>
    </div>
</div>
""", unsafe_allow_html=True)
