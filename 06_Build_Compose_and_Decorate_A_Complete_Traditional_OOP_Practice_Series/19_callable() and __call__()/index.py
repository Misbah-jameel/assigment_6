class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, number):
        return number * self.factor

# Object bana rahe hain
m = Multiplier(5)

# Check karte hain callable() se
print(callable(m))   # Output: True

# Object ko function ki tarah call karte hain
result = m(10)
print(result)        # Output: 50
