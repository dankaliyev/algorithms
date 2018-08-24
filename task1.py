print('Введите трехзначное число')
a = input('Ввод числа: ')

mult = 1
summa = 0

for x in a:
    summa += int(x)


for z in a:
    mult *= int(z)

print(f'Сумма чисел равна {summa:.3f}')
print(f'Произведение чисел равно {mult:.3f}')

