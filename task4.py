a = input('Введите элементы через пробел: ')
a = a.split(" ")
summa = 0
for i in a:
    if i[0] == '-':
        x = float(i[1:])
        summa -= x
    else:
        i = float(i)
        summa += i

print(f'Сумма введенных элементов: {summa:.3f}')
