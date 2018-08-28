n = int(input('Введите натуральное число: '))
s = 0
for i in range(1, n + 1):
    s += i
m = n * (n + 1) // 2
print(f'1+2+...+n = {s}')
print(f'n(n+1)/2 = {m}')
