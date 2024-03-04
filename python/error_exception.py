import os

# A python program to create user-defined exception class MyError
# to derived from super class Exception.
class MyError(Exception):
    # Constructor or initializer.
    def __init__(self, value):
        self.value = value

    def __str__(self) -> str:
        return (repr(self.value))
    
if __name__ == '__main__':
    while True:
        try:
            x = int(input('Please enter a number: '))
            break
        except ValueError:
            print('Oops! That was no valid number. Try again...')
    
    try:
        f = open('temp_file.txt', 'w+')
        s = f.readline()
        i = int(s.strip)
    except OSError as err:
        print('OS error', err)
    except ValueError:
        print('Could not convert data to an integer.')
    except TypeError:
        print('TypeError: int() argument must be a string')
    except Exception as err:
        print(f'Unexpected {err=}, {type(err)=}')
        raise

    os.remove('temp_file.txt')

    try:
        raise(MyError(3 * 2))
    except MyError as error:
        print('A new exception occurred:', error.value)
