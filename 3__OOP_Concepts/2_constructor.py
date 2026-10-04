"""

WHAT IS CONSTRUCTOR :-
--- special method that is automatically called when an object of a class is created.

---------------------------------------------------------------------------------------
VERY IMPORTANT STATEMENT :- Its main purpose is to initialize the object's attributes.
---------------------------------------------------------------------------------------

--- In Python, the constructor method is named as __init__.

"""



# Create Class Person
class Person:

    # Create Constructor by using "__init__" Keyword
    def __init__(self):
        print ("Hey , I am Constructor. I calls everytime when class calls...")
    
    # Body of the class
    name = "Zalak"
    occ = "UI/UX Designer"
    def info(self):
        print(f"{self.name} is a {self.occ} by Profession.")

# Create Instance
a = Person() # NOTE :- Automatically calls constructor







# Create Class called Car

class Car:
    def __init__(self , name , model , brand , price):
        self.name = name
        self.model = model
        self.brand = brand
        self.price = price
    
    def carInfo (self):
        print(f"Car name is {self.name} & It's model is {self.model}. Price is {self.price} thousand Ruppes")


# Create Instance of class Car
b = Car("Alto","A5647","Suzuki",5000)
b.carInfo()
    
        