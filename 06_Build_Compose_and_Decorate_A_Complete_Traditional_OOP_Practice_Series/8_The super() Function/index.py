class Person:
    def __init__(self,name):
        self.name = name


class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)     # Calling parent constructor
        self.subject = subject


# Object bana rahe hain
t = Teacher("Misbah", "Math")
 
 
# Output check
print("Teacher Name:", t.name)
print("Subject:", t.subject)