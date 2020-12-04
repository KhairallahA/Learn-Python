# from abc import ABC
# class ParentClass:
#     def print_msg(ABS):
#         print('Normal method defined in an abstract class')

# class ChildClass(ParentClass):
#     pass

# obj = ChildClass()
# obj.print_msg()

# ///////////////////////////////////////////////////////
# ////////////////////////////////////////////////////////

from abc import ABC, abstractmethod
class ParentClass(ABC):
    def m1(self):
        print("m1: m1-g")

    @abstractmethod
    def m2(self):
        pass

    @abstractmethod
    def m3(self):
        print("m3: m3-g")

class ChildClass(ParentClass):
    def m2(self):
        print("m2: m2-g")

    def m3(self):
        super().m3()
        print("m3: m3-g too")

obj = ChildClass()
obj.m1()
obj.m2()
obj.m3()