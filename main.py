import tkinter as tk
import ctypes
import sqlite3


user32 = ctypes.windll.user32



age_years = ["5","6","7","8","9","10"]


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.create_widgets()
        root.geometry("%sx%s" %(user32.GetSystemMetrics(0)-150, user32.GetSystemMetrics(1)-150))
        root.configure(bg="#21252b")
        self.configure(bg="#21252b")
        #Grid.rowconfigure(root, 0, weight=1)
        #Grid.columnconfigure(root, 0, weight=1)


    def create_widgets(self):
        year_buttons = []

        for i in age_years:
            b = tk.Button(self)
            b["text"] = (i)
            b["command"] = (lambda i=i: self.years(i))
            year_buttons.append(b)


        num = ((user32.GetSystemMetrics(0)-150)/len(year_buttons))
        for i in range(len(year_buttons)):

            year_buttons[i].grid(row = 1, column = i+2,  sticky="N"+"S"+"E"+"W")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.grid(row=10, column=10)

    def years(self, *args, **kwargs):
        print(*args)

root = tk.Tk()
app = Application(master=root)
app.mainloop()
