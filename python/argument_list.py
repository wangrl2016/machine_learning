def standard_arg(arg):
    print(arg)

def pos_only_arg(arg, /):
    print(arg)

def kwd_only_arg(*, arg):
    print(arg)

def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)

# This function definition which has a potential collision between the positional argument
# `name` and `**kwds` which has `name` as a key.
# def foo(name, **kwds):
#     return 'name' in kwds
def foo(name, /, **kwds):
    return 'name' in kwds

def concat(*args, sep='/'):
    return sep.join(args)

def parrot(voltage, state='a stiff', action='voom'):
    print('-- This parrot wouldn\'t', action, end=' ')
    print('if you put', voltage, 'volts through it.', end=' ')
    print('E\'s', state, '!')

# Small anonymous functions can be created with the `lambda` keyword.
def make_incrementor(n):
    return lambda x: x + n

def my_function():
    '''Do nothing, but document it.

    No, really, it doesn't do anything.
    '''
    pass

# Annotations are stored in the `__annotations__` attribute of the function as a dictionary and have no effect on
# any other part of the function.
def f_anno(ham: str, eggs: str = 'eggs') -> str:
    print('Annotations:', f.__annotations__)
    print('Arguments:', ham, eggs)
    return ham + ' and ' + eggs


if __name__ == '__main__':
    standard_arg(2)
    standard_arg(arg=2)

    pos_only_arg(1)
    # pos_only_arg(arg=1)

    # kwd_only_arg(3)
    kwd_only_arg(arg=3)

    # combined_example(1, 2, 3)
    combined_example(1, 2, kwd_only=3)
    combined_example(1, standard=2, kwd_only=3)
    # combined_example(pos_only=1, standard=2, kwd_only=3)

    foo(1, **{'name': 2})

    # Any formal parameters which occur after the `*args` parameter are 'keyword-only' arguments.
    print(concat('earth', 'mars', 'venus'))

    print(list(range(3, 6)))
    args = [3, 6]
    # Call with the *-operator to unpack the arguments out of a list or tuple.
    print(list(range(*args)))

    d = {'voltage': 'four million',
         'state': 'bleedin\' demised',
         'action': 'VOOM'}
    parrot(**d)

    f = make_incrementor(42)
    print(f(0))

    pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
    pairs.sort(key=lambda pair: pair[1])
    print(pairs)

    print(my_function.__doc__)

    print(f_anno('spam'))
