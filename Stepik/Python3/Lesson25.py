a = int(input())
b = int(input())
c = int(input())
d = int(input())

print('', end='\t')
for k in range(c,d+1):
    print(k, end='\t')
print('')
for i in range(a,b+1):
    print(i, end='\t')
    for j in range(c,d+1):
        print(i*j, end='\t')
    print('')
