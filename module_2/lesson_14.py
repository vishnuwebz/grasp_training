# Decorators Modifying Function Behavior

def simple_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

def say_whee():
    print("Whee!")

# Manually applying the decorator
say_whee = simple_decorator(say_whee)

say_whee()

# output
"""
Something is happening before the function is called.
Whee!
Something is happening after the function is called.
"""

print("\n")
@simple_decorator
def say_hello():
    print("Hello!")

say_hello()
"""

Something is happening before the function is called.
Hello!
Something is happening after the function is called.
"""
print("\n")

import time
def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        # all the original function, passing all arguments, and capture its return value
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"'{func.__name__}' ran in {end_time - start_time:.4f} secs")
        # return the original function's result
        return result
    return wrapper

@timer_decorator
def complex_calculation(a,b):
    '''This function simulates a complex calculation'''
    print("Doing some work...")
    time.sleep(1)
    return a + b

# now we can call our decorated function with arguments
sum_result = complex_calculation(5, 3)
print(f"The result is: {sum_result}")

print('*' * 18)
print()

"""
Create a decorator called debug_logger. This decorator should print the following information when the decorated function is called:

The name of the function being called.
The positional arguments (args) passed to it.
The keyword arguments (kwargs) passed to it.
The value that the function returns.
Apply this decorator to a function that adds two numbers and returns the result.
"""


def debug_logger(func):
    def wrapper(*args, **kwargs):
        # 1. Print function name and arguments
        print(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")

        # Call the original function and get the result
        result = func(*args, **kwargs)

        # 4. Print the return value
        print(f"{func.__name__} returned: {result}")

        # Return the result
        return result

    return wrapper


@debug_logger
def add_numbers(x, y):
    """Adds two numbers together."""
    return x + y


# Test the decorated function
add_numbers(10, 5)

# Expected output:
# Calling add_numbers with args: (10, 5), kwargs: {}
# add_numbers returned: 15


print(complex_calculation.__name__)   # Prints 'wrapper', not 'complex_calculation'
print(complex_calculation.__doc__)    # Prints None, not our helpful docstring

print("-" * 20)

import time
from functools import wraps

def timer_decorator(func):
    @wraps(func) # Apply the wraps decorator to the wrapper
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args,**kwargs)
        end_time = time.time()
        print(f"'{func.__name__}' ran in {end_time - start_time:.4f} secs")
        return result
    return wrapper

@timer_decorator
def another_function():
    """This is another function."""
    pass

# The metadata is now preserved!
print(another_function.__name__) # Prints 'another_function'
print(another_function.__doc__) # Prints 'This is another function.'

'''Rule of thumb: Always use @functools.wraps when writing decorators.'''

"""
Key Takeaways:

Purpose: Decorators add functionality to an existing function without modifying its source code, promoting code reuse and the single responsibility principle.
Structure: A decorator is a function that accepts a function, defines an inner wrapper function, and returns the wrapper.
General-Purpose: A robust decorator's wrapper should accept *args, **kwargs and also return the original function's result.
@ Syntax: The @decorator syntax is a clean and readable way to apply a decorator to a function.
Best Practice: Always use @functools.wraps on your wrapper function to preserve the original function's name, docstring, and other important metadata.
"""