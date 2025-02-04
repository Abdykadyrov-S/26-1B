"Циклы for and while"

"""Циклы предназначены для повторения 
определенного кода
и для перебора значений"""

number_str = '12345678'
#             01234567

number_lis = [12, "qwert", (12,), [12,12,12]]
#             0     1        2         3

number_tuple = (12,12,34,56,8)
#               0   1  2 3  4



"Цикл for"

"""
for переменная in итер.тип:
    код который зависит от цикла
    код который сработает несколько раз

for переменная in range(5):
    код который зависит от цикла
    код который сработает несколько раз
"""


# my_list = [0,1,2,3,4,5,6]

# print(my_list[1:6])
# range(1,6)

# for i in range(20, 30, 2):
#     # print("Hello world !")
#     print(i)

"""
Итерация (Iteration) – это одно из повторений цикла 
(один шаг или один "виток" циклического процесса). 
К примеру цикл из 3-х повторений можно представить 
как 3 итерации.
"""

# numbers = [0,1,2,3,4]
# for number in numbers:
#     print(number)
#     # 0
#     # 1
#     print("Hello world !")

# for i in range(1, 6):
#     age = int(input("Введите возраст: "))
#     print(f"{i} ребенку {age}")
#     if age < 12:
#         print("you can pass")
#     else:
#         print("sorry")

"""
continue 
break
"""
# students = ['Шермамат', 'Мундуз', 'Нурсеит', 'Бекзат', 'Тамерлан', 'Абдуллох']

# for student in students:
#     if student == 'Бекзат':
#         print(f"Привет {student}")
#         continue
#     print(student)
#     print("Hello world!") 

#     if student == 'Нурсеит':
#         break




"Цикл while - бесконечный чикл"

"""
while условие:
    код который зависит от цикла
    код который сработает если условие правильное

while 4 > 3:
    print("Hello world!")

while True:

"""


# while 4 > 3: 
#     print("Hello world!")


# if True:
#     print("Hello world!")

# while True:
#     print("Hello world!")

num = 0
while True:
    print(num) 
    if num == 4:
        break
    print("Hello world!")
    # num = num + 1
    num += 1
else:
    print("Конец")



