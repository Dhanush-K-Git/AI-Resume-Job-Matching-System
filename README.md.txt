# AI Resume–Job Matching System

An AI-based resume screening system that compares multiple resumes against a job description, calculates match scores, and performs skill gap analysis using NLP techniques.

---

## 🚀 Features
- Parses multiple resume PDFs
- Reads job descriptions from text files
- Calculates resume–job match scores using TF-IDF and cosine similarity
- Extracts and compares skills between resumes and job descriptions
- Ranks resumes from best to worst match
- Provides explainable output (matching & missing skills)

---

## 🧠 How It Works (High Level)
1. Resume PDFs and job descriptions are converted into text
2. Text is vectorized using TF-IDF
3. Cosine similarity is used to compute match scores
4. Predefined skill keywords are extracted from both resumes and job descriptions
5. Skill gap analysis identifies missing and matching skills
6. Resumes are ranked based on match score

---

## 🛠 Tech Stack
- Python
- scikit-learn
- PyPDF2
- Natural Language Processing (NLP)

---

## 📂 Project Structure
AI-Resume-Job-Matching-System/
│
├── data/
│ ├── resume/
│ │ └── sample_resume.pdf
│ ├── jobs/
│ │ └── sample_job.txt
│
├── main.py
├── requirements.txt
└── README.md


---

## ▶️ How to Run
1. Clone the repository
2. Install dependencies:

pip install -r requirements.txt
3. Run the application:

python main.py

---

## 📌 Sample Output

---
Resume Ranking (Best Match First)

Resume: ai_ml_sample_resume.pdf
Match Score : 34.82 %
Matching Skills : python, machine learning, nlp
Missing Skills : tensorflow, pytorch


---

## 📈 Future Improvements
- Support for DOCX resumes
- Skill weightage based on importance
- Web interface using Streamlit
- Integration with embeddings or LLMs

---

## 👤 Author
Dhanush Kumar

