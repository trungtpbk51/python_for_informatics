fname = raw_input('Enter a file name: ')
try:
    fhand = open(fname)
except:
    print fname, ': File not found'
    exit()
    
count = 0
for line in fhand:
    line = line.split()
    if len(line) == 0 or line[0] != 'From':
        continue
    if len(line) > 1:
        print line[1]
    else:
        print 'Unknown'
    count = count + 1
print 'There were ', count, ' lines in this file with From as the first word'
