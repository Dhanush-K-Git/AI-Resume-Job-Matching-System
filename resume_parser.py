import pdfplumber
import re

def extract_text_from_pdf(pdf_path):
    """Extracts and cleans text from a PDF for semantic matching."""
    text = ""
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + " "
        
        # Cleaning: This ensures the 'Vector' we create later is accurate
        text = re.sub(r'\s+', ' ', text)  # Remove extra spaces/newlines
        text = re.sub(r'[^\x00-\x7F]+', ' ', text)  # Remove special symbols
        
        return text.strip()
    except Exception as e:
        print(f"Error reading {pdf_path}: {e}")
        return None

if __name__ == "__main__":
    # Test it with one of your resumes
    from pathlib import Path
    test_path = Path("data") / "resumes" / "sample_resume.pdf" # Adjust name if needed
    print(extract_text_from_pdf(test_path))
