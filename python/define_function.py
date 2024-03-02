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

if __name__ == '__main__':
    fib(2000)
    f100 = fib2(100)
    print(f100)

