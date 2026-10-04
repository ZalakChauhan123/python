"""
Method Overriding :- Replace with NEWEST method 
--------------------------------------------------------
It occurs when a child class defines a 
method with the -- same name -- as a method in its parent class. 


The child class method -->> replaces (overrides) -->> the parent method
when -->> called -->> from an instance of the child class.


In Below Example
- There is 2 Area methods (same names) in parent & child class
- If I comments child class Area method, then Python calls Parent class 
  Area method.
- It is called ---- METHOD OVERRIDING ----

"""


class Shape:
    def Area(self):
        print("PARENT CLASS Area method")

class Circle(Shape):
    pass
    # def Area(self):
    #     print("CHILD CLASS Area method")

C_ins = Circle()
C_ins.Area()