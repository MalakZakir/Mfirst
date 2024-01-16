import re
fhand = input('Enter file name: ')
fname = open(fhand)
count = 0 
tot = 0
for line in fname:
    line = line.rstrip
    y = re.findall('^X-\s+:', line)
    print(y)
