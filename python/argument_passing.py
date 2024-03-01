import sys


# 2.1.2.1 PEP 299 - Special __main__() function in modules
# https://peps.python.org/pep-0299/
# The standard name of the 'main function' should be `__main__`. When a module is invoked on the command
# line, such as: `python my_module.py`
if __name__ == '__main__':
    print(sys.version)
