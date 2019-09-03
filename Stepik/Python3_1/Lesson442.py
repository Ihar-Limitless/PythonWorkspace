import re

str = ['catcat', 'cat and cat', 'catac', 'cat', 'ccaatt']
pattern = r"cat.*cat"
for i in str:
    if re.search(pattern, i):
        print(i)



# import sys
# import re
# [print(line.rstrip()) for line in sys.stdin if len(re.findall(r"cat", line)) > 1]