import argparse
import doctest
import glob
import math
import os
import random
import re
import statistics
import shutil
import sys
import unittest
import zlib

from datetime import date
from timeit import Timer
from urllib.request import urlopen

# Execute command: python3 python/std_lib_intro1.py file.txt -l 10

def average(values):
    '''Computes the arithmetic mean of a list of numbers.

    >>> print(average([20, 30, 70]))
    40.0
    '''
    return sum(values) / len(values)

if __name__ == '__main__':
    print(os.getcwd())
    # Change current working directory
    # os.chdir('/server/access_logs')
    # Run the command mkdir in the system shell.
    # os.system('mkdir today')

    # The build-in `dir()` and `help()` functions are useful as interactive aids for working
    # with large modules like `os`.
    print(dir(os))
    # help(os)

    # shutil.copyfile('data.db', 'archive.db')
    # shutil.move('/build/executables', 'install_dir')

    print(glob.glob('python/*.py'))

    print(sys.argv)

    # The `argparse` module provides a more sophisticated mechanism to process command
    # line arguments.
    parser = argparse.ArgumentParser(
        prog='top',
        description='Show top lines from each file')
    parser.add_argument('filenames', nargs='+')
    parser.add_argument('-l', '--lines', type=int, default=10)
    args = parser.parse_args()
    print(args.lines)

    sys.stderr.write('Warning, log file not found starting a new one\n')

    # The `re` module provides regular expression tools for advanced string processing.
    print(re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest'))

    print(math.cos(math.pi / 4))
    print(math.log(1024, 2))

    print(random.choice(['apple', 'pear', 'banana']))

    # Sampling without replacement.
    print(random.sample(range(100), 10))
    # Random float.
    print(random.random())
    print(random.randrange(6))

    data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
    print(statistics.mean(data))
    print(statistics.median(data))
    print(statistics.variance(data))

    with urlopen('http://worldtimeapi.org/api/timezone/etc/UTC.txt') as response:
        for line in response:
            # Convert bytes to a str
            line = line.decode()
            if line.startswith('datetime'):
                print(line.strip())

    now = date.today()
    print(now)
    now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")

    birthday = date(1964, 7, 31)
    age = now - birthday
    print(age.days)

    s = b'witch which has which witches wrist watch'
    print(len(s))
    t = zlib.compress(s)
    len(t)

    zlib.decompress(t)
    zlib.crc32(s)

    print(Timer('t=a; a=b; b=t', 'a=1; b=2').timeit())
    print(Timer('a,b = b,a', 'a=1; b=2').timeit())

    # Automatically validate the embedded tests.
    doctest.testmod()
