neighrange = (-1, 0, 1)
n, m = (int(x) for x in input().split())
a = [[int(c == 'X') for c in input()] for _ in range(n)]

for i in range(n):
    for j in range(m):
        x = a[i][j]
        print('i j = ',i,j)
        for dj in neighrange:
            for di in neighrange:
                print('i+di j+dj',i+di, j+dj)
                print('{0} {1}'.format((i+di)%n, (j+dj)%m))
#         neighbors = sum(a[(i+di) % n][(j+dj) % m] for di in neighrange for dj in neighrange) - x
#         if x and neighbors == 2 or neighbors == 3:
#             print('X', end='')
#         else:
#             print('.', end='')
#     print()

# a = list(map(int,input().split()))
# def is_life(x,y):
#     if b[x][y]=="X":
#         return True
#     else:
#         return False
# def find_life(x,y):
#     sum=0
#     if is_life((x+1)%a[0],y):
#         sum+=1
#     if is_life(x-1,y):
#         sum+=1
#     if is_life(x,(y+1)%a[1]):
#         sum+=1
#     if is_life(x,y-1):
#         sum+=1
#     if is_life((x+1)%a[0],(y+1)%a[1]):
#         sum+=1
#     if is_life(x-1,y-1):
#         sum+=1
#     if is_life(x-1,(y+1)%a[1]):
#         sum+=1
#     if is_life((x+1)%a[0],y-1):
#         sum+=1
#     if sum==3 and b[x][y]==".":
#         return 'X'
#     elif (sum==2 or sum==3) and b[x][y]=="X":
#         return 'X'
#     else:
#         return '.'
# b=[]
# for i in range (a[0]):
#     b+=[list(input())]
# for i in range(len(b)):
#     for j in range(len(b[i])):
#         print(find_life(i,j),end="")
#     print()

