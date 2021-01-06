def send_message(Parent, message):
    Parent.SendStreamMessage(message)
    return

def send_whisper(Parent, user, message):
    Parent.SendStreamWhisper(user, message)
    return

def log(Parent, message):
    Parent.Log("Poker Bot", message)
    return