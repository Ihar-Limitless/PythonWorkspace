num_map = {1000: 'M',900: 'CM', 800: 'DCCC', 700: 'DCC', 600: 'DC', 500: 'D', 400: 'CD', 300: 'CCC', 200: 'CC',
100: 'C', 90: 'XC', 80: 'LXXX', 70: 'LXX', 60: 'LX', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 8: 'VIII', 7: 'VII', 6: 'VI', 5: 'V',
4: 'IV', 3: 'III', 2: 'II', 1: 'I', }

num = int(input())
num1000 = num // 1000
num100 = (num % 1000) // 100
num10 = ((num % 1000) % 100) // 10
num1 = (((num % 100) % 100) % 10)
# print(num1000, num100, num10, num1)
if num1000 > 0:
    print(num_map[1000] * num1000, end='')
if num100 > 0:
    print(num_map[num100 * 100], end = '')
if num10 > 0:
    print(num_map[num10 * 10], end = '')
if num1 > 0:
    print(num_map[num1], end = '')

# dic = {1:"I", 4:"IV", 5:"V", 9:"IX", 10:"X", 40:"XL", 50:"L", 90:"XC", 100:"C", 400:"CD", 500:"D", 900:"CM", 1000:"M"}
#
# def convert(n):
#     if n == 0: return ""
#     m = max([x for x in dic if x <= n])
#     return dic[m] + convert(n - m)
#
# print(convert(int(input())))
