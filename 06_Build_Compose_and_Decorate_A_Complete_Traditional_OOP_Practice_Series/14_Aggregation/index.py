class Employee:
    def __init__(self, name):
        self.name = name

class Department:
    def __init__(self, department_name, employee):
        self.department_name = department_name
        self.employee = employee  # Aggregation

    def show_details(self):
        print(f"Department: {self.department_name}")
        print(f"Employee: {self.employee.name}")

# Example usage:
emp1 = Employee("Misbah")  # Employee apne aap bana
dept1 = Department("IT", emp1)  # Department ne Employee ko reference kiya

dept1.show_details()
