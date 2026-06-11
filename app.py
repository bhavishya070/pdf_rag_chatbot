import streamlit as st
from pypdf import PdfReader
from google import genai
from dotenv import load_dotenv
import os

# Load API key
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

st.set_page_config(
    page_title="Universal PDF Q&A Assistant",
    page_icon="📄",
    layout="wide"
)

st.title("📄 Universal PDF Q&A Assistant")
st.subheader("📁 Upload PDF & Ask Questions")

# Check API key
if not api_key:
    st.error("GEMINI_API_KEY not found in .env file")
    st.stop()

# Gemini client
client = genai.Client(api_key=api_key)

# Upload PDF
uploaded_file = st.file_uploader(
    "Upload any PDF",
    type=["pdf"]
)

if uploaded_file:

    pdf_reader = PdfReader(uploaded_file)

    pdf_text = ""

    for page in pdf_reader.pages:
        text = page.extract_text()
        if text:
            pdf_text += text + "\n"

    st.success("PDF Loaded Successfully!")

    st.write(f"**Total characters:** {len(pdf_text)}")

    with st.expander("Preview PDF Text"):
        st.text(pdf_text[:3000])

    question = st.text_input(
        "Ask your question from the uploaded PDF"
    )

    if st.button("Get Answer"):

        if not question:
            st.warning("Please enter a question.")
        else:

            prompt = f"""
You are a PDF assistant.

Use ONLY the information provided below.

PDF Content:
{pdf_text}

Question:
{question}

Answer clearly and concisely.
"""

            try:

                with st.spinner("Analyzing PDF..."):

                    response = client.models.generate_content(
                        model="gemini-2.5-flash",
                        contents=prompt
                    )

                st.markdown("## 🤖 Answer")
                st.write(response.text)

            except Exception as e:
                st.error(f"Gemini Error: {e}")