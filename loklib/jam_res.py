import os
import time

import whisper
model = whisper.load_model("base.en")

from loklib.llm import ChatGPT as cht
ch = cht(headless=True,wait=10)

def jam_gpt(au_path):
    pmt = model.transcribe(au_path)
    os.remove(au_path)
    pmt = pmt["text"]
    ch.send_prompt(pmt)
    time.sleep(5)
    res = ch.get_gpt_response()
    ch.send_prompt("none")
    time.sleep(5)
    res = ch.get_gpt_response()
    return res[-1]


  







