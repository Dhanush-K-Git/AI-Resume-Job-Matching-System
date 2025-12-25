# AI Resume–Job Matching System

##  Overview

The AI Resume–Job Matching System is an NLP-based application that automatically matches multiple resumes with a given job description.
It analyzes resume content, computes relevance scores using TF-IDF and cosine similarity, performs skill gap analysis, and ranks resumes based on suitability.

This project demonstrates practical application of Natural Language Processing (NLP) techniques for recruitment automation.


## Features
   PDF Resume Parsing (supports multiple resumes)
   Job Description Text Parsing
   TF-IDF Vectorization + Cosine Similarity Scoring

🧠 Skill Gap Analysis
    Identifies matched skills
    Highlights missing skills

🏆 Automatic Resume Ranking
🧪 Tested locally with real resume and job description files


## Tech Stack
Programming Language: Python
Libraries & Tools:
scikit-learn
pandas
numpy
PyPDF2
nltk


Concepts Used:
Natural Language Processing (NLP)
Text preprocessing
TF-IDF
Cosine similarity

## Project Structure
AI-Resume-Job-Matching-System/
│
├── data/
│   ├── resumes/              # PDF resumes
│   └── job_description/      # Job description text
│
├── resume_parser.py
├── job_parser.py
├── text_loader.py
├── main.py
├── requirements.txt
└── README.md


## How to Run the Project

1️⃣ Clone the repository
git clone https://github.com/Dhanush-K-Git/AI-Resume-Job-Matching-System.git
cd AI-Resume-Job-Matching-System

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Add files
Place resume PDFs inside:data/resumes/
Place job description text file inside:data/job_description/

4️⃣ Run the application
  python main.py

## Sample Output
  Resume: Resume_1.pdf
  Match Score: 0.82
  Matched Skills: Python, NLP, Machine Learning
  Missing Skills: Docker, AWS

  Resume: Resume_2.pdf
  Match Score: 0.65

  Top Ranked Resume: Resume_1.pdf


## How It Works

-Extracts text from PDF resumes
-Preprocesses resume and job description text
-Converts text into TF-IDF vectors
-Computes cosine similarity scores
-Performs skill matching against predefined skill sets
-Ranks resumes based on relevance score

## 🎯 Use Case
This system can be used by recruiters or HR teams to:
- Automatically shortlist resumes
- Identify skill gaps for candidates
- Reduce manual resume screening effort
- Improve hiring efficiency


## Future Enhancements

Integrate transformer-based embeddings (BERT)
Add Streamlit web interface
Support DOCX resumes
Improve skill extraction using skill taxonomy
Deploy as a web application


## Author
Dhanush Kumar
GitHub: https://github.com/Dhanush-K-Git
