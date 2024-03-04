class Reverse:
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

def reverse(data):
    for index in range(len(data) - 1, -1, -1):
        yield data[index]

if __name__ == '__main__':
    rev = Reverse('spam')
    for char in rev:
        print(char)

    for char in reverse('golf'):
        print(char)

    print(sum(i * i for i in range(10)))

    x = [10, 20, 30]
    y = [7, 5, 3]
    print(sum(x * y for x, y in zip(x, y)))

    golf = 'golf'
    print(list(golf[i] for i in range(len(golf) - 1, -1, -1)))
