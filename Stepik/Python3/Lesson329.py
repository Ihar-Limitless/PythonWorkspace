s = []
num = input()
while(num!='End'):
    s.append(num)
    num = input()
for i in s:
    print('Processing "{}" command...'.format(i))
print('Good bye!')