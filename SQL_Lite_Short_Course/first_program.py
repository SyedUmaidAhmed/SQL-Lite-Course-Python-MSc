import sqlite3

#conn = sqlite3.connect(':memory:')

conn = sqlite3.connect('customer.db')
c = conn.cursor()


c.execute("""CREATE TABLE customers(

	first_name text,
	last_name text,
	email text

	)""")

#NULL, INTEGER, REAL, TEXT, BLOB

conn.commit()
conn.close()