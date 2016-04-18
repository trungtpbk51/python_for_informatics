total = 0
count = 0
avg = 0

while True:
    try:
        prompt = raw_input('Enter a number: ')
        if prompt == 'done':
            break
        num = float(prompt)
        total = total + num
        count = count + 1
    except:
        print 'Invalid input'
        continue
        
if count > 0:
    avg = total / count
    
print total, count, avg
