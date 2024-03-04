class Animal:
    # Attribute and method of the parent class.
    name = ''

    def eat(self):
        print('I can eat')

# Inherit from Animal.
class Dog(Animal):
    # New method in subclass
    def display(self):
        # Access name attribute of superclass using self.
        print('My name is ', self.name)

class Cat(Animal):
    # Override eat() method
    def eat(self):
        # Call eat() method of the superclass using `super()`.
        super().eat()
        print('I like to eat fish')

if __name__ == '__main__':
    # Create an object of the subclass.
    labrador = Dog()
    # Access superclass attribute and method
    labrador.name = 'Rohu'
    labrador.eat()
    # Call subclass method
    labrador.display()

    # Create an object of the subclass.
    persian = Cat()
    # Call eat() method on the persian object.
    persian.eat()
