def plus(a,b):
    return a+b
def minus(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b == 0:
        return None
    else:
        return a//b
num = input().split()
num[0] = int(num[0])
num[2] = int(num[2])

if num[1] == 'plus':
    print(plus(num[0], num[2]))
if num[1] == 'minus':
    print(minus(num[0], num[2]))
if num[1] == 'multiply':
    print(multiply(num[0], num[2]))
if num[1] == 'divide':
    print(divide(num[0], num[2]))

# operators = {
#     'plus': lambda x, y: x + y,
#     'minus': lambda x, y: x - y,
#     'multiply': lambda x, y: x * y,
#     'divide': lambda x, y: x // y
# }
# s = input().split(' ')
# print(operators[s[1]](int(s[0]), int(s[2])))

# put your python code here
# m={'plus':'+', 'minus':'-', 'multiply':'*', 'divide':'//'}
# print(*[eval(s1+m[s2]+s3) for [s1,s2,s3] in [input().split()]])


# print(eval (input()
#     .replace("plus", "+")
#     .replace("minus", "-")
#     .replace("multiply", "*")
#     .replace("divide", "//")))