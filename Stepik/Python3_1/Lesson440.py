s = str(input())
t = str(input())
i = 0

while True:
    if t in s:
        s = s[s.find(t)+1:]
        i+=1
    else:
        print(i)
        break

# s = input()
# t = input()
# ans = 0
# for i in range(len(s)):
#     if s[i:].startswith(t):
#         ans += 1
#
# print(ans)

# s = input()
# t = input()
#
# print(sum(1 for i in range(len(s)) if s.startswith(t, i)))