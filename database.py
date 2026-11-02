import sqlite3
def create_database():
    conn = sqlite3.connect('expense.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS expense (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 amount real not null,
                 date text not null,
                 category text not null,
                 description text)''')
    print(c.fetchall())
    conn.commit()
    conn.close()
print('Database and table created successfully')
create_database()