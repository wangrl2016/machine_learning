from collections import deque

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

    



