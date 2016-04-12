try:
    hours = input('Enter Hours: ')
    h = int(hours)
    rate = input('Enter Rate: ')
    r = float(rate)
    if h > 40:
        pay = 40*r + (h-40)*r*1.5
    else:
        pay = h*r
    print 'Pay: ' + str(pay)
except:
    print 'Error, please enter numeric input'
