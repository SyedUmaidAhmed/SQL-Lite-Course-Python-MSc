import sqlite3

#conn = sqlite3.connect(':memory:')
conn = sqlite3.connect('customer.db')
c = conn.cursor()

c.execute("DELETE FROM customers WHERE rowid=4")


conn.commit()

# DESC Row ID, Access only last 2 elements


c.execute("SELECT rowid, * FROM customers ORDER BY rowid DESC LIMIT 2")



items = c.fetchall()
for item in items:
	print(item)




conn.close()