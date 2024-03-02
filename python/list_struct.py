if __name__ == '__main__':
    # List be written as a list of comma-separated values (items) between squares brackets.
    squares = [1, 4, 9, 16, 25]
    print(squares)

    # Lists can be indexed and sliced.
    print(squares[0])
    print(squares[-1])
    # Slicing returns a new list.
    print(squares[-3:])

    # Returns a shallow copy of the list.
    print(squares[:])

    # Support operations like concatenation.
    print(squares + [36, 49, 64, 81, 100])

    # List are a mutable type.
    cubes = [1, 8, 27, 65, 125]
    cubes[3] = 64
    print(cubes)

    # Add new items at the end of the list.
    cubes.append(216)
    cubes.append(7 ** 3)
    print(cubes)

    # Assignment to slices is also possible.
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    # Replace some values.
    letters[2:5] = ['C', 'D', 'E']
    print(letters)
    # Remove them
    letters[2:5] = []
    print(letters)
    # Clear the list by replacing all the elements with an empty list.
    letters[:] = []
    print(letters)

    letters = ['a', 'b', 'c', 'd']
    # The built-in function len() also applies to lists.
    print(len(letters))

    # Nest liss (create lists containing other lists).
    x = ['a', 'b', 'c']
    y = [1, 2, 3]
    z = [x, y]
    print(z)
    print(z[0])
    print(z[0][1])

    colors = ['red', 'blue', 'green']
    print(colors[0])
    print(colors[2])
    print(len(colors))

    fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
    print(fruits.count('apple'))
    print(fruits.index('banana'))
    # Find next banana starting at position 4.
    print(fruits.index('banana', 4))
    fruits.reverse()
    print(fruits)
    fruits.append('grape')
    print(fruits)
    fruits.sort()
    print(fruits)
    print(fruits.pop())
