class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name          # public
        self._salary = salary     # protected
        self.__ssn = ssn          # private

emp = Employee("Misbah", 50000, "123-45-6789")

print("Name (Public):", emp.name)         
print("Salary (Protected):", emp._salary) 
print("SSN (Private):", emp._Employee__ssn)  # ✅ This works
