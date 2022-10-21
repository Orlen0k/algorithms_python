"""
Задание 1.
Вам нужно взять 5 любых скриптов, написанных ВАМИ в рамках работы над ДЗ
курсов Алгоритмы и Основы Python
На каждый скрипт нужно два решения - исходное и оптимизированное.
Вы берете исходное, пишете что это за задание и с какого оно курса.
Далее выполняете профилирование скрипта средствами memory_profiler
Вы оптимизируете исходное решение.
Далее выполняете профилирование скрипта средствами memory_profiler
Вам нужно написать аналитику, что вы сделали для оптимизации памяти и
чего добились.
ВНИМАНИЕ:
1) скрипты для оптимизации нужно брать только из сделанных вами ДЗ
курсов Алгоритмы и Основы
2) нельзя дублировать, коды, показанные на уроке
3) для каждого из 5 скриптов у вас отдельный файл, в нем должна быть версия до
и версия после оптимизации
4) желательно выбрать те скрипты, где есть что оптимизировать и не брать те,
где с памятью и так все в порядке
5) не нужно писать преподавателю '''я не могу найти что оптимизировать''', это
отговорки. Примеров оптимизации мы перечислили много: переход с массивов на
генераторы, numpy, использование слотов, применение del, сериализация и т.д.
Это файл для первого скрипта
"""

from itertools import groupby
from collections import Counter
from memory_profiler import memory_usage


def memory_measur(func):
    def wrapper(*args, **kwargs):
        m1 = memory_usage()
        res = func(args[0])
        m2 = memory_usage()
        mem_diff = m2[0] - m1[0]
        return mem_diff

    return wrapper


string = "2000 10003 1234000 44444444 9999 11 11 22 123"


# Базовая реализация
@memory_measur
def order_weight(strng):
    start_dict = {key: sum([int(el) for el in key]) for key in strng.split(' ')}
    count_element = Counter(strng.split(' '))
    value = list(start_dict.values())
    value.sort()
    result = []
    for num in [el for el, _ in groupby(value)]:
        sort_list = []
        for key, value in start_dict.items():
            if num == value:
                for _ in range(count_element[key]):
                    sort_list.append(key)
        else:
            sort_list.sort()
            for val in sort_list:
                result.append(val)
    return ' '.join(result)


# Оптимизированная реализация
@memory_measur
def order_weight_up(strng):
    return ' '.join(sorted(sorted(strng.split(' ')), key=lambda x: sum(int(c) for c in x)))


print(f"Базовая реализация заняла памяти: {order_weight(string)} Mib")
print(f"Оптимизированная реализация заняла памяти: {order_weight_up(string)} Mib")

'''Выводы
Базовая реализация заняла памяти: 0.01171875 Mib
Оптимизированная реализация заняла памяти: 0.0 Mib
'''
'''Анализ измененного кода
Упростил решение, избавился от создания лишних переменных, за счет этого получилось потратить меньше памяти 
'''