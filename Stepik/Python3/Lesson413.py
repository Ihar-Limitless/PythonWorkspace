with open(r'd:/PythonWorkspace/test11.txt','w') as f:
    f.write('Hello file world!\n')
    f.write('Goodbye file world!\n')

with open(r'd:/PythonWorkspace/test11.txt','r') as f:
    for i in f:
        print(i.strip())