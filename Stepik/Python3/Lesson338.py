n = int(input())
matrix = [[0 for i in range(n+2)] for j in range(n+2)]
c = 1
a = 1
b = 1
angle = ['right', 'down', 'left', 'up']
ang = 0
for i in range(n+2):
    matrix[0][i]=1
    matrix[n+1][i]=1
    matrix[i][0]=1
    matrix[i][n+1]=1


def revers(step):
    global a
    global b
    global c
    global ang
    if (step == 'right'):
        while(matrix[a][b]==0):
            matrix[a][b]=c
            b+=1
            c+=1
        ang +=1
        b-=1
        a+=1
    if (step == 'down'):
        while(matrix[a][b]==0):
            matrix[a][b]=c
            a+=1
            c+=1
        ang +=1
        b-=1
        a-=1
    if (step == 'left'):
        while(matrix[a][b]==0):
            matrix[a][b]=c
            b-=1
            c+=1
        ang +=1
        a-=1
        b+=1
    if (step == 'up'):
        while(matrix[a][b]==0):
            matrix[a][b]=c
            a-=1
            c+=1
        ang = 0
        a+=1
        b+=1


while c<=n*n:
    revers(angle[ang])
for i in range(1,n+1):
    print(*matrix[i][1:n+1])


# inp = int(input())
# list = [[[] for i in range(inp)] for i in range(inp)]
# num = 1
# a = 0
# b = 0
# c = 0
#
# while a != inp:
#    inp -= 1
#
#    while b < inp:
#       list[a][b] = str(num)
#       num += 1
#       b += 1
#
#    while a < inp:
#       list[a][b] = str(num)
#       num += 1
#       a += 1
#
#    while b > c:
#       list[a][b] = str(num)
#       num += 1
#       b -= 1
#
#    c += 1
#
#    while a > c:
#       list[a][b] = str(num)
#       num += 1
#       a -= 1
#
# list[a][b] = str(num)
# for row in list:
#     print(*row)