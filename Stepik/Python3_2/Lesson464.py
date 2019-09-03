def func(message):
    print(message)

func("Wow! Thats great!")


def child(f, arg):
    f(arg)
shedule = [(func, 'One!'), (func, 'Two!'), (func, 'One-Two One-Two!')]
for (f, args) in shedule:
    f(args)