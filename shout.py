fname = raw_input('Enter a file name: ')
try:
    fhand = open(fname)
except:
    print fname, ': File not found'
    exit()
for line in fhand:
    line = line.rstrip()
    print line.upper()
