lst = ['first', 'second', 'third']
book = {1:'first', 2:'second', 3:'trird'}
iterator = iter(book)
while True:
    try:
        i = next(iterator)
        print(i, book[i])

    except StopIteration:
        break