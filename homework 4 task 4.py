"""
Задание 4.
Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.
Сделайте профилировку каждого алгоритма через timeit
Обязательно напишите третью версию (здесь возможно даже решение одной строкой).
Сделайте замеры и опишите, получилось ли у вас ускорить задачу
"""
from timeit import timeit

array = [1, 3, 1, 3, 4, 5, 1, 5, 5, 5, 5, 5, 5]


def func_1():
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


def func_2():
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'


def func_3():
    new_array = {array.count(elem): elem for elem in set(array)}
    return f'Чаще всего встречается число {new_array[max(new_array)]}, ' \
           f'оно появилось в массиве {max(new_array)} раз(а)'


print("Замеры времени для func_1")
print(func_1())
print(timeit("func_1()", "from __main__ import func_1,array", number=100000))
print(timeit("func_1()", globals=globals(), number=100000))
print('-' * 50)
print("Замеры времени для func_2")
print(func_2())
print(timeit("func_2()", "from __main__ import func_2,array", number=100000))
print(timeit("func_2()", globals=globals(), number=100000))
print('-' * 50)
print("Замеры времени для func_3")
print(func_3())
print(timeit("func_3()", "from __main__ import func_3,array", number=100000))
print(timeit("func_3()", globals=globals(), number=100000))

''' РЕЗУЛЬТАТЫ
Замеры времени для func_1
Чаще всего встречается число 5, оно появилось в массиве 7 раз(а)
0.15871830000833143
0.1675249999971129
--------------------------------------------------
Замеры времени для func_2
Чаще всего встречается число 5, оно появилось в массиве 7 раз(а)
0.19914750001044013
0.20635619999666233
--------------------------------------------------
Замеры времени для func_3
Чаще всего встречается число 5, оно появилось в массиве 7 раз(а)
0.13114710000809282
0.12883240000519436
ВЫВОДЫ: получилось реализовать более эффективный алгоритм, благодаря использованию словаря для подсчетов
'''