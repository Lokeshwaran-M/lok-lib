
# lok-lib

A library to power an AI digital assistant

It is a Python library that I built to use for my own personal projects. It contains modules to build AI assistant and other general-purpose tools. Some modules are built from scratch while others contain dependencies on other libraries or modules, so it may break in the future. Feel free to raise an issue if you encounter any problems. 

It is still under development

---

## JAM - AI :

[JAM](https://github.com/Lokeshwaran-M/Jam-AI) is an AI assistant that I'm currently building using the lok-lib library. check out below

```
https://github.com/Lokeshwaran-M/Jam-AI
```
---

## Instalation :

use pip and install in your local site-packages directory

```
pip install git+https://github.com/Lokeshwaran-M/lok-lib
```


## DOCS :

refere [test.ipynb](test.ipynb) for understandig library

> The documentation for each module will be updated soon

---

## Requirement :

use pip and download the [lok-lib](https://github.com/Lokeshwaran-M/lok-lib) in your local site-packages directory

```
pip install git+https://github.com/Lokeshwaran-M/lok-lib
```
### ffmpeg audio 

```
# on Ubuntu or Debian
sudo apt update && sudo apt install ffmpeg

# on Arch Linux
sudo pacman -S ffmpeg

# on MacOS using Homebrew (https://brew.sh/)
brew install ffmpeg

# on Windows using Chocolatey (https://chocolatey.org/)
choco install ffmpeg

# on Windows using Scoop (https://scoop.sh/)
scoop install ffmpeg
```

### text to speech

```
sudo apt install alsa-utils
sudo apt install espeak
```
### python module :

If there are errors with the dependencies during installation, you can try installing specific packages using the following pip commands

```bash
pip install pyaudio

# whisper
pip install -U openai-whisper
## for updated version
pip install git+https://github.com/openai/whisper.git 
## To upgrade 
pip install --upgrade --no-deps --force-reinstall git+https://github.com/openai/whisper.git

## whisper dependencies
pip install torch ffmpeg-python tiktoken numba setuptools-rust

pip install openai

## text to speech
pip install gtts playsound pyttsx3

```


