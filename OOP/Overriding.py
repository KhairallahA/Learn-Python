# class CountryInfo:
#     def print_language():
#         print('English')

# class Australia(CountryInfo):
#     pass

# class Lebanon(CountryInfo):
#     def print_language():
#         print('Arabic')

# class Spain(CountryInfo):
#     def print_language():
#         print('Spanish')

# au = Australia
# le = Lebanon
# sp = Spain

# au.print_language()
# le.print_language()
# sp.print_language()

# ///////////////////////////////////////////////////////
# ////////////////////////////////////////////////////////

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# class Student(Person):
#     def __init__(self, name, age, specialization):
#         super().__init__(name, age)
#         self.specialization = specialization

# s = Student('Mhamad', 24, 'Computer Science')
# print("Name:", s.name)
# print("Age:", s.age)
# print("Specialization:", s.specialization)

# ///////////////////////////////////////////////////////
# ////////////////////////////////////////////////////////
# Error

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# class Student(Person):
#     def __init__(self, name, age, specialization):
#         super().__init__(name, age)
#         self.specialization = specialization

#     def print_info():
#         print('Name:', self.name)
#         print("age:", self.age)
#         print("specialization:", self.specialization)

# s = Student('Mhamad', 24, 'Computer Science')
# s.print_info()