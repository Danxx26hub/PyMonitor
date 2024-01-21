import tkinter as tk
from tkinter import ttk, messagebox, Listbox, HORIZONTAL
import time
import threading
import psutil
from config import get_settings


class Window:
    """Class creates the main window for the application,
    by adding more methods you can add the number of items
    being monitored on your system. Check out the psutil docs
    https://psutil.readthedocs.io/en/latest/
    App also uses threading to run the methods in the background and
    off of the main thread that runs the GUI loop. This app demonstrates
    those concepts.

    """

    def __init__(self, master) -> None:
        self.master = master
        self.greeting = tk.Label(text=get_settings("dev").bar_label_cpu)
        self.p = ttk.Progressbar(
            master, orient=HORIZONTAL, length=100, mode="determinate"
        )
        self.greeting.pack()
        self.p.pack()
        self.l = Listbox(master, height=10)
        self.heading2 = tk.Label(text=get_settings("dev").bar_label_ram)
        self.p2 = ttk.Progressbar(
            master, orient=HORIZONTAL, length=100, mode="determinate"
        )
        self.p2.pack()
        self.heading2.pack()
        self.l.pack()
        self.x = threading.Thread(target=self.check_cpu, daemon=True)
        self.y = threading.Thread(target=self.ram_check, daemon=True)
        self.y.start()
        self.x.start()
        self.Button = ttk.Button(master, text="Quit", command=self.master.quit)
        self.Button.pack()

    def check_cpu(self):
        """Method Checks the CPU usage takes no arguments"""
        cpubar = None
        # self.text_window.config(state='normal')

        while True:
            # self.text_window.delete("1.0", tk.END)

            cpubar = psutil.cpu_percent(interval=0)

            cpubar = int(round(cpubar))

            self.p.start(10)
            self.l.delete(1, tk.END)
            self.l.insert(1, f"CPU: {cpubar}%")

            self.p["value"] = cpubar
            self.p.step(5)
            self.l.after(1)
            self.master.update()

    def ram_check(self):
        """Method Checks the RAM usage takes no arguments"""
        rambar = None
        while True:
            rambar = psutil.virtual_memory().percent
            rambar = int(round(rambar))
            self.l.delete(2)
            self.l.insert(2, f"RAM: {rambar}%")
            self.p2["value"] = rambar
            self.p2.step(5)

            self.master.update()


if __name__ == "__main__":
    # line below creates the main window and runs in main loop for testing.
    root = tk.Tk()
    root.title("System Monitor")

    Window(root)
    root.mainloop()
