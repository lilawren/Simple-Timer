import time
import sys
from tkinter import *

root = Tk()

w = Label(root, text="Hello, World!")
w.pack()

root.mainloop()


minutes = int(input('Enter number of minutes:'))
seconds = 0

time_start = time.time()

while True:
    sys.stdout.write("\r{minutes} Minutes {seconds} Seconds".format(minutes=minutes, seconds=seconds))
    sys.stdout.flush()
    time.sleep(0.05)

    if minutes == 0 and seconds == 0:
        break
    elif seconds == 0:
        minutes -= 1
        seconds = 59
    else:
        seconds -= 1