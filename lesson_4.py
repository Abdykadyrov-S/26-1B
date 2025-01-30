"Методы строк"
"""
'текст(строка)'.название(х)
"""

# text = "qwerty"
# print(len(text))

# text = "qwertyqq"

# print(text.count("q"))
# print(text.count("y"))

# print(text.upper())

# text_2 = 'qwert'.upper()
# print(text_2)

# print(text_2.count("W"))

# text = "qwqwghyvghQbdqwe Qwewq hbhbrqQ, qwe".upper()

# # q_1 = text.count("q")
# # q_2 = text.count("Q")

# print(text.count("Q"))


# text = "qwqwghyvghQbdqwe Qwewq hbhbrqQ, qwe".lower()

# print(text)



"Условия. Ветвления в Python"
"Условные операторы. Условные конструкции"

"""
if - условный оператор который создает условную конструкцию

if условие:
    код который должен сработать если условие правильное
if 5 > 4:
    print("Hello world")

if True:
    код работает

if False:
    код не работает
"""

# if 2 < 8:
#     print("Hello world")

# print(2 < 8)


# if True:
#     print("hi")

# if False:
#     print("hi")


# if 34 > 5:
#     print("qwerty")


# if 5 > 4:
#     print("5 > 4")
# if 5 < 4:
#     print("5 < 4")
# if 5 == 4:
#     print("5 == 4")

"""
elif - условный оператор который ставится всегда после if 
так же он может использоваться много раз
"""

# if 5 > 4:
#     print("5 > 4")
# elif 5 > 4:
#     print("5 < 4")
# elif 5 > 4:
#     print("5 == 4")


# age = int(input("Введите возраст: "))

# if  12 > age > 6:
#     print("Добро пожаловать!")
# elif 2 < age <= 6:
#     print("Добро пожаловать но с опекуном!")
# elif age > 12:
#     print("Не Добро пожаловать!")


"""
else - условный оператор который срабатывает 
если все выше указанные условия не правильные
всегда пишется в конце
"""

# age = int(input("Введите возраст: "))

# if age > 12:
#     print("Вход доступен только для детей не достигших 12")
# else: 
#     print("Добро пожаловать!")



num1 = int(input("ВВедите первое число: "))
choice = input("Выберите действие: ")
num2 = int(input("ВВедите второе число: "))

if choice == '+':    
    num = 12
    if 3 > 2:
        print("12345")
    elif 4 > 5:
        print("qwerty")
    else:
        print("qwerty")
    
    print(num1 + num2)
elif choice == '-':
    print(num1 - num2)
elif choice == '*':
    print(num1 * num2)
elif choice == '/':
    print(num1 / num2)
else:
    print("Выберите одно из действий: +, -, *, /")