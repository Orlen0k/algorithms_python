"""
Задание 2.
Попытайтесь выполнить профилирование памяти в любом скрипте с рекурсией.
Вам нужно обнаружить проблему в процессе этого. Но проблема связана не с тем,
что рекурсия потребляет много памяти, а с самим процессом замеров.
Опищите эту проблему и найдите простой путь ее решения.
Опишите этот путь и покажите его применение
"""

from memory_profiler import memory_usage
from memory_profiler import profile


# Декоратор для профилирования памяти у методов классов
def memory_measur(func):
    def wrapper(*args, **kwargs):
        m1 = memory_usage()
        res = func(*args)
        m2 = memory_usage()
        mem_diff = m2[0] - m1[0]
        print(f"Выполнение заняло {mem_diff} Mib")
        return res

    return wrapper

@memory_measur
def decorator(number):
    def reverse_number(number=None, result=''):
        if number is None:
            number = int(input('Введите число, которое требуется перевернуть: '))
        last_num = number % 10
        result += str(last_num)
        if last_num == number:
            return f"Перевернутое число: {result}"
        return reverse_number(number // 10, result)

    return reverse_number(10000000)

print(decorator(10000000))

# Оптимизированная реализация
@memory_measur
def reverse_number(number=None):
    if number is None:
        number = int(input('Введите число, которое требуется перевернуть: '))
    return f"Перевернутое число: {str(number)[::-1]}"

print(reverse_number(10000000))

'''Результат
Выполнение заняло 0.01171875 Mib
Перевернутое число: 00000001
Выполнение заняло 0.0 Mib
Перевернутое число: 00000001
'''

"""Вывод
Для корректных замеров функции с рекурсией необходимо обернуть функцию, содержащую рекурсию, во внешнюю, после чего 
применять декоратор профилирования памяти именно к обертке, что позволит получить точный результат.
Это связано с тем, что функция, вызывая сама себя провоцирует работу генератора и последний делает множество замеров 
"""
'''Анализ измененного кода
Для изменения количества потребляемой памяти избавился от рекурсии
'''