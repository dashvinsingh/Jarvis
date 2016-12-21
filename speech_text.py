#Requires PyAudio and PySpeech

import speech_recognition as sr
import datetime, webbrowser, pyglet, os, sys
from j_functions import *
from os import *
from j_music import *
from alarm  import *

r = sr.Recognizer()

with sr.Microphone() as source:
    print('Jarvis Initializing!')
    system('say Hi Dash! How can I help you today?')
    audio = r.listen(source)
    

try:
    text = r.recognize_google(audio).lower()
    #print(text)
    
#PLAY MUSIC
    if any(word in text for word in ['music', 'song', 'songs', 'play']):
        if any(word in text for word in  ['play', 'open']):
            song_list(text)
        if any(word in text for word in ['what', 'have', 'can you play','can', 'playlist']):
            with sr.Microphone() as source1:
                print('I can play these songs: \n{0}'.format(playlist()))
                system('say I can play songs from this playlist. Please choose one.')
                audio1 = r.listen(source1)
                new_text = r.recognize_google(audio1).lower()
                song_list(new_text)

#OPEN WEBSITE
    try:
        if any(word in text for word in ['website', 'open', '.com', 'internet']):
            lst = text.split()
            for item in lst:
                if ('.com' in item) or ('.net' in item) or ('.org' in item) or ('.ca' in item):
                    url = item
            system('say Opening: {0}'.format(url))
            print('Opening: http://{0}'.format(url))
            open_website('http://{0}'.format(url))
    except:
        system('say This is an invalid website command')

#TIME
    if any(word in text for word in  ['time']):
        try:
            if any(word in text for word in ['time', 'what', 'is', 'now']):
                current_time()
        except:
            system('say This is an invalid time command')

#DATE
    if any(word in text for word in ['date', 'day']):
        try:
            if any(word in text for word in ['date', 'what', 'is', 'today']):
                date_today()
        except:
            system('say This is an invalid date command')

#SET ALARM
    if any(word in text for word in ['set', 'alarm', 'set alarm']):
        print('Input the HOUR integer from 0 to 23')
        system('say INPUT the HOUR integer from 0 to 23')
        with sr.Microphone() as source2:
            hour_voice = r.listen(source2)
            hour_text = r.recognize_google(hour_voice)
            system('say Hour input is {0}'.format(hour_text))
            print('INPUT the MINUTE integer from 0 to 59')
            system('say INPUT the MINUTE ingteger from 0 to 59')
        with sr.Microphone() as source3:
            min_voice = r.listen(source3)
            min_text = r.recognize_google(min_voice)
            system('say Minute input is {0}'.format(min_text))
            main_alarm(int(hour_text), int(min_text))
        
            

#WHO CREATED YOU
    try:
        if any(word in text for word in ['name', 'your', 'who']):
            print('My Name is Jarvis 1.0, I was created by Dashvin Singh on Decomber 21, 2016')
            system('say My Name is Jarvis 1.0, I was created by Dashvin Singh on December 21, 2016')
    except:
        system("I don't understand what you mean")

        
except sr.UnknownValueError:
    print("Could you try that again please?")
    system("say Could you try that again Please?")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))


