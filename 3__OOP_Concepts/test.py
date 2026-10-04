class Animal:
    def __init__(self, name):
        self.name = name
    def ShowAnimal(self):
        print(f"Name of the Animal is {self.name}")

class Cat(Animal):
    def __init__(self, name, sound, age):
        super().__init__(name)
        self.sound = sound
        self.age = age

    def CatSound(self):
        print(f"Cat Sound is {self.sound}")
    
    def ShowCatDetails(self):
        print(f"Name is {self.name} & Age is {self.age}")

c1 = Cat("Olga","MWWW",4)
c1.ShowCatDetails()
    
