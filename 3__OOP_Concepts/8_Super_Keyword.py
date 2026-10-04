"""
super() :- this function used for calling parent methods inside child classes
NOTE - Always use super() inside a method, not at the class level.

"""

class Parent_class:

    def Parent_method(self):
        print("Parent method -->> Parent Class")

class Child_class(Parent_class):

    def Child_method(self):
        print("Child method -->> Child Class")
        
        # Calling Parent method from Parent class by Super() keyword
        super().Parent_method()

    def Parent_method(self):
        print("Parent method -->> Child Class")
    

# Instance of child class
c_ins = Child_class()
c_ins.Child_method()
c_ins.Parent_method()

# What if there is no method in child class (like you can comment def Parent_method)
# in that case it calls Parent_class -->> Parent_method
# Why -->> because Child class doesn't have it's own Parent_method

print(help(c_ins.Child_method))