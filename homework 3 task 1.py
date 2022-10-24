"""
Задание 1.
Реализуйте функции:
a) заполнение списка, оцените сложность в O-нотации (операции нужно провдить в цикле)
 заполнение словаря, оцените сложность в O-нотации (операции нужно провдить в цикле)
 сделайте аналитику, что заполняется быстрее и почему
 сделайте замеры времени
b) получение элемента списка, оцените сложность в O-нотации (операции нужно провдить в цикле)
 получение элемента словаря, оцените сложность в O-нотации (операции нужно провдить в цикле)
 сделайте аналитику, что заполняется быстрее и почему
 сделайте замеры времени
с) удаление элемента списка, оцените сложность в O-нотации (операции нужно провдить в цикле)
 удаление элемента словаря, оцените сложность в O-нотации (операции нужно провдить в цикле)
 сделайте аналитику, что заполняется быстрее и почему
 сделайте замеры времени
ВНИМАНИЕ: в задании три пункта
НУЖНО выполнить каждый пункт
обязательно отделяя каждый пункт друг от друга
Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)
вы уже знаете, что такое декоратор и как его реализовать,
обязательно реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к своим функциям!
"""

from time import time

n = 10 ** 5

def time_decorator(func):
    def timer(*args, **kwargs):
        stat = time()
        result = func(*args, **kwargs)
        end = time()
        print(f'Функция {func.__name__}' f' Выполнилась за {end - stat}')
        return result
    return timer

@time_decorator
def fill_list_append(lst, num):
    for i in range(num):
        lst.append(i)     #Сложность О(1)

some_list = []
fill_list_append(some_list, n)
print('_' * 100)

@time_decorator
def fill_list_insert(lst, num):
    for i in range(num):
        lst.insert(0, i)   # сложность О(n)

some_list = []
fill_list_insert(some_list, n)
print('_' * 100)


@time_decorator
def fill_dict(dct, num):
    for i in range(num):     # сложность O(1)
        dct[i] = i


some_dict = {}
fill_dict(some_dict, n)
print('_' * 100)
#
# Функция fill_list_append Выполнилась за 0.004122018814086914
# ____________________________________________________________________________________________________
# Функция fill_list_insert Выполнилась за 1.3407790660858154
# ____________________________________________________________________________________________________
# Функция fill_dict Выполнилась за 0.016201019287109375
# ____________________________________________________________________________________________________
#
# Process finished with exit code 0

# Функция fill_list_append, Функция fill_dict имееет О (1) означает, что данной операции требуется константное время.
# Такие операции не зависят от количества входных данных.
# При этом работа с  типом данных list занимает меньше времени чем с dict, поэтому первая функция выполняется быстрее

# удаление, получение индекса по ключу

@time_decorator
def change_list(lst):
    for i in range(10000):
        lst.pop(i)
    for j in range(1000):
        lst[j] = lst[j + 1]

change_list(some_list)
print('_' * 100)

# В функции change_list если обращаться по индексу с изменением элемента списка выполняется за О(1)
# если с конца списка lst.pop(i) то за О(n)

@time_decorator
def change_dict(dct):
    for i in range(10000):
        dct.pop(i)
    for j in range(1000, 2002):
        dct[j] = 'fill'

change_dict(some_dict)
print('_' * 100)

# В функции change_dict(some_dict) операции изменения проходят за О(1) и отрабатывает быстрее
# Функция change_list Выполнилась за 1.6875998973846436
# ____________________________________________________________________________________________________
# Функция change_dict Выполнилась за 0.001047372817993164
# ____________________________________________________________________________________________________
#
# Process finished with exit code 0
#
