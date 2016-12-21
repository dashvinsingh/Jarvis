import datetime, webbrowser, pyglet, os, sys
import speech_recognition as sr

def play_music(song):
    song = pyglet.media.load(os.path.abspath(song))
    player = pyglet.media.Player()
    player.queue(song)
    player.play()
    r = sr.Recognizer()
    #print('Say Stop to end music')
 
##    while True and text != 'stop':
##        with sr.Microphone() as source:
##            audio = r.listen(source)
##        text = r.recognize_google(audio)
##        if any(word in text for word in ['stop', 'music', 'end']):
##            player.pause()
##            break

    while True:
        end = input('Type 0 to stop: ')
        if end == '0':
            player.pause()
            break
