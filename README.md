# AI-Powered Resume Job Matching System 🚀

This project is a high-performance **Semantic Search Engine** designed to rank resumes against job descriptions. By utilizing modern **Natural Language Processing (NLP)**, it moves beyond simple keyword counting to understand the actual meaning and context of a candidate's experience.

## 🛠️ Tech Stack
* **Language:** Python 3.12
* **Embedding Model:** Sentence-Transformers (`all-MiniLM-L6-v2`)
* **Vector Database:** ChromaDB for persistent, high-speed storage
* **Document Parsing:** pdfplumber for precise text extraction

## 🧠 Core Architecture
1. **Data Ingestion:** The system extracts text from PDF resumes using `pdfplumber`.
2. **Semantic Vectorization:** Text is converted into 384-dimensional embeddings using a Transformer model, capturing semantic relationships.
3. **Persistence:** Embeddings are stored in a local **ChromaDB vault**, ensuring data is indexed and searchable without re-processing.
4. **Contextual Ranking:** The system calculates **Cosine Similarity** between a Job Description and the resume vault to identify the best conceptual matches.

## 📈 Major Upgrades (Version 2.0)
* **Evolved from TF-IDF:** Replaced word-frequency matching with **Deep Learning embeddings** for better synonym handling.
* **Persistent Database:** Integrated ChromaDB to handle scaling and local data storage.
* **Isolated Environment:** Implemented a dedicated `.venv` for professional dependency management.
## 🚀 How to Run the Project
### 1. Clone & Setup
```powershell
git clone [https://github.com/Dhanush-K-Git/AI-Resume-Job-Matching-System.git](https://github.com/Dhanush-K-Git/AI-Resume-Job-Matching-System.git)
cd AI-Resume-Job-Matching-System