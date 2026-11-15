from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI
import os
from similarity import cosine_similarity


#load_dotenv("./.env")
load_dotenv(dotenv_path="../.env")

client = OpenAI(api_key=os.getenv("API_KEY"), base_url=os.getenv("BASE_URL"))

text1 = "Python is a programming language."
text2 = "ram playing ball."

response1 = client.embeddings.create(
    model=os.getenv("MODEL_EMBEDDING"),
    input=text1
).data[0].embedding

response2 = client.embeddings.create(
    model=os.getenv("MODEL_EMBEDDING"),
    input=text2
).data[0].embedding

print(len(response1))
print(len(response2))

score = cosine_similarity(response1, response2)
print(score)

