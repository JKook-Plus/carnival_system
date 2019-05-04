import sqlite3



conn = sqlite3.connect(":memory:")

c = conn.cursor()

c.execute("""CREATE TABLE students(
            Surname text,
            Name text,
            Gender text,
            Year integer,
            House text,
            Tutor text,
            DOB text,
            ID integer
            )""")

import pandas as pd
read_file = ((pd.read_excel('D:/Users/JKook Studios/Downloads/Files/School/IT/carnival_system/Book2.xlsx')))




df = pd.DataFrame(read_file)
index = read_file.index

print(list(list(df.iterrows())[0][1]))


columns = (list(df.columns.values))


for index,row in df.iterrows():
    details = []
    for i in columns:
        print(row[i])
        details.append(row[i])
    c.execute("INSERT INTO students VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (details[0],details[1],details[2],details[3],details[4],details[5],str(details[6]),details[7]))
    #print("\n")




#c.execute("INSERT INTO students VALUES ()")





conn.commit()

conn.close()
