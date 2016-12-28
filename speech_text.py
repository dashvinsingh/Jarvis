#Requires PyAudio and PySpeech

import speech_recognition as sr
import datetime, webbrowser, pyglet, sys
from j_functions import *
from os import *
from j_music import *
from j_translate import *
from j_math import *
from j_weather import *
from alarm  import *
import subprocess
#from j_GUI import exit_jarvis_total



def jarvis_bot():
    r = sr.Recognizer()
 
    with sr.Microphone() as source:
        print('Jarvis Initializing!')
        #system('say Hi Dash! How can I help you today?')
        system('afplay /Users/abhin/OneDrive\ -\ University\ of\ Toronto/CS108/Winter\ Projects/Python\ Projects/SpeechRec/Jarvis/siri1.mp3')
        audio = r.listen(source)
        text = r.recognize_google(audio).lower()
        jarvis_speech(text)



def jarvis_speech(text):
    try:
        #print(text)
        
    #PLAY MUSIC
        if any(word in text for word in ['music', 'song', 'songs', 'play']):
            if any(word in text for word in  ['play', 'open']):
                song_list(text)
            if any(word in text for word in ['what', 'have', 'can you play', 'playlist']):
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

    #TIME (Fixed)
        if any(word in text for word in  ['is the time']):
            try:
                if any(word in text for word in ['time', 'what', 'is', 'now']):
                    print(current_time())
                    system('say {0}'.format(current_time()))
            except:
                system('say This is an invalid time command')

    #DATE (Fixed)
        if any(word in text for word in ['date', 'day']):
            try:
                if any(word in text for word in ['date', 'what', 'is', 'today']):
                    print(date_today())
                    system('say {0}'.format(date_today()))
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

        try:
            #Addition
            if any(word in text for word in ['add', 'plus', 'addition', '+']):
                #print(text)
                addition(text)

            #Subtraction
            if any(word in text for word in ['minus', 'subtrct', 'subtraction', 'subtrcted', 'difference']):
                subtraction(text)

            #Multiplication
            if any(word in text for word in ['multiply', 'times', 'x', 'product', 'mulitplied', 'multiplies', 'multiplying']):
                multiplication(text)

            #Power
            if any(word in text for word in ['to the power of', 'power of', 'power', 'square', 'sqaured', 'cube', 'cubed']):
                power(text)

            #Square Root
            if any(word in text for word in ['square root', 'squared root', 'root']):
                sqrt(text)

            #SINE
            if any(word in text for word in ['sine', 'harmonic sign', 'sin', 'sign']):
                sin(text)

            #COSINE
            if any(word in text for word in ['cos', 'cosine', 'harmonic cosine', 'harmonic cos']):
                cos(text)

            #TANGENT
            if any(word in text for word in ['tan', 'tangent', 'harmonic tan', 'harmonic tangent']):
                tan(text)
        except:
            print('This is an invalid math command, please try again.')
            system('say This is an invalid math command, please try again.')
            jarvis_bot()
        
    

    #SHUT DOWN
        if any(word in text for word in ['shut down', 'turn off', 'shut down computer']):
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

    #RESTART
        if any(word in text for word in ['restart computer', 'restart']):
            with sr.Microphone() as s:
                print('Are you sure you want to restart? Yes = TRUE')
                system('say Are you sure you want to restart?')
                shut_down = r.listen(s)
                shut_text = r.recognize_google(shut_down)
                if 'yes' in shut_text:
                    print('Restarting Mac.')
                    system('say See you soon Dash')
                    #os.system("shutdown -h now")
                    subprocess.call(['osascript', '-e', 'tell app "System Events" to restart'])
                else:
                    print('Computer will not restart.')
                    system('say Computer will not restart')


    #GOOGLE SEARCH
        if any(word in text for word in ['google search', 'google']):
            google_search(text)

    #LIVE WEATHER
        try:
            if any(word in text for word in ['weather', 'forecast', 'tempurate']):
                if any(word in text for word in ['what is', 'weather in', 'weather']):
                    if any(word in text for word in ['weather in', 'here', 'me']):
                        if any(word in text for word in ['my location', 'me', 'here']):
                            city = current_location()
                            print('Getting weather information for: {0}'.format(city.title()))
                            one_line_weather(city)
                        else:
                            text = text.lower()
                            if any(word in text for word in ['what is ', 'weather in']):
                                city = extract_city(text)
                                print('Getting weather information for: {0}'.format(city.title()))
                                one_line_weather(city)
                        

                else:                            
                    print("Please tell me the city (ex. Bangkok, Thailand  or Toronto, Ontario, Canada)")
                    system('say Please tell me the city in the format requested')
                    with sr.Microphone() as weather_source:
                        city_voice = r.listen(weather_source)
                        city_text = r.recognize_google(city_voice)
                        print('Getting weather information for: {0}'.format(city_text.title()))
                        one_line_weather(city_text)

        except:
            print('Something might have gone wrong, please try again.')

    #WHAT CAN YOU DO
        if any(word in text for word in ['do', 'functions', 'operations']):
            print("I can: \nPlay music\nOpen a Website\nTell the Date and Time\
\nTranslate from English\nGive Weather Data\nSet an Alarm\nGoogle Search\nDo Math")
            system('say I can: Play music,Open a Website,Tell the Date and Time\
,Translate from English,Give Weather Data,Set an Alarm,Google Search,Do Math')
    #WHO CREATED YOU
        try:
            if any(word in text for word in ['name', 'your', 'who']):
                print('My Name is Jarvis 1.0, I was created by Dashvin Singh on Decomber 21, 2016')
                system('say My Name is Jarvis 1.0, I was created by Dashvin Singh on December 21, 2016')
        except:
            system("say I don't understand what you mean")

    #GOOD MORNING
        try:
            if any(word in text for word in ['good mornning', 'morning']):
                print('Good Morning Dashvin! Merry Christmas')
                system('say Good Morning Dashvin! Merry Christmas')
                current_time()
                date_today()
                one_line_weather('Mississauga Ontario Canada')
        except:
            system('say Something Went wrong')

    #EXIT JARVIS
        try:
            if any(word in text for word in ['exit jarvis', 'close jarvis', 'quit jarvis', 'exit yourself']):
 #               exit_jarvis_total()
                 system('say Press the Exit Button')
                 sys.exit()
        except:
            system("I didn't quite get that")
                            
    except sr.UnknownValueError:
        print("Could you try that again please?")
        system("say Could you try that again Please?")
        #jarvis_bot()
        
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))


