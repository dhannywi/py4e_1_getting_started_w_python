largest = None
smallest = None
#input loop
while True:
    num = input('Enter a number: ')
    if num == 'done' :
        break
    try :
        val = int(num)
    except : #error msg
        print('Invalid input')
        continue
    #value check
    if largest is None :
        largest = val
    elif val > largest :
        largest = val
    if smallest is None :
        smallest = val
    elif val < smallest :
        smallest = val
#result
print('Maximum is', largest)
print('Minimum is', smallest)
