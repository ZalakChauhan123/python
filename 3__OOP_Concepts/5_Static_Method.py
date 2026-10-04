"""
It is a method that does not depend on the instance of the class or the class itself.
Syntax = @staticmethod

Key Point : 

- Can be called using the class name or an instance.
- N0 Self parameter needed
- Used as a utility functions related to the class, but not need to access class or instance data.

"""

class Number:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    
    def NormalAdditionMethod(self):
        print(f"Normal Addition Method {self.num1 + self.num2}")
    
    @staticmethod
    def Addition(a, b):
        print(f"Static Addition Method {a + b}")


# Calling Normal method by Instace of the class
N_ins = Number(20,30)
N_ins.NormalAdditionMethod()



# Calling Static Method by class name
print(Number.Addition(2,3))

# Calling Static Method by Instace of the class
print(N_ins.Addition(7,3))