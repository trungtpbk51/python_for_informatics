fname = raw_input('Enter a file name: ')
try:
    fhand = open(fname)
except:
    print fname, ": File not found"
    exit()

dow = dict()
for line in fhand:
    line = line.split()
    if len(line) == 0 or line[0] != "From" or len(line) < 3:
        continue
    dow[line[2]] = dow.get(line[2], 0) + 1

print dow
