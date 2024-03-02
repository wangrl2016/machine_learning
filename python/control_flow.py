if __name__ == '__main__':
    x = int(input('Please enter an integer: '))
    # The most well-known statement type is the `if` statement. There can be zero or
    # more `elif` parts, and the `else` part is optional.
    if x < 0:
        print('Negative')
    elif x == 0:
        print('Zero')
    elif x == 1:
        print('Single')
    else:
        print('More')

    # Python's for statement iterates over the items of any sequence (a list or a string), in
    # the order that they appear in the sequence.
    words = ['cat', 'window', 'defenestrate']
    for w in words:
        print(w, len(w))
    
    # Code that modifies a collection while iterating over the same collection can be tricky to
    # get right. Instead, it is usually more straight-forward to loop over a copy of the collection
    # or to create a new collection.
    users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}
    # Strategy: iterate over a copy.
    for user, status in users.copy().items():
        if status == 'inactive':
            del users[user]
    for user, status in users.items():
        print(user, status)
    
    # Strategy: create a new collection.
    active_users = {}
    users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}
    for user, status in users.items():
        if status == 'active':
            active_users[user] = status
    for user, status in active_users.items():
        print(user, status)

    # If you do need to iterate over a sequence of numbers, the built-in function
    # `range()` comes in handy.
    for i in range(5):
        print(i, end=', ')
    print()

    # Is is possible to let the range start at another number, or to specify a different
    # increment (even negative; sometimes this is called the step).
    print(list(range(5, 10)))
    print(list(range(0, 10, 3)))
    print(list(range(-10, -100, -30)))

    # To iterate over the indices of a sequence, you can combine `range()` and `len()` as follows:
    a = ['Mary', 'had', 'a', 'little', 'lamb']
    for i in range(len(a)):
        print(i, a[i])
    
    # In many ways the object return by `range()` behaves as if it is a list, but in face it isn't.
    # It is a `iterable` object suitable as a target for functions and constructs that expect
    # something from which they can obtain successive items until the supply is exhausted.
    print(sum(range(4))) # 0 + 1 + 2 + 3

    # The `break` statement breaks out of the innermost enclosing `for` or `while` loop.
    # In a `for` loop, the else clause is executed after the loop reaches its final iteration.
    # Search for prime numbers.
    for n in range(2, 10):
        for x in range(2, n):
            if n % x == 0:
                print(n, 'equals', x, '*', n//x)
                break
        else:
            # Loop fell through without finding a factor.
            print(n, 'is a prime number')

    # The `continue` statement continues with the next iteration of the loop.
    for num in range(2, 10):
        if num % 2 == 0:
            print('Found an even number', num)
            continue
        print('Found an odd number', num)
        
