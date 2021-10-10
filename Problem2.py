#Cake candles

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    # Write your code here
   # n = int(input().strip())
   # height = [int(height_temp) for height_temp in input().strip().split(' ')]

   # HH=height.count(max(height))
   # return HH
    return candles.count(max(candles))
    return
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()
    
    #___________________________________________________________________________
    #Number Line Jumps

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#

def kangaroo(x1, v1, x2, v2):
    # Write your code here
    return 'YES' if (v1 > v2) and (x2 - x1) % (v2 - v1) == 0 else 'NO'




if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

   # first_multiple_input = input().rstrip().split()

    #x1 = int(first_multiple_input[0])

    #v1 = int(first_multiple_input[1])

    #x2 = int(first_multiple_input[2])

    #v2 = int(first_multiple_input[3])
    x1, v1, x2, v2 = map(int, input().split())
    print(kangaroo(x1, v1, x2, v2))
    #result = kangaroo(x1, v1, x2, v2)

    #fptr.write(result + '\n')

    #fptr.close()
#__________________________________________________________________
#Viral Advertising

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'viralAdvertising' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#


def viralAdvertising(n):
  m = [2]
  for i in range(n-1):
    m.append(m[-1]*3//2)
  return sum(m)
  
  
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()
#________________________________________________________________________
#Recursive Digit Sum

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def superDigit(n, k):
    s = str(sum([int(i) for i in n]))
    if len(n) == 1:
        if k == 1:
            return n
        else:
            return superDigit(n * k, 1)
    else:
        return superDigit(s, k)
    
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
#_____________________________________________________________________________________________
#Insertion Sort - Part 1

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#used duscussion



def insertionSort1(n, arr):
    target = arr[-1]
    idx = n-2
    
    while (target < arr[idx]) and (idx >= 0):
        arr[idx+1] = arr[idx]
        print(' '.join(map(str, arr)))
        idx -= 1
        
    arr[idx+1] = target
    print(' '.join(map(str, arr)))
    
if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    insertionSort1(n, arr)
#_________________________________________________________________________________
#Insertion Sort - Part 2

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort2' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#used advices from discussion


b=int(input())
a=[int(x) for x in input().strip().split(' ')]
for i in range(1,len(a)):
    key=a[i]
    j=i-1
    while j>=0 and a[j]>key:
        a[j+1]=a[j]
        j=j-1
    a[j+1]=key
    print(*a)

