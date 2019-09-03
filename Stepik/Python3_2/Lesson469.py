import math
import os
def prime (*y):
    lst2 = list(math.sqrt(i) for i in y)
    print(lst2)

lst = [1, 2, 3, 4, 5, 7, 9]
prime(*lst)
os.system("pause")

