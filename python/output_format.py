import math

if __name__ == '__main__':
    # To use formatted string literals, begin a string with `f` or `F` before the opening
    # quotation mark or triple quotation mark.
    year = 2024
    event = 'Referendum'
    print(f'Results of the {year} {event}')

    # The `str.format()` method of strings requires more manual effort.
    yes_votes = 42_572_654
    no_votes = 43_132_495
    percentage = yes_votes / (yes_votes + no_votes)
    print('{:-9} YES votes {:2.2%}'.format(yes_votes, percentage))

    s = 'Hello, world!'
    print(str(s))
    # The repr() of a string adds string quotes and backslashes.
    print(repr(s))
    hello = 'hello, world\n'
    print(repr(hello))
    print(str(1/7))
    x = 10 * 3.25
    y = 200 * 200
    s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
    print(s)

    # The argument to repr() may be any Python object.
    print(repr((x, y, ('spam', 'eggs'))))

    # Round pi to three places after the decimal.
    print(f'The value of pi is approximately {math.pi:.3f}')

    # Passing an integer after the `:` will cause that field to be manimum number of characters wide.
    table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
    for name, phone in table.items():
        print(f'{name:10} ===> {phone:10d}')

    # The `=` specifier can be used to expand an expression to the text of the expression, an
    # equal sign, then the representation of the evaluated expression.
    bugs = 'roaches'
    count = 13
    area = 'living room'
    print(f'Debugging {bugs=} {count=} {area=}')

    print('We are the {} who say "{}!"'.format('knights', 'Ni'))
    print('{0} and {1}'.format('spam', 'eggs'))
    print('{1} and {0}'.format('spam', 'eggs'))
    print('This {food} is {adjective}.'.format(
        food='spam', adjective='absolutely horrible'))
    # Positional and keyword arguments can be arbitrarily combined.
    print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred', other='Georg'))

    table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637}
    print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))

    for x in range(1, 11):
        print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))

    # The `str.rjust` method of string objects right-justfies a string in a field of a given width
    # by padding it with spaces on the left.
    for x in range(1, 11):
        print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
        # Note use of 'end' on previous line.
        print(repr(x*x*x).rjust(4))
    
