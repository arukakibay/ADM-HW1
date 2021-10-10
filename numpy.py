#Arrays



def arrays(arr):
    # complete this function
    # use numpy.array

    return numpy.flip(numpy.array(arr,float)) 

#Shape and Reshape

import numpy

print(numpy.reshape(numpy.array(list(map(int,input().split()))),(3,3)))



#Transpose and Flatten

import numpy
n, m = map(int, input().split())
array = numpy.array([input().strip().split() for _ in range(n)], int)
print (array.transpose())
print (array.flatten())


#Concatenate

import numpy

a, b, c = map(int,input().split())
arr_1= numpy.array([input().split() for _ in range(a)],int)
arr_2= numpy.array([input().split() for _ in range(b)],int)
print(numpy.concatenate((arr_1, arr_2), axis = 0))



#Eye and Identity

import numpy

print(str(numpy.eye(*map(int,input().split()))).replace('1',' 1').replace('0',' 0'))


#Array Mathematics

import numpy as np



N, M = map(int, input().split())
A, B = (np.array([input().split() for _ in range(N)], dtype=int) for _ in range(2))
print(A+B, A-B, A*B, A//B, A%B, A**B, sep='\n')



#Sum and Prod

import numpy as np



n, m = map(int, input().split())
Ax = np.array([input().split() for _ in range(n)],int)
print(np.prod(np.sum(Ax, axis=0), axis=0))




#Dot and Cross
import numpy
a=int(input())

arr1=numpy.array([list(map(int,input().split())) for _ in range(a)])

arr2=numpy.array([list(map(int,input().split())) for _ in range(a)])

print(numpy.dot(arr1,arr2))


#Polynomials

import numpy



print(__import__('numpy').polyval(list(map(float,input().split())),float(input())))
