from openai import OpenAI
from dotenv import load_dotenv
import os
from tool_maneger import execute_tool
from tools import read_file



#load_dotenv("./.env")
load_dotenv(dotenv_path="../.env")

client = OpenAI(api_key=os.getenv("API_KEY"), base_url=os.getenv("BASE_URL"))
print("=" * 50)
print("My AI assistant...")
print("=" * 50)
role = {  "1": "You are a friendly school teacher. Explain every concept using simple language and real-life examples.",

    "2": "You are a senior Python developer. Explain programming concepts clearly and always include Python examples.",

    "3": "You are an experienced travel guide. Recommend places, food, transportation and travel tips.",

    "4": "You are a motivational coach. Encourage the user and give practical advice with a positive attitude.",

    "5": "You are a professional interviewer. Ask one interview question at a time and provide feedback after each answer."
}
print("\nChoose Your Role\n")

print("1. Teacher")
print("2. Python Expert")
print("3. Travel Guide")
print("4. Motivational Coach")
print("5. Interviewer")

messages = []   
role_choice = input("Select a role (1-5): ")

messages.append({
    "role": "system",
    "content": role.get(role_choice, "You are a helpful AI assistant.")
})

while True:
    user_input = input("You: ")
    tool_response = execute_tool(user_input)

    if user_input.lower().startswith("summarize"):
        file_name = user_input[10:].strip()
        file_content = read_file(f"data/{file_name}")
        
        prompt = f"Summarize the following file content:\n\n{file_content}"
        messages.append({
            "role": "user",
            "content": prompt
        })

    if user_input.lower().startswith("ask"):
        parts = user_input.split(maxsplit=2)
        #print(parts)
        file_name = parts[1]
        question = parts[2]
        file_content = read_file(f"data/{file_name}")
        prompt = f"""You are given a document.Answer the user's question using
        only the information present in the document.
        If the answer is not available,say:'I couldn't find that informationin the document.'
        Question: {question}
        Document:{file_content}"""
       
        messages.append({
            "role": "user",
            "content": prompt
        })
        

        response = client.chat.completions.create(
            model=os.getenv("MODEL"),
            messages=messages
        )
        print("Assistant: ", response.choices[0].message.content)
        messages.append({
            "role": "assistant",
            "content": response.choices[0].message.content
        })
        continue
    if user_input.lower() in ["exit", "quit"]:
        print("Assistant: Goodbye! Have a great day.")
        break
    if tool_response is not None:
            print("Assistant: ", tool_response)
            continue


    messages.append({
        "role": "user",
        "content": user_input
    })
    response = client.chat.completions.create(
        model=os.getenv("MODEL"),
        messages=messages
    )
    print("Assistant: ", response.choices[0].message.content)
    messages.append({
        "role": "assistant",
        "content": response.choices[0].message.content
    })
    
   
  

