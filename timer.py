import time
import sys
from tkinter import *




def run_timer_label(label):
    global minutes
    def run_timer():
        global seconds
        global minutes
        minutes = e1.get()
        label.config(text=str("\r{minutes} Minutes {seconds} Seconds".format(minutes=minutes, seconds=seconds)))

        '''if minutes == 0 and seconds == 0:
            return
        elif seconds == 0:
            minutes -= 1
            seconds = 59
        else:
            seconds -= 1'''
        label.after(1000, run_timer)

    print(minutes)
    minutes = e1.get()
    run_timer()

root = Tk()
root.title("Meditation Timer")

minutes = IntVar()
minutes.set(0)
seconds = 0

label = Label(root, fg="green")
label.pack()

e1 = Entry(root)
e1.pack()

b2 = Button(root, text='Start Timer', command=(run_timer_label(label)))
b2.pack()

root.mainloop()

