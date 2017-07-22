# This python file parse file mbox.txt and print all Organizations
import re

fname = 'mbox.txt'
if ( len(fname) < 1 ) : fname = 'mbox-short.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): continue
    line = line.rstrip()
    # Find email domain using regular expression
    x = re.findall('[A-Za-z0-9._%+-]+@([A-Za-z0-9.-]+\.[A-Za-z]{2,6})', line)
    print(x)