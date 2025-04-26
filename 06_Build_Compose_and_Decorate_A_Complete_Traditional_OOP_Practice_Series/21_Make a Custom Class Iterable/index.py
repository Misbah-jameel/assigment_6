class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < 0:
            raise StopIteration
        else:
            num = self.current
            self.current -= 1
            return num

# Example usage:
cd = Countdown(5)

for number in cd:
    print(number)

