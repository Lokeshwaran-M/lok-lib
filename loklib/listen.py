
import pyaudio
import wave
import os
import time
import datetime
import sys

import whisper
model = whisper.load_model("tiny.en")

import speech_recognition as sr
r = sr.Recognizer()

# Initialize audio input/output devices
audio = pyaudio.PyAudio()
stream = audio.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)

# handelling audio folder error
if not os.path.exists('./audio'):
    os.makedirs('./audio')


def out(duration=20):
    frames = []
    # print(f"Recording audio for {duration} seconds...")
    print("Listening : ")
    for i in range(int(44100 / 1024 * duration)):
        data = stream.read(1024)
        frames.append(data)
    print("processing : ")
    # recording and saving audio file
    current_time = datetime.datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
    au_wave_file = f"au-{current_time}.wav"
    wave_file = wave.open(f"./audio/{au_wave_file}", "wb")
    wave_file.setnchannels(1)
    wave_file.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
    wave_file.setframerate(44100)
    wave_file.writeframes(b''.join(frames))
    wave_file.close()
    au_path = f"./audio/{au_wave_file}"

    res = []
    # transcribing by whisper
    res_whisper = model.transcribe(au_path)
    res.append(res_whisper["text"])
  
    # transcribing by google
    try :
        with sr.AudioFile(au_path) as source :
            audio_data = r.record(source)
            res_google = r.recognize_google(audio_data)
            res.append(res_google)
    except Exception as e:
        print(f"exception occurred : {e}")
        print(f"res : {res}")

    os.remove(au_path)
    return res


# Close audio input/output devices
def close_audio():
    stream.stop_stream()
    stream.close()
    audio.terminate()




if __name__ == "__main__":
    while True:
        print(out(5))
   







