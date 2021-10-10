#Detect Floating Point Number

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
for _ in range(int(input())):
    print(bool(re.match(r'^[-+]?[0-9]*\.[0-9]+$', input())))

    #____________________________________________________________
 #Group(), Groups() & Groupdict()

# Enter your code here. Read input from STDIN. Print output to STDOUT
#used discussion
import re
m = re.search(r'([a-zA-Z0-9])\1+', input().strip())
print(m.group(1) if m else -1)
#______________________________________________________________
#Re.findall() & Re.finditer()

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
s = '[qwrtypsdfghjklzxcvbnm]' #Consonants 
a = re.findall('(?<=' + s +')([aeiou]{2,})' + s, input(), re.I)
print('\n'.join(a or ['-1']))
#_________________________________________________________________
#Re.start() & Re.end()


import re
#used discussions
s, k = input(), input()
matches = list(re.finditer(r'(?={})'.format(k), s))
if matches:
    print('\n'.join(str((match.start(),
          match.start() + len(k) - 1)) for match in matches))
else:
    print('(-1, -1)')

 #___________________________________________________________________
#Regex Substitution
# Enter your code here. Read input from STDIN. Print output to STDOUT
for _ in range(int(input())):
    lines = input()
    
    while ' && ' in lines or ' || ' in lines:
        lines = lines.replace(" && ", " and ").replace(" || ", " or ")
    
    print(lines)
#______________________________________________________________________
#Validating Roman Numerals
regex_pattern = r""	# Do not delete 'r'.
thousand = "(?:(M){0,3})?"
hundred  = "(?:(D?(C){0,3})|(CM)|(CD))?"
ten      = "(?:(L?(X){0,3})|(XC)|(XL))?"
unit     = "(?:(V?(I){0,3})|(IX)|(IV))?"

regex_pattern = r"^" + thousand + hundred + ten + unit + "$"

#____________________________________________________________________
#Hex Color Code

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
pattern=r'(#[0-9a-fA-F]{3,6}){1,2}[^\n ]'
for _ in range(int(input())):
    for x in re.findall(pattern,input()):
        print(x)
#_________________________________________________________________________
#Validating UID
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
#explanation got from discussions
for _ in range(int(input())):
    s = input()
    print('Valid' if all([re.search(r, s) for r in [r'[A-Za-z0-9]{10}',r'([A-Z].*){2}',r'([0-9].*){3}']]) and not re.search(r'.*(.).*\1', s) else 'Invalid')
