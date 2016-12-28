from os import *
from j_functions import *
os.chdir('/Users/abhin/OneDrive - University of Toronto/CS108/Winter Projects/Python Projects/SpeechRec/Jarvis/Songs')
import random

def playlist():
    return("James Bay: Hold Back the River\
\nDrake: Hotline Bling\
\nAdele: Hello\
\nAdele: Send my Love\
\nEd Sheeran: All of the Stars\
\nEd Sheeran: Give me love\
\nEd Sheeran: Latch (Acoustic)\
\nColdplay: A Sky full of stars\n")


def song_list(text):
    os.chdir('/Users/abhin/OneDrive - University of Toronto/CS108/Winter Projects/Python Projects/SpeechRec/Jarvis/Songs')
    text = text
    list_ = ['drake', 'hotline', 'bling', "drake's"]
    if any(word in text for word in list_):
        print('Playing: Hotline Bling by Drake')
        system('say Playing: Hotline Bling by Drake')
        play_music(('Hotline_bling.mp3'))
        

    list_ = ['james', 'bay', 'hold', 'back', 'the', 'river']
    if any(word in text for word in list_):
        print('Playing: Hold Back the River by James Bay')
        system('say Playing: Hold Back the River by James Bay')
        play_music(('HoldBackJamesBay.mp3'))
        

    if any(word in text for word in ['ed', 'sheeran']):
        list_ = ['all', 'of', 'the', 'stars']
        if any(word in text for word in list_):
            name = 'All of the stars by Ed Sheeran'
            print('Playing: {0}'.format(name))
            system('say Playing: {0}'.format(name))
            play_music(('all_of_the_stars_ed.mp3'))
            

        list_ = ['give', 'me', 'love']
        if any(word in text for word in list_):
            name = 'Give me Love by Ed Sheeran'
            print('Playing: {0}'.format(name))
            system('say Playing: {0}'.format(name))
            play_music(('give_me_love_ed.mp3'))
            

        list_ = ['latch', 'acoustic']
        if any(word in text for word in list_):
            name = 'Latch (Acoustic) by Ed Sheeran'
            system('say Playing: {0}'.format(name))
            print('Playing: {0}'.format(name))
            play_music(('latch_ed.mp3'))

    if any(word in text for word in ['coldplay', 'cold']):
        list_ = ['sky', 'full', 'of', 'stars']
        if any(word in text for word in list_):
            name = 'A sky full of Stars by Coldplay'
            print('Playing: {0}'.format(name))
            system('say Playing: {0}'.format(name))
            play_music(('sky_full_of_stars_coldplay.mp3'))

    if any(word in text for word in ['adele']):
        list_ = ['hello', 'from', 'the', 'other']
        if any(word in text for word in list_):
            name = 'Hello by Adele'
            print('Playing: {0}'.format(name))
            system('say Playing: {0}'.format(name))
            play_music(('hello_adele.mp3'))

        list_ = ['send', 'my', 'love']
        if any(word in text for word in list_):
            name = 'Send my Love by Adele'
            print('Playing: {0}'.format(name))
            system('say Playing: {0}'.format(name))
            play_music(('send_my_love_adele.mp3'))
    if any(word in text for word in ['christmas']):
        os.chdir('/Users/abhin/OneDrive - University of Toronto/CS108/Winter Projects/Python Projects/SpeechRec/Jarvis/Songs/c_songs')
        lst = ['Feliz Navidad- Jose Feliciano lyrics HQ', 'Have Yourself a Merry Little Christmas by Frank Sinatra', "Idina Menzel Ft.Michael Bublé - Baby It's Cold Outside (Lyrics)", "It's Beginning To Look A Lot Like Christmas", "It's the Most Wonderful Time of the Year (Lyrics).", "Jingle Bell Rock- Lyrics", "John Lennon - So this is christmas with lyrics", "Last Christmas by Taylor Swift +Lyrics", "Let it snow! By_Dean Martin Lyrics _)", "Mariah Carey - All I Want For Christmas Is You - Lyrics", "Mariah Carey - Joy to the World (audio)", "Mele Kalikimaka", "Michael BubléWinter Wonderland", "Pentatonix - Little Drummer Boy (HD LYRICS)", "ROCKIN AROUND THE CHRISTMAS TREE", "Rudolph the Red-Nosed Reindeer", "Santa Tell Me (With Lyrics) - Ariana Grande", "Silent Night (with lyrics)", "Sleigh Ride Lyrics"]
        song = random.choice(lst)
        print('Playing: {0}'.format(song))
        system('say Playing: Random Christmas Song.')
        play_music('{0}.mp3'.format(song))


        
