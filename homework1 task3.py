"""
Задание 3.
Для этой задачи
1) придумайте 2-3 решения (обязательно с различной сложностью)
2) оцените сложность каждого выражения в этих решениях в нотации О-большое
3) оцените итоговую сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему
Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.
Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""


companies = {'ARS': 526879.45, 'SECT': 895674.32, 'FOX': 789456213.78, 'ZZZ': 478956213.56, 'XXX': 4789555555.55}

# 1 способ O(N^2)
def sorted_1(companies):
    list_from_dict = list(companies.items())
    for i in range(len(list_from_dict)):
        lowest_value_index = i
        for j in range(i + 1, len(list_from_dict)):
            if list_from_dict[j][1] > list_from_dict[lowest_value_index][1]:
                lowest_value_index = j
        list_from_dict[i], list_from_dict[lowest_value_index] = list_from_dict[lowest_value_index], list_from_dict[i]
    print(list_from_dict[0:3])

(sorted_1(companies))
#
# 2 способ
sorted_companies = sorted(companies, key=companies.get, reverse=True)[:3]
for i in sorted_companies:
    print(i, ':', companies.get(i))

# O(1)

#
# Эффективнее 2 способ