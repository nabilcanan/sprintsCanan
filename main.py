# Nabil Canan
import json
import sys
import requests
import sqlite3
from secrets import wufoo_key
from requests.auth import HTTPBasicAuth


def get_wufoo_data() -> dict:  # comment to test workflow
    url = "https://nabilcanan.wufoo.com/api/v3/forms/m16i9gqh089msfx/entries/json"
    response = requests.get(url, auth=HTTPBasicAuth(wufoo_key, 'pass'))

    if response.status_code != 200:
        print(f"Failed to get data, response code:{response.status_code} and error message: {response.reason} ")
        sys.exit(-1)

    jsonresponse = response.json()
    ## print(jsonresponse)
    return jsonresponse['Entries']


def write_wufoo_data():
    try:
        db_connection = sqlite3.connect('wufoo_data.db')
        db_cursor = db_connection.cursor()

        db_cursor.execute('''CREATE TABLE IF NOT EXISTS entries 
        (Entry_Id text, 
        Goes_By text, 
        First_Name text, 
        Last_Name text, 
        title text, 
        job_type text,
        email_address text , 
        website text, 
        phone_number text, 
        opportunities text, 
        time_period text, 
        other_yes_box text,   
        Date_Created text, 
        Created_By text, 
        Date_Updated text, 
        Updated_By text)''')

    except sqlite3.Error as db_error:
        print(f'A Database Error has occurred: {db_error}')

    finally:
        if db_connection:
            db_connection.close()
            print('Database connection closed.')
    insert_database()


def insert_database():
    data = get_wufoo_data()
    try:
        db_connection = sqlite3.connect('wufoo_data.db')
        db_cursor = db_connection.cursor()

        db_cursor.execute('DELETE FROM entries')

        for item in data:
            db_cursor.execute(
                "INSERT INTO entries VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (item['EntryId'],
                 ##item.get('EntryId', ''),
                 # goes by mr, ms ...
                 item.get('Field5', ''),
                 # First Name
                 item.get('Field8', ''),
                 # Last Name
                 item.get('Field9', ''),
                 # Title
                 item.get('Field11', ''),
                 # Job
                 item.get('Field12', ''),
                 # Email Address
                 item.get('Field13', ''),
                 # Website
                 item.get('Field14', ''),
                 # Phone Number
                 item.get('Field15', ''),
                 '.'.join([item.get('Field16', ''),  # Course Project Box
                           # Guest Speaker Box
                           item.get('Field17', ''),
                           # Site Visit Box
                           item.get('Field18', ''),
                           # Job Shadow Box
                           item.get('Field19', ''),
                           # Internships Box
                           item.get('Field20', ''),
                           # Control Panel Box
                           item.get('Field21', ''),
                           # Networking event Box
                           item.get('Field22', '')]),

                 # Summer 2022 Box
                 ','.join([item.get('Field216', ''),
                           # Fall 2022 Box
                           item.get('Field217', ''),
                           # Spring 2023 Box
                           item.get('Field218', ''),
                           # Summer 2023 Box
                           item.get('Field219', ''),
                           # Other Box
                           item.get('Field220', '')]),
                 # Yes Final Field
                 item.get('Field316', ''),

                 item.get('DateCreated'),
                 item.get('CreatedBy'),
                 item.get('DateUpdated'),
                 item.get('UpdatedBy')))

        db_connection.commit()

    except sqlite3.Error as db_error:
        print(f'A Database Error has occurred: {db_error}')

    finally:
        if db_connection:
            db_connection.close()
    print('Database connection closed.')


if __name__ == "__main__":
    write_wufoo_data()
