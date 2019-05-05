from tkinter import *
import ctypes
import sqlite3
import datetime
import db_interact



user32 = ctypes.windll.user32


age_years = ["5","6","7","8","9","10)"]
genders = ["M", "F"]
houses = ["Water", "Fire", "Air", "Earth"]

options = {"gender" : genders, "year" : age_years, "house": houses}

background = "#18191c"
background_2 = "#36393f"

class Application(Frame):
    def __init__(self, root=None):
        super().__init__(root, bg=background)
        self.root = root
        self.grid()


        self.create_widgets()
        root.geometry("%sx%s" %(user32.GetSystemMetrics(0)-150, user32.GetSystemMetrics(1)-150))
        root.configure(bg=background)





    def create_widgets(self):

        db_interact.start()
        db_interact.create_table()
        db_interact.data_entry()

        search_options = db_interact.get_data_types()
        search_opts_crap = []
        #print(search_options)


        root.bind('<Return>', lambda event: self.record(year.get(), gender.get(), minute.get(), second.get()))



        year = StringVar(root)
        year.set(age_years[0])
        popupMenu = OptionMenu(root, year, *age_years)
        popupMenu.configure(bg = background_2, bd = 3, fg = "white", highlightthickness = 0)
        popupMenu.grid(row = 2, column = 0, sticky="w")


        gender = StringVar(root)
        gender.set(genders[0])
        popupMenu = OptionMenu(root, gender, *genders)
        popupMenu.configure(bg = background_2, bd = 3, fg = "white", highlightthickness = 0)
        popupMenu.grid(row = 3, column = 0, sticky="w")

        time = StringVar(root)
        minute = Entry(root)
        minute.configure(bg=background_2, fg = "white")
        Label(root, text="Minute: ", bg = background, fg = "white").grid(row=5,column=0)
        minute.grid(row=5,column=3)

        second = Entry(root)

        second.configure(bg=background_2, fg = "white")
        Label(root, text="Second: ", bg = background, fg = "white").grid(row=6,column=0)
        second.grid(row=6,column=3)






        search = StringVar(root)
        search.set(search_options[3])
        popupMenu = OptionMenu(root, search, *search_options)
        popupMenu.configure(bg = background_2, bd = 3, fg = "white", highlightthickness = 0)
        popupMenu.grid(row = 3, column = 1, sticky="w")
        search.trace("w", lambda *args: self.testing(search.get()))


        #options = search_options[3]
        #print[x for x in options[search.get()]]

        for i in options[search.get()]:
            search_opts_crap.append(i)


        search_opts = StringVar(root)
        search_opts.set(search_options[3])
        self.search_opt_box = OptionMenu(root, search_opts, *search_opts_crap)
        self.search_opt_box.configure(bg = background_2, bd = 3, fg = "white", highlightthickness = 0)
        self.search_opt_box.grid(row = 4, column = 1, sticky="w")
        #listbox.insert(END, "")



        #(db_interact.get_info())
        #info = db_interact.get_info()
        #print((db_interact.get_info(search.get(), gender.get())))

        listbox = Listbox(root)
        listbox.config(bd=0, bg = background, fg = "white",width = 100, height = 20)

        search_column = search.get() # eg gender, name , ect

        for item in (db_interact.get_info(search_column, gender.get())):
            listbox.insert(END, item)

        #if search.get() ==

        listbox.grid()
        Button(text="Update Search", command=lambda: self.clear_listbox(listbox), bg=background_2, bd = 3, fg = "white").grid(row=3,column=2)
        Button(text="Record Time", command = lambda: self.record(year.get(),gender.get(),minute.get(),second.get()), bg=background_2, bd = 3, fg = "white").grid(row=10,column=0)
        #command=lambda: self.record(year.get(), gender.get(), minute.get(), second.get())


        quit = Button(self, text="QUIT", fg="red", command=lambda: exit(), bg = background_2, bd = 3)
        quit.grid(row=10, column=10)

        db_interact.close()


    def record(self, year, gender, minute, second):
        # print(minute, second)
        # print(type(second))
        second = 0 if second == "" else second
        #year + ", " + gender + ", " + minute + "." + second + ", " + str(datetime.datetime.now()) +"\n"
        with open("output.csv", "a+") as f:
            text = ("%s  %s, %s, %s.%s\n" %(str(datetime.datetime.now()), year, gender, minute, second))
            f.write(text)
            f.close()

    def clear_listbox(self,listbox):
        listbox.delete(0,END)

    def populate(search_column, ):

        for item in (db_interact.get_info(search_column, )):
            listbox.insert(END, item)
#listbox.get(listbox.curselection())
    def testing(self, val):
        print("====================")
        print(options[val])

        
        #self.search_opt_box.configure(optsthing=options[val])





root = Tk()
app = Application(root=root)
app.mainloop()
