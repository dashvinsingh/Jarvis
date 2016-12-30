#Requires PyAudio and PySpeech

import speech_recognition as sr
import datetime, webbrowser, pyglet, sys
from j_functions import *
from os import *
from j_music import *
from j_translate import *
from j_math import *
from j_weather import *
from j_movies import *
from Sports.j_soccer import *
from alarm  import *

import subprocess
#from j_GUI import exit_jarvis_total



def jarvis_bot():
    r = sr.Recognizer()
 
    with sr.Microphone() as source:
        print('Jarvis Initializing!')
        #system('say Hi Dash! How can I help you today?')
        system('afplay /Users/abhin/OneDrive\ -\ University\ of\ Toronto/CS108/Winter\ Projects/Python\ Projects/SpeechRec/Jarvis/misc/siri1.mp3')
        audio = r.listen(source)
        text = r.recognize_google(audio).lower()
        jarvis_speech(text)


silent = True
def jarvis_speech(text, silent=False):

    r = sr.Recognizer()
##    if silent == True:
##        system("osascript -e 'set volume output muted true'")
    try:
        #print(text)
        
    #PLAY MUSIC
        if any(word in text for word in ['music', 'song', 'songs', 'play']):
            if any(word in text for word in  ['play', 'open']):
                song_list(text)
            if any(word in text for word in ['what', 'have', 'can you play', 'playlist']):
                with sr.Microphone() as source1:
                    print('I can play these songs: \n{0}'.format(playlist()))
                    if slience == False:
                        system('say I can play songs from this playlist. Please choose one.')
                    audio1 = r.listen(source1)
                    new_text = r.recognize_google(audio1).lower()
                    song_list(new_text)

    #OPEN WEBSITE (With Silent)
        try:
            if any(word in text for word in ['website', 'open', '.com', 'internet']):
                lst = text.split()
                for item in lst:
                    if ('.com' in item) or ('.net' in item) or ('.org' in item) or ('.ca' in item):
                        url = item
                if silent == False:
                    system('say Opening: {0}'.format(url))
                print('Opening: http://{0}'.format(url))
                open_website('http://{0}'.format(url))
        except:
            if silent == False:
                system('say This is an invalid website command')
            else:
                print('This is an invalid website command')

    #TIME (With Silence)
        if any(word in text for word in  ['is the time', 'time', ' time']):
            try:
                if any(word in text for word in ['time', 'what', 'is', 'now']):
                    print(current_time())
                    if silent == False:
                        system('say {0}'.format(current_time()))
            except:
                if silent == False:
                    system('say This is an invalid time command')
                else:
                    print("This is an invalid time command")

    #DATE (With Silence)
        if any(word in text for word in ['date', 'day']):
            try:
                if any(word in text for word in ['date', 'what', 'is', 'today']):
                    print(date_today())
                    if silent == False:
                        system('say {0}'.format(date_today()))
            except:
                if silent == False:
                    system('say This is an invalid date command')
                else:
                    print("This is an invalid date command")

    #SET ALARM (With Silence)
        if any(word in text for word in ['set', 'alarm', 'set alarm']):
            if silent == True:
                hour = input('Input the HOUR integer from 0 to 23')
            else:
                print('Input the HOUR integer from 0 to 23')
                system('say INPUT the HOUR integer from 0 to 23')
                with sr.Microphone() as source2:
                    hour_voice = r.listen(source2)
                    hour_text = r.recognize_google(hour_voice)
                    system('say Hour input is {0}'.format(hour_text))
            if silent == True:
                minute = input('INPUT the MINUTE integer from 0 to 59')
            else:
                print('INPUT the MINUTE integer from 0 to 59')
                system('say INPUT the MINUTE ingteger from 0 to 59')
                with sr.Microphone() as source3:
                    min_voice = r.listen(source3)
                    min_text = r.recognize_google(min_voice)
                    system('say Minute input is {0}'.format(min_text))
            if silent == False:
                main_alarm(int(hour_text), int(min_text))
            else:
                main_alarm(int(hour), int(minute))

    #TRANSLATE ENGLISH TO WTV (With Sielnce)
        if any(word in text for word in ['translate', 'language','translator']):
