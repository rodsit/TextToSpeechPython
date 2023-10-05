# TextToSpeechPython
A simple python script that performs text to speech: 
# Made with python 3.11
# pip install pyttsx3
import pyttsx3
engine = pyttsx3.init()
text = "Hello, this is an example of text-to-speech synthesis using pyttsx3."
engine.say(text)
engine.runAndWait()
