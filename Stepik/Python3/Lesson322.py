dct = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
s = [dct[num] for num in [num for num in input()]]
num = s[0]
sum = sum(s)
for i in s:
    if (i > num):
        sum  = sum  - (2 * num)
    num = i
print(sum)
