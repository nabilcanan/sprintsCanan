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

# create title label
title_label = tk.Label(root, text="Current Database Entries:", font=("Times New Roman", 22))
title_label.pack(pady=20)

# create listbox to display entries
listbox = tk.Listbox(root, width=300)
listbox.pack(padx=100, pady=100, fill=tk.BOTH, expand=True)

# populate listbox with entries
for entry in entries:
    listbox.insert(tk.END, entry[0][:50])
    edit_button = tk.Button(root, text="Edit", command=lambda index=listbox.size() - 1: show_entry(index))
    edit_button.pack()

goes_by_entry = tk.StringVar()
first_name_entry = tk.StringVar()
last_name_entry = tk.StringVar()
job_title_entry = tk.StringVar()
job_type_entry = tk.StringVar()
email_entry = tk.StringVar()
website_entry = tk.StringVar()
cell_num_entry = tk.StringVar()
opportunities_entry = tk.StringVar()
time_period_entry = tk.StringVar()
other_yes_box_entry = tk.StringVar()


def add_entry(entry_id, goes_by, first_name, last_name, job_title, job_type, email_address, website, phone_num,
              opportunities,
              time_period, other_yes_box, created_by, updated_by):
    conn = sqlite3.connect('wufoo_data.db')
    c = conn.cursor()
    c.execute(
        "INSERT INTO entries (entry_id, goes_by, First_name, Last_name, job_title, job_type, email_address, website, "
        "phone_num, "
        "opportunities, time_period, other_yes_box, Date_Created, Created_By, Date_Updated, Updated_by) VALUES (?, ?, "
        "?, ?, ?, ?, ?, ?, ?, ?, ?, ?, )", 
        (
            entry_id, goes_by, first_name, last_name, job_title, job_type, email_address, website, phone_num,
            opportunities,
            time_period,
            other_yes_box, created_by, updated_by))
    conn.commit()
    conn.close()


def add_entry_from_input(entry_id=None):
    # get input values from entry widgets
    top = tk.Toplevel(root)
    goes_by = goes_by_entry.get()
    first_name = first_name_entry.get()
    last_name = last_name_entry.get()
    job_title = job_title_entry.get()
    job_type = job_type_entry.get()
    email = email_entry.get()
    website = website_entry.get()
    cell_num = cell_num_entry.get()
    opportunities = opportunities_entry.get()
    time_period = time_period_entry.get()
    other_yes_box = other_yes_box_entry.get()

    # add new entry to the database
    add_entry(entry_id, goes_by, first_name, last_name, job_title, job_type, email, website, cell_num, opportunities, time_period,
              other_yes_box, "User", "User")

    # clear the input widgets
    goes_by_entry.delete(0, tk.END)
    first_name_entry.delete(0, tk.END)
    last_name_entry.delete(0, tk.END)
    job_title_entry.delete(0, tk.END)
    job_type_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    website_entry.delete(0, tk.END)
    cell_num_entry.delete(0, tk.END)
    opportunities_entry.delete(0, tk.END)
    time_period_entry.delete(0, tk.END)
    other_yes_box_entry.delete(0, tk.END)

    submit_button = tk.Button(top, text="Submit", command=add_entry_from_input)
    submit_button.grid(row=11, column=1)


def show_entry(event):
    # get selected entry
    index = listbox.curselection()[0]
    entry = entries[index]

    # create new window to display complete entry data
    top = tk.Toplevel(root)
    top.title("Entry Details")

    submit_button = tk.Button(top, text="Submit", command=add_entry_from_input)
    submit_button.grid(row=11, column=1)

    tk.Label(top, text="Goes By:").grid(row=0, column=0, )
    goes_by_entry = tk.Entry(top)
    goes_by_entry.insert(tk.END, entry[1])
    goes_by_entry.grid(row=0, column=1)

    tk.Label(top, text="First Name:").grid(row=1, column=0)
    first_name_entry = tk.Entry(top)
    first_name_entry.insert(tk.END, entry[2])
    first_name_entry.grid(row=1, column=1)

    tk.Label(top, text="Last Name:").grid(row=2, column=0)
    last_name_entry = tk.Entry(top)
    last_name_entry.insert(tk.END, entry[3])
    last_name_entry.grid(row=2, column=1)

    tk.Label(top, text="Job Title:").grid(row=3, column=0)
    job_title_entry = tk.Entry(top)
    job_title_entry.insert(tk.END, entry[4])
    job_title_entry.grid(row=3, column=1)

    tk.Label(top, text="Job Type:").grid(row=4, column=0)
    job_type_entry = tk.Entry(top)
    job_type_entry.insert(tk.END, entry[5])
    job_type_entry.grid(row=4, column=1)

    tk.Label(top, text="Email:").grid(row=5, column=0)
    email_entry = tk.Entry(top)
    email_entry.insert(tk.END, entry[6])
    email_entry.grid(row=5, column=1)

    tk.Label(top, text="Website:").grid(row=6, column=0)
    website_entry = tk.Entry(top)
    website_entry.insert(tk.END, entry[7])
    website_entry.grid(row=6, column=1)

    tk.Label(top, text="Cell Number:").grid(row=7, column=0)
    cell_num_entry = tk.Entry(top)
    cell_num_entry.insert(tk.END, entry[8])
    cell_num_entry.grid(row=7, column=1)

    tk.Label(top, text="Opportunities:").grid(row=8, column=0)
    opportunities_entry = tk.Entry(top)
    opportunities_entry.insert(tk.END, entry[9])
    opportunities_entry.grid(row=8, column=1)

    tk.Label(top, text="Time Period:").grid(row=9, column=0)
    time_period_entry = tk.Entry(top)
    time_period_entry.insert(tk.END, entry[10])
    time_period_entry.grid(row=9, column=1)

    tk.Label(top, text="Other Yes Box:").grid(row=10, column=0)
    other_yes_box_entry = tk.Entry(top)
    other_yes_box_entry.insert(tk.END, entry[11])
    other_yes_box_entry.grid(row=10, column=1)


# bind listbox selection to show_entry function
listbox.bind("<<ListboxSelect>>", show_entry)

# run main loop
root.mainloop()
