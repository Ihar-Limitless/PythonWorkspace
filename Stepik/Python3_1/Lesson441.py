import re
print(re.match)
print(re.search)
print(re.findall)
print(re.sub)

pattern = r'abc'
string = 'abc'
match_obj = re.match(pattern, string)
print(match_obj)

string = 'babc'
match_obj = re.search(pattern, string)
print(match_obj)