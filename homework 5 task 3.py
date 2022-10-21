"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно
что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list
Задача: создайте простой список (list) и очередь (deque).
Выполните различные операции с каждым из объектов.
Сделайте замеры и оцените, насколько информация в документации
соответствует дейстивтельности.
1) сравнить операции
append, pop, extend списка и дека и сделать выводы что и где быстрее
2) сравнить операции
appendleft, popleft, extendleft дека и соответствующих им операций списка
и сделать выводы что и где быстрее
3) сравнить операции получения элемента списка и дека
и сделать выводы что и где быстрее
Подсказка:
для того, чтобы снизить погрешность, желательно операции по каждой ф-ции
(append, pop и т.д.) проводить в циклах. Для замеров используйте timeit.
"""
from collections import deque
from timeit import timeit

normal_list = list(range(1000))
normal_deque = deque(normal_list)
elem = 1000


# 1) сравнить операции
# append, pop, extend списка и дека и сделать выводы, что и где быстрее

def append_list(elem):
    normal_list.append(elem)


def append_deque(elem):
    normal_deque.append(elem)


print("Замеры функции append для list")
print(timeit("append_list(elem)", globals=globals(), number=1000000)) # > 0.1049763
print("Замеры функции append для deque")
print(timeit("append_deque(elem)", globals=globals(), number=1000000)) # > 0.088698
print('-' * 50)


def pop_list():
    normal_list.pop()


def pop_deque():
    normal_deque.pop()


print("Замеры функции pop для list")
print(timeit("pop_list()", globals=globals(), number=1000000))  # > 0.0745238
print("Замеры функции pop для deque")
print(timeit("pop_deque()", globals=globals(), number=1000000))  # > 0.0721398
print('-' * 50)


def extend_list(*args):
    normal_list.extend(args)


def extend_deque(*args):
    normal_deque.extend(args)


print("Замеры функции extend для list")
print(timeit("extend_list([1,2,3])", globals=globals(), number=1000000))  # > 0.1705338
print("Замеры функции extend для deque")
print(timeit("extend_list([1,2,3])", globals=globals(), number=1000000))  # > 0.1698810
print('-' * 50)

'''Выводы
Все функции +- выполняются с одинаковой скоростью что в deque, что в list
'''


# сравнить операции
# appendleft, popleft, extendleft дека и соответствующих им операций списка
# и сделать выводы что и где быстрее


def appendleft_list(elem):
    normal_list.insert(0, elem)


def appendleft_deque(elem):
    normal_deque.appendleft(elem)


print("Замеры функции appendleft(insert()) для list")
print(timeit("appendleft_list(elem)", globals=globals(), number=1000)) # > 1.4961048999999997
print("Замеры функции appendleft для deque")
print(timeit("appendleft_list(elem)", globals=globals(), number=1000)) # > 1.4961048999999997
print('-' * 50)


def popleft_list():
    del normal_list[0]


def popleft_deque():
    normal_deque.popleft()


print("Замеры функции popleft для list")
print(timeit("popleft_list()", globals=globals(), number=1000)) # > 1.6299241999999996
print("Замеры функции popleft для deque")
print(timeit("popleft_deque()", globals=globals(), number=1000))  # > 7.540000000005875e-05
print('-' * 50)


def extendleft_list(*args):
    normal_list.reverse()
    normal_list.extend(args)
    normal_list.reverse()


def extendleft_deque(*args):
    normal_deque.extendleft(args)


print("Замеры функции extendleft для list")
print(timeit("extendleft_list([1,2,3])", globals=globals(), number=1000))  # > 2.7488536999999997
print("Замеры функции extendleft_deque для deque")
print(timeit("extend_list([1,2,3])", globals=globals(), number=1000))  # > 0.00014619999999965216
print('-' * 50)

'''Выводы
Все функции, которые взаимодействуют с началом массива быстрее выполняются в deque
'''


# 3) сравнить операции получения элемента списка и дека
# и сделать выводы что и где быстрее

def get_element_list(elem):
    return normal_list[0]


def get_element_deque(elem):
    return normal_deque[0]


print("Замеры функции get_element_list() для list")
print(timeit("get_element_list(elem)", globals=globals(), number=10000000)) # > 0.6624785
print("Замеры функции get_element_deque для deque")
print(timeit("get_element_deque(elem)", globals=globals(), number=10000000)) # > 0.702499099999999
print('-' * 50)

'''Выводы
Получение элемента по индексу быстрее проходит в list, чем в deque
'''