#Requires PyAudio and PySpeech

import speech_recognition as sr
import datetime, webbrowser, pyglet, os, sys
from jarvis_functions import *
from os import *

r = sr.Recognizer()

with sr.Microphone() as source:
    print('Jarvis Initializing!')
    system('say Hi Dash! How can I help you today?')
    audio = r.listen(source)

try:
    text = r.recognize_google(audio).lower()

    if any(word in text for word in ['music', 'play', 'song']):
        list_ = ['drake', 'hotline', 'bling', "drake's"]
        if any(word in text for word in list_):
            system('say Playing: Hotline Bling by Drake')
            print('Playing: Hotline Bling by Drake')
            play_music(os.path.abspath('Hotline_bling.mp3'))

        list_ = ['james', 'bay', 'hold', 'back', 'the', 'river']
        if any(word in text for word in list_):
            system('say Playing: Hold Back the River by James Bay')
            print('Playing: Hold Back the River by James Bay')
            play_music(os.path.abspath('hbtr.mp3'))
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))


