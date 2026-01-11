import os
import chromadb
from chromadb.utils import embedding_functions
from resume_parser import extract_text_from_pdf

# 1. Setup Persistent Storage
# This creates a folder 'resume_vault' where your vectors will live permanently
client = chromadb.PersistentClient(path="./resume_vault")

# 2. Choose the Brain (Embedding Model)
# We use 'all-MiniLM-L6-v2'. It's fast, popular, and runs locally.
sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="all-MiniLM-L6-v2"
)

# 3. Create a 'Collection' (Like a table in a database)
# If it exists, we load it; if not, we create it.
collection = client.get_or_create_collection(
    name="resumes_collection", 
    embedding_function=sentence_transformer_ef
)

def ingest_resumes(directory):
    """Processes all PDFs in a folder and adds them to ChromaDB."""
    for filename in os.listdir(directory):
        if filename.endswith(".pdf"):
            path = os.path.join(directory, filename)
            print(f"Vectorizing: {filename}...")
            
            text = extract_text_from_pdf(path)
            
            if text:
                # Add to ChromaDB with Metadata
                # 'ids' must be unique. We use the filename.
                collection.add(
                    documents=[text],
                    metadatas=[{"source": filename}],
                    ids=[filename]
                )
                print(f"Done! {filename} is now in the database.")

if __name__ == "__main__":
    RESUME_PATH = "data/resumes"
    if not os.path.exists(RESUME_PATH):
        print(f"Error: Folder '{RESUME_PATH}' not found!")
    else:
        ingest_resumes(RESUME_PATH)
        print(f"\nTotal resumes in database: {collection.count()}")