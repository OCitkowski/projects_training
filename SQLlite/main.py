import sqlite3;

con = sqlite3.connect("db.sqlite3")
cursor = con.cursor()

if __name__ == '__main__':
    cursor.execute("SELECT * FROM home_page_home")
    print(cursor.fetchall())
