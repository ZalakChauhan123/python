# Create class by using class Keyword followed by Class name

class Person:
    name = "Zalak"
    occupation = "UI/UX designer"
    networth = 10
    def info(self):
        print(f"---{self.name} is a {self.occupation}")


# Create Instace of the class
a = Person()

# Accessing properties of Person by Instance named as "a"
print(a.name , a.occupation)
a.info()

# -----------------

# Create 2nd Instance of the class
b = Person()

# Accessing and manupulate Properties of class Person by instance "b"
b.name = "Shubham"
b.occupation = "Full Stack Developer"
b.networth = 1000
b.info()

print(f"{b.name} , {b.occupation} , {b.networth}")