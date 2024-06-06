import time
import threading
import customtkinter
from CTkListbox import *
import pygetwindow

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("800x650")


def track_windows(listbox):

    active_window_name = ""
    start_time = 0

    while True:
        new_window_name = pygetwindow.getActiveWindowTitle()

        if active_window_name != new_window_name:
            end_time = time.time()
            if active_window_name != "":
                time_spent = end_time - start_time
                entry = f"{active_window_name} - Time Spent: {int(time_spent)} sec."
#                print(entry)
                listbox.insert("end", entry)  # Update listbox with window name and time spent
            active_window_name = new_window_name
            start_time = time.time()

        # 5 second interval to check the active window.
        time.sleep(5)


frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Track System")
label.pack(pady=12, padx=10)

# CTkListbox to print the window name and time spent on the window.
listbox = CTkListbox(frame)
listbox.pack(fill="both", expand=True, padx=10, pady=10)

# Using threads to track windows
thread = threading.Thread(target=track_windows, args=(listbox,))
thread.daemon = True
thread.start()

root.mainloop()
