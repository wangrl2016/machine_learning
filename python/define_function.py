# The keyword `def` introduces a function definition. It must be followed by the function name
# and the parenthesized of formal parameters.
# The statements that form the body of the function start at the next line, and must be indented.
def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end= ' ')
        a, b = b, a + b
    print()

def fib2(n):
    # Return a list containing the Fibonacci series up to n.
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    # The `return` statement returns with a value from a function.
    return result

# The most useful form is to specify a default value for one or more arguments.
def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        reply = input(prompt)
        if reply in {'y', 'ye', 'yes'}:
            return True
        if reply in {'n', 'no', 'nop', 'nope'}:
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)

def f_list(a, L=[]):
    L.append(a)
    return L

def f_none(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

# Function can also be called using keyword argument of the form kwarg=value.
# Accepts one required argument (voltage) and three optional arguments (state, action, and type).
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print('if you put', voltage, 'volts through it.')
    print('-- Lovely plumage, the', type)
    print("-- It's", state, '!')

# When a final formal parameter of the form **name is present, it receives a dictionary containing
# all keyword arguments except for those corresponding to a formal parameter. This may be conbined
# with a formal parameter of the form *name which receives a tuple containing the positional
# arguments beyond the formal parameter list.
def cheeseshop(kind, *arguments, **keywords):
    print('-- Do you have any', kind, '?')
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print('-' * 40)
    for kw in keywords:
        print(kw, ':', keywords[kw])

if __name__ == '__main__':
    fib(2000)
    f100 = fib2(100)
    print(f100)

    # Give only the mandatory argument.
    ask_ok('Do you really want to quit? ')
    # Give one of the optional arguments.
    ask_ok('OK to overwrite the file? ', 2)

    # The following function accumulates the arguments passed to it on subsequent calls.
    print(f_list(1))
    print(f_list(2))
    print(f_list(3))

    # Don't want the default to be shared between subsequent calls.
    print(f_none(1))
    print(f_none(2))
    print(f_none(3))

    # 1 positional argument
    parrot(1000)
    # 1 keyword argument
    parrot(voltage=1000)
    # 2 keyword argument
    parrot(voltage=1000099, action='V00000M')
    # 1 positional, 1 keyword
    parrot('a thousand', state='pushing up the daisies')

    cheeseshop("Limburger", "It's very runny, sir.",
               "It's really very, VERY runny, sir.",
               shopkeeper="Michael Palin",
               client="John Cleese",
               sketch="Cheese Shop Sketch")
