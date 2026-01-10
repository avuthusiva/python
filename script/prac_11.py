import re
pattren = 'ab+c'
string = 'aaabbbccc'
if re.match(pattren, string, re.IGNORECASE):
    print("Match found")
else:
    print("No match")

if re.search(pattren, string, re.IGNORECASE):
    print("Match found")
else:
    print("No match")