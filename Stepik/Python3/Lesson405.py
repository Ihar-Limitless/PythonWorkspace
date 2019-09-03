num = list(map(int, input().split()))
lst = list(range(1, len(num)))
lst2 = []
for i in range(1, len(num)):
    lst2.append(abs(num[i]-num[i-1]))
if len(num) > 1:
    if (sorted(lst2) == lst):
        print('Jolly')
    else:
        print('Not jolly')
else:
    print('Jolly')

# a = [int(i) for i in input().split()]
# print('Jolly' if sorted([abs(a[i]-a[i+1]) for i in range(len(a)-1)]) == [i for i in range(1,len(a))] else 'Not jolly')

# z = list(map(int,input().split()))
# y = sorted(map(lambda x:abs(x[1]-x[0]),zip(z[:-1],z[1:])))
# print('Jolly' if all(map(lambda x:(abs(x[1]-x[0])) == 1,zip(y[:-1],y[1:]))) else 'Not jolly')


# nums = tuple(map(int, input().split()))
# is_jolly = sorted(abs(nums[i] - nums[i-1]) for i in range(1, len(nums))) == list(range(1, len(nums)))
# print('Jolly' if is_jolly else 'Not jolly')