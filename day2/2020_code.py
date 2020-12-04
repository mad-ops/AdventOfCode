#get data
import os
import re
scriptdir = os.path.dirname(os.path.abspath(__file__))
match = re.compile('''(\d*)-(\d*) (.): (.*)''')
old_policy_passwords = []
new_policy_passwords = []
with open(os.path.join(scriptdir,'2020_input.txt')) as passwords:
    for password in passwords:
        l, h, x, p = match.search(password).group(1,2,3,4)
        l, h, p = int(l), int(h), ' ' + p.strip()
        if l <= p.count(x) <= h:
            old_policy_passwords.append(p)
        #part two 
        if (p[l] == x) ^ (p[h] == x) :
            new_policy_passwords.append(p)

print(len(old_policy_passwords))
print(len(new_policy_passwords))