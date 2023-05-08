import tkinter as tk
import time

class FocusTimer:
    def __init__(self, master):
        self.master = master
        self.master.title("Focus Timer")
        self.master.geometry("300x100")

        self.time_label = tk.Label(self.master, text="", font=("Arial", 30))
        self.time_label.pack(pady=10)

        self.start_button = tk.Button(self.master, text="Start", command=self.start_timer)
        self.start_button.pack()

        self.stop_button = tk.Button(self.master, text="Stop", command=self.stop_timer, state="disabled")
        self.stop_button.pack()

        self.minutes = 0
        self.seconds = 0
        self.is_running = False
        self.timer = None

    def start_timer(self):
        self.minutes = 25
        self.seconds = 0
        self.is_running = True
        self.start_button.config(state="disabled")
        self.stop_button.config(state="normal")
        self.update_time()

    def stop_timer(self):
        self.is_running = False
        self.start_button.config(state="normal")
        self.stop_button.config(state="disabled")
        self.time_label.config(text="")

        if self.timer is not None:
            self.master.after_cancel(self.timer)

    def update_time(self):
        if self.is_running:
            if self.minutes == 0 and self.seconds == 0:
                self.stop_timer()
                return

            time_str = f"{self.minutes:02d}:{self.seconds:02d}"
            self.time_label.config(text=time_str)

            if self.seconds == 0:
                self.minutes -= 1
                self.seconds = 59
            else:
                self.seconds -= 1

            self.timer = self.master.after(1000, self.update_time)

root = tk.Tk()
app = FocusTimer(root)
root.mainloop()
