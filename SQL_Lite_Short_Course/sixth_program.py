import sqlite3

#conn = sqlite3.connect(':memory:')
conn = sqlite3.connect('customer.db')
c = conn.cursor()

#ROW_ID's
c.execute("SELECT rowid, * FROM customers")


items = c.fetchall()
for item in items:
	print(item)


conn.commit()
conn.close()