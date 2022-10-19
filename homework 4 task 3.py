"""
Задание 3.
Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.
Сделайте профилировку каждого алгоритма через timeit
Обязательно предложите еще свой вариант решения!
Сделайте вывод, какая из четырех реализаций эффективнее и почему!
"""
from timeit import timeit
from random import randint


def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers(enter_num, revers_num)


STR_REVERS = '''
def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers(enter_num, revers_num)
revers(1000000000000000000000)
'''


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


STR_REVERS_2 = ''' 
def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num
revers_2(1000000000000000000000)
'''


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


STR_REVERS_3 = '''
def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num
revers_3(1000000000000000000000)
'''


def revers_4(enter_num):
    return str(enter_num)[::-1]


STR_REVERS_4 = '''
def revers_4(enter_num):
    return str(enter_num)[::-1]
revers_4(1000000000000000000000)
'''
enter_num = 1000000000000000000000
print("Замеры времени для revers")
print(timeit(STR_REVERS, number=100000))
print(timeit("revers(enter_num)", "from __main__ import revers,enter_num", number=100000))
print(timeit("revers(enter_num)", globals=globals(), number=100000))

print("Замеры времени для revers_2")
print(timeit(STR_REVERS_2, number=100000))
print(timeit("revers_2(enter_num)", "from __main__ import revers_2,enter_num", number=100000))
print(timeit("revers_2(enter_num)", globals=globals(), number=100000))

print("Замеры времени для revers_3")
print(timeit(STR_REVERS_3, number=100000))
print(timeit("revers_3(enter_num)", "from __main__ import revers_3,enter_num", number=100000))
print(timeit("revers_3(enter_num)", globals=globals(), number=100000))

print("Замеры времени для revers_4")
print(timeit(STR_REVERS_4, number=100000))
print(timeit("revers_4(enter_num)", "from __main__ import revers_4,enter_num", number=100000))
print(timeit("revers_4(enter_num)", globals=globals(), number=100000))

''' РЕЗУЛЬТАТЫ:
Замеры времени для revers
0.3528879999939818
0.34695199999259785
0.34116029999859165
Замеры времени для revers_2
0.20867230001022108
0.20829870000306983
0.21137669999734499
Замеры времени для revers_3
0.025790400002733804
0.020687199998064898
0.027305600000545382
Замеры времени для revers_4
0.024825999993481673
0.019934900003136136
0.020816900010686368
'''

'''
Выводы: При проведении замеров мы получаем, что revers_3 и revers_4 почти одинаковы по эффективности, однако revers_4 
немного быстрее revers_3, т.к. он использует такой же механизм работы, только немного сокращенный.
revers_3 и revers_4 являются наиболее эффективными, так как в них нет сложной логики, а просто происходит отзеркаливание
строки из числа, в то время как в revers используется рекурсия, что сильно влияет на скорость, а в revers_2 используется
цикл, что, конечно, быстрее, однако все равно не так эффективно
'''