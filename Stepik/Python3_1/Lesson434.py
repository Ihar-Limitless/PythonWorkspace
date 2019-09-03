with open('text.txt') as r:
    lst = r.read().split()
lst.reverse()
with open('text_reverse.txt', 'w') as w:
    w.write("\n".join(lst))

# with open('dataset_24465_4.txt', 'r') as fr, open('dataset_24465_4_w.txt', 'w') as fw:
#     fw.writelines(fr.readlines()[::-1])

# print(*reversed(open("sample.txt").readlines()), sep="")

# lines = open("input.txt").readlines()
# with open("output.txt", "w") as out:
#     out.writelines(reversed(lines))