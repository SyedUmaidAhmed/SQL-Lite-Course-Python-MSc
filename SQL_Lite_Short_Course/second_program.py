import sqlite3

#conn = sqlite3.connect(':memory:')

conn = sqlite3.connect('customer.db')
c = conn.cursor()


c.execute("INSERT INTO customers VALUES ('Ahmed', 'Young', 'syed@lovefordata.com')")

print("Successful Execution")
#NULL, INTEGER, REAL, TEXT, BLOB

conn.commit()
conn.close()