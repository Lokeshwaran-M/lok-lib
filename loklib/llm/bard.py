import os
from Bard import Chatbot
from dotenv import load_dotenv

if load_dotenv(".env"):
    load_dotenv(".env")
elif load_dotenv():
    load_dotenv()
else:
    print(".env is not defined")

BARDTOKEN = os.getenv("BARDTOKEN")
# Paste your Bard Token (check README.md for where to find yours) 
token = BARDTOKEN
# Initialize Google Bard API
chatbot = Chatbot(token)

def res(prompt):
    response = chatbot.ask(prompt)
    return response['content']

