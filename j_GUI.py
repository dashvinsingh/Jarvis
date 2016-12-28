from tkinter import *
from os import *
from speech_text import *
from j_functions import *
import speech_recognition as sr
import threading

os.chdir('/Users/abhin/OneDrive - University of Toronto/CS108/Winter Projects/Python Projects/SpeechRec/Jarvis')

r = sr.Recognizer()
class Jarvis_GUI:
    def __init__(self, master):
        self.frame = Frame(master, bg='black')
        self.frame.pack(expand=True)
        master.minsize(width=250, height=250)
        master.maxsize(width=300, height=300)
        master.config(bg='black')

        self.title = Label(self.frame, text = 'Jarvis!',font=('BPDots', 40), fg='green', bg='black')
        self.title.pack()

        self.button1 = Button(master, anchor=CENTER, command=start_jarvis, bg = 'black')
        self.photo=PhotoImage(file='mic.gif')
        self.photo.config(height=100, width=49)
        self.button1.config(image=self.photo, width=100, height=100, bg = 'black')
        self.button1.pack(side=BOTTOM, expand=YES)
        self.button2 = Button(master, text="STOP Command", command=stop_process)
        self.button2.pack()
        self.button3 = Button(master, text="Exit Jarvis", command=exit_jarvis_total)
        self.button3.pack()

    

def start_jarvis():
    jarvis_bot()
    a

def exit_jarvis_total():
    print('Exiting Jarvis, Good Bye Dash.')
    system('say Exiting Jarvis, Good Bye Dash.')
    root.destroy()
    sys.exit()
    return None

def stop_process():
    end_music()
    a


root = Tk()
jarvis_object = Jarvis_GUI(root)

root.title('Jarvis')

#root.mainloop()
def listen():
    def hi_jarvis():
        try:
            with sr.Microphone() as source:
                audio= r.listen(source)
                text = r.recognize_google(audio).lower()
                if text in ['hi jarvis', 'hey jarvis', 'jarvis', 'hello jarvis', 'hi']:
                    start_jarvis()
                    listen()
                else:
                    try:
                        listen()
                    except:
                        listen()
                        pass
        except:
            listen()
   
    a_thread = threading.Thread(target = hi_jarvis)
    a_thread.start()
system('say Hi Dash, How can I help you today?')
listen()
a = listen

root.mainloop()
