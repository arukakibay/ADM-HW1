#Zipped!

# Enter your code here. Read input from STDIN. Print output to STDOUT
n, x = map(int, input().split()) 

sheet = []
for _ in range(x):
    sheet.append( map(float, input().split()) ) #entering data to mark sheet 

for i in zip(*sheet):  # as in example x=a+b+c
    print( sum(i)/len(i) ) # sum and divide to num of sbjects

#________________________________________________________
#Athlete Sort


#!/bin/python3

import math
import os
import random
import re
import sys


#used in discussion an advice
n_m = list(map(int, input().split()))

table = list()

for i in range(n_m[0]):
    table.append(list(map(int, input().split())))
    
k = int(input())

sorted_table = sorted(table, key=lambda record: record[k])

for item in sorted_table:
    print(*item)
