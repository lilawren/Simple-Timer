import time
import sys
from tkinter import *

minutes = 2
seconds = 0

def run_timer_label(label):
    def run_timer():
        global minutes
        global seconds
        minutes = int(e1.get())

        label.config(text=str("\r{minutes} Minutes {seconds} Seconds".format(minutes=minutes, seconds=seconds)))

        if minutes == 0 and seconds == 0:
            return
        elif seconds == 0:
            minutes -= 1
            seconds = 59
        else:
            seconds -= 1
        label.after(1000, run_timer)
    run_timer()

root = Tk()
root.title("Meditation Timer")
label = Label(root, fg="green")
label.pack()
e1 = Entry(root)
e1.pack()
b2 = Button(root, text='Start Timer', command=(run_timer_label(label)))
b2.pack()
button = Button(root, text='DESTROY', width=25, command=root.destroy)
button.pack()

root.mainloop()

