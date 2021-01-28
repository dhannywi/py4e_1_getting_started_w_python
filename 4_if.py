
def computepay(h,r):
    #regular
    if h <= 40 :
        p = h * r
    #overtime
    elif h > 40 :
        p = 40 * r + (h - 40) * (1.5 * r)
    return p

h = input("Enter Hours: ")
h = float(h)
r = input("Enter Rate: ")
r = float (r)
p = computepay(h,r)
print("Pay",p)
