# Multipal Inheritence
"""
Class can inherit from more than one parent class
"""


class Employee:
    def __init__(self, name):
        self.name = name
    def Show(self):
        print(f"Name is {self.name}")

class Dancer:
    def __init__(self, dance):
        self.dance = dance
    def Show(self):
        print(f"Dance is {self.dance}")

class EmployeeeDancer(Employee, Dancer):
    def __init__(self, name, dance):
        self.name = name
        self.dance = dance

Ed_ins = EmployeeeDancer("Alex", "Kathak")
print(Ed_ins.name)

# Which method is calls -- Employee or Dance class ????
Ed_ins.Show() # calls Employee
"""
--- WHY IT HAPPENS
--- here class EmployeeeDancer(Employee, Dancer): line -->> Employee class added in 1st position
--- To check Execution order of the methods -->> Method called = class_name.mro()
"""
print(EmployeeeDancer.mro())

"""
mro() = Method Resolution Order
-- It shows the order in which Python will search classes when looking for a method or attribute.
"""

        
