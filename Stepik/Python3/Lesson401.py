import turtle
# def koch(n):
#     if n > 0:
#         koch(n - 1)
#         print('turn 60')
#         koch(n - 1)
#         print('turn -120')
#         koch(n - 1)
#         print('turn 60')
#         koch(n - 1)
#
#
# koch(int(input()))

# n = int(input())
# ans = [60, -120, 60]
#
# if n > 1:
#     for i in range(n-1):
#         for j in range(len(ans)+1)[::-1]:
#             ans.insert(j, 60)
#             print(j, ans)
#             ans.insert(j, -120)
#             print(j, ans)
#             ans.insert(j, 60)
#             print(j, ans)
#
# for el in ans:
#     print('turn {}'.format(el))

# n = int(input())
# lst = [60, -120, 60]
# lst_sum = []
#
# for i in range(1,n):
#     for j in range(1,n):
#         lst_sum.append(lst)
#         lst_sum.append([60])
#         lst_sum.append(lst)
#         lst_sum.append([-120])
#         lst_sum.append(lst)
#         lst_sum.append([60])
# lst_sum.append(lst)
# for i in lst_sum:
#     for j in i:
#         print('turn {}'.format(j))
#
# def koch_turns(n):
#     angles = [60, -120, 60]
#     if n == 1:
#         return angles
#     else:
#         kch = koch_turns(n-1)
#         res = []
#         for i in range(7):
#             if i % 2 == 0:
#                 res.extend(kch)
#             else:
#                 res.append(angles[(i - 1) // 2])
#         return res
#
#
# def koch_curve(n, line_length=10):
#     for move in koch_turns(n):
#         turtle.forward(line_length)
#         turtle.left(move)
#     turtle.forward(line_length)
#     turtle.exitonclick()
#
# koch_curve(10)