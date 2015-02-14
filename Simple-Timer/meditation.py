import time
import sys

time_start = time.time()
seconds = 0
minutes = 2

while True:

    time.sleep(1)
    if seconds == 0:
        minutes -= 1
        seconds = 59
    else:
        seconds -= 1

    sys.stdout.write("\r{minutes} Minutes {seconds} Seconds".format(minutes=minutes, seconds=seconds))
    sys.stdout.flush()