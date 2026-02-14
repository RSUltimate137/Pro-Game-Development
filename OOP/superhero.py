class Superhero:
    def __init__(self,name,power,health):
        self.name = name
        self.power = power
        self.health = health

    def use_power(self):
        print(f"{self.name} uses his {self.power}!")
        
    def take_damage(self,damage):
        self.health = self.health-damage
        print(f"{self.name} now has {self.health}")

superhero1 = Superhero("The Flash","Speed",100)
superhero1.use_power()

superhero2 = Superhero("Spiderman","Web-slinging",100) 
superhero2.use_power()
superhero2.take_damage(50)