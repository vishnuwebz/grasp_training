# Custom Iterators and Generators with 'yield'

# a simple for loop what we normally writes

nums_list = [1, 2, 3]

for num in nums_list:
    print(num)

print("-" * 20)

# what python does in the background

nums_iterator = iter(nums_list) # calls nums_list.iter__() to get an iterator

while True:
    try:
        # get the next item from the iterator
        item = next(nums_iterator) # calls nums_iterator.__next__()
        print(item)
    except StopIteration:
        # The iterator is exhausted, so we stop the loop
        break
"""
1: iter(iterable) returns an iterator.
2: next(iterator) returns the next item.
3: When there are no more items, next(iterator) raises a StopIteration exception, which the for loop catches to terminate gracefully.
"""


class MyRange:
    """A custom iterator that mimics the behavior of range()."""

    def __init__(self, start, end):
        self.value = start
        self.end = end

    def __iter__(self):
        # This method makes the object an iterable.
        # Since this class is also the iterator, we just return the instance itself.
        return self

    def __next__(self):
        # This method makes the object an iterator.
        if self.value >= self.end:
            # Signal that the iteration is complete.
            raise StopIteration

        # Get the current value to return
        current_value = self.value
        # Increment for the next call
        self.value += 1
        return current_value




print("-" * 20)


# Now we can use our custom iterator in a for loop!
nums = MyRange(1, 5)
for num in nums:
    print(num)  # Prints 1, 2, 3, 4


def my_range_generator(start, end):
    """A generator function that mimics range()"""
    current = start
    while current < end:
        yield current
        current += 1

# using the generator is the same as using the class-based iterator
nums = my_range_generator(1, 10)
for num in nums:
    print(num)

# # lets confirm it's an iterator
# print(next(nums))


"""
The Ultimate Benefit: Memory Efficiency
The most significant advantage of generators is their memory efficiency. They produce values one at a time, on-demand—a concept known as lazy evaluation. A regular function would have to create a list of all the values and return it at once, consuming a large amount of memory for big datasets.
"""
print("#" * 25)

# list comprehension (creates a list in memory)
my_list = [i * i for i in range(1, 11)]

# generator expression (creates a generator-iterator)
my_generator = (i * i for i in range(1, 11))

print("List:", my_list)
print("Generator object:", my_generator)

# you can loop over the generator to get its values
print("Values from generator:")
for val in my_generator:
    print(val, end=' ')

print('\n')
print('*' * 25)

"""
Write a generator function named even_numbers that takes two arguments, start and end. It should yield all the even numbers in the range from start to end (inclusive).

Then, use a for loop to print the even numbers from 10 to 20 using your generator."""

def even_numbers(start, end):
    """A generator that yields even numbers in a given range."""
    current = start
    # if the starting number is odd, move to the next one
    if current % 2 != 0:
        current += 1

    while current <= end:
        yield current
        current += 2 # move to the next even number
# test the generator
print("Even numbers from 10 to 20:")
for number in even_numbers(10, 20):
    print(number)

"""
What actually happens when you run it:
You call even_numbers(10, 20)

It starts at 10 (already even)

Yields: 10

Adds 2 → 12

Yields: 12

Adds 2 → 14

...continues until it reaches 20

Output will be: 10, 12, 14, 16, 18, 20
"""

'''
Key Takeaways:

Iterator Protocol: The __iter__ and __next__ special methods define how iteration works in Python.
Custom Iterators: You can create your own iterators by defining a class that implements the iterator protocol.
Generators: A generator function uses the yield keyword to create an iterator in a much simpler and more readable way.
Memory Efficiency: Generators are "lazy," producing values on-demand. This makes them ideal for processing large or even infinite streams of data without consuming excessive memory.
Generator Expressions: A concise, comprehension-like syntax (expr for item in iterable) for creating simple generators.
'''