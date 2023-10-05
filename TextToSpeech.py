# Python 3.11 
import pyttsx3
engine = pyttsx3.init(
text = "Hello, this is an example of text-to-speech synthesis using pyttsx3."
engine.say(text)
engine.runAndWait()
