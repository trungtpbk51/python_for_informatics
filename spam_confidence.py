fname = raw_input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print fname, ': File not found'
    exit()

count = 0
total = 0
for line in fhand:
    if not line.startswith('X-DSPAM-Confidence:'):
        continue
    count = count + 1
    total = total + float(line[19:])

avg = 0
if count > 0:
    avg = total / count
print 'Average spam confidence: ', avg
