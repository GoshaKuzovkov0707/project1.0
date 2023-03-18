from random import randint

chislo = randint(1, 100)

game = True

print('Попробуйте угадать число от 1 до 100')

while game:
    god = int(input('Ваш выбор : '))
    if god == chislo :
        print('Вы угадали!')
        game = False
    elif god < chislo:
        print(f'Ответ неправильный, попоробуй число больше чем {god}')
    elif god > chislo:
        print(f'Ответ неправильный, попоробуй число меньше чем {god}')