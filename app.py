import time
import pygetwindow

active_window_name = ""
startTime = 0

while True:

    new_window_name = (pygetwindow.getActiveWindowTitle())

    if active_window_name != new_window_name:
        endTime = time.time()
        if active_window_name != "":
            time_used = endTime - startTime
            print(active_window_name)
            print("Time used: " + str(int(time_used)) + " sec.")
        active_window_name = new_window_name
        startTime = time.time()

    time.sleep(5)
