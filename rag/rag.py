from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI
import os
from similarity import cosine_similarity
from embedding import create_embedding  
from retriver import load_documents



#load_dotenv("./.env")
load_dotenv(dotenv_path="../.env")

client = OpenAI(api_key=os.getenv("API_KEY"), base_url=os.getenv("BASE_URL"))

documents = load_documents()
embeddings = {}
for file,content in documents.items():
    embeddings[file] = create_embedding(content)

print("=" * 40)
print("      My AI Assistant")
print("=" * 40)


while True:
    query = input("\nYou: ")
    if query.lower() in ["exit", "quit"]:
        print("Assistant: Goodbye! Have a great day.")
        break
    query_embedding = create_embedding(query)
    best_similarity = -1;
    best_document = None
    for file, embedding in embeddings.items():
        similarity = cosine_similarity(query_embedding, embedding)
        if similarity > best_similarity:
            best_similarity = similarity
            best_document = file
    context = documents[best_document]
    prompt = f"""Answer the question using onlythe following information.
    Context:{context}
    Question:{query}"""
    
    response = client.chat.completions.create(
        model=os.getenv("MODEL"),
        messages=[{"role": "user",
                    "content": prompt
                }]
    )
    print(f"\nAssistant: {response.choices[0].message.content}")
    





    
            
        

   

   

