import time
import sys
from tkinter import *


def run_timer():
    global seconds, minutes, timer, v

    print("Pressed the button")

    if minutes == 0 and seconds == 0:
        return
    elif seconds == 0:
        minutes -= 1
        seconds = 59
    else:
        seconds -= 1
    timer.configure(text=v)
    v.set(str("\r{minutes} Minutes {seconds} Seconds".format(minutes=minutes, seconds=seconds)))
    root.after(1000, run_timer())


minutes = 2
seconds = 0


root = Tk()
v = StringVar()
v.set("")
root.title("Meditation Timer")

timer = Label(root, textvariable=v, fg="green")
timer.pack()

e1 = Entry(root)
e1.pack()

start = Button(root, text='Start Timer', command=run_timer)
start.pack()

root.mainloop()

