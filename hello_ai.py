from openai import OpenAI
from dotenv import load_dotenv
import os
from pathlib import Path

load_dotenv(dotenv_path=Path(__file__).resolve().with_name(".env"))

api_key = os.getenv("API_KEY") or os.getenv("OPENAI_API_KEY")
if not api_key:
    raise RuntimeError(
        "Missing API key. Set API_KEY or OPENAI_API_KEY in the environment or .env file."
    )

client = OpenAI(
    base_url=os.getenv("BASE_URL"),
    api_key=api_key
)
response = client.chat.completions.create(
    model=os.getenv("MODEL"),
    messages=[
        {
            "role": "user",
            "content": "Hello, how are you?"
        }
    ]
)
print(response.choices[0].message.content)
