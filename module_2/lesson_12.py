# customizing classes with dunder methods

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __repr__(self):
        class_name = type(self).__name__
        return f'{class_name}(title{self.title!r}, author{self.author!r})'

    def __str__(self):
        return f' "{self.title}" by {self.author} '

odyssey = Book("The Odyssey", "Homer")

print(repr(odyssey))
print(str(odyssey))

print("\n_____")

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

    # Developer-facing representation
    def __repr__(self):
        return f"Employee('{self.first}', '{self.last}', {self.pay})"

    # User-facing representation
    def __str__(self):
        return f'{self.fullname()} - {self.email}'

# --- Testing __str__ and __repr__ ---
emp_1 = Employee('John', 'Doe', 80000)

print(emp_1)
# Output: John Doe - john.doe@company.com

# You can call str() and repr() directly to see both
print(str(emp_1))   # Calls __str__
# Output: John Doe - john.doe@company.com

print(repr(emp_1))  # Calls __repr__
# Output: Employee('John', 'Doe', 80000)


# You could literally copy-paste the output to recreate the object!
emp_1_recreated = Employee('John', 'Doe', 80000)
print(emp_1_recreated)


# by default, f-strings user __str__
print(f"User display: {emp_1}")

# use !s to explicitly call __str__ (same as default)
print(f"User display: {emp_1!s}")

# user !r to explicitly call __repr__
print(f"Developer log: {emp_1!r}")


print("\n ##################################### \n")

class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

    # 2. implement __repr__ for Developer
    def __repr__(self):
        return f"Developer('{self.first}', '{self.last}', '{self.pay}', '{self.prog_lang}')"

    # 3. implement __str__ for Developer
    def __str__(self):
        return f'{self.fullname()} - {self.prog_lang} Developer'

# 4 Test the implementation

dev_1 = Developer('Jane', 'Doe', 95000, 'Python')

print("--- Testing the Developer class ---")

print(f"Default print(uses __str__): {dev_1}")
print(f"Explicit str (uses __str__): {dev_1!s}")
print(f"Explicit repr (uses __repr__): {dev_1!r}")

# let's verify the reper output works
dev_1_recreated = Developer('Jane', 'Doe', 95000, 'Python')
print(f"Recreated object: {dev_1_recreated!r}")

"""
Key Takeaways:

Special (Dunder) Methods like __repr__ and __str__ let you integrate your custom classes with Python's built-in features.
__repr__ provides an official, unambiguous representation for developers. It should ideally be code that can recreate the object.
__str__ provides a readable, informal representation for end-users. It's what print() uses by default.
Fallback Rule: If __str__ is missing, Python uses __repr__ as a fallback. Therefore, you should always aim to implement __repr__.
You can explicitly request a representation in f-strings using the !r (__repr__) and !s (__str__) flags.
"""