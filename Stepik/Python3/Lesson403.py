count = 0
def recur(n):
    global count
    if n > 1:
        recur(n-1)
        count += 1
        print('я в первом', count, 'n = ', n)
        # recur(n-1)
        # count += 1
        # print('я во втором', count, 'n = ', n)
        # recur(n-1)
        # count += 1
        # print('я в третьем', count, 'n = ', n)
recur(4)