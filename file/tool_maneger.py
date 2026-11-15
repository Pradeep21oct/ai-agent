from tools import(get_current_datetime,
                   roll_dice,
                   generate_password)
def execute_tool(user_input):
    input_lower = user_input.lower()
    if "dice" in input_lower or "die" in input_lower:
        return roll_dice()
    if "password" in input_lower or "pwd" in input_lower:
        return generate_password()
    if "time" in input_lower or "datetime" in input_lower or "clock" in input_lower or "now" in input_lower:
        return get_current_datetime()
    return None
