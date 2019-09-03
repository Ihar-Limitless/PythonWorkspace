n,m = map(int, input().split(' '))
lst = []
lst.append('.'*(m+2))
for i in range(n):
    lst.append('.'+input()+'.')
lst.append('.'*(m+2))

print(*lst)


def ret(a,b):
    global lst
    if(lst[a][b] == '*'):
        return 1
    else:
        return 0

def count(a,b):
    sum = 0
    sum = ret(a+1, b+1)+ret(a-1, b-1)+ret(a+1, b-1)+ret(a-1, b+1)+ret(a,b-1)+ret(a, b+1)+ret(a+1,b)+ret(a-1,b)
    return sum

for i in range(1,n+1):
    for j in range(1,m+1):
        if lst[i][j] !='*':
            print(count(i,j), end = '')
        else:
            print('*', end = '')
    print('')

# n, m = map(int, input().split())
# a = []
# for i in range(n):
#     a.append(list(input()))
# for i in range(n):
#     for j in range(m):
#         if a[i][j] == '.':
#             a[i][j] = 0
#             for di in range(-1, 2):
#                 for dj in range(-1, 2):
#                     ai = i + di
#                     aj = j + dj
#                     if 0 <= ai < n and 0 <= aj < m and a[ai][aj] == '*':
#                         a[i][j] += 1
# for row in a:
#         print(''.join([str(elem) for elem in row]))

# n, m = [int(x) for x in input().split()]
# stars = [(i, j) for i in range(n) for j, c in enumerate(input()) if c == '*']
#
# for i in range(n):
#     for j in range(m):
#         if (i, j) in stars:
#             print('*', end='')
#         else:
#             print (sum(1 for x in (i-1, i, i+1) for y in (j-1, j, j+1) if (x, y) in stars), end='')
#     print()