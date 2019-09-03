import os

lst2 = []
lst = set()
for cur_dir, subdir, files in os.walk(os.getcwd()):
    for i in files:
        if i.endswith(".py"):
            print(cur_dir, i)
            break

# for cur_dir, subdirs, files in os.walk("main"):
#     for file in files:
#         if file.endswith(".py"):
#             print(cur_dir)
#             break

# for current_dir, dirs, files in os.walk("main"):
#     if [1 for f in files if f[-3:] == '.py']: print(current_dir)