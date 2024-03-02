# System-specific parameters and functions
# This module provides access to some variables used or maintained by the interpreter and to
# functions that interact strongly with the interpreter.
import sys


# PEP 299 - Special __main__() function in modules
# https://peps.python.org/pep-0299/
# The standard name of the 'main function' should be `__main__`. When a module is invoked on the
# command line, such as: `python my_module.py`
if __name__ == '__main__':
    # PEP 3105 – Make print a function
    # print(*objects, spe=' ', end='\n', file=None, flush=False)
    # Print objects to the text stream file, separated by sep and followed by end.
    print('Hello, world!')
    
    # A string containing the version number of the Python interpreter plus additonal information
    # on the build number and compiler used.
    print(sys.version)

    # sys.argv (command line arguments)
    # The list of command line arguments passed to a Python script.
    # argv[0] is the script name.
    print(sys.argv[0:])
