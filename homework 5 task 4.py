"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.
Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы
И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""

from collections import OrderedDict
from timeit import timeit

ord_dict = OrderedDict([(elem,elem) for elem in list(range(1000))])
normal_dict = {elem:elem for elem in list(range(1000))}

def get_normal_dict():
    return normal_dict[500]

def get_ord_dict():
    return ord_dict[500]


print("Замеры получения элемента по индексу для normal_dict")
print(timeit("get_normal_dict()", globals=globals(), number=10000000))  # > 0.6412126
print("Замеры получения элемента по индексу для ord_dict")
print(timeit("get_ord_dict()", globals=globals(), number=10000000))  # > 0.6935593
print('-' * 50)


def del_normal_dict():
    del normal_dict[1]

def del_ord_dict():
    del ord_dict[1]


print("Замеры удаления элемента по индексу для normal_dict")
print(timeit("del_normal_dict()", globals=globals(), number=1))  # > 1.3000000000928935e-06
print("Замеры удаления элемента по индексу для ord_dict")
print(timeit("del_ord_dict()", globals=globals(), number=1))  # > 1.000000000139778e-06
print('-' * 50)

def ch_normal_dict():
    normal_dict[500] = 1

def ch_ord_dict():
    ord_dict[500] = 1


print("Замеры изменения элемента по индексу для normal_dict")
print(timeit("ch_normal_dict()", globals=globals(), number=10000000))  # > 0.7502898
print("Замеры изменения элемента по индексу для ord_dict")
print(timeit("ch_ord_dict()", globals=globals(), number=10000000))  # > 0.9843513000000002
print('-' * 50)

'''Выводы:
Почти все основные действия ord_dict выполняет дольше, чем normal_dict, за исключением удаления элемента по индексу.
Я считаю, что OrderedDict еще можно использовать в различных задачах и есть смысл его использования.
'''