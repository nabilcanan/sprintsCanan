import tkinter as tk
import sqlite3

# connect to database and fetch entries
conn = sqlite3.connect('wufoo_data.db')
c = conn.cursor()
c.execute("SELECT * FROM entries ")
entries = c.fetchall()

# create main window
root = tk.Tk()
root.geometry("800x500")
root.title("Database Entries")
title_label = tk.Label(root, text="Current Database Entries:", font=("Times New Roman", 22))
title_label.pack(pady=20)

listbox = tk.Listbox(root, width=300)
listbox.pack(padx=100, pady=100, fill=tk.BOTH, expand=True)

for entry in entries:
    listbox.insert(tk.END, entry[0][:50])


def show_entry(event):
    # get selected entry
    index = listbox.curselection()[0]
    entry = entries[index]

    # create new window to display complete entry data
    top = tk.Toplevel(root)
    top.title("Entry Details")

    tk.Label(top, text="Goes By:").grid(row=0, column=0, )
    tk.Label(top, text=entry[1]).grid(row=0, column=1)
    tk.Label(top, text="First_Name:").grid(row=1, column=2)
    tk.Label(top, text=entry[2]).grid(row=2, column=2)
    tk.Label(top, text="Last_Name:").grid(row=2, column=3)
    tk.Label(top, text=entry[3]).grid(row=3, column=3)
    tk.Label(top, text="Job_Title:").grid(row=3, column=4)
    tk.Label(top, text=entry[4]).grid(row=4, column=4)
    tk.Label(top, text="Job_Type:").grid(row=4, column=5)
    tk.Label(top, text=entry[5]).grid(row=5, column=5)
    tk.Label(top, text="Email:").grid(row=5, column=6)
    tk.Label(top, text=entry[6]).grid(row=6, column=6)
    tk.Label(top, text="Website:").grid(row=6, column=7)
    tk.Label(top, text=entry[7]).grid(row=7, column=7)
    tk.Label(top, text="CellNum:").grid(row=7, column=8)
    tk.Label(top, text=entry[8]).grid(row=8, column=8)
    tk.Label(top, text="Opportunities:").grid(row=8, column=9)
    tk.Label(top, text=entry[9]).grid(row=9, column=9)
    tk.Label(top, text="Time_Period:").grid(row=9, column=10)
    tk.Label(top, text=entry[10]).grid(row=10, column=10)
    tk.Label(top, text="Other_Yes_Box:").grid(row=10, column=11)
    tk.Label(top, text=entry[11]).grid(row=11, column=11)
    tk.Label(top, text="Date_Created:").grid(row=11, column=12)
    tk.Label(top, text=entry[12]).grid(row=12, column=12)
    tk.Label(top, text="Created_By:").grid(row=12, column=13)
    tk.Label(top, text=entry[13]).grid(row=13, column=13)
    tk.Label(top, text="Date_Updated:").grid(row=13, column=14)
    tk.Label(top, text=entry[14]).grid(row=14, column=14)
    tk.Label(top, text="Updated_By:").grid(row=14, column=15)
    tk.Label(top, text=entry[15]).grid(row=15, column=15)


# bind listbox selection to show_entry function
listbox.bind("<<ListboxSelect>>", show_entry)

# run main loop

root.mainloop()
