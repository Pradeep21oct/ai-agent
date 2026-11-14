from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path=".env")

client = OpenAI(api_key=os.getenv("API_KEY"), base_url=os.getenv("BASE_URL"))
print("=" * 50)
print("My AI assistant...")
print("=" * 50)
messages = []
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Assistant: Goodbye! Have a great day.")
        break
    messages.append({
        "role": "user",
        "content": user_input
    })
    response = client.chat.completions.create(
        model=os.getenv("MODEL"),
        messages=messages
    )
    
    messages.append({
        "role": "assistant",
        "content": response.choices[0].message.content
    })
    print("=" * 50)
    print("Chat history:start")
    print("=" * 50)
    print("Assistant: ", response.choices[0].message.content)
    for message in messages:
        print(f"{message['role']}: {message['content']}")
    print("*" * 50)

