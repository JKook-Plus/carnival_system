import tkinter as tk
import ctypes
import sqlite3
import datetime

user32 = ctypes.windll.user32


age_years = ["5 (2008)","6 (2007)","7 (2006)","8 (2005)","9 (2004)","10 (2003)"]
genders = ["M", "F"]

background = ("#18191c")
background_2 = ("#36393f")

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()



        self.create_widgets()
        root.geometry("%sx%s" %(user32.GetSystemMetrics(0)-150, user32.GetSystemMetrics(1)-150))
        root.configure(bg=background)
        self.configure(bg=background)





    def create_widgets(self):


        year = tk.StringVar(root)
        year.set(age_years[0])
        popupMenu = tk.OptionMenu(root, year, *age_years)
        popupMenu.configure(bg=background_2, bd = 3, fg = "white", highlightthickness = 0)
        popupMenu.grid(row = 2, column = 0, sticky="w")


        gender = tk.StringVar(root)
        gender.set(genders[0])
        popupMenu = tk.OptionMenu(root, gender, *genders)
        popupMenu.configure(bg=background_2, bd = 3, fg = "white", highlightthickness = 0)
        popupMenu.grid(row = 3, column = 0, sticky="w")

        time = tk.StringVar(root)
        entry_box = tk.Entry(root)
        entry_box.bind('<Return>', lambda event: self.start(year.get(),gender.get(), entry_box.get()))
        entry_box.configure(bg=background_2, fg = "white")
        entry_box.grid()



        tk.Button(text="Record Time", command=lambda: self.start(year.get(),gender.get(), entry_box.get()), bg=background_2, bd = 3,fg = "white").grid(row=5,column=5)



        quit = tk.Button(self, text="QUIT", fg="red", command=self.master.destroy, bg = background_2, bd = 3)

        quit.grid(row=4, column=1)


    def start(self, year, gender, time):
        print(time)

        with open("output.csv", "a+") as f:
            text = (year + ", " + gender + ", " + time + ", " + str(datetime.datetime.now()) +"\n")
            f.write(text)
            f.close()




root = tk.Tk()
app = Application(master=root)
app.mainloop()
