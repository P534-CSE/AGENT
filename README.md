# AGENT

This repository contains a simple PDF-based retrieval-augmented generation (RAG) example.

## Setup

1. Create a virtual environment.
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project root with:

   ```bash
   OPENAI_API_KEY=your_api_key_here
   PDF_PATH=C:\Users\M.Pavitra\OneDrive\Desktop\CAT\document.pdf
   ```

4. Run the app:

   ```bash
   python pdf_rag.py
   ```

5. Type a question and press Enter. Type `exit` to quit.

## Notes

- The script loads a PDF file, converts it into embeddings, stores it in a FAISS vector database, and answers questions using OpenAI.
- Make sure your PDF location is correct before running the script.
