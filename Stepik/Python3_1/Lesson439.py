# s = 'aabbcc'
# a = 'aa'
# b = 'aaa'
s = input()
a = input()
b = input()
count = 0

while True:
    if a in b and a in s:
        print('Impossible')
        break
    if a in s:
        s = s.replace(a,b)
        count+=1
    else:
        print(count)
        break

# s, a, b = (input() for _ in range(3))
# def repl_gen(s, a, b):
#     while a in s: s = s.replace(a, b); yield True
# print('Impossible' if a in b and a in s else sum(repl_gen(s, a, b)))