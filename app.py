import streamlit as st
import tempfile
import pymupdf4llm
from llama_cpp import Llama

# Load local model
llm = Llama(
    model_path="models/qwen2.5-3b-instruct-q4_k_m.gguf",
    n_ctx=4096,
    verbose=False
)

st.set_page_config(
    page_title="Local Document Q&A",
    page_icon="📄",
    layout="wide"
)

st.title("📄 Local-First Document Q&A")
st.subheader("PyMuPDF4LLM + Llama.cpp")

uploaded_file = st.file_uploader(
    "Upload PDF",
    type=["pdf"]
)

def split_sections(markdown_text):
    return markdown_text.split("\n# ")

def retrieve_context(question, sections):

    best_section = ""
    best_score = 0

    for section in sections:

        score = sum(
            word.lower() in section.lower()
            for word in question.split()
        )

        if score > best_score:
            best_score = score
            best_section = section

    return best_section

if uploaded_file is not None:

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".pdf"
    ) as tmp:

        tmp.write(uploaded_file.read())
        pdf_path = tmp.name

    with st.spinner("Extracting document..."):
        markdown_text = pymupdf4llm.to_markdown(pdf_path)

    sections = split_sections(markdown_text)

    st.success("Document processed successfully!")

    with st.expander("Preview Extracted Content"):
        st.text(markdown_text[:3000])

    question = st.text_input(
        "Ask a question about the document"
    )

    if st.button("Get Answer"):

        if not question:
            st.warning("Please enter a question.")

        else:

            context = retrieve_context(
                question,
                sections
            )

            prompt = f"""
You are a document assistant.

Use ONLY the provided context.

Context:
{context}

Question:
{question}

Answer clearly and concisely.
"""

            with st.spinner("Generating answer..."):

                response = llm(
                    prompt,
                    max_tokens=300
                )

            answer = response["choices"][0]["text"]

            st.markdown("## 🤖 Answer")
            st.write(answer)
