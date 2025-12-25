from pypdf import PdfReader
from pathlib import Path

def extract_text_from_pdf(pdf_path):
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        if page.extract_text():
            text += page.extract_text()
    return text


if __name__ == "__main__":
    pdf_path = Path("data") / "resume" / "sample_resume.pdf"
    print(extract_text_from_pdf(pdf_path)[:1000])
