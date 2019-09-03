import os
list_dir = os.listdir(r'd:/PythonWorkspace/Shakespeare/')
print(list_dir)
with open(r'd:/PythonWorkspace/shekespeare.txt', 'w') as fw:
    for name in list_dir:
        name = r'd:/PythonWorkspace/Shakespeare/'+name
        with open(name, 'r') as fr:
            for read in fr:
                if 'love' in read:
                    print('bingo!')
                    fw.write(read)