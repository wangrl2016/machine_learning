# -*- coding: utf-8 -*-
# By default, Python source files are treated as encoded in UTF-8. In that encoding,
# characters of most languages in the world can be used simultaneously in string literals,
# identifiers and comments.

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
    # Chinese greet sentence.
    print('你好')
    # Use commas to join multiple sentences into one sentence
    print('Constructing a model from input data',
          'without corresponding output labels is termed unsupervised learning.')
    # Display multiple lines on terminal.
    print('Rather than learning a mapping from input to output,\n'
          'the goal is to describe or understand the structure of the data.')
    
    # A string containing the version number of the Python interpreter plus additional information
    # on the build number and compiler used.
    print(sys.version)
    print('System platform:', sys.platform)
    print('System API version:', sys.api_version)
    # sys.argv (command line arguments)
    # The list of command line arguments passed to a Python script.
    # argv[0] is the script name.
    print(sys.argv[0:])

    # Built-in Functions
    # https://docs.python.org/3/library/functions.html
    # The Python interpreter has a number of functions and types built into it that are always
    # available. They are listed here in alphabetical order.
    print(len(sys.argv))
    print(pow(2, 3))
    print(sum([1, 2, 3, 4, 5]))
    print(round(4.5))
    print(abs(-10))
