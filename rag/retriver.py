from pathlib import Path

def load_documents():
    documents = {}
    folder=Path("knowledge")
    for file in folder.glob("*.txt"):
        documents[file.name] = file.read_text(encoding="utf-8")

    return documents

def retrive(query):
    documents = load_documents()
    for name, content in documents.items():
        if query.lower() in content.lower():
            return name, content
    return None, None