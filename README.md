# 📄 Universal PDF Q&A Assistant

## Overview

Universal PDF Q&A Assistant is an AI-powered web application that allows users to upload any PDF document and ask questions about its contents. The application extracts text from the uploaded PDF and uses Google's Gemini AI to generate accurate and context-aware answers based on the document.

## Features

* Upload any PDF document
* Ask questions related to the uploaded PDF
* AI-generated answers using Google Gemini
* PDF text extraction and processing
* Interactive and user-friendly interface
* Fast and accurate document understanding

## Technologies Used

* Python
* Streamlit
* Google Gemini API
* PyPDF
* Python Dotenv

## How It Works

1. Upload a PDF document.
2. The application extracts text from the PDF.
3. Enter a question related to the document.
4. Gemini AI analyzes the document content.
5. The application generates and displays an answer based on the uploaded PDF.

## Installation

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Future Enhancements

* Multi-PDF support
* Chat history
* Real RAG implementation using embeddings and vector databases
* PDF summarization
* Keyword highlighting
* Citation-based responses

## Project Goal

The goal of this project is to make document understanding easier by enabling users to interact with PDF files through natural language questions and receive intelligent AI-generated responses.

## Team

Developed as an AI-powered document question-answering solution using Streamlit and Google Gemini.
