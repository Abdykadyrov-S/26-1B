"Исключения"

# print(2 + 2)
# print(12 / 0)
# print(2 + 2)

"""
try:
    код который написан с ошибкой
    код который нужно обработать
except ВидИсключения as переменное:
    print("Описание ошибки")
"""

# print("Hello world!")

# try:
#     print(12 / 0)
# except BaseException :
#     print("Делить на ноль нельзя!") 

# print("Hello world!")


# try:
#     print(12 / 0)
# except ZeroDivisionError as e:
#     print(f"Выходит ошибка: {e}") 

# try:
#     print(12 + '23')
# except TypeError as e:
#     print(f"Выходит ошибка: {e}") 

# try:
#     while True:
#         print("Привет Мир")
# except KeyboardInterrupt as e:
#     print("Выход")


try:
    "исполняем какой-то код"
except Exception as e:
    "обработка исключения"
else:
    """
    код, который будет исполнен в случае, 
    когда не возникает исключения
    """
finally:
    """
    код, который гарантированно будет исполнен 
    последним (всегда исполняется)
    """

# print(12 + '12')


# try:
#     number = int(input("Введите число: "))
#     print(number + '12')
# except BaseException as error:
#     raise TypeError("Разные типы данных")
#     # print(f"Разные типы данных \nПодробнее: {error}")
# else:
#     print("Исключение не сработало")
# finally:
#     print("Hello world!")

# n_save_p = ['12345678', 'abcdrfg', 'qwertyu', '11111111111']

# user_password = input("Введите пароль: ")
# if len(user_password) < 8:
#     # print("не менее 8 символов")
#     raise BaseException("Пароль должен быть не менее 8 символов")
# for p in n_save_p:
#     if p == user_password:
#         raise BaseException("Не безопасный пароль")


"Функции"
"""
Функция в программировании представляет собой обособленный участок кода,
который можно вызывать, обратившись к нему по имени, которым он был
назван. При вызове происходит выполнение команд тела функции.
"""

"""
Функция - это изолированный участок кода который
мы можем вызвать когда нам это необходимо
"""

"""
def назв_функции():
    код который будет изолирован

назв_функции()
"""

# def greeting():
#     print("Привет Мира!")

# print(2 + 2)
# print(2 == 2)

# greeting()


def hi():
    num = 0
    while True:
        if num == 4:
            break
        print("Hello world!")
        num += 1

hi()

