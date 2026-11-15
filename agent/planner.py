from openai import OpenAI
from dotenv import load_dotenv
import os

#load_dotenv("./.env")
load_dotenv(dotenv_path="../.env")

client = OpenAI(api_key=os.getenv("API_KEY"), base_url=os.getenv("BASE_URL"))

def choose_tool(query):
     planner_prompt = f"""You are an AI planner.

Available tools:

1. get_current_time
   Use when the user asks for the current date or time.

2. roll_dice
   Use when the user asks to roll a dice.

3. generate_password
   Use when the user wants a secure password.

If no tool is required, return:

none
Return ONLY the tool name.

User Request:{query}
"""
     response = client.chat.completions.create(
         model=os.getenv("MODEL"),
         messages=[{"role": "user",
                     "content": planner_prompt
                 }]
     )
     return response.choices[0].message.content.strip()
     