import sqlite3
import main
import GUI


# here

def test_wufoo_data_received():
    data = main.get_wufoo_data()
    assert len(data) == 5
    # asserting 10 for this test


def test_database():
    db_connection = sqlite3.connect('wufoo_data.db')
    db_cursor = db_connection.cursor()

    db_cursor.execute("SELECT * FROM entries")
    rows = db_cursor.fetchall()
    assert rows[4] == (
        ('5',
         'Mr.',
         'test',
         'test',
         'test',
         'test.com',
         'test12@gmail.com',
         'test12.com',
         '1231331234',
         'Course Project.Guest Speaker.Site Visit.Job Shadow.Internships.Career Panel.Networking Event',
         ' Summer 2022 (June 2022- August 2022),Fall 2022 (September 2022- December '
         +
         '2022), Spring 2023 (January 2023- April 2023), Summer 2023 (June 2023- '
         'August 2023),Other',
         'No',
         '2023-02-16 22:00:56',
         'public',
         '',
         None,
         ))


def test_gui_entries():
    db_connection = sqlite3.connect('wufoo_data.db')
    db_cursor = db_connection.cursor()

    db_cursor.execute("SELECT * FROM entries")
    entry = GUI.entries
    assert test_gui_entries[5] == (
        'Mr.', 'test', 'test', 'test', 'test.com', 'test12@gmail.com', 'test12.com', '1231331234',
        'Course Project.Guest Speaker.Site Visit.Job Shadow.Internships.Career Panel.Networking Event',
        'No', '2023-02-16 22:00:56', 'public', '', ''
    )
