from collections import deque
from math import pi

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

    



