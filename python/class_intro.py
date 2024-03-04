class MyClass:
    # A Simple example class
    i = 12345

    # When a class defines an `__init__()` method, class instantiation automatically
    # invokes `__init__()` for the newly created class instance.
    def __init__(self):
        self.data = []

    def fun(self):
        print('Hello, world!')

class Complex:
    def __init__(self, real, imag):
        self.r = real
        self.i = imag

class Dog:
    # Class variable shared by all instances.
    kind = 'canine'

    def __init__(self, name):
        # Instance variable unique to each instance.
        self.name = name

class MistakenDog:
    # Mistaken use of a class variable
    tricks = []

    def __init__(self, name):
        self.name = name

    def add_trick(self, trick):
        self.tricks.append(trick)

class CorrectDog:
    def __init__(self, name):
        self.name = name
        # Creates a new empty list for each dog.
        self.tricks = []

    def add_trick(self, trick):
        self.tricks.append(trick)

if __name__ == '__main__':
    x = MyClass()
    print(x.i)
    x.fun()

    x = Complex(3.0, -4.5)
    print(x.r)
    print(x.i)

    d = Dog('Fido')
    e = Dog('Buddy')
    print(d.kind)
    print(e.kind)
    print(d.name)
    print(e.name)

    d = MistakenDog('Fido')
    e = MistakenDog('Buddy')
    d.add_trick('roll over')
    e.add_trick('play_dead')
    # Unexpectedly shared by all dogs.
    print(d.tricks)

    d = CorrectDog('Fido')
    e = CorrectDog('Buddy')
    d.add_trick('roll over')
    e.add_trick('play dead')

    print(d.tricks)
    print(e.tricks)
