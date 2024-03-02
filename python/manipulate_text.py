if __name__ == '__main__':
    # String literals are written in a variety of ways:
    # (1) single quotes
    print('spam eggs')
    # (2) double quotes
    print('Paris rabbit got your back')
    # (3) triple quotes
    print('''Triple quoted strings may span multiple lines - 
    all associated whitespace will be included in the string literal.''')

    # Use \' to escape the single quote.
    print('doesn\'t')
    # Or use double quotes instead.
    print("doesn't")
    print('"Yes," they said.')

    # with print(), special characters are interpreted, so \n produces new first line.
    print('First line.\nSecond line.')

    # If you don't want characters preface by \ to be interpreted as special characters, you
    # can use raw strings by adding an r before the first quote.
    # Here \n means newline.
    print('C:\\some\name')
    # Note the r before the quote.
    print(r'C:\\some\name')

    # String can be concatenated with the + operator, and repeated with * operator.
    print(3 * 'un' + 'ium')
    # Two or more string literals next to each other are automatically concatednated.
    print('Py' 'thon')
    # This feature is particularly useful when you want to break long string.
    print('Put several strings within parenthese '
          'to have them joined together.')
    
    prefix = 'Py'
    # can't concatenate a variable and a string literal.
    # print(prefix 'thon')
    print(prefix)
    # Use + to concatenate variables and a literal.
    print(prefix + 'thon')

    word = 'Python'
    # String can be indexed(subscripted), with the first character having index 0.
    print(word[0])
    print(word[5])
    
    # Indices may also be negative numbers, to start couning from the right.
    print(word[-1])
    # second-last character
    print(word[-2])

    # While indexing is used to obtain individual characters, slicing allows you to obtain
    # a substring.
    # Charaters from position 0 (included) to 2 (excluded).
    print(word[0:2])
    print(word[4:6])

    # An omitted first index default to zero.
    print(word[:2])
    # An omitted second index defaults to the size of the string being sliced.
    print(word[4:])
    # Characters from the second-last (included) to the end.
    print(word[-2:])
