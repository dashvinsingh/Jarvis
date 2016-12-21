#Requires PyAudio and PySpeech

import speech_recognition as sr
import datetime, webbrowser, pyglet, os, sys

r = sr.Recognizer()

with sr.Microphone() as source:
    print('Say something!')
    audio = r.listen(source)


try:
    print('You said: ' + r.recognize_google(audio))
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))

text = r.recognize_google(audio).lower()

if any(word in text for word in ['music', 'play', 'song']):
    list_ = ['drake', 'hotline', 'bling', "drake's"]
    if any(word in text for word in list_):
        song = pyglet.media.load(os.path.abspath('Hotline_Bling.mp3'))
        player = pyglet.media.Player()
        player.queue(song)
        player.play()

    list_ = ['james', 'bay', 'hold', 'back', 'the', 'river']
    if any(word in text for word in list_):
        song = pyglet.media.load(os.path.abspath('hbtr.mp3'))
        player = pyglet.media.Player()
        player.queue(song)
        player.play()


