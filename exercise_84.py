fname = raw_input('Enter file name: ')
try:
    fhand = open(fname)
except:
    print fname, ': File not found'
    exit()

words = list()
for line in fhand:
    for w in line.split():
        if not w in words:
            words.append(w)
words.sort()
print words
