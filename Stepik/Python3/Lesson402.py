c1, c2, c3, c4 = 0,0,0,0
def koch(n):
    global c1,c2,c3,c4
    if n > 0:
        koch(n - 1)
        c1+=1
        print(n,c1,c2,c3,c4,'turn 60')
        koch(n - 1)
        c2+=1
        print(n,c1,c2,c3,c4,'turn -120')
        koch(n - 1)
        c3+=1
        print(n, c1,c2,c3,c4,'turn 70')
        koch(n - 1)
        c4+=1
        print(n, c1,c2,c3,c4)
koch(int(input()))