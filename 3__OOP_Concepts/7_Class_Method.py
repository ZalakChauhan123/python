"""
Class Method :

- It is a method that is bound to the class and not the instance of the class.
- It can access and modify class variables that are shared among all instances.



Key points :

- Use @classmethod decorator.
- The first parameter is cls, which refers to the class itself.
- Can access or modify class variables, but not instance variables directly.
- Can be called using the class name or an instance.


NOTE -->> what's the purpose ???
- If I want to change class varible then I can use class method


NOTE --->> STAY FOCUS & PATIENCE. IT'S QUITE CONFUSING.... READ TILL LAST LINE
"""


class Employee:

    # Class Varible
    company = "Apple"


    # Normal Method
    def Show(self):
        print(f"Name of the employee is -- {self.name} -- & Company is -- {self.company}")
    

    # Normal method --> for change company
    def ChangeCompany_Instance_Level(cls, newCompany):
        cls.company = newCompany
    
    
    def ChangeCompany(cls, newCompany):
        cls.company = newCompany


# By Instance change Employee name & run show() method
e1 = Employee()
e1.name = "John"
e1.Show()
# Now, Change Company Name by ChangeCompany() method
e1.ChangeCompany("Tesla")
e1.Show()
# Check for Class Level Company Change or not ???
print(Employee.company) # It still gives Apple
print(e1.company)


"""
WHY IT HAPPEND - because change is made on instance level not on class level

TO DO CHANGE ON CLASS LEVEL -- 
-- our ChangeCompany() method should be Class Method, not normal one. 
-- For that I copy everything below with little change of class name
"""

class Emp:

    def Show(self):
        print(f"Name of the employee is -- {self.name} -- & Company is -- {self.Company}")
    
    # Class varible
    Company = "Apple"

    @classmethod
    def ChangeCompany(cls, newCompany):
        cls.Company = newCompany

e1 = Emp()
e1.name = "John"
e1.Show()
e1.ChangeCompany("Tesla")
e1.Show()

# Check for Class Level
print(Emp.Company) # Tesla
print(e1.Company)  # Tesla

print(help(e1))