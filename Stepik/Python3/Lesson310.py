n = int(input())
dct = {}
str1 = []
lst = ['Зенит;3;Спартак;1', 'Спартак;1;ЦСКА;1', 'ЦСКА;0;Зенит;2', 'Франция;1;Румыния;1', 'Италия;2;Ирландия;1']

for i in range(n):
#    str = input().strip().split(';')
    str = lst[i].strip().split(';')
    dct[str[0]] = [0, 0, 0, 0, 0]
    dct[str[2]] = [0, 0, 0, 0, 0]
    str1.append(str)

def game(player1,p1w, p1d, p1l, p1p, player2, p2w, p2d, p2l, p2p):
    dct[player1][0]+= 1
    dct[player1][1]+= p1w
    dct[player1][2]+= p1d
    dct[player1][3]+= p1l
    dct[player1][4]+= p1p
    dct[player2][0]+= 1
    dct[player2][1]+= p2w
    dct[player2][2]+= p2d
    dct[player2][3]+= p2l
    dct[player2][4]+= p2p

for j in range(n):
    if (str1[j][1] == str1[j][3]):
        game(str1[j][0], 0, 1, 0, 1, str1[j][2], 0, 1, 0, 1)
    elif (str1[j][1] > str1[j][3]):
        game(str1[j][0], 1, 0, 0, 3, str1[j][2], 0, 0, 1, 0)
    elif (str1[j][1] < str1[j][3]):
        game(str1[j][0], 0, 0, 1, 0, str1[j][2], 1, 0, 0, 3)

for i,j in dct.items():
    print("{}:{} {} {} {} {}".format(i, j[0], j[1], j[2], j[3], j[4]))