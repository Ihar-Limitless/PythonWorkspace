n, k = map(int, input().split())

def comb(n, k):
    """Генерация сочетаний из `n` по `k` без повторений."""

    d = list(range(0, k))
    yield d

    while True:
        i = k - 1
        while i >= 0 and d[i] + k - i + 1 > n:
            i -= 1
        if i < 0:
            return

        d[i] += 1
        for j in range(i + 1, k):
            d[j] = d[j - 1] + 1

        yield d
len = 0
for c in comb(n, k):
    len+=1
print(len)
