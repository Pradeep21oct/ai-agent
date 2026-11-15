from openai import OpenAI
from dotenv import load_dotenv
import os
from tool_maneger import execute_tool



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
    

    if user_input.lower() in ["exit", "quit"]:
        print("Assistant: Goodbye! Have a great day.")
        break
    if tool_response is not None:
            print("Assistant: ", tool_response)
            continue
    #if "dice" in user_input.lower() or "die" in user_input.lower():
       # print("Assistant: You rolled a", roll_dice())
        #continue
    #if "password" in user_input.lower() or "pwd" in user_input.lower():
       # print("Assistant: Your generated password is", generate_password())
       # continue
    #if "time" in user_input.lower() or "datetime" in user_input.lower() or "clock" in user_input.lower() or "now" in user_input.lower():
       # print("Assistant: The current datetime is", get_current_datetime())
       # continue

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
    
   
  

