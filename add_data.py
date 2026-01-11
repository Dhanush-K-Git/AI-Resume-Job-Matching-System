import chromadb

# 1. Connect to the storage we created earlier
client = chromadb.PersistentClient(path="./chroma_storage")
collection = client.get_collection(name="resume_collection")

# 2. These represent the resumes you want to store
# Later, we will write code to read your actual PDF files
collection.add(
    documents=[
        "Python Developer with experience in AI and FastAPI.",
        "Biotechnology graduate with a focus on Machine Learning.",
        "Technical Support Engineer with 4 months of experience."
    ],
    ids=["id1", "id2", "id3"],
    metadatas=[
        {"source": "python_dev.pdf"},
        {"source": "biotech_grad.pdf"},
        {"source": "tech_support.pdf"}
    ]
)

print(f"Successfully added {collection.count()} resumes to the database!")