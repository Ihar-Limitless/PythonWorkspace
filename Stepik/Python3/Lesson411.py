exceptions = {}
throwed_exceptions = []

def found_path(exceptions, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if start not in exceptions:
        return []
    for node in exceptions[start]:
        if node not in path:
            newpath = found_path(exceptions, node, end, path)
            if newpath: return newpath
    return []

n = int(input())
for _ in range(n):
    inpt = input().split()
    child = inpt[0]
    parents = inpt[2:]
    exceptions[child] = parents

m = int(input())
for _ in range(m):
    throwing = input()
    for throwed_exception in throwed_exceptions:
        if len(found_path(exceptions, throwing, throwed_exception)) > 1:
            print(throwing)
            break
    throwed_exceptions.append(throwing)

# ____________________________________________________________________________________
# # put your python code here
# n = int(input())
# classes = {}
# for i in range(n):
#     line = input()
#     parts = line.split(" : ")
#     cls = parts[0]
#     if len(parts) == 1:
#         classes[cls] = []
#     else:
#         classes[cls] = parts[1].split(" ")
#
#
# def check(src, dest):
#     if src == dest:
#         return True
#     return any([check(child, dest) for child in classes[src]])
#
#
# m = int(input())
# used = []
#
# for i in range(m):
#     cls = input()
#     if any([check(cls, used_one) for used_one in used]):
#         print(cls)
#     used.append(cls)

# ____________________________________________________________________________________
# def is_known_exception(ex):
#     return (ex in known_ex) or any(map(lambda p: is_known_exception(p), family[ex]))
#
#
# family, known_ex = {}, set()
# for _ in range(int(input())):
#     ex, *parent = input().split(" : ")
#     family[ex] = parent[0].split() if len(parent) else []
#
# for _ in range(int(input())):
#     [print(ex) if is_known_exception(ex) else known_ex.add(ex) for ex in [input()]]