str = input().lower().split()
dic = {}

for str_temp in str:
    if (str_temp in dic):
        dic[str_temp] += 1
    else:
        dic[str_temp] = 1

for key, val in dic.items():
    print(key, val)
