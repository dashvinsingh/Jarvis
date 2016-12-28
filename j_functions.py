import webbrowser, pyglet, os, sys, calendar
import speech_recognition as sr
from os import *
from time import *
from datetime import *
from google import search
global player
def play_music(song):
    song = pyglet.media.load(os.path.abspath(song))
    global player
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
def end_music():
    player.pause()
    pass
    
##    while True:
##        end = input('Type 0 to stop: ')
##        if end == '0':
##            player.pause()
##            break

def open_website(url):
    webbrowser.open(url)

def current_time():
    hour = localtime().tm_hour
    mins = localtime().tm_min
    sec = localtime().tm_sec
    if hour > 12:
        hour_cus = hour - 12
        if mins < 10:
            return('The time right now is: {0}:0{1} PM'.format(hour_cus, mins))
        else:
            return('The time right now is: {0}:{1} PM'.format(hour_cus, mins))
    else:
        hour_cus = hour
        if mins < 10:
            return('The time right now is: {0}:0{1} AM'.format(hour, mins))
        else:
            return('The time right now is: {0}:{1} AM'.format(hour, mins))
   
            

def date_today():
    now = datetime.now()
    day = now.day
    month = now.month
    year = now.year
    my_date = date.today()
    day_eng = calendar.day_name[my_date.weekday()]
    month_eng = calendar.month_name[month]
    final_date = "{0}, {1} {2} {3}".format(day_eng,str(day),month_eng,str(year))
    return('The date today is: {0}.'.format(final_date))

def date_time():
    pass

def google_search(search_text):
    #google search how to get away with murder
    lst = search_text.split()
    if 'google' in lst:
        lst.remove('google')
    if 'search' in lst:
        lst.remove('search')
    if 'ask' in lst:
        lst.remove('ask')
    search_text= ' '.join(lst)
    x = 'http://www.google.com/search?q={0}&btnG=Google+Search'.format(search_text)
    print('Searching for: ({0}) on Google'.format(search_text))
    system("say 'Searching for: ({0}) on Google'".format(search_text))
    webbrowser.open(x)

def quit_jarvis():
    exit_jarvis()
