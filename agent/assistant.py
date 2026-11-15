from openai import OpenAI
from dotenv import load_dotenv
import os
from planner import choose_tool
from tools import (get_current_datetime,generate_password,roll_dice)


#load_dotenv(dotenv_path=".env")
load_dotenv(dotenv_path="../.env")

client = OpenAI(api_key=os.getenv("API_KEY"), base_url=os.getenv("BASE_URL"))
print("=" * 50)
print("My AI Agent...")
print("=" * 50)
messages = []
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Assistant: Goodbye! Have a great day.")
        break

    tool = choose_tool(user_input)
    if tool == "get_current_time":
        result = get_current_datetime()

    elif tool == "roll_dice":
        result = roll_dice()

    elif tool == "generate_password":
        result = generate_password()
    else:
        result = "No tool selected."

    prompt = f""" The User asked: {user_input}
            The tool returned:: {result}
            Answer the user naturally.don't add anything from your side in the answer. if tool is none, then answer it from llm model."""
    
    messages.append({
        "role": "user",
        "content": prompt
    })
    response = client.chat.completions.create(
        model=os.getenv("MODEL"),
        messages=messages
    )

    print("Assistant: ", response.choices[0].message.content)
   