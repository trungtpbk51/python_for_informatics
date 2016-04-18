def computepay(hours, rate):
    if hours > 40:
        pay = 40*rate + (hours-40)*rate*1.5
    else:
        pay = hours*rate
    return pay
    
try:
    hours = input('Enter Hours: ')
    h = int(hours)
    rate = input('Enter Rate: ')
    r = float(rate)
    print 'Pay: ', computepay(h, r)
except:
    print 'Error, please enter numeric input'
