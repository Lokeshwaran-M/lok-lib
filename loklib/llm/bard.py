

from Bard import Chatbot
# Paste your Bard Token (check README.md for where to find yours) 
token = "XAh2yKJMb0dYsIWgvzrPzFxPcHRv9M5K7oSO-2NUkGtC09UWwULiUEH3ebT_v_1fd4QS3A."
# Initialize Google Bard API
chatbot = Chatbot(token)

def res(prompt):
    response = chatbot.ask(prompt)
    return response['content']

