#What's Your Name?

#
# Complete the 'print_full_name' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING first
#  2. STRING last
#

def print_full_name(first, last):
    # Write your code here
    print("Hello "+first+" "+last+"! You just delved into python.")
#____________________________________________________________________
#Mutations

def mutate_string(string, position, character):
    l = list(string)
    l[position] = character
    string = ''.join(l)  
    return string
 # _____________________________________________________________
#Find a string

def count_substring(string, sub_string):
    num = 0
    for i in range(0, len(string)):
        if string[i:i+len(sub_string)] == sub_string:
            num += 1
    return num    
    
    #return (string.count(sub_string))
#_______________________________________________________________
#String Validators

#if __name__ == '__main__':
#   s = input()
    
def fulfill_condition(predicate, string):
    for character in string:
        if predicate(character):
            return True
    return False
if __name__ == '__main__':
    s = input()
    print(fulfill_condition(str.isalnum, s))
    print(fulfill_condition(str.isalpha, s))
    print(fulfill_condition(str.isdigit, s))
    print(fulfill_condition(str.islower, s))
    print(fulfill_condition(str.isupper, s))
    
#_______________________________________________________________________    
#Text alognments
#Replace all ______ with rjust, ljust or center. 

thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))
#_______________________________________________________________________________________________________    
#Text Wrap


def wrap(string, max_w):
    return textwrap.fill(string,max_w)


