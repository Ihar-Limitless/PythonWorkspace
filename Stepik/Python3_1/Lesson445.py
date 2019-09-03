import re, sys

str = [r'\w denotes word character',
       r'world is mine \ the world is ours',
       'No slashes here']

[print(line.rstrip()) for line in str if re.search(r'\\', line)]
# print(*filter(lambda line: "\\" in line, sys.stdin), sep='')