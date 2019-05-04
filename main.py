import tkinter as tk
import ctypes
import sqlite3
import datetime

user32 = ctypes.windll.user32


age_years = ["2008","2007","2006","2005","2004","2003)"]
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
        popupMenu.configure(bg = background_2, bd = 3, fg = "white", highlightthickness = 0)
        popupMenu.grid(row = 2, column = 0, sticky="w")


        gender = tk.StringVar(root)
        gender.set(genders[0])
        popupMenu = tk.OptionMenu(root, gender, *genders)
        popupMenu.configure(bg = background_2, bd = 3, fg = "white", highlightthickness = 0)
        popupMenu.grid(row = 3, column = 0, sticky="w")

        time = tk.StringVar(root)
        minute = tk.Entry(root)
        minute.configure(bg=background_2, fg = "white")
        minute.grid()

        second = tk.Entry(root)
        second.bind('<Return>', lambda event: self.record(year.get(), gender.get(), minute.get(), second.get()))
        second.configure(bg=background_2, fg = "white")
        second.grid()



        tk.Button(text="Record Time", command=lambda: self.record(year.get(), gender.get(), minute.get(), second.get()), bg=background_2, bd = 3,fg = "white").grid(row=5,column=5)



        quit = tk.Button(self, text="QUIT", fg="red", command=self.master.destroy, bg = background_2, bd = 3)

        quit.grid(row=4, column=1)


    def record(self, year, gender, minute, second):
        print(minute, second)
        print(type(second))
        if second == "":
            second = 0
        #year + ", " + gender + ", " + minute + "." + second + ", " + str(datetime.datetime.now()) +"\n"
        with open("output.csv", "a+") as f:
            text = ("%s  %s, %s, %s.%s\n" %(str(datetime.datetime.now()), year, gender, minute, second))
            f.write(text)
            f.close()




root = tk.Tk()
app = Application(master=root)
app.mainloop()
