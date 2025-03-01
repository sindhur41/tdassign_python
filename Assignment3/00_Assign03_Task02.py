#Problem Statement: Write a Python program that:
#Asks the user for a number as input.
#Uses the math module to calculate the:
#Square root of the number
#Natural logarithm (log base e) of the number
#Sine of the number (in radians)

n=float(input('Enter a number ='))
from math import *
sq = sqrt(n)
if n==0 :
    ln= 'undefined'
else :
    ln= log (n)
sin_v= sin (n)
print (f'Square root of {n} is = ', sq )
print (f'Natural Logarithm of {n} is = ', ln )
print (f'Sine of {n} is = ', sin_v )