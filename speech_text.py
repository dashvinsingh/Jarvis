#Requires PyAudio and PySpeech

import speech_recognition as sr
import datetime, webbrowser, pyglet, sys
from j_functions import *
from os import *
from j_music import *
from j_translate import *
from alarm  import *
import subprocess
#from j_GUI import exit_jarvis_total

def jarvis_bot():
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

    #TRANSLATE ENGLISH TO WTV
        if any(word in text for word in ['translate', 'language','translator']):
##            print('What language do you want to translate from? ex. english')
##            system('say What language do you want to translate from?')
##            with sr.Microphone() as t_lang:
##                to_voice = r.listen(t_lang)
##                to_text = r.recognize_google(to_voice)
            print('What do you want to translate? Say Message in English.')
            system('say What do you want to translate?')
            with sr.Microphone() as source3:
                  message_voice = r.listen(source3)
                  message_text = r.recognize_google(message_voice)
            print('What language do you want to translate to? ex. spanish')
            system('say What language do you want to translate to?')
            with sr.Microphone() as source4:
                  language_voice = r.listen(source4)
                  language_text = r.recognize_google(language_voice)
                
            print('Translating: ({0}) to {1}'.format(message_text,language_text))
            system('say Translating: {0} to {1}'.format(message_text,language_text))
            translate(message_text, language_text.lower())
    # DO MATH

    ##    if any(word in text for word in ['add', 'plus', 'addition', 'math']):
    ##        split = text.split()
            

    #SHUT DOWN
        if any(word in text for word in ['shut down', 'turn off', 'computer']):
            with sr.Microphone() as s:
                print('Are you sure you want to shutdown? Yes = TRUE')
                system('say Are you sure you want to shutdown?')
                shut_down = r.listen(s)
                shut_text = r.recognize_google(shut_down)
                if 'yes' in shut_text:
                    print('Shutting down.')
                    system('say Good Bye Dash')
                    #os.system("shutdown -h now")
                    subprocess.call(['osascript', '-e', 'tell app "System Events" to shut down'])
                else:
                    print('Computer will not shut down.')
                    system('say Computer will not shut down')


    #GOOGLE SEARCH
        if any(word in text for word in ['google search', 'google']):
            google_search(text)

    #WHO CREATED YOU
        try:
            if any(word in text for word in ['name', 'your', 'who']):
                print('My Name is Jarvis 1.0, I was created by Dashvin Singh on Decomber 21, 2016')
                system('say My Name is Jarvis 1.0, I was created by Dashvin Singh on December 21, 2016')
        except:
            system("I don't understand what you mean")

    #EXIT JARVIS
        try:
            if any(word in text for word in ['exit jarvis', 'close jarvis', 'quit jarvis', 'exit yourself']):
 #               exit_jarvis_total()
                 system('say Press the Exit Button')
        except:
            system("I didn't quite get that")
                            
    except sr.UnknownValueError:
        print("Could you try that again please?")
        system("say Could you try that again Please?")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))


