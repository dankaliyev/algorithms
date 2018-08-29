from random import random

N = 10
a = [0] * N
for i in range(N):
    a[i] = int(random() * 50)
    print(f'{a[i]:3d}', end='')
print()

min_id = 0
max_id = 0
for i in range(1, N):
    if a[i] < a[min_id]:
        min_id = i
    elif a[i] > a[max_id]:
        max_id = i
print(a[min_id], a[max_id])

if min_id > max_id:
    min_id, max_id = max_id, min_id

summa = 0
for i in range(min_id + 1, max_id):
    summa += a[i]
print(summa)
