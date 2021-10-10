#Introduction
#1 Say "Hello, World!" With Python
if __name__ == '__main__':
    print "Hello, World!"
    
#2 Python If-Else


import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(raw_input().strip())
if n%2!=0:
    print("Weird")
elif n in range (2,5):
    print("Not Weird")
elif n in range (6, 21):
    print("Weird")
elif n>20:
    print("Not Weird")
    
#3 Arithmetic Operators

if __name__ == '__main__':
    a = int(input())
    b = int(input())
c=a+b
print (c)
d=a-b
print (d)
f=a*b
print (f)

#4 Python: Division
if __name__ == '__main__':
    a = int(input())
    b = int(input())
c=a//b
d=a/b
print(a//b)
print(a/b)


#5 Loops

if __name__ == '__main__':
    n = int(raw_input())
for i in range (n):
    print(i*i)

    
#6 Print Function

from __future__ import print_function

if __name__ == '__main__':
    n = int(raw_input())

for i in range(1,n+1):
        print(i,end="")

