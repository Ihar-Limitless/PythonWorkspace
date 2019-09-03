import os
print(os.listdir())
print(os.getcwd())
print(os.listdir(r'd:/PythonWorkspace'))
print(os.path.exists('d:\PythonWorkspace\Stepik'))
print(os.path.abspath('Lesson401.py'))

for i in os.walk("."):
    print(i)