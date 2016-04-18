min_val = None
max_val = None

while True:
    try:
        prompt = raw_input('Enter a number: ')
        if prompt == 'done':
            break
        num = float(prompt)
        if min_val is None or num < min_val:
            min_val = num
        if max_val is None or num > max_val:
            max_val = num
    except:
        print 'Invalid input'
        continue
          
print min_val, max_val
