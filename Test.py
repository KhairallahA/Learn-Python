print("hello world!")

# language = [str] * 4
# # هنا قمنا بوضع قيمة في كل عنصر فيها
# language[0] = 'Arabic'
# language[1] = 'English'
# language[2] = 'French'
# language[3] = 'Spanish'
# # هنا قمنا بإضافة عنصر جديد على المصفوفة
# language.append('German')
# # هنا قمنا بعرض قيم المصفوفة و عدد عناصرها
# print('Stored languages:', language)
# print('Number of stored languages is:', len(language))

# ///////////////////////////////////////////////////////
# ////////////////////////////////////////////////////////

# languages = ('Arabic', 'English','Spanish', 'German')
# print('Stored languages:', languages)
# print('Number of stored languages is:', len(languages))

# ///////////////////////////////////////////////////////
# ////////////////////////////////////////////////////////

# languages = {'Arabic', 'English','Spanish', 'German'}
# print('Stored languages:', languages)
# print('Number of stored languages is:', len(languages))

# ///////////////////////////////////////////////////////
# ////////////////////////////////////////////////////////

# يتألف من 5 عناصر dictionary هنا قمنا بتعريف
# dictionary = {
#     1: 'One',
#     2: 'Tow',
#     3: 'Three',
#     4: 'Four',
#     5: 'Five'
# }
# هنا قمنا بعرض قيمة العنصر الذي يحمل المفتاح رقم 3
# print(dictionary[2])

# ///////////////////////////////////////////////////////
# ////////////////////////////////////////////////////////

# userr= "Khale"
# if userr == "Khaled":
#     print("hello Khaled!")
# elif userr == "Khairallah":
#     print("hello Khairallah!")
# else:
#     print("No hello!")

# ///////////////////////////////////////////////////////
# ////////////////////////////////////////////////////////

# first_name = 'Khairallah'
# last_name = 'AL-Awady'
# full_name = first_name + ' ' + last_name
# print(full_name)

# full_namee = 'Khaled' ' AL-Awady'
# print(full_namee)

# s = 'hello world!!'
# print(len(s))

# s = 'My name is khairallah\n\nI am from Yemen'
# print(s)

# ///////////////////////////////////////////////////////
# ////////////////////////////////////////////////////////

# days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
# for day in days:
#     print(day)

# for n in range(5):
#     print(n)

# for n in range(5, 0, -1):
#     print(n)

# i = 1
# while i <= 10:
#     print(i)
#     i += 1
# else:
#     print("hello world!!")

# for i in range(1, 6):
#     if i==4:
#         continue
#     print(i)

# sentence = 'Khairallah'
# for n in sentence:
#     if n == 'r':
#         continue
#     print(n)

# ///////////////////////////////////////////////////////
# ////////////////////////////////////////////////////////
# Lists

# names = ['Rami', 'Sara', 'Nada', 'Mhamad', 'Salem']
# # print(names[-1])
# # print(names[-2])
# for i in names:
#     print(i)

# numbers = [10, 20, 30, 40, 50]
# total = 0
# for i in numbers:
#     total += i
# print(total)

# numbers = [10, 20, 30, 40, 50]
# del numbers[0]
# del numbers[1]
# print(numbers)   # Result = [20, 40, 50]

# numbers = [10, 20, 30, 40, 50]
# del numbers[0:3]
# print(numbers)   # Result = [40, 50]

# numbers = [10, 20, 30, 40, 50]
# print(numbers[0:3])
# numbers2 = numbers[0:3]
# print(numbers2)

# arr1 = [1, 2, 3]
# arr2 = [4, 5, 6]
# arr3 = arr1 + arr2
# print(arr3)

# arr = ['python'] * 3
# print(arr)

# arr = ['Mhamad', 'Rony', 'Rima', 'Sara']
# x = 'Rony'
# print(x in arr)

# arr = ['Mhamad', 'Rony', 'Rima', 'Sara']
# arr.append('Khairallah')
# print(arr)

# arr = ['Mhamad', 'Rony', 'Rima', 'Sara']
# arr.insert(2, 'Khairallah')
# print(arr)

# arr = ['Mhamad', 'Rony', 'Rima', 'Sara']
# languages = ['Arabic', 'English','Spanish', 'German']
# arr.extend(languages)
# print(arr)

# arr = ['Mhamad', 'Rony', 'Rima', 'Sara']
# arr2 = arr.copy()
# print(arr2)

# arr = ['Mhamad', 'Rony', 'Rima', 'Sara']
# arr.reverse()
# print(arr)

# arr_ages = [1, 2, 3, 2]
# print(arr_ages.count(2))

# arr_ages = [1, 2, 4, 3, 2, 1, 1, 2]
# arr_ages.sort()
# print(arr_ages)   # Result = [1, 1, 1, 2, 2, 2, 3, 4]

# arr_ages = [1, 2, 4, 3, 2, 1, 1, 2]
# arr_ages.clear()
# print(arr_ages)     # Result = []

# ///////////////////////////////////////////////////////
# ////////////////////////////////////////////////////////
# Tuples

# names = ('Rami', 'Sara', 'Nada', 'Mhamad', 'Salem')
# print(names[0])
# print(names[-1])

# names = ('Rami', 'Sara', 'Nada', 'Mhamad', 'Salem')
# for x in names:
#     print(x)

# numbers = (10, 20, 30, 40, 50)
# total = 0
# for x in numbers:
#     total += x
# print(total)

# numbers = (10, 20, 30, 40, 50)
# numbers2 = numbers[0:3]
# print(numbers2)

# arr1 = (1, 2, 3)
# arr2 = (4, 5, 6)
# arr3 = arr1 + arr2
# print(arr3)

# arr = ('Python',) * 3
# print(arr)

# names = ('Rami', 'Sara', 'Nada', 'Mhamad', 'Salem')
# x = 'Sara'
# print(x in names)

# numbers = (10, 20, 30, 40, 50)
# print(min(numbers))
# print(max(numbers))

# names = ('Rami', 'Sara', 'Nada', 'Mhamad', 'Salem')
# names2 = tuple(names)
# print(names2)

# ///////////////////////////////////////////////////////
# ////////////////////////////////////////////////////////
# Sets

# numbers = {10, 20, 30, 40, 50}
# print(numbers)

# names = {'Rami', 'Rami', 'Rami', 'Nada', 'Nada', 'Ahmad'}
# print(names)

# names = {'Rami', 'Nada', 'Ahmad'}
# del names
# print(names)

# names = {'Rami', 'Nada', 'Ahmed'}
# x = 'Ahmed'
# print(x in names)

# names = {'Rami', 'Nada', 'Ahmad'}
# names.add('Khairallah')
# print(names)

# names = {'Rami', 'Nada', 'Ahmad'}
# names.discard('Nada')          # Result = {'Rami', 'Ahmad'}
# names.remove('Rami')           # Result = {'Nada', 'Ahmad'}
# print(names)

# names = {'Rami', 'Nada', 'Ahmad'}
# names.clear()
# print(names)

# names = {'Rami', 'Nada', 'Ahmad'}
# names2 = names.copy()
# print(names2)

# set1 = {1, 2, 3, 4, 5}
# set2 = {1, 2, 3}
# newSet = set1.difference(set2)
# print(newSet)           # Result = {4, 5}

# set1 = {1, 2, 3, 4, 5}
# set2 = {1, 2, 3}
# set1.difference_update(set2)
# print(set1)           # Result = {4, 5}

# set1 = {1, 2, 3, 4, 5}
# set2 = {1, 2, 3}
# newSet = set1.intersection(set2)
# print(newSet)           # Result = {1, 2, 3}

# set1 = {1, 2, 3, 4, 5}
# set2 = {1, 2, 3}
# newSet = set1.symmetric_difference(set2)
# print(newSet)           # Result = {4, 5}

# set1 = {1, 2, 3, 5, 8, 7}
# set2 = {7, 2, 3, 5, 6, 1}
# set3 = {3, 4, 5, 8, 7, 9}
# newSet = set1.union(set2, set3)
# print(newSet)           # Result = {1, 2, 3, 4, 5, 6, 7, 8, 9}
# set1.update(set2, set3)
# print(set1)           # Result = {1, 2, 3, 4, 5, 6, 7, 8, 9}

# set1 = {1, 2, 3}
# set2 = {1, 7}
# set3 = {4, 5, 6}
# print('set1 disjoint set2?', set1.isdisjoint(set2))    # False
# print('set1 disjoint set3?', set1.isdisjoint(set3))    # True

# set1 = {1, 2, 3, 4, 5}
# set2 = {1, 2, 3}
# print(set1.issuperset(set2))    # True
# set1 = {1, 2, 3}
# set2 = {1, 2, 3, 4, 5}
# print(set1.issuperset(set2))    # False

# set1 = {1, 2, 3}
# set2 = {1, 2, 3, 4, 5}
# print(set1.issubset(set2))    # True
# set1 = {1, 2, 3, 4, 5}
# set2 = {1, 2, 3}
# print(set1.issubset(set2))    # False

# ///////////////////////////////////////////////////////
# ////////////////////////////////////////////////////////
# dict

# data = {
#     'id': 1,
#     'name': 'Khairallah',
#     'moblie': 7777777777
# }
# print(data)
# print(data['name'])

# data = {
#     1: 'Admin',
#     2: 'Editor',
#     3: 'Reader'
# }
# print(data[1])

# data = {
#     1: 'Admin',
#     2: 'Editor',
#     3: 'Reader'
# }
# for key in data:
#     print(key)

# data = {
#     1: 'Admin',
#     2: 'Editor',
#     3: 'Reader'
# }
# for key in data:
#     print(data[key])

# data = {
#     1: 'Admin',
#     2: 'Editor',
#     3: 'Reader'
# }
# data[4] = 'Author'
# print(data)

# data = {
#     1: 'Admin',
#     2: 'Editor',
#     3: 'Reader'
# }
# data[3] = 'Subscriber'
# print(data)           # Result = {1: 'Admin', 2: 'Editor', 3: 'Subscriber'}

# data = {
#     1: 'Admin',
#     2: 'Editor',
#     3: 'Reader'
# }
# del data[3]
# print(data)           # Result = {1: 'Admin', 2: 'Editor'}

# data = {
#     1: 'Admin',
#     2: 'Editor',
#     3: 'Reader'
# }
# print(3 in data)      # True

# data = {
#     1: 'Admin',
#     2: 'Editor',
#     3: 'Reader'
# }
# print(len(data))

# data = {
#     1: 'Admin',
#     2: 'Editor',
#     3: 'Reader'
# }
# print(data.popitem())         # Result = (3, 'Reader')

# data = {
#     1: 'Admin',
#     2: 'Editor',
#     3: 'Reader'
# }
# print(data.keys())           # Result = dict_keys([1, 2, 3])
# print(data.values())         # Result = dict_values(['Admin', 'Editor', 'Reader'])
# print(data.items())         # Result = dict_items([(1, 'Admin'), (2, 'Editor'), (3, 'Reader')])

# ///////////////////////////////////////////////////////
# ////////////////////////////////////////////////////////
# Function

# def my_function():
#     print("hello")
# my_function()

# def greeting(name):
#     print('hello ' + name)
# #1
# user = 'Khairallah'
# greeting(user)
# #2
# name = 'Khairallah'
# greeting(name)
# #3
# greeting('Khairallah')

# def get_sum(a, b):
#     return a + b
# #1
# x = get_sum(3, 5)
# print(x)
# #2
# print(get_sum(3, 7))

# def print_language(language='English'):
#     print('Your language is: ', language)
# print_language()
# print_language('Arabic')

# def print_info(name, salary):
#     print('Name: ', name)
#     print('Salary: ', salary)
#     print('--------------------------')
# print_info('Khairallah', 1500)
# print_info(salary= 2000, name = 'Khaled')

# def print_args(*args):
#     for e in args:
#         print(e)
# print_args(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# def print_average(*values):
#     print(sum(values) + len(values))   #Result = 14
# print_average(1, 2, 3, 4)

# def print_user_average(user, *notes):
#     avg = sum(notes) + len(notes)
#     print('You are:', user, 'is:', avg)
# print_user_average('Khairallah', 1, 2, 3, 4)

# x = 1
# def test():
#     print('Global x:', x)
# test()

# x = 1
# def test():
#     x = 5
#     print("Local x:", x)   # Result = Local x: 5
# test()
# print("Global x:", x)   # Result = Global x: 1

# x = 1
# def test():
#     global x
#     x = 5
# test()
# print("Global x:", x)   # Result = Global x: 5

# total_pay = lambda price, tax: price + tax
# print(total_pay(500, 40))   # Result = 540
