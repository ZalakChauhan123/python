# Creating Programer class from Emoplyee class

class Employee:
    def __init__(self , emp_name , id):
        self.emp_name = emp_name
        self.id = id

    def showEmpName(self):
        print(f"Employee name is {self.emp_name} from ---Parent Class---.")
    def showEmpId(self):
        print(f"Employee ID is {self.id} from ---Parent Class---.")



# Class Programmer inherited from Employee
class programer(Employee):
    def __init__(self, department, role , emp_name, emp_id):

        self.department = department
        self.role = role

        # FOR USE ATTRIBUTES OF PARENT CLASS BELOW IS IMPORTANT
        super().__init__(emp_name,emp_id)


    def showDepartmentName(self):
        print(f"Programmer's Department is {self.department} from ---Child Class---")

    def showRole(self):
        print(f"Programmer's role is {self.role} from ---Child Class---")




# Instance of Child class
programmer_obj = programer("Frontend Development" , "UI/UX Design" , "Maya", 400)

# BY Instance of child class calling methods of Child class
programmer_obj.showDepartmentName()
programmer_obj.showRole()


# BY Instance of child class calling methods of Parent class
programmer_obj.showEmpName()
programmer_obj.showEmpId()
