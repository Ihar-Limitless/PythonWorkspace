
import sys

data = {}

def findAncestor(clazz, targetAncestor):
    global data
    for ancestor in data[clazz]:
        if ancestor == targetAncestor:
            return True
        elif findAncestor(ancestor, targetAncestor):
            return True
        else:
            continue
    return False

def main():
    n = int(sys.stdin.readline()) # число классов
    while n > 0:
        line = sys.stdin.readline().rstrip()
        if ':' in line:
            clazz, ancestry = map(str, line.split(':'))
            clazz = clazz.rstrip()
            ancestors = ancestry.strip().split(' ')
        else:
            clazz = line
            ancestors = []
        if not clazz in data:
            data[clazz] = []
        data[clazz].extend(ancestors)
        n = n - 1
    # print(data)
    q = int(sys.stdin.readline()) # количество запросов
    while q > 0:
        maybeAncestor, clazz = map(str, sys.stdin.readline().split())
        if (maybeAncestor == clazz) or findAncestor(clazz, maybeAncestor):
            print('Yes')
        else:
            print('No')
        q -= 1

main()
#
# n = int(input())
# lst = []
# for i in range(0, n):
# # lst = ['A','B : A', 'C : A', 'D : B C']
#     lst.append(input())
# lst2 = []
# set1 = set()
# set2 = set()
# cls = set()
# for i in lst:
#     lst2.append(i.replace(' ', '').replace(':', ''))
# for i in lst2:
#     if(len(i) == 1):
#         set1.add(i+i)
#     else:
#         for j in range(1,len(i)):
#             set1.add(i[0]+i[j])
# for i in set1:
#     cls.add(i[1])
#
# for i in set1:
#     for j in cls:
#         if((i[1]+j) in set1):
#             set2.add(i[0]+j)
# set1 = set1.union(set2)
#
#
# n2 = int(input())
# lst3 = []
# # lst3 = ['A B','B D','C D','D A']
# for i in range(0, n2):
#     lst3.append(input())
# lst4 =[]
# for i in lst3:
#     lst4.append(i.replace(' ',''))
# for i in lst4:
#     if(i in set1):
#         print ('No')
#     else:
#         print('Yes')