s = input()
str1 = s[0]
str_sum = ''
count = 0
for i in s:
    if (str1 == i):
        count += 1
    else:
        str_sum = str_sum+str1+str(count)
        str1 = i
        count = 1
str_sum = str_sum+str1+str(count)

print(str_sum)
