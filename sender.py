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
    hist[line[1]] = hist.get(line[1], 0) + 1

most_msg_sender = None
for sender in hist:
    if most_msg_sender is None or hist[sender] > hist[most_msg_sender]:
        most_msg_sender = sender

print most_msg_sender, hist[most_msg_sender]