##            print('What language do you want to translate from? ex. english')
##            system('say What language do you want to translate from?')
##            with sr.Microphone() as t_lang:
##                to_voice = r.listen(t_lang)
##                to_text = r.recognize_google(to_voice)
            if silent == False:
                print('What do you want to translate? Say Message in English.')
                system('say What do you want to translate?')
                with sr.Microphone() as source3:
                      message_voice = r.listen(source3)
                      message_text = r.recognize_google(message_voice)
            else:
                message = input('What do you want to translate? Type message in English\n')

            if silent == False:
                print('What language do you want to translate to? ex. spanish')
                system('say What language do you want to translate to?')
                with sr.Microphone() as source4:
                      language_voice = r.listen(source4)
                      language_text = r.recognize_google(language_voice)
            if silent == True:
                language = input('What language do you want to translate to? ex. spanish\n')
                
            if silent == False:
                print('Translating: ({0}) to {1}'.format(message_text,language_text))
                system('say Translating: {0} to {1}'.format(message_text,language_text))
                translate(message_text, language_text.lower())
            else:
                print('Translating: ({0}) to {1}'.format(message,language))
                translate(message, language.lower(), silent = True)
                
    # DO MATH (With Silence)

        try:
            #Addition
            if any(word in text for word in ['add', 'plus', 'addition', '+']):
                #print(text)
                addition(text, silent)

            #Subtraction
            if any(word in text for word in ['minus', 'subtrct', 'subtraction', 'subtrcted', 'difference']):
                subtraction(text, silent)

            #Multiplication
            if any(word in text for word in ['multiply', 'times', 'x', 'product', 'mulitplied', 'multiplies', 'multiplying']):
                multiplication(text, silent)

            #Power
            if any(word in text for word in ['to the power of', 'power of', 'power', 'square', 'sqaured', 'cube', 'cubed']):
                power(text, silent)

            #Square Root
            if any(word in text for word in ['square root', 'squared root', 'root']):
                sqrt(text, silent)

            #SINE
            if any(word in text for word in ['sine', 'harmonic sign', 'sin', 'sign']):
                sin(text, silent)

            #COSINE
            if any(word in text for word in ['cos', 'cosine', 'harmonic cosine', 'harmonic cos']):
                cos(text, silent)

            #TANGENT
            if any(word in text for word in ['tan', 'tangent', 'harmonic tan', 'harmonic tangent']):
                tan(text, silent)
        except:
            print('This is an invalid math command, please try again.')
            if silent == False:
                system('say This is an invalid math command, please try again.')
 #           jarvis_bot()
        
    

    #SHUT DOWN (With Silence)
        if any(word in text for word in ['shut down', 'turn off', 'shut down computer']):
            if silent == False:
                with sr.Microphone() as s:
                    print('Are you sure you want to shutdown? Yes = TRUE')
                    system('say Are you sure you want to shutdown?')
                    shut_down = r.listen(s)
                    shut_text = r.recognize_google(shut_down)
            else:
                shut_text = input('Are you sure you want to shutdown? Yes = TRUE')
            if 'yes' in shut_text.lower():
                print('Shutting down.')
                if silent == False:
                    system('say Good Bye Dash')
                #os.system("shutdown -h now")
                subprocess.call(['osascript', '-e', 'tell app "System Events" to shut down'])
            else:
                print('Computer will not shut down.')
                if silent == False:
                    system('say Computer will not shut down')

    #RESTART (With Silence)
        if any(word in text for word in ['restart computer', 'restart']):
            if silent == False:
                with sr.Microphone() as s:
                    print('Are you sure you want to restart? Yes = TRUE')
                    system('say Are you sure you want to restart?')
                    shut_down = r.listen(s)
                    shut_text = r.recognize_google(shut_down)
            else:
                shut_text = input('Are you sure you want to restart? Yes = TRUE')
            if 'yes' in shut_text:
                print('Restarting Mac.')
                if silent == False:
                    system('say See you soon Dash')
                #os.system("shutdown -h now")
                subprocess.call(['osascript', '-e', 'tell app "System Events" to restart'])
            else:
                print('Computer will not restart.')
                if silent == False:
                    system('say Computer will not restart')


    #GOOGLE SEARCH (With Silence)
        if any(word in text for word in ['google search', 'google']):
            if silent == False:
                google_search(text)
            else:
                google_search(text, silent=True)

    #LIVE WEATHER (With Silence, still to test)
        try:
            if any(word in text for word in ['weather', 'forecast', 'tempurate']):
                if any(word in text for word in ['what is', 'weather in']):
                    if any(word in text for word in ['weather in', 'here', 'me']):
                        if any(word in text for word in ['my location', 'me', 'here']):
                            city = current_location()
                            print('Getting weather information for: {0}'.format(city.title()))
                            if silent == False:
                                one_line_weather(city)
                            else:
                                one_line_weather(city, True)

                        else:
                            text = text.lower()
                            if any(word in text for word in ['what is ', 'weather in']):
                                city = extract_city(text)
                                print('Getting weather information for: {0}'.format(city.title()))
                                if silent == False:
                                    one_line_weather(city)
                                else:
                                    one_line_weather(city, True)

                        

                else:
                    if silent == False:
                        print("Please tell me the city (ex. Bangkok, Thailand  or Toronto, Ontario, Canada)")
                        system('say Please tell me the city in the format requested     ')
                        with sr.Microphone() as weather_source:
                            city_voice = r.listen(weather_source)
                            city_text = r.recognize_google(city_voice)
                            print('Getting weather information for: {0}'.format(city_text.title()))
                            one_line_weather(city_text)
                    else:
                        city = input('Please type the city (ex. Bangkok, Thailand  or Toronto, Ontario, Canada)\n')
                        print('Getting weather information for: {0}'.format(city.title()))
                        one_line_weather(city, True)
        except:
            print('Something might have gone wrong, please try again.')

    #GET MOVIE INFO
        if any(word in text for word in ['movie information', 'movie data', 'movie']):
            if any(word in text for word in ['movie information', 'movie data', 'movie stats', 'movie info']):
                if silent == False:
                    print('Please tell me the name of the movie')
                    system('say Please tell me the name of the movie')
                    with sr.Microphone() as movie_source:
                        movie_voice = r.listen(movie_source)
                        movie_text = r.recognize_google(movie_voice)
                        print('Here is the information for {0}\n'.format(movie_text.title()))
                        get_m_basic_info(movie_text)
                        system('say Here is the information you are looking for')
                else:
                    movie_text = input('INPUT the name of the movie.\n')
                    print('Here is the information for {0}:\n'.format(movie_text.title()))
                    get_m_basic_info(movie_text)

    #GET TV SHOW INFO
        if any(word in text for word in ['tv information', 'tv data', 'tv']):
            if any(word in text for word in ['tv information', 'tv data', 'tv stats', 'tv info', 'tv shows']):
                if silent == False:
                    print('Please tell me the name of the TV Show')
                    system('say Please tell me the name of the TV Show')
                    with sr.Microphone() as tv_source:
                        tv_voice = r.listen(tv_source)
                        tv_text = r.recognize_google(tv_voice)
                        print('Here is the information for {0}\n'.format(tv_text.title()))
                        get_tv_basic_info(tv_text)
                        system('say Here is the information you are looking for')
                else:
                    tv_text = input('INPUT the name of the TV Show.\n')
                    print('Here is the information for {0}:\n'.format(tv_text.title()))
                    get_tv_basic_info(tv_text)

    #English Premier League Information
        if any(word in text for word in ['standings', 'team stats', 'stats', 'teams', 'soccer', 'football', 'english', 'league', 'games', 'next']):
            #LEAGUE STANDINGS
            if any(word in text for word in ['standings', 'table']):
                if silent == False:
                    print('Standings for the English Premier League')
                    (get_standings())
                    system('say Here are the current standings of the Premier League')
                else:
                    print('Standings for the English Premier League')
                    get_standings()
                
            #TEAM STATS
            if any(word in text for word in ['team', 'stats', 'information']):
                team_name = extract_name(text)
                print(get_team_stats(team_name))
                if silent == False:
                    system('say Here are the stats for {0}'.format(team_name))

            if any(word in text for word in ['next match', 'next game', 'next','game', 'games']):
                days = extract_match_num(text)
                team_name = extract_name(text)
                g_list = next_game_com(team_name, days)
                for item in g_list:
                    print(item)
                if silent == False:
                    string = g_list[len(g_list)-1]
                    index = string.find('(')
                    system('say {0} have {1} games in the next {2} days'.format(team_name.title(), days,string[index+1:string.find(' ',index)]))
                        
        #RESULT (SCORE)            
        if any(word in text for word in ['versus', 'score', 'vs']):
            if any(word in text for word in ['versus', 'score', 'vs', 'and']):
                fs = get_raw_score(extract_t1(text), extract_t2(text))
                if type(fs) == dict:
                    print("Final Score: {0} {1}-{2} {3}".format(fs['home'], fs[fs['home']], fs[fs['away']], fs['away']))
                    if silent == False:
                        system('say Final Score: {0} {1} and {2} {3}'.format(fs['home'], fs[fs['home']], fs['away'], fs[fs['away']]))
                else:
                    print(get_raw_score(extract_t1(text), extract_t2(text)))
                    if silent == False:
                          system('say {0}'.format('This Match has not started.'))
                         
    #WHAT CAN YOU DO (With silence)
        if any(word in text for word in ['what can you do', 'functions', 'operations', 'can do', 'jarvis do']):
            print("I can: \nPlay music\nOpen a Website\nTell the Date and Time\nTranslate from English\nGive Weather Data\nSet an Alarm\nGoogle Search\nDo Math")
            if silent == False:
                system('say I can: Play music,Open a Website,Tell the Date and Time\
    ,Translate from English,Give Weather Data,Set an Alarm,Google Search,Do Math')
    #WHO CREATED YOU (With silence)
        try:
            if any(word in text for word in ['name', 'your', 'who']):
                print('My Name is Jarvis 1.0, I was created by Dashvin Singh on Decomber 21, 2016')
                if silent == False:
                    system('say My Name is Jarvis 1.0, I was created by Dashvin Singh on December 21, 2016')
        except:
            if silent == False:
                system("say I don't understand what you mean")
            else:
                print("I don't understand what you mean")

    #GOOD MORNING (With Silence)
        try:
            if any(word in text for word in ['good mornning', 'morning']):
                print('Good Morning Dashvin!')
                if silent == False:
                    system('say Good Morning Dashvin!')
                    print(current_time())
                    system('say {0}'.format(current_time()))
                    print(date_today())
                    system('say {0}'.format(date_today()))
                    one_line_weather('Mississauga Ontario Canada')
                else:
                    print(current_time())
                    print(date_today())
                    one_line_weather("Mississauaga Ontario Canada", True)
      
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
        if silent == False:
            system("say Could you try that again Please?")
        #jarvis_bot()
        
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))


