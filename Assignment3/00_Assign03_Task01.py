#Factorial of a number
a=int(input('Enter a positive integer= '))

def fact(a) :
    if a<2 :
        return 1
    else :
        return a * fact(a-1)
f=fact(a)
print ('factorial of ' +str(a)+ ' is =', f )