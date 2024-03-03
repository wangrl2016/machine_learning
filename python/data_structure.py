from collections import deque
from math import pi
import math

if __name__ == '__main__':
    queue = deque(['Eric', 'John', 'Michael'])

    queue.append('Terry')
    queue.append('Graham')
    print(queue.popleft())
    print(queue.popleft())
    print(queue)

    squares = []
    for x in range(10):
        squares.append(x**2)
    print(squares)

    sqaures = list(map(lambda x: x**2, range(10)))
    print(sqaures)

    sqaures = [x**2 for x in range(10)]
    print(sqaures)

    combs = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
    print(combs)

    combs = []
    for x in [1, 2, 3]:
        for y in [3, 1, 4]:
            if x != y:
                # If the expression is a tuple (e.g. the (x, y)), it must be parenthesized.
                combs.append((x, y))
    print(combs)

    vec = [-4, -2, 0, 2, 4]
    # Create a new list with the values doubled.
    print([x*2 for x in vec])
    # Fliter the list to exclude negative numbers.
    print([x for x in vec if x >= 0])
    # Apply a function to all the elements.
    print([abs(x) for x in vec])
    # Call a method on each element.
    fruit = [' banana', ' loganberry', 'passion fruit ']
    print([weapon.strip() for weapon in fruit])
    # Create a list of 2-tuples like (number, square).
    print([(x, x**2) for x in range(6)])
    # The tuple must be parenthesized, otherwise an error is raised.
    # [x, x**2 for x in range(6)]
    
    # Flatten a list using a listcomp with two 'for'.
    vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print([num for elem in vec for num in elem])

    print([str(round(pi, i)) for i in range(1, 6)])

    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
    ]

    # Transpose rows and columns.
    print([[row[i] for row in matrix] for i in range(4)])

    transposed = []
    for i in range(4):
        transposed.append([row[i] for row in matrix])
    print(transposed)

    transposed = []
    for i in range(4):
        # The following 3 lines implement the nested listcomp.
        transposed_row = []
        for row in matrix:
            transposed_row.append(row[i])
        transposed.append(transposed_row)
    print(transposed)

    # The `del` statement remove an item from a list given its index instead of its value.
    a = [-1, 1, 66.25, 333, 333, 1234.5]
    del a[0]
    print(a)
    del a[2:4]
    print(a)
    del a[:]
    print
    # `del` can also be used to delete entire variables.
    del a

    t = 12345, 54321, 'hello!'
    print(t[0])
    print(t)
    
    # Tuples may be nested.
    u = t, (1, 2, 3, 4, 5)
    print(u)

    # Tuples are immutable.
    # t[0] = 99

    empty = ()
    singleton = 'hello',
    print(len(empty))
    print(len(singleton))
    print(singleton)

    # Sequence unpacking requires that there are as many variables on the left side of
    # the equals sign as there are elements in the sequence.
    x, y, z = t
    print(x)
    print(y)
    print(z)

    # Curly braces or the `set()` function can be used to create sets.
    basket = {'apple', 'organe', 'apple', 'pear', 'orange', 'banana'}
    print(basket)
    print('orange' in basket)
    print('crabgrass' in basket)

    # Demonstrate set operations on unique letters from two words.
    a = set('abracadabra')
    b = set('alacazam')
    print(a)
    print(b)
    # Letter in a but not in b.
    print(a - b)
    # Letter in a or b or both.
    print(a | b)
    # Letters in both a and b.
    print(a & b)
    # Letters in a or b but or both.
    print(a ^ b)

    # Set comprehensions are supported.
    print({x for x in 'abracadabra' if x not in 'abc'})

    # dictionary
    tel = {'jack': 4098, 'sape': 4139}
    tel['guido'] = 4217
    print(tel)
    print(tel['jack'])
    del tel['sape']
    tel['irv'] = 4127
    print(tel)
    print(list(tel))
    sorted(tel)
    print('guido' in tel)
    print('jack' not in tel)

    # The `dict()` constructor builds dictonaries directly from sequences of key-value pairs.
    print(dict([('sape', 4139), ('guido', 4127), ('jack', 4098)]))
    print({x: x**2 for x in (2, 4, 6)})

    # Key and corresponding value can be retrieved at the same time using the `items()` method.
    knights = {'gallahad': 'the pure', 'robin': 'the brave'}
    for k, v in knights.items():
        print(k, v)
    
    # The position index and corresponding value can be retrieved at the same time
    # using the `enumerate()` function.
    for i, v in enumerate(['tic', 'tac', 'toe']):
        print(i, v)
    
    # To loop over two or more sequences at the same time, the entries can be paired with
    # the `zip()` function.
    questions = ['name', 'quest', 'favorite color']
    answers = ['lancelot', 'the holy grail', 'blue']
    for q, a in zip(questions, answers):
        print('What is your {0}? It is {1}.'.format(q, a))

    # Loop over a sequence in reverse.
    for i in reversed(range(1, 10, 2)):
        print(i)

    # Loop over a sequence in sorted order.
    basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
    for i in sorted(basket):
        print(i, end=' ')
    print()
    
    for f in sorted(set(basket)):
        print(f, end=' ')
    print()

    # Change a list while looping over it.
    raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
    filtered_data = []
    for value in raw_data:
        if not math.isnan(value):
            filtered_data.append(value)
    print(filtered_data)

