import datetime
import time, webbrowser
import pyglet
import os, sys

def first_alarm():
    print("Hi! Welcome to the first alarm clock app. \nPlease follow the instructions below\n")

    hour = input('Input the hour integer between 0 and 23:\n')
    minute = input('Input the minute integer between 0 and 59:\n')
    message = input('Enter the alarm message:\n')

    alarm_time = datetime.time(int(hour), int(minute))
    print('Alarm has been set for {0}:{1}'.format(hour, minute))

    while True:
        cur = datetime.time(time.localtime().tm_hour, time.localtime().tm_min)
        if cur == alarm_time:
            print(message)
            break

def second_alarm():
    print("\nHi! Welcome to the second alarm clock app. \nPlease follow the instructions below\n")

    hour = input('Input the hour integer between 0 and 23:\n')
    minute = input('Input the minute integer between 0 and 59:\n')
    message = input('Enter the alarm message:\n')
    url = "https://www.youtube.com/watch?v=RbiEESkyaeM"
    alarm_time = datetime.time(int(hour), int(minute))
    print('\nAlarm has been set for {0}:{1}'.format(hour, minute))

    while True:
        cur = datetime.time(time.localtime().tm_hour, time.localtime().tm_min)
        if cur == alarm_time:
            print(message)
            break
    print('\nThe current time is {0}.'.format(cur))
    webbrowser.open(url)

def third_alarm():
    print("\nHi! Welcome to the third alarm clock app. \nPlease follow the instructions below\n")
    
    hour = input('Input the hour integer between 0 and 23:\n')
    minute = input('Input the minute integer between 0 and 59:\n')
    #message = input('Enter the alarm message:\n')
    
    if int(hour) in range(0,24) and int(minute) in range(0,60):    
        alarm_time = datetime.time(int(hour), int(minute))
    else:
        print('VALUE ERROR\nPlease make sure of the following:\n\
    1. Hour (first) parameter is between 0 and 23\n    2. Minute (second) parameter is between 0 and 59.\nPlease call the function again.')
        sys.exit()
        
    snooze_per = input('Enter the max snooze period (eg. 2 mins, 5 mins):\n')
    snooze_max = input('Enter the maximum snooze limit (eg. how many mins from initial alarm):\n')
    counter = 0
    
    print('\nAlarm has been set for {0}'.format(alarm_time))
    counter = 0
    try:
        while True:
            cur = datetime.time(time.localtime().tm_hour, time.localtime().tm_min)
            if cur == alarm_time:
                #print(message)
                print('\nThe current time is {0}. Alarm Ringing, Wake Up!'.format(cur))
                song = pyglet.media.load(os.path.abspath('ring2.mp3'))
                player = pyglet.media.Player()
                player.queue(song)
                player.play()
                while True:
                    end = input('Type 0 to stop, 1 to snooze\n')
                    if end == '1' and (counter < int(snooze_max)):
                        player.pause()
                        alarm_time = datetime.time(time.localtime().tm_hour, (time.localtime().tm_min + int(snooze_per)))
                        counter += int(snooze_per)
                        print('You have snoozed for {0} mins.'.format(counter))
                        break
                    elif end == '0':
                        player.pause()
                        sys.exit()
                    elif end == '1' and (counter >= int(snooze_max)):
                        player.pause()
                        print('You have reached the snooze limit. The time is {0}. Alarm will stop.'.format(cur))
                        sys.exit()
    except (KeyboardInterrupt):
        print('Alarm has been stopped, please reset it by calling the function again.')
        

            

def main_alarm(hour, minute, snooze_per = 0, snooze_max=0):
##    print("\nHi! Welcome to the third alarm clock app. \nPlease follow the instructions below\n")

    if hour in range(0,24) and minute in range(0,60):    
        alarm_time = datetime.time(int(hour), int(minute))
    else:
        print('VALUE ERROR\nPlease make sure of the following:\n\
    1. Hour (first) parameter is between 0 and 23\n    2. Minute (second) parameter is between 0 and 59.\nPlease call the function again.')
        sys.exit()
    print('\nAlarm has been set for {0}\n'.format(alarm_time))
    counter = 0
    try:
        while True:
            cur = datetime.time(time.localtime().tm_hour, time.localtime().tm_min)
            if cur == alarm_time:
                #print(message)
                print('\nThe current time is {0}. Alarm Ringing, Wake Up!'.format(cur))
                song = pyglet.media.load(os.path.abspath('ring2.mp3'))
                player = pyglet.media.Player()
                player.queue(song)
                player.play()
                while True:
                    end = input('Type 0 to stop, 1 to snooze\n')
                    if end == '1' and (counter < int(snooze_max)):
                        player.pause()
                        alarm_time = datetime.time(time.localtime().tm_hour, (time.localtime().tm_min + int(snooze_per)))
                        counter += int(snooze_per)
                        print('You have snoozed for {0} mins.'.format(counter))
                        break
                    elif end == '0':
                        player.pause()
                        sys.exit()
                    elif end == '1' and (counter >= int(snooze_max)):
                        player.pause()
                        print('You have reached the snooze limit. The time is {0}. Alarm will stop.'.format(cur))
                        sys.exit()
    except (KeyboardInterrupt):
        print('Alarm has been stopped, please reset it by calling the function again.')
        
       

if __name__ == "__main__":
    print('Hi! Welcome to the alarm clock program. There are two functions you can run:\n\
   1. third_alarm()\n     -This function will ask you for information in the \
   shell.\n   2. main_alarm(hour, min,...)\n     -This function will requre certain parameters to run.\n\
To reset an alarm after starting its loop just hit "ctrl + C" in the shell.\n\
Have Fun!')
