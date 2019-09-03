import re
str = ['axq','aq','xq','aaq','xxq']
for i in str:
    print(re.findall(r'a*x*q', i))