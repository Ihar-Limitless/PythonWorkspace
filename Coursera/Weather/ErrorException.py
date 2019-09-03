import os.path
import traceback
my_path = "file/not/found"
try:
    if not os.path.exists(my_path):
        raise ValueError("Файл не существует мать его", my_path)

except ValueError as err:
    trace = traceback.print_exc()
    print(trace)