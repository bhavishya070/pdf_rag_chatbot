# 📄 Local-First PDF Q&A Assistant

A lightweight Retrieval-Augmented Generation (RAG) application that allows users to upload PDF documents and ask questions about their content.

This project follows a local-first approach using **PyMuPDF4LLM** for document extraction and **Llama.cpp** for local language model inference.

---

## 🚀 Features

- Upload PDF documents
- Extract structured content using PyMuPDF4LLM
- Convert documents into Markdown format
- Retrieve relevant context from the document
- Answer questions using a local LLM
- Offline document question answering
- Lightweight RAG workflow

---

## 🏗️ Architecture

```
PDF Upload
    ↓
PyMuPDF4LLM
    ↓
Markdown Extraction
    ↓
Context Retrieval
    ↓
Llama.cpp
    ↓
Answer Generation
```

---

## 🛠️ Technologies Used

- Python
- Streamlit
- PyMuPDF4LLM
- PyMuPDF
- Llama.cpp
- Qwen2.5-3B-Instruct GGUF Model

---

## 📂 Project Structure

```
PDF_RAG_CHATBOT/
│
├── app.py
├── requirements.txt
├── AGENT.md
├── SKILLS.md
├── README.md
│
└── models/
    └── qwen2.5-3b-instruct-q4_k_m.gguf
```

---

## ⚙️ Installation

### 1. Clone Repository

```bash
git clone <repository-url>
cd PDF_RAG_CHATBOT
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

### 3. Activate Environment

Windows:

```bash
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Download GGUF Model

Download:

```
Qwen2.5-3B-Instruct-Q4_K_M.gguf
```

Place it inside:

```text
models/
```

---

## ▶️ Run Application

```bash
streamlit run app.py
```

---

## 📖 How It Works

1. User uploads a PDF document.
2. PyMuPDF4LLM extracts content and converts it to Markdown.
3. The document is divided into sections.
4. Relevant context is retrieved based on the user's question.
5. Llama.cpp processes the retrieved context.
6. The system generates an answer locally.

---

## 🎯 Objectives

- Build a local-first document intelligence system.
- Reduce dependency on cloud APIs.
- Implement a lightweight RAG workflow.
- Enable offline PDF question answering.

---

## 🔮 Future Improvements

- Vector database integration
- Semantic search using embeddings
- Multi-document support
- Improved retrieval ranking
- Chat history support

---

## 👨‍💻 Author

Bhavishya Beesaiah Gari

Internship Project – PDF RAG Chatbot using PyMuPDF4LLM and Llama.cpp
