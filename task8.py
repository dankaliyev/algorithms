M = 5
N = 4
a = []
for i in range(N):
    b = []
    s = 0
    print(f'{i}-я строка:')
    for j in range(M - 1):
        n = int(input())
        s += n
        b.append(n)
    b.append(s)
    a.append(b)

for i in a:
    print(i)
