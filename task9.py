n = int(input('Введите число: '))
max_s = 0
max_m = 0
while n != 0:
    m = n
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    if s > max_s:
        max_s = s
        max_m = m
    n = int(input('Введите число или введите 0 для завершения: '))
print(f'Число {max_m} имеет максимальную сумму цифр: {max_s}')
