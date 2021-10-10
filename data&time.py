#Calendar Module

# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar
n1,n2,n3=map(int,input().split()) #day month year
print((calendar.day_name[calendar.weekday(n3,n1,n2)]).upper()) #search in cAlendar
