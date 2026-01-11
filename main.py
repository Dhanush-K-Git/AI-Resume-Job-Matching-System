import re

def normalize_text(text):
    text = text.lower()
    text = text.replace("&", " ")
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()

import os
from PyPDF2 import PdfReader
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# ---- Skill list for gap analysis ----
SKILLS = [
    "python",
    "machine learning",
    "deep learning",
    "nlp",
    "scikit learn",
    "tensorflow",
    "pytorch",
    "data analysis",
    "pandas",
    "numpy",
    "TF-IDF",
    "cosine similarity"
]


# ---- Load resume text from PDF ----
def load_pdf_text(file_path):
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        if page.extract_text():
            text += page.extract_text()
    return text

# ---- Load job description ----
def load_text(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()

job_text = load_text("data/jobs/sample_job.txt")
print("\nAI Resume–Job Matching System")
print("-" * 35)


# ---- Extract skills from job description ----
job_text_lower = normalize_text(job_text)


job_skills = []
for skill in SKILLS:
    if skill in job_text_lower:
        job_skills.append(skill)

resume_folder = "data/resume"
resume_files = [f for f in os.listdir(resume_folder) if f.endswith(".pdf")]

results = []


print("\nResume–Job Match Scores:\n")

for resume_file in resume_files:
    resume_path = os.path.join(resume_folder, resume_file)
    resume_text = load_pdf_text(resume_path)

    # ---- Extract skills from resume ----
    resume_text_lower = normalize_text(resume_text)

    resume_skills = []
    for skill in SKILLS:
        if skill in resume_text_lower:
            resume_skills.append(skill)
    # ---- Skill gap analysis ----
    matching_skills = []
    missing_skills = []

    for skill in job_skills:
        if skill in resume_skills:
            matching_skills.append(skill)
        else:
            missing_skills.append(skill)


    # ---- Similarity score ----
    vectorizer = TfidfVectorizer(stop_words="english")
    vectors = vectorizer.fit_transform([resume_text_lower, job_text_lower])


    similarity = cosine_similarity(vectors[0], vectors[1])[0][0]

    results.append({
    "resume": resume_file,
    "score": round(similarity * 100, 2),
    "matching_skills": matching_skills,
    "missing_skills": missing_skills
})

# ---- Rank resumes by match score ----
results = sorted(results, key=lambda x: x["score"], reverse=True)
print("\nResume Ranking (Best Match First)")
print("-" * 30)

for idx, result in enumerate(results, start=1):
    print(f"{idx}. Resume: {result['resume']}")
    print(f"   Match Score      : {result['score']} %")
    print(f"   Matching Skills  : {', '.join(result['matching_skills']) if result['matching_skills'] else 'None'}")
    print(f"   Missing Skills   : {', '.join(result['missing_skills']) if result['missing_skills'] else 'None'}\n")


print("\nResume Ranking (Best to Worst):\n")

for idx, result in enumerate(results, start=1):
    print(f"{idx}. Resume: {result['resume']}")
    print(f"   Match Score: {result['score']} %")
    print(f"   Matching Skills: {', '.join(result['matching_skills']) if result['matching_skills'] else 'None'}")
    print(f"   Missing Skills: {', '.join(result['missing_skills']) if result['missing_skills'] else 'None'}\n")



    