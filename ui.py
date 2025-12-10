import streamlit as st
from app import generate_test_cases
import json
import pandas as pd
from io import StringIO

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI Test Case Generator",
    layout="centered",
    page_icon="🧪"
)

# ---------------- STYLES ----------------
st.markdown("""
<style>
body {
    background-color: #f6f7fb;
}

.main {
    max-width: 1100px;
    margin: auto;
}

.card {
    background: white;
    padding: 20px;
    border-radius: 14px;
    box-shadow: 0 8px 20px rgba(0,0,0,0.04);
    margin-bottom: 20px;
}

.kpi {
    background: #f8f9fa;
    padding: 18px;
    border-radius: 12px;
    text-align: center;
}

.kpi h2 {
    margin: 0;
}

.kpi p {
    margin: 4px 0 0 0;
    color: #6c757d;
    font-size: 14px;
}

button {
    height: 3rem;
    font-weight: 600;
}
</style>
""", unsafe_allow_html=True)

# ---------------- STATE ----------------
if "test_cases" not in st.session_state:
    st.session_state.test_cases = None

# ---------------- HEADER ----------------
st.markdown("<div class='main'>", unsafe_allow_html=True)

st.title("AI Test Case Generator")
st.caption("Generate professional QA test cases with AI. Export as CSV, Text, or JSON.")

# ---------------- INPUT CARD ----------------
st.markdown("<div class='card'>", unsafe_allow_html=True)

preset = st.selectbox(
    "Example Presets",
    ["", "Login Form", "Dashboard with Filters", "User Registration API", "File Upload Module"]
)

module_text = st.text_area(
    "Module / Page Description",
    value=preset,
    height=140,
    placeholder="Describe the page, module, or API behavior"
)

col1, col2 = st.columns(2)
generate = col1.button("🚀 Generate Test Cases", use_container_width=True)
clear = col2.button("🧹 Clear Output", use_container_width=True)

st.markdown("</div>", unsafe_allow_html=True)

# ---------------- ACTION HANDLERS ----------------
if clear:
    st.session_state.test_cases = None
    st.toast("Output cleared ✅")

if generate:
    if not module_text.strip():
        st.warning("Please enter a module description")
    else:
        with st.spinner("Generating test cases..."):
            result = generate_test_cases(module_text)

        if not result or "error" in result:
            st.error("Generation failed")
            st.code(result.get("raw_response", "Unknown error"))
        else:
            st.session_state.test_cases = result
            st.success("Test cases generated successfully ✅")

# ---------------- OUTPUT ----------------
if st.session_state.test_cases:
    data = st.session_state.test_cases
    test_cases = data.get("test_cases", [])

    # -------- KPI CARDS --------
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    k1, k2, k3 = st.columns(3)

    k1.markdown(
        f"<div class='kpi'><h2>{len(test_cases)}</h2><p>Total Test Cases</p></div>",
        unsafe_allow_html=True
    )
    k2.markdown(
        "<div class='kpi'><h2>CSV</h2><p>Export</p></div>",
        unsafe_allow_html=True
    )
    k3.markdown(
        "<div class='kpi'><h2>Text</h2><p>Export</p></div>",
        unsafe_allow_html=True
    )

    st.markdown("</div>", unsafe_allow_html=True)

    # -------- PREPARE DATAFRAME --------
    rows = []
    for tc in test_cases:
        rows.append({
            "ID": tc["id"],
            "Scenario": tc["scenario"],
            "Type": tc["type"],
            "Steps": " → ".join(tc["steps"]),
            "Expected Result": tc["expected_result"]
        })

    df = pd.DataFrame(rows)

    # -------- TABS --------
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    tab1, tab2, tab3 = st.tabs(["📊 Table View", "📄 Text View", "🧩 JSON"])

    with tab1:
        st.dataframe(df, use_container_width=True)

    with tab2:
        text_output = []
        for tc in test_cases:
            text_output.append(f"""
ID: {tc['id']}
Scenario: {tc['scenario']}
Type: {tc['type']}
Steps:
""" + "\n".join([f"  {i+1}. {s}" for i, s in enumerate(tc["steps"])]) + f"""
Expected Result: {tc['expected_result']}
{'-'*60}
""")
        st.text("".join(text_output))

    with tab3:
        st.json(data)

    st.markdown("</div>", unsafe_allow_html=True)

    # -------- EXPORTS --------
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("Export")

    csv_buffer = StringIO()
    df.to_csv(csv_buffer, index=False)

    e1, e2 = st.columns(2)
    e1.download_button(
        "⬇ Download CSV",
        csv_buffer.getvalue(),
        "test_cases.csv",
        "text/csv"
    )
    e2.download_button(
        "⬇ Download Text",
        "\n".join(text_output),
        "test_cases.txt",
        "text/plain"
    )

    st.markdown("</div>", unsafe_allow_html=True)

else:
    st.info("No test cases yet. Enter a module description and generate.")

st.markdown("</div>", unsafe_allow_html=True)
