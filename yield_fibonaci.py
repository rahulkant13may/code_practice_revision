# A simple generator for Fibonacci Numbers
def fib(limit):

    # Initialize first two Fibonacci Numbers
    a, b = 0, 1
    i = 0
    # One by one yield next Fibonacci Number
    while i < limit:
        yield a
        a, b = b, a + b
        i += 1

# Create a generator object
x = fib(5)

# Iterating over the generator object using next
print(x.next()); # In Python 3, __next__()
print(x.next());
print(x.next());
print(x.next());
print(x.next());

# Iterating over the generator object using for
# in loop.
print("\nUsing for in loop")
for i in fib(15): 
    print(i)
