"Dict - Словари"
"""
dict()
Словарь — неупорядоченная структура данных, 
которая позволяет хранить пары «ключ — значение».
"""

"""
peremen = {'key':'value'}
"""
# my_list = ["Akbar", 17, 1.90, ['basketball', 'coding']]
#             0      1    2            3

# my_list[0] = 'no name'
# print(my_list)
# print(my_list[0])



# my_dict = {'name':"Akbar", 'age':17, 'height':1.90, 'hobbies':['basketball', 'coding']}

# my_dict['name'] = 'no name'
# print(my_dict)
# print(my_dict['name'])


# my_dict = dict(key=123, key2='qwerty', key3=True)
# print(my_dict)


# my_dict = {
#     'name':"Akbar", 
#     'age':17, 
#     'height':1.90, 
#     'hobbies':['basketball', 'coding'],
#     'dict2': {
#         'key1': 1,
#         'key2': 2
#     }
# }


# res = my_dict.get('age2', 12)
# res_2 = my_dict['age2']

# print(my_dict['age'])

# print(my_dict.get('age2', 12))
# print(my_dict)

# print()
# print(my_dict.setdefault('age2', 'default'))
# print(my_dict)


"dict.keys()"

my_dict = {'name':"Akbar", 'age':17, 'height':1.90}

# print(my_dict)
# print(my_dict.keys())

# for i in my_dict:
#     print(i)

# for i in my_dict.keys():
#     print(i)

"dict.values()"

# my_dict = {'name':"Akbar", 'age':17, 'height':1.90}

# print(my_dict)
# print(my_dict.values())

# for i in my_dict.values():
#     print(i)

"dict.items()"

# my_dict = {'name':"Akbar", 'age':17, 'height': 1.90}

# print(my_dict)
# print(my_dict.items())

# for k,v in my_dict.items():
#     # print(k)
#     # print(v)
#     print(f"{k} - {v}")


"Множества в Python (set, frozenset)"
"""Можно сказать, что set напоминает словарь, 
в котором ключи не имеют соответствующих им значений"""

# my_set = {12}
# print(type(my_set))

# my_set = {"Akbar", 17, 1.90}
# #           0       1    2

# print(my_set)

# set_numbers = {1,3,5,6,8, 'qw', 'a', 'b', 1.2, True,1,2,9,3,4,7,2,3,4,8,6}
# print(set_numbers)


my_list = [True, 12, 1.2, "text", (12,12), "text", 1.2]
# print(my_list)

new_set = set(my_list)
# print(type(new_set))
# print(new_set)

# for i in new_set:
#     print(i)

