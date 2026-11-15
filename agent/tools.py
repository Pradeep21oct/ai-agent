from datetime import datetime

def get_current_datetime():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def roll_dice():
    import random
    return random.randint(1, 6)

def generate_password(length=12):
    import random
    import string
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

def read_file(file_path):
    try:
        with open(file_path, "r") as file:
            return file.read()
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return f"An error occurred: {e}"