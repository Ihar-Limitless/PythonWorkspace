import re, sys

str = ['blabla is a tandem repetition',
       r'123123 is good too',
       'go go',
       'aaa',
       'bbbb',
       'cc',
       'asd aaa123123',
       'bez povtorov']

# [print(line.rstrip()) for line in str if re.search(r'/\s(\w+\s)\1/i', line)]
# print(*filter(lambda line: "\\" in line, sys.stdin), sep='')


# pattern = r'(?P<word>\b\w+)\s+(?P=word)' # это регуоярное выражение для поиска одинаковых слов в строке
# pattern = r'(?P<word>\b\w+)(?P=word)' # это регуоярное выражение для поиска повторяющихся комбинаций в слове (123123)
# print(re.search(pattern, str).group())
# for line in str:
#     print(re.search(pattern, line))

# [print(line.rstrip()) for line in str if re.search(r'(\b\w+)+\1\b', line)]
# [print(line.rstrip()) for line in sys.stdin if re.search(r'(?P<word>\b\w+){2}(?P=word)', line)]

pattern = r'\b(\w+)\1\b'
for line in str:
       line = line.strip()
       if re.search(r"\b(\w+)\1\b", line):
              print(line)