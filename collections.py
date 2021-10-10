#collections.Counter()

# Enter your code here. Read input from STDIN. Print output to STDOUT
import collections
#used the code in discussions
numShoes = int(input())
shoes = collections.Counter(map(int, input().split()))
numCust = int(input())

income = 0

for i in range(numCust):
    size, price = map(int, input().split())
    if shoes[size]: 
        income += price
        shoes[size] -= 1

print (income)
#________________________________________________________________
#Collections.namedtuple()

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple
#person = namedtuple('person','ID MARKS NAME CLASS')
n=int(input())
    
Student = namedtuple('Student', input())
print("{:.2f}".format(sum([int(Student(*input().split()).MARKS) for _ in range(n)]) / n))
