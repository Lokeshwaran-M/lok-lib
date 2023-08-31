from loklib import speech_senth as ss
import sys
print(" press Ctrl + D or Ctrl + Z to end ")
def chat():
    while True:
        print("cmd : ")

        pmt = sys.stdin.read()
        if "stop" in pmt.lower().split() :
            break
        print("\nnarrating : ")
        ss.say(pmt)

chat()