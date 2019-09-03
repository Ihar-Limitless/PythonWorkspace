import re

str = [r"this is a text",
       r"this' !is. ?n1ce,"]

# for line in str:
#        line = line.rstrip()
#        print(re.sub(r'\b(\w)(\w)', r"\2\1", line))

for line in str:
    line = line.strip()
    line = re.sub(r"\b(\w)(\w)(\w)(\w*)\b", r"\4\3\2\1", line) #побуквенно переворачиваем слово
    print(line)