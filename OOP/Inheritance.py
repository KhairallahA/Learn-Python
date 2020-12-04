# class A:
#     x = 10
#     def print_msg():
#         print('Hello from class A')

# class B(A):
#     y = 20

# b = B
# print('y:', b.y)
# print('x:', b.x)
# b.print_msg()

# ///////////////////////////////////////////////////////
# ////////////////////////////////////////////////////////

# class A:
#     def print_a():
#         print('Hello from class A')

# class B(A):
#     def print_b():
#         print('Hello from class B')

# class C(B):
#     def print_c():
#         print('Hello from class C')

# c = C
# c.print_a()
# c.print_b()
# c.print_c()

# ///////////////////////////////////////////////////////
# ////////////////////////////////////////////////////////

# class A:
#     def print_a():
#         print('Hello from class A')

# class B:
#     def print_b():
#         print('Hello from class B')

# class C(A, B):
#     def print_c():
#         print('Hello from class C')

# c = C
# c.print_a()
# c.print_b()
# c.print_c()

# ///////////////////////////////////////////////////////
# ////////////////////////////////////////////////////////

# class A:
#     def print_a():
#         print('Hello from class A')

# class B(A):
#     def print_b():
#         print('Hello from class B')

# class C(A):
#     def print_c():
#         print('Hello from class C')

# b = B
# b.print_a()
# b.print_b()

# c = C
# c.print_a()
# c.print_c()

# ///////////////////////////////////////////////////////
# ////////////////////////////////////////////////////////

# class A:
#     def print_msg():
#         print('Hello from class A')

# class B:
#     def print_msg():
#         print('Hello from class B')

# class C(A, B):
#     def call_print_msg():
#         print('Hello from class C')

# c = C
# c.print_msg()
# c.call_print_msg()

# ///////////////////////////////////////////////////////
# ////////////////////////////////////////////////////////

# class A:
#     __x = 10
#     def __print_msg():
#         print('Hello from class A')

# class B(A):
#     __x = 20
#     def __print_msg():
#         print('Hello from class B')

# b = B
# print('__x from A =', b._A__x)
# print('__x from B =', b._B__x)
# b._A__print_msg()
# b._B__print_msg()

# ///////////////////////////////////////////////////////
# ////////////////////////////////////////////////////////