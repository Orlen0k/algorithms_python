"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"
Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница или нет
есть ли в кэше соответствующая страница или нет
Пример кэша: {'url-адрес': 'хеш url-а'; 'url-адрес': 'хеш url-а'; ...}
Если страница в кэше есть, просто вернуть значение хеша, например, 'хеш url-а'
Если страницы в кэше нет, то вычислить хеш и записать в кэш
Подсказка: задачу решите обязательно с применением 'соленого' хеширования
и одного из алгоритмов, например, sha512
Можете усложнить задачу, реализовав ее через ООП
"""
import hashlib

# #
# salt = uuid4().hex
# cache_obj = {}
#
# def get_page(url):
#     if cache_obj.get(url):
#         print(f'этот адрес: {url} присуствует в кэшэ')
#     else:
#         res = hashlib.sha256(salt.encode() + url.encode()).hexdigest()
#         cache_obj[url] = res
#         print(cache_obj)
#
# get_page('https://geekbrains.ru/')
# get_page('https://geekbrains.ru/')
# get_page('https://geekbrains.ru/')


url = input('https://yandex.ru /')

kash = {'77fca5950e249d66b4e8bc9761ffdc7a6a5b31c619babcbdad4dd8ff4aaa5f50'}


def chek_url(u):
    hash_u = hashlib.sha256(u.encode()).hexdigest()
    if hash_u in kash.keys():
        return True
    else:
        return {hash_u: u}


chek_url(url)

try:
    kash.update(chek_url(url))
except TypeError:
    print("Такой объект уже есть в кэше")

print(kash)



