class Dog:
    def __init__(self,name,color):
        self.name = name
        self.color = color
    def bark(self):
        print(f"woof woof I am {self.name} and I am of {self.color} color")
dog1 = Dog("Floppy","yellow")
dog1.bark()
dog2 = Dog("Oliver","brown")
dog2.bark()