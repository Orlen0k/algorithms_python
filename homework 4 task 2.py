"""
Задание 2.
Приведен код, который формирует из введенного числа
обратное по порядку входящих в него цифр.
Задача решена через рекурсию
Выполнена попытка оптимизировать решение мемоизацией
Сделаны замеры обеих реализаций.
Сделайте аналитику, нужна ли здесь мемоизация или нет и почему?!!!
П.С. задание не такое простое, как кажется
"""

from timeit import timeit
from random import randint


def recursive_reverse(number):
    if number == 0:
        return str(number % 10)
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'


num_100 = randint(10000, 1000000)
num_1000 = randint(1000000, 10000000)
num_10000 = randint(100000000, 10000000000000)

print('Не оптимизированная функция recursive_reverse')
print(
    timeit(
        "recursive_reverse(num_100)",
        setup='from __main__ import recursive_reverse, num_100',
        number=10000))
print(
    timeit(
        "recursive_reverse(num_1000)",
        setup='from __main__ import recursive_reverse, num_1000',
        number=10000))
print(
    timeit(
        "recursive_reverse(num_10000)",
        setup='from __main__ import recursive_reverse, num_10000',
        number=10000))


def memoize(f):
    cache = {}

    def decorate(*args):

        if args in cache:
            return cache[args]
        else:
            cache[args] = f(*args)
            return cache[args]
    return decorate


@memoize
def recursive_reverse_mem(number):
    if number == 0:
        return ''
    return f'{str(number % 10)}{recursive_reverse_mem(number // 10)}'


print('Оптимизированная функция recursive_reverse_mem')
print(
    timeit(
        'recursive_reverse_mem(num_100)',
        setup='from __main__ import recursive_reverse_mem, num_100',
        number=10000))
print(
    timeit(
        'recursive_reverse_mem(num_1000)',
        setup='from __main__ import recursive_reverse_mem, num_1000',
        number=10000))
print(
    timeit(
        'recursive_reverse_mem(num_10000)',
        setup='from __main__ import recursive_reverse_mem, num_10000',
        number=10000))


from timeit import timeit
from random import randint


def recursive_reverse(number):
    if number == 0:
        return str(number % 10)
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'


num_100 = randint(10000, 1000000)
num_1000 = randint(1000000, 10000000)
num_10000 = randint(100000000, 10000000000000)

print('Не оптимизированная функция recursive_reverse')
print(
    timeit(
        "recursive_reverse(num_100)",
        setup='from __main__ import recursive_reverse, num_100',
        number=10000))
print(
    timeit(
        "recursive_reverse(num_1000)",
        setup='from __main__ import recursive_reverse, num_1000',
        number=10000))
print(
    timeit(
        "recursive_reverse(num_10000)",
        setup='from __main__ import recursive_reverse, num_10000',
        number=10000))


def memoize(f):
    cache = {}
    def decorate(*args):
        if args in cache:
            return cache[args]
        else:
            cache[args] = f(*args)
            return cache[args]
    return decorate


@memoize
def recursive_reverse_mem(number):
    if number == 0:
        return str(number % 10)
    return f'{str(number % 10)}{recursive_reverse_mem(number // 10)}'

print('Оптимизированная функция recursive_reverse_mem')
print(
    timeit(
        'recursive_reverse_mem(num_100)',
        setup='from __main__ import recursive_reverse_mem, num_100',
        number=10000))
print(
    timeit(
        'recursive_reverse_mem(num_1000)',
        setup='from __main__ import recursive_reverse_mem, num_1000',
        number=10000))
print(
    timeit(
        'recursive_reverse_mem(num_10000)',
        setup='from __main__ import recursive_reverse_mem, num_10000',
        number=10000))

print('-'*50)
STR_CODE_1 = '''
from random import randint
def recursive_reverse(number):
    if number == 0:
        return str(number % 10)
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'
recursive_reverse(randint(100000000, 10000000000000))
'''

print('Не оптимизированная функция recursive_reverse')
print(timeit(STR_CODE_1, number=10000))
print(timeit(STR_CODE_1, number=10000))
print(timeit(STR_CODE_1, number=10000))


STR_CODE_2 = '''
from random import randint
def memoize(f):
    cache = {}
    def decorate(*args):
        if args in cache:
            return cache[args]
        else:
            cache[args] = f(*args)
            return cache[args]
    return decorate
@memoize
def recursive_reverse_mem(number):
    if number == 0:
        return ''
    return f'{str(number % 10)}{recursive_reverse_mem(number // 10)}'
recursive_reverse_mem(randint(100000000, 10000000000000))
'''
print('Оптимизированная функция recursive_reverse_mem')
print(timeit(STR_CODE_2, number=10000))
print(timeit(STR_CODE_2, number=10000))
print(timeit(STR_CODE_2, number=10000))

'''
РЕЗУЛЬТАТ СТАРОЙ ПРОГРАММЫ
Не оптимизированная функция recursive_reverse
0.013200900008087046
0.01499459998740349
0.0281785000115633
Оптимизированная функция recursive_reverse_mem
0.00113640000927262
0.0011029999877791852
0.0011336000025039539
'''

'''
РЕЗУЛЬТАТ НОВОЙ ПРОГРАММЫ
Не оптимизированная функция recursive_reverse
0.04887040000176057
0.04414849999011494
0.04058909999730531
Оптимизированная функция recursive_reverse_mem
0.06846899999072775
0.06551289999333676
0.06719770000199787
'''

'''
Анализ: 
Использование мемоизации не корректно в данном номере, так как она применяется для оптимизации вычислений, но в данном 
примере их нет. Мы видим большую скорость выполнения за счет того, что мы передаем одно и тоже число в нашу функцию, и 
это число уже хранится в памяти.
Если попробовать произвести замеры, когда входные числа будут меняться, тогда мы увидим противоположный результат и 
поймем неэффективность данного метода в данной ситуации.
'''