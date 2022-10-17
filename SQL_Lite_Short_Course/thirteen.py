import sqlite3

conn = sqlite3.connect('customer.db')
c = conn.cursor()

c.execute("DELETE TABLE customers")

conn.commit()

c.execute("SELECT rowid, * FROM customers")
items = c.fetchall()
for item in items:
	print(item)



conn.comit()
conn.close()