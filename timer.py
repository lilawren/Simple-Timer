import time
import sys
from tkinter import *

def start_timer():
    global minutes
    minutes = int(e1.get())
    run_timer()

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

    v.set(str("\r{minutes} Minutes {seconds} Seconds".format(minutes=minutes, seconds=seconds)))
    timer.configure(text=v)
    root.after(1000, run_timer)


minutes = 0
seconds = 0

root = Tk()
v = StringVar()
v.set("")
root.title("Meditation Timer")

timer = Label(root, textvariable=v, fg="green")
timer.pack()

e1 = Entry(root)
e1.pack()

start = Button(root, text='Start Timer', command=start_timer)
start.pack()

root.mainloop()

