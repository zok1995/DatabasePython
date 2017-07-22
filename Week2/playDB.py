import sqlite3
import re

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('''DROP TABLE IF EXISTS Counts''')

cur.execute('''CREATE TABLE Counts (org TEXT, count INTEGER)''')

fname = 'mbox.txt'
if (len(fname) < 1): fname = 'mbox-short.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): continue
    line = line.rstrip()
    x = re.findall('[A-Za-z0-9._%+-]+@([A-Za-z0-9.-]+\.[A-Za-z]{2,6})', line)
    if len(x) > 0:
        domain = x[0]
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (domain,))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count)
                VALUES (?, 1)''', (domain,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
                    (domain,))
    conn.commit()

sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()