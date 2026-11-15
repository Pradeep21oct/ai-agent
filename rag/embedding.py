from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv(dotenv_path="../.env")

client = OpenAI(api_key=os.getenv("API_KEY"), base_url=os.getenv("BASE_URL"))   

def create_embedding(content):
    return client.embeddings.create(
        model=os.getenv("MODEL_EMBEDDING"),
        input=content
    ).data[0].embedding 