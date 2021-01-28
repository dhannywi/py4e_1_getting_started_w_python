#letter grade
score = input("Enter Score: ")
try :
    grade = float(score)
    if grade > 1 :
        print('Error, out of range')
    elif grade < 0 :
        print('Error, out of range')
except :
    quit()
#letter grade conversion
if grade >= 0.9 :
    print('A')
elif grade >= 0.8 :
    print('B')
elif grade >= 0.7 :
    print('C')
elif grade >= 0.6 :
    print('D')
elif grade < 0.6 :
    print('F')
