"""
Задание 1.
Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива
Сделайте замеры времени выполнения кода с помощью модуля timeit
Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры
ОБЯЗАТЕЛЬНО! Добавьте аналитику: что вы сделали и какой это принесло эффект
"""


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


from timeit import timeit

STR_CODE_1 = '''
def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr

func_1(range(1000))
'''


def func_1(nums):  # O(N)
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):  # O(N)
    return [i for i in range(len(nums)) if nums[i] % 2 == 0]


'''
Анализ оптимизированного кода: заполнение массива происходит при помощи list comprehension, что позволило не создавать 
новый массив, также удалось избавится от команды append
'''
STR_CODE_2 = '''
def func_2(nums):
    return [i for i in range(len(nums)) if nums[i] % 2 == 0]
func_2(range(1000))
'''

nums = range(1000)

print("Замеры времени для func_1")
print(timeit(STR_CODE_1, number=1000))
print(timeit("func_1(nums)", "from __main__ import func_1,nums", number=1000))
print(timeit("func_1(nums)", globals=globals(), number=1000))
print("Замеры времени для оптимизированной функции")
print(timeit(STR_CODE_2, number=1000))
print(timeit("func_2(nums)", "from __main__ import func_2,nums", number=1000))
print(timeit("func_2(nums)", globals=globals(), number=1000))

'''
Результаты:
Замеры времени для func_1
0.08553630000096746
0.08505729999160394
0.08515339999576099
Замеры времени для оптимизированной функции
0.07145309999759775
0.06903139999485575
0.06839970000146423
Вывод: нам удалось оптимизировать функцию и ускорить время ее выполнения
'''