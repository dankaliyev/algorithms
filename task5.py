list = [r'a', 'b', 'c', 'd', 'e', 'f', 'g',
         'h', 'i', 'j', 'k', 'l', 'm', 'n',
         'o', 'p', 'q', 'r', 's', 't', 'u',
         'v', 'w', 'x', 'y', 'z']
x = input('Введите первый символ: ')
y = input('Введите последний символ: ')
a = list.index(x)
b = list.index(y)
if a > b:
    z = a - b
else:
    z = b - a
print(f'{x} - место {a + 1}, {y} - место {b + 1}, разница {z}')