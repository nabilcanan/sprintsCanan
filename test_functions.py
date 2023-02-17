import sqlite3
import json
from urllib import response
import main
import pytest


def test_retrieve_data(self):
    self.assertEqual(response.status_code, 200)
    data = json.loads(response.text)
    self.assertGreater(len(data["Entries"]), 10)


def test_wufoo_data_received():
    data = main.get_wufoo_data()
    assert len(data) == 10
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
         'test.com',
         'test12@gmail.com',
         'test12.com',
         '1231331234',
         'Course Project.Guest Speaker.Site Visit.Job Shadow.Internships.Career Panel, Networking Event '
         ' Summer 2022 (June 2022- August 2022),Fall 2022 (September 2022- December '
         '2022), Spring 2023 (January 2023- April 2023), Summer 2023 (June 2023- '
         'August 2023),Other'
         'No',
         '2023-02-16 22:00:56',
         'public',
         '',
         'None'))


def test_db_entry(db_cursor, item):
    db_cursor.execute("SELECT * FROM entries WHERE EntryId=?", (item['EntryId'],))
    result = db_cursor.fetchone()
    if result is None:
        return False
    return (result[1] == item.get('Field1', '') and
            result[2] == item.get('Field2', '') and
            result[3] == item.get('Field3', '') and
            result[4] == item.get('Field4', '') and
            result[5] == item.get('Field5', '') and
            result[6] == item.get('Field6', '') and
            result[7] == item.get('Field7', '') and
            result[8] == item.get('Field8', '') and
            result[9] == item.get('Field9', '') and
            result[10] == item.get('Field10', '') and
            result[11] == item.get('Field105', '') and
            result[12] == item.get('Field107', '') and
            result[13] == item.get('DateCreated') and
            result[14] == item.get('CreatedBy') and
            result[15] == item.get('DateUpdated') and
            result[16] == item.get('UpdatedBy'))
