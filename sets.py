#Introduction to Sets

def average(array):
    # your code goes here
    return sum(set(array))/len(set(array))
#_____________________________________________________________ 
#Symmetric Difference
# Enter your code here. Read input from STDIN. Print output to STDOUT
a,b=(int(input()),input().split()) #a it is size of b
c,d=(int(input()),input().split()) #c is size of d
x=set(b) 
y=set(d)
p=y.difference(x) # as in example finding their difference 
q=x.difference(y)
r=p.union(q) #at the end union differences in order to print out and do it as sorted 
print ('\n'.join(sorted(r, key=int)))
#__________________________________________________________________
#Set .add()

# Enter your code here. Read input from STDIN. Print output to STDOUT
num = int(raw_input())
countries = set()
for i in range(num):
    countries.add(raw_input())
print len(countries)

#______________________________________________________________

