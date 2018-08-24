print('Введите три числа: ')
a = int(input('Первое число: '))
b = int(input('Второе число: '))
c = int(input('Третье число: '))

if b < a < c or c < a < b:
    print('Среднее:', a)
elif a < b < c or c < b < a:
    print('Среднее:', b)
else:
    print('Среднее:', c)