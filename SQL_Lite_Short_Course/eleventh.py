import sqlite3

#conn = sqlite3.connect(':memory:')
conn = sqlite3.connect('customer.db')
c = conn.cursor()

c.execute("DELETE FROM customers WHERE rowid=4")


conn.commit()

c.execute("SELECT rowid, * FROM customers ORDER BY rowid DESC")

#ASC = ASCENDING
# ORDER by last_name (Alphabetical Order)
# USE AND and OR condition for desc + Alphabetic order


items = c.fetchall()
for item in items:
	print(item)




conn.close()