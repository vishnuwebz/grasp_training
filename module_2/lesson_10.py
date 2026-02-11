# Inheritance

class Employee:
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f'{first.lower()}.{last.lower()}@company.com'

    def fullname(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

# developer is a child class of Employee
class Developer(Employee):
    #pass # for now it inherits everything without changes
    raise_amount = 1.10 # override the parent's value

    def __init__(self, first, last, pay, prog_lang):
        # call the parent class's __init__ method
        super().__init__(first, last, pay)
        # add the new attribute specific to developer
        self.prog_lang = prog_lang

# now we must provide the programming language when creating a Developer
dev_3 = Developer('John', 'Peter', 80000, 'Python')
print(dev_3.fullname())
print(dev_3.email)
print(dev_3.prog_lang)

print()
print(dev_3.pay)
dev_3.apply_raise()
print(f"Pay after 10% raise: {dev_3.pay}")


# let's see the effect
dev_2 = Developer('Vishnu', 'Webz', 100000, 'Python')
print(f"Initial pay: {dev_2.pay}")
dev_2.apply_raise()
print(f"Pay after 10% raise: {dev_2.pay}")


emp_2 = Employee('Test', 'User', 90000)
print(f"\nInitial pay: {emp_2.pay}")
emp_2.apply_raise()
print(f"Pay after 4% raise: {emp_2.pay}")

# create instances
emp_1 = Employee('John', 'Doe', 50000)
dev_1 = Developer('Jane', 'Doe', 60000, "JavaScript")

print(emp_1.email)
print(dev_1.email) # this works because Developer inherits from Employee!

print(dev_1.fullname()) # Methods are also inherited

"""
When we try to access dev_1.email, Python first looks for an __init__ method in the Developer class. Since it doesn't find one, it walks up the "chain of inheritance" to the parent Employee class and uses its __init__ method.
"""

# is dev_1 an instance of Developer?
print(isinstance(dev_1, Developer))
print(isinstance(dev_2, Developer))

# is dev_1 an instance of Employee? Yes, because Developer is a child of Employee
print(isinstance(dev_1, Employee)) # True

# is the Developer class a subclass of Employee? Yes
print(issubclass(Developer, Employee)) # True

# is the Employee class a subclass of Developer?  No
print(issubclass(Employee, Developer)) # False

"""
Python provides two helpful built-in functions to check the relationships between your objects and classes:

isinstance(object, Class): Returns True if the object is an instance of the class or any of its parent classes.
issubclass(Child, Parent): Returns True if the first class is a subclass of the second.

Key Takeaways:

Inheritance allows a child class to receive all attributes and methods from a parent class.
This is done with the syntax: class ChildClassName(ParentClassName):.
Child classes can override parent attributes and methods by redefining them.
To extend a parent's method without completely replacing it, use super().method_name(). This is most common with the __init__ constructor.
Child classes can have their own unique attributes and methods, making them specialized versions of the parent.
"""