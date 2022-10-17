import sqlite3

#conn = sqlite3.connect(':memory:')
conn = sqlite3.connect('customer.db')
c = conn.cursor()

#Search Value by Column Name
c.execute("SELECT * FROM customers WHERE first_name LIKE 'Ah%' ")


items = c.fetchall()
for item in items:
	print(item)


conn.commit()
conn.close()