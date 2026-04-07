# rag.py
import os
import numpy as np
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from langchain_core.embeddings import Embeddings

# ----------------------------- Configuration ---------------------------------
USE_MOCK = True  # Always True: fully offline, no OpenAI

# ----------------------------- Mock Embeddings --------------------------------
class MockEmbeddings(Embeddings):
    def embed_documents(self, texts):
        return [np.random.rand(1536).tolist() for _ in texts]

    def embed_query(self, text):
        return np.random.rand(1536).tolist()

# ----------------------------- Load documents ---------------------------------
def load_docs(folder="docs"):
    """
    Load all .txt files from a folder as Document objects.
    """
    docs = []

    if not os.path.exists(folder):
        print(f"[Warning] Folder '{folder}' does not exist!")
        return docs

    files = [f for f in os.listdir(folder) if f.endswith(".txt")]
    if not files:
        print(f"[Warning] No .txt documents found in '{folder}'")
        return docs

    for file in files:
        path = os.path.join(folder, file)
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
            docs.append(Document(page_content=content))
    return docs

# ----------------------------- Create FAISS Vectorstore ----------------------
def create_vectorstore(folder="docs"):
    docs = load_docs(folder)
    embeddings = MockEmbeddings()

    if not docs:
        # Dummy vectorstore if no documents exist
        db = FAISS.from_texts(["empty"], embeddings)
    else:
        db = FAISS.from_documents(docs, embeddings)

    return db, embeddings

# ----------------------------- Query Vectorstore -----------------------------

def rag_answer(db, embeddings, query, k=3):
    if not db:
        print("RAG vectorstore is empty!")
        return []

    # Unpack (document, score) tuples safely
    results = db.similarity_search_with_score(query, k=k)

    if not results:
        print("No relevant documents found.")
        return []

    print("\n--- Retrieved Documents ---")
    for i, (doc, score) in enumerate(results):
        print(f"Doc {i+1} (score: {score:.4f}): {doc.page_content[:500]}...\n")
    print("--------------------------\n")

    docs = [doc for doc, score in results]
    return docs
