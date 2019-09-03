import sys
from tkinter import Button, mainloop
x = Button(
    text='Press me',
    command=(lambda: sys.stdout.write('Yes!!!! You press me motherfucker!!!\n'))
)
x.pack()
mainloop()