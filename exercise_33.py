def computegrade(score):
    if s < 0.0 or s > 1.0:
        return 'Bad score'
    elif s >= 0.9:
        return 'A'
    elif s >= 0.8:
        return 'B'
    elif s >= 0.7:
        return 'C'
    elif s >= 0.6:
        return 'D'
    else:
        return 'F'
try:
    score = input('Enter score: ')
    s = float(score)
    print computegrade(s)
except:
    print 'Bad score'
