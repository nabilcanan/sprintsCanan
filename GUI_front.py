import tkinter as tk
import sqlite3

# connect to database and fetch entries
conn = sqlite3.connect('wufoo_data.db')
c = conn.cursor()
c.execute("SELECT * FROM entries")
entries = c.fetchall()

# create main window
root = tk.Tk()
root.title("Database Entries")

# create listbox to display entries
listbox = tk.Listbox(root, width=100)
listbox.pack(padx=100, pady=100)

# add entries to listbox
for entry in entries:
    listbox.insert(tk.END, entry[1][:30])  # display first 30 characters of entry


# create function to display complete entry data
def show_entry(event):
    # get selected entry
    index = listbox.curselection()[0]
    entry = entries[index]

    # create new window to display complete entry data
    top = tk.Toplevel(root)
    top.title("Entry Details")

    # display complete entry data
    tk.Label(top, text="Name:").grid(row=0, column=0, sticky="w")
    tk.Label(top, text=entry[1]).grid(row=0, column=1, sticky="w")
    tk.Label(top, text="Email:").grid(row=1, column=0, sticky="w")
    tk.Label(top, text=entry[2]).grid(row=1, column=1, sticky="w")
    tk.Label(top, text="Message:").grid(row=2, column=0, sticky="w")
    tk.Label(top, text=entry[3]).grid(row=2, column=1, sticky="w")


# bind listbox selection to show_entry function
listbox.bind("<<ListboxSelect>>", show_entry)

# run main loop
root.mainloop()
