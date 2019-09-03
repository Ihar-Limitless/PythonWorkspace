num = list(map(int, input().strip().split()))
num2 = int(input())
b = False
for i in range(0, len(num)):
    if (num[i] == num2):
        print(i, end =' ')
        b = True
if b == False:
    print('None')

# s,a=input().split(),input()
# res=[str(i) for i in range(len(s)) if s[i]==a]
# print(' '.join(res) if res!=[] else None)

# a, b = input().split(), input()
# print(' '.join([str(i) for i in range(len(a)) if a[i] == b]) if b in a else None)