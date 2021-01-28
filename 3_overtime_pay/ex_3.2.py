#pay calc with overtime
hrs = input("Enter Hours: ")
try :
    h = float(hrs)
except :
    print('Error, please enter numeric input')
    quit()
rate = input("Enter Rate: ")
try :
    r = float(rate)
except :
    print('Error, please enter numeric input')
    quit()
#regular
if h <= 40 :
    reg = h * r
    pay = (reg)
#overtime
elif h > 40 :
    reg = h * r
    otp = (h - 40) * (1.5 * r)
    pay = reg + otp

print('Pay: ',pay)
