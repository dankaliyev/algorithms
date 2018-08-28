import random
secret = random.randint(1, 100)
print('Отгадай число от 1 до 100 за 10 попыток!')
tries = 10
while True:
    if tries == 0:
        print('Попытки кончились!')
        break
    guess = int(input('Твой вариант? > '))
    tries -= 1
    if guess < secret:
        print(f'Это слишком мало, осталось попыток {tries}')
    elif guess > secret:
        print(f'Это слишком много, осталось попыток {tries}')
    elif guess == secret:
        print('Угадал, красавчик!')
        break