from random import random

M = 10
N = 5
a = []
for i in range(N):
    b = []
    for j in range(M):
        n = int(random() * 200)
        b.append(n)
        print(f'{n:4d}', end='')
    a.append(b)
    print()

mx = -1
for j in range(M):
    mn = 200
    for i in range(N):
        if a[i][j] < mn:
            mn = a[i][j]
    if mn > mx:
        mx = mn
print(f'Максимальный среди минимальных: {mx}')