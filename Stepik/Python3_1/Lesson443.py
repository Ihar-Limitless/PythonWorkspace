import re, sys
[print(line.rstrip()) for line in sys.stdin if re.search(r'\b(cat)\b', line)]

# # put your python code here
# import sys
# import re
# pattern = r'\b(cat)\b'
# for i in sys.stdin:
#     i = i.rstrip()
#     if re.search(pattern, i):
#         print(i)

#
import re, sys
# print("\n".join([line.rstrip() for line in sys.stdin if re.match(r'.*\bcat\b.*', line)]))