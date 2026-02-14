# polymorphism

class Employee:
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f'{first.lower()}.{last.lower()}@company.com'

    # method
    def fullname(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
    # method
    def show_details(self):
        print(f"Employee: {self.fullname()}, Pay: ${self.pay}")

class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

    # This method overrides the parent's show_details() method
    # def show_details(self):
    #     print(f"Developer: {self.fullname()}, Pay: ${self.pay}, Language: {self.prog_lang}")

    # overriding and EXTENDING the parent's method
    def show_details(self):
        # First, call the parent's method to print the general info
        super().show_details()
        # Then, add the info specific to a Developer
        print(f" -> Specialization: {self.prog_lang} Developer")

dev_2 = Developer('Corey', 'Schafer', 105000, 'JavaScript')

print("\n--- Extending with super() ---")
dev_2.show_details()

# Create instance
emp_1 = Employee('John', 'doe', 80000)
dev_1 = Developer('Jane', 'Doe', 100000, 'Python')

# Call the same method on both objects
print("--- Calling show_details() on each object ---")
emp_1.show_details() # calls Employee.show_details()
dev_1.show_details() # calls Developer.show_details()

class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    # We'll override show_details() here too
    def show_details(self):
        print(f"Manager: {self.fullname()}, Pay: ${self.pay}, Supervises: {len(self.employees)} employees")

emp_1 = Employee('John', 'doe', 80000)
dev1 = Developer('Jane', 'Doe', 100000, 'Python')
mgr_1 = Manager('Sue', 'Smith', 120000, [dev_1])

# A list containing objects of different, but related, classes
employees = [emp_1, dev_1, mgr_1]

print("\n--- Iterating through a list of employees ---")
for employee in employees:
    # we don't care about the specific type, we just call the method!
    employee.show_details()