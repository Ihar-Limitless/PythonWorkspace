import re
s = r'1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 23 24 25 26 '
match1 = re.findall(r'\b[1-9]\b',s)
print(match1)
match2 = re.findall(r'\b1[0-6]\b',s)
print(match2)
match3 = re.findall(r'\b1[7-9]\b',s)
print(match3)
match4 = re.findall(r'\b2[0-6]\b',s)
print(match4)