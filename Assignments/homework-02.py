"""
Name: Clorissa Callender
Email: ccallender1996@gmail.com
Assignment: Homework 2 - Fraction Class
Due: 26 Sep @ 1:00 p.m.
"""


def gcd(n, d):
    while n != d:
        if n > d:
            n = n - d
        else:
            d = d - n
    return n
class fraction(object):
    def __init__(self,n=None,d=None):
        self.numerator = int(n / gcd(abs(n), abs(d)))
        self.denominator = int(d / gcd(abs(n), abs(d)))
 
    def __str__(self):
        return "%s / %s" % (self.numerator , self.denominator)

    def numerator(self,n):
        self.numerator = n 

    def denominator(self,d):
        self.denominator = d

    def __mul__(self,rhs):
        x = self.numerator * rhs.numerator
        y = self.denominator * rhs.denominator
        return fraction(x,y)
    
    def __add__(self, other):
        j = self.numerator*other.denominator + self.denominator*other.numerator
        k = self.denominator*other.denominator
        if (j==k):
        	return 1
        else:
        	if (k>j):
        		return fraction(j,k)
        	else:
        		return str (str(j//k) +' '+ str( fraction ((j%k),k)))
        

a = fraction(1,2)
b = fraction(4,5)
c = a * b
d = a+b
print(c)
print(d)