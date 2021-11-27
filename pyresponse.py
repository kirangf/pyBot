from datetime import datetime

def bot_response(input_text):
    user_message = str(input_text).lower()

    if user_message in ("hello", "hi", "hai"):
        return "Hi, How are you?"
    
    if user_message in ("who are you", "who are you?", "who r u?", "who r u"):
        return "I am py Bot"
    
    if user_message in ("what is the time now?", "time", "what's the time?", "whats the time", "time?", "time now"):
        date_time = datetime.now.strftime("%y-%m-%d %H:%M:%S")

        return str(date_time)
    
    return "Sorry, I dont understand you"
