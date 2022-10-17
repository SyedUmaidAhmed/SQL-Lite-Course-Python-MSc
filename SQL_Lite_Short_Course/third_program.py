import sqlite3

#conn = sqlite3.connect(':memory:')
conn = sqlite3.connect('customer.db')
c = conn.cursor()

many_persons = [
	('Naveed', 'Mid', 'naveed@lfd.com'),
	('Shahid', 'Old', 'ahmnav@lfd.com'),
	('Asad', 'Younger', 'asad@lfd.com'),
]

c.executemany("INSERT INTO customers VALUES (?,?,?)", many_persons)
print("Successful Execution")
#NULL, INTEGER, REAL, TEXT, BLOB
conn.commit()
conn.close()