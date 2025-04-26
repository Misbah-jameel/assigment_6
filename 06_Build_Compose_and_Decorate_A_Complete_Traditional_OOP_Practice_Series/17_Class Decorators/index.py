# Class Decorator
def add_greeting(cls):
    # Ek naya method banaya
    def greet(self):
        return "Hello from Decorator!"
    
    # Class ke andar ye method daal diya
    cls.greet = greet
    return cls

# Apply decorator to Person class
@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

# Example usage
p = Person("Ali")
print(p.greet())
