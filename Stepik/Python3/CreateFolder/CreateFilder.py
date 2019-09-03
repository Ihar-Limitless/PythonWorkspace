path = r'D:/Тегрус/Папки/FolderList.txt'
path2 = r'D:/Тегрус/Папки/FL_bat.bat'
lst = []
with open(path, 'r', encoding='cp866') as f:
    for line in f.readlines():
        lst.append(line.strip())
with open(path2, 'w', encoding='cp866') as f:
    for i in lst:
        f.write("mkdir " + "\""+i+"\"\n")
