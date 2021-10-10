cube = lambda x: pow(x,3)
def fibonacci(n):
    # return a list of fibonacci numbers
    listt = [0,1]
    for i in range(2,n):
        listt.append(listt[i-2] + listt[i-1])
    return(listt[0:n])

