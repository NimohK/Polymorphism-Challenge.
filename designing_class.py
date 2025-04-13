# Creating a class for a superhero

class Superhero:
    def __init__(self, name, age,):
        self.name = name
        self.age = age

    def introduction(self):
        print(f"Hello, meet {self.name} and she is {self.age} years old.")

# The first superhero(child class)
class dog(Superhero):
    def __init__(self, name, age,personality, superpower):
        super().__init__(name, age)
        self.superpower = superpower
        self.personality = personality

    def powers(self):
        print(f"{self.name} has the power of {self.superpower} and {self.personality} personality. Do you want to see her powers?")

# The second superhero(child class)
class cat(Superhero):
    def __init__(self, name, age,personality, superpower):
        super().__init__(name, age)
        self.superpower = superpower
        self.personality = personality

    def powers(self):
        print(f"{self.name} has the power of {self.superpower} and {self.personality} personality. Keep your eyes wide open!")

# The third superhero(child class)
class rabbit(Superhero):
    def __init__(self, name, age,personality, superpower):
        super().__init__(name, age)
        self.superpower = superpower
        self.personality = personality

    def powers(self):
        print(f"{self.name} has the power of {self.superpower} and {self.personality} personality. Keep it a secret!")

# Creating objects for the superheroes
superhero1 = dog("Bolt", 5, "loyal", "speed")
superhero2 = cat("Nyx", 3, "mysterious", "invisibility")
superhero3 = rabbit("Thumper", 2, "optimistic", "teleportation")

# Using the methods for the superheroes
superhero1.introduction()
superhero1.powers()

superhero2.introduction()
superhero2.powers()

superhero3.introduction()
superhero3.powers()









