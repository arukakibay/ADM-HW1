#Standardize Mobile Number Using Decorators

def wrapper(f):
    def fun(l):
       f(map(lambda x: "+91 " + x[-10:-5] + " " + x[-5:], l)) 
    return fun

#Decorators 2 - Name Directory



def person_lister(f):
    def inner(people):
        # complete the function
        return map(f, sorted(people, key=lambda x: int(x[2])))         
    return inner
