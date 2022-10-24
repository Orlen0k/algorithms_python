''' Задача
Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число». Реализуйте перегрузку методов
сложения и умножения комплексных чисел. Проверьте работу проекта. Для этого создаёте экземпляры класса
(комплексные числа), выполните сложение и умножение созданных экземпляров. Проверьте корректность полученного результата
'''
import re
from memory_profiler import memory_usage


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


class СomplexNumber:

    def __init__(self, number):
        number = number.replace(" ", "")
        try:
            self.valid = int(re.match("\d+[+-]+", number).group()[:-1])
            self.novalid = int(re.search("[+-]\d+", number).group())
        except AttributeError:
            print("Введенное число некорректно")

    @memory_measur
    def __add__(self, other):
        res = self.novalid + other.novalid
        return f"{self.valid + other.valid}" if res == 0 else f"{self.valid + other.valid}{'+' if res > 0 else ''}{res}i"

    def __mul__(self, other):
        res = self.valid * other.novalid + self.novalid * other.valid
        return f"{self.valid * other.valid - self.novalid * other.novalid}" if res == 0 else f"{self.valid * other.valid - self.novalid * other.novalid}{'+' if res > 0 else ''}{res}i"


a = СomplexNumber("12+44i")
b = СomplexNumber("15-3i")
c = СomplexNumber("1sd2-3i")
print(f"Сумма: {a + b}")


@memory_measur
def sum_complex_number(x, y):
    return x + y


print(f"Сумма: {sum_complex_number(12 + 44j, 15 - 3j)}")

'''Результаты 
Выполнение заняло 0.0078125 Mib
Сумма: 27+41i
Выполнение заняло 0.0 Mib
Сумма: (27+41j)
'''
'''Анализ измененного кода
Для работы с комплексными числами воспользовался встроенными операциями для упрощения кода 
'''