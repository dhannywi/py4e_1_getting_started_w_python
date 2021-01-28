#pay calc with overtime
hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate:")
r = float(rate)
#regular fulltime
if h <= 40 :
    pay = h * r
#overtime
elif h > 40 :
    pay = 40 * r + (h - 40) * (1.5 * r)

print(pay)
