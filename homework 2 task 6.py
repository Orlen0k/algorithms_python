"""
Задание 6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.
Решите через рекурсию. В задании нельзя применять циклы.
"""

from random import randint


def random_number_game(attempts_count=10, number=None, ):
    if number is None:
        number = randint(1, 100)
    print(f'Осталось попыток: {attempts_count}')
    assumption = int(input('Какое число от 1 до 100 я загадал?\n'))
    if assumption == number:
        print('Вы угадали :)')
        return 1
    elif assumption > number:
        print('Загаданное число меньше')
    else:
        print('Загаданное число больше')
    if attempts_count == 1:
        print('Вы проиграли :(')
        return 0
    return random_number_game(attempts_count - 1, number)


random_number_game()