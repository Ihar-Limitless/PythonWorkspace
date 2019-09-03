
import re
str = [r'There’ll be no more "Aaaaaaaaaaaaaaa"',
       'AaAaAaA AaAaAaA']
for line in str:
       line = line.rstrip()
       # print(re.sub(r'(\w+[a|A])\b','arch', line,count=1))
       # print(re.sub(r'(\w+([aA])+)','arch', line,count=1))
       print(re.sub(r"\ba+\b", "argh", line, count=1, flags=re.IGNORECASE))

# import sys
# import re
# [print(re.sub(r'\b[aA]+\b', 'argh', line.rstrip(), 1)) for line in sys.stdin]