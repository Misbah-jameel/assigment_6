class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} says: Woof woof!")

# Object banate hain
my_dog = Dog("Bruno", "Labrador")

# Method call karte hain
my_dog.bark()
