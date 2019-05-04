import tkinter as tk
import ctypes
import sqlite3
import datetime
import db_interact



user32 = ctypes.windll.user32


age_years = ["5","6","7","8","9","10)"]
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

        db_interact.start()
        db_interact.create_table()
        db_interact.data_entry()

        search_options = db_interact.get_data_types()
        #print(search_options)


        root.bind('<Return>', lambda event: self.record(year.get(), gender.get(), minute.get(), second.get()))



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
        tk.Label(root, text="Minute: ", bg = background, fg = "white").grid(row=5,column=0)
        minute.grid(row=5,column=3)

        second = tk.Entry(root)

        second.configure(bg=background_2, fg = "white")
        tk.Label(root, text="Second: ", bg = background, fg = "white").grid(row=6,column=0)
        second.grid(row=6,column=3)

        search = tk.StringVar(root)
        search.set(search_options[2])
        popupMenu = tk.OptionMenu(root, search, *search_options)
        popupMenu.configure(bg = background_2, bd = 3, fg = "white", highlightthickness = 0)
        popupMenu.grid(row = 3, column = 1, sticky="w")



        #listbox.insert(tk.END, "")


        #(db_interact.get_info())
        #info = db_interact.get_info()
        #print((db_interact.get_info(search.get(), gender.get())))

        listbox = tk.Listbox(root)
        listbox.config(bd=0, bg = background, fg = "white",width = 100, height = 20)

        for item in (db_interact.get_info(search.get(), "M")):
            listbox.insert(tk.END, item)

        if search.get() ==

        listbox.grid()
        tk.Button(text="Update Search", command=lambda: self.clear_listbox(listbox), bg=background_2, bd = 3, fg = "white").grid(row=3,column=2)
        tk.Button(text="Record Time", bg=background_2, bd = 3, fg = "white").grid(row=10,column=0)
        # command=lambda: self.record(year.get(), gender.get(), minute.get(), second.get())


        quit = tk.Button(self, text="QUIT", fg="red", command=self.master.destroy, bg = background_2, bd = 3)
        quit.grid(row=10, column=10)

        db_interact.close()


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

    def clear_listbox(self,listbox):
        listbox.delete(0,tk.END)

        #listbox.get(listbox.curselection())






root = tk.Tk()
app = Application(master=root)
app.mainloop()
