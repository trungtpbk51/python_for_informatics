fname = raw_input('Enter a file name: ')
try:
    fhand = open(fname)
except:
    print fname, ": File not found"
    exit()

hist = dict()
for line in fhand:
    line = line.split()
    if len(line) == 0 or line[0] != "From" or len(line) < 2:
        continue
    mail = line[1].split('@')
    if len(mail) < 2:
        continue
    school = mail[1]
    hist[school] = hist.get(school, 0) + 1

print hist
