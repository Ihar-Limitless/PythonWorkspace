lst = [int(i) for i in input().split()]
def modify_list(lst):
    tmp = 0
    while tmp < len(lst):
        if lst[tmp] % 2 == 0:
            lst[tmp] = lst[tmp]//2
            tmp += 1
        else:
            lst.pop(tmp)
    print(lst)

modify_list(lst)