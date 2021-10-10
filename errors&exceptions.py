#Exceptions

# Enter your code here. Read input from STDIN. Print output to STDOUT

for i in range(int(input())):
    try:
        a,b=map(int,input().split())
        print(a//b)
    except Exception as e:
        print("Error Code:",e)
#Incorrect Regex

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
#used discussion
def isvalidregex(regex):
    try: re.compile(regex)
    except re.error: return False
    return True

for i in range(int(input())):
    print(isvalidregex(input()))
