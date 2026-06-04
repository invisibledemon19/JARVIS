import csv
import os
import sqlite3

con = sqlite3.connect("jarvis.db")
cursor = con.cursor()

# Create tables
query = "CREATE TABLE IF NOT EXISTS sys_command(id integer primary key, name VARCHAR(100) UNIQUE, path VARCHAR(1000))"
cursor.execute(query)

query = "INSERT OR IGNORE INTO sys_command VALUES (null,'one note', 'C:\\Program Files\\Microsoft Office\\root\\Office16\\ONENOTE.exe')"
cursor.execute(query)
con.commit()

query = "CREATE TABLE IF NOT EXISTS web_command(id integer primary key, name VARCHAR(100) UNIQUE, url VARCHAR(1000))"
cursor.execute(query)

query = "INSERT OR IGNORE INTO web_command VALUES (null,'youtube', 'https://www.youtube.com/')"
cursor.execute(query)
con.commit()

# Create contacts table
cursor.execute('''CREATE TABLE IF NOT EXISTS contacts (id integer primary key, name VARCHAR(200), mobile_no VARCHAR(255), email VARCHAR(255) NULL, address VARCHAR(255) NULL)''')

# Create personal info table
cursor.execute("CREATE TABLE IF NOT EXISTS info(name VARCHAR(100), designation VARCHAR(50), mobileno VARCHAR(40), email VARCHAR(200), city VARCHAR(300))")
con.commit()

# Import contacts from CSV if file exists
if os.path.exists('contacts.csv'):
    desired_columns_indices = [0, 1]
    with open('contacts.csv', 'r', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            try:
                selected_data = [row[i] for i in desired_columns_indices]
                cursor.execute('''INSERT OR IGNORE INTO contacts (id, name, mobile_no) VALUES (null, ?, ?);''', tuple(selected_data))
            except (IndexError, Exception) as e:
                print(f"Skipping row: {e}")
    con.commit()
    print("Contacts imported successfully.")
else:
    print("No contacts.csv found, skipping import.")

# Test query
try:
    app_name = "one note"
    cursor.execute('SELECT path FROM sys_command WHERE name IN (?)', (app_name,))
    results = cursor.fetchall()
    if results:
        print(f"Test query result: {results[0][0]}")
    else:
        print("Test query: no results found")
except Exception as e:
    print(f"Test query error: {e}")

con.close()
print("Database setup complete.")