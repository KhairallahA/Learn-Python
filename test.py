print("hello world!!")

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
