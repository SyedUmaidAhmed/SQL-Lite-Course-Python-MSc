import sqlite3

#conn = sqlite3.connect(':memory:')
conn = sqlite3.connect('customer.db')
c = conn.cursor()


c.execute("SELECT * FROM customers")


#c.fetchone()
#c.fetchmany(3)

print(c.fetchall())

conn.commit()
conn.close()