import random

print('Выберете диапазон случайной генерации:')
print('i - случайное число,')
print('f - случайное вещественное число,')
print('w - случайный символ')

a = input('Выберете метод генерации: ')
list = [r'a', 'b', 'c', 'd', 'e', 'f', 'g',
         'h', 'i', 'j', 'k', 'l', 'm', 'n',
         'o', 'p', 'q', 'r', 's', 't', 'u',
         'v', 'w', 'x', 'y', 'z']

if a == 'i':
    x = int(input('Введите минимальное значение: '))
    y = int(input('Введите максимальное значение: '))
    z = random.randint(x, y)
    print(f'Ваше случайное число: {z}')
elif a == 'f':
    x = float(input('Введите минимальное значение: '))
    y = float(input('Введите максимальное значение: '))
    z = random.uniform(x, y)
    print(f'Ваше случайное число: {z:.3f}')
elif a == 'w':
    x = input('Введите первый символ: ')
    y = input('Введите последний символ: ')
    x = list.index(x)
    y = list.index(y)
    list_end = list[x:y+1]
    x = random.choice(list_end)
    print(f'Ваш случайный символ: {x}')
