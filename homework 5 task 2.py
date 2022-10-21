"""
Задание 2.
Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив,
элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F.
Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
Подсказка:
Попытайтесь решить это задание в двух вариантах
1) через collections
defaultdict(list)
int(, 16)
reduce
2) через ООП
вспомните про перегрузку методов
__mul__
__add__
"""

class HexNumbers:

    def __init__(self, num):
        self.number = [elem for elem in num]

    def __add__(self, other):
        num1 = int(''.join(self.number), 16)
        num2 = int(''.join(other.number), 16)
        return hex(num1 + num2).split('x')[-1]

    def __mul__(self, other):
        num1 = int(''.join(self.number), 16)
        num2 = int(''.join(other.number), 16)
        return hex(num1 * num2).split('x')[-1]


hex1 = HexNumbers("A2")  # > cf1
hex2 = HexNumbers("C4F")  # > 7c9fe
print(hex1 + hex2)
print(hex1 * hex2)