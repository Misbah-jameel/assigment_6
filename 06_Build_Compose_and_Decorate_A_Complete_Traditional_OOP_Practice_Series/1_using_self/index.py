class Student:
    def __init__(self,name,marks):
        self.name = name   # student ka naam
        self.marks = marks  # student ke marks

    def display(self):
        print("Name:",self.name)
        print("Marks:",self.marks)

s1 = Student("Misbah" ,90)
s1.display()
