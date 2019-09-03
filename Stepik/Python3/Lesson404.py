n1, n2 = map(int, input().split('/'))
def fraction(n1, n2):
    count1 = n1//n2
    print(count1, end = ' ')
    count2 = n1%n2
    if count2 != 0:
        fraction(n2, count2)


fraction(n1,n2)

# a, b = map(int, input().split('/'))
# while b:
#     print(a // b, end=' ')
#     a, b = b, a % b

# a,b=map(int,input().split('/'))
# f=lambda a,b: b!=0 and "%s %s"%(str(a//b),f(b,a%b)) or ''
# print(f(a,b))
