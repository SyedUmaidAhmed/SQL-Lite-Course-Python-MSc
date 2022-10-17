import sqlite3

#conn = sqlite3.connect(':memory:')
conn = sqlite3.connect('customer.db')
c = conn.cursor()

c.execute("""UPDATE customers SET first_name = "Najeeb"
	WHERE last_name='Mid'

	""")


conn.commit()

c.execute("SELECT * FROM customers")


items = c.fetchall()
for item in items:
	print(item)




conn.close()