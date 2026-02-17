"""Resource Management with `with` Statement"""

'''
file = open("my_file.txt", "w")
try:
    # An error might happen here!
    file.write("Hello, Full Stack Developer!")
finally:
    # This block is *always* executed, ensuring the file is closed.
    print("Closing the file.")
    file.close()
'''

"""
__init__: Takes initial arguments.
__enter__: Performs the setup action and returns the resource.
__exit__: Performs the cleanup action.
"""

'''
with open("my_file.txt", "w") as file:
    file.write("Hello, Full Stack Developer!")

# The file is automatically closed when the 'with' block is exited.

'''
# context manager
from contextlib import contextmanager

@contextmanager
def my_context_manager():
    # Setup code runs here
    print("Setting up resource")
    resource = "My Resource"

    try:
        yield resource # The code in the 'with' block runs here
    finally:
        # Teardown code runs here
        print("Tearing down resource...")

with my_context_manager() as res:
    print(f"Working with {res}")