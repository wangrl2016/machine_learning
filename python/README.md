## [The Python Tutorial](https://docs.python.org/3/tutorial/index.html)

This tutorial does not attempt to be comprehensive and cover every single feature, or even
every commonly used feature. Instead, it introduces many of Python's most noteworthly features,
and will give you a good idea of the language's flavor and style.

| Chapter | Code                   | Code                | Code            | code                |
| ------- | ---------------------- | ------------------- | --------------- | ------------------- |
| 1       |                        |                     |                 |                     |
| 2       | argument_passing.py    |                     |                 |                     |
| 3       | simple_calculator.py   | manipulate_text.py  | list_struct.py  | fibonacci_series.py |
| 4       | control_flow.py        | define_function.py  | argument_list.py                      |
| 5       | stack_impl.py          | data_structure.py   |                 |                     |
| 6       | intro_module.py        | fibo.py             |                 |                     |
| 7       | output_format.py       | file_read_write.py  |                 |                     |
| 8       | class_intro.py         | class_inheritance.py| class_iterator.py                     |
| 9       | error_exception.py     |                     |                 |                     |

### 1. Whetting Your Appetite

#### 1.1 What Python can do?

Python is simple to use, but it is a real programming language, offering much more structure and
support for large programs than shell scripts or batch files can offer.

The rest of the tutorial introduces various features of the Python language and system through
examples, beginning with simple expressions, statements and data types, through functions and
modules, and finally touching upon advanced concepts like exceptions and user-defined classes.

#### 1.2 Python Installing

Download python installer from [Python download page](https://www.python.org/downloads/)，install
Python as prompted.
Open terminal type `python3` to see if installed successfully.

```
Python 3.12.2 (v3.12.2:6abddd9f6a, Feb  6 2024, 17:02:06) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
```

Everythin is OK, celebration!

#### 1.3 Code editor

There are many editors on the market, here are the recommended [Visual Studio code](https://code.visualstudio.com/).
Visual Studio code is a lightweight but powerful source code editor which runs on you desktop and
is availabel for Windows, macOS and Linux.

Install VS Code for your platform and configure the tool set for your development needs.

### 2. Using the Python Interpreter

#### 2.1 Invoking the Interpreter

There are 2 way to invoking the interpreter:

* Interactive mode: commands are read from terminal.
* Argument passing: script file is used.


##### 2.1.1 Interactive Mode

Open terminal and type `which python3`, it will show path of python installed.

```
/Library/Frameworks/Python.framework/Versions/3.12/bin/python3
```

Type `python3` in termianl will enter python interpreter, which is said to be in interactive mode. In this mode
it prompts for the next command with the primary prompt, usually three greater-than signs (>>>); for continuation
lines it prompts with the secondary prompt, by default three dots(...).

```
>>> the_world_is_flat = True
>>> if the_world_is_flat:
...     print('Be careful not to fall off!')
...
Be careful not to fall off!
>>>
```

Typing and end-of-file character (Control-D on Unix, Control-Z on Windows) at the primary prompt
causes the interpreter to exit with a zero exit status. If that doesn't work, you can exit the interpreter by typing the following command: `quit()`.

##### 2.1.2 [Argument Passing](argument_passing.py)

Type `python3 -h` will print help infomation.

```
-c cmd : program passed in as string (terminates option list)
-m mod : run library module as a script (terminates option list)
Arguments:
file   : program read from script file
-      : program read from stdin (default; interactive mode if a tty)
arg ...: arguments passed to program in sys.argv[1:]
```

Type `python3 python/argument_passing.py` will execute commands from file.

* PEP 299 - Special `__main__()` function in modules
* PEP 3105 – Make print a function
* sys — System-specific parameters and functions

### 3. An Informal Introduction to Python

#### 3.1 [Numbers and Variable](simple_calculator.py)

The integer numbers (e.g. 2, 4, 20) have type `int`, the ones with a fractional part (e.g. 5.0, 6.0)
have type `float`.

Variables are essential for holding onto and referencing values throughout our application. By
storing a value into a variable, you can reuse it as many times and in whatever way you like
throughout your project.

You can think of variables as boxes with labels, where the label represents the variable name
and the content of the box is the value that the variable holds.

#### 3.2 [Text](manipulate_text.py)

Textual data in Python is handled with `str` objects, or strings. Strings are immutable sequences
of Unicode code points.

One way to remember how slices work is to think of the indices as pointing between characters, with
the left edge of the first character numbered 0. Then the right edge of the last character of a
string of n characters has index n, for example:

```
 +---+---+---+---+---+---+
 | P | y | t | h | o | n |
 +---+---+---+---+---+---+
 0   1   2   3   4   5   6
-6  -5  -4  -3  -2  -1
```

#### 3.3 [The introduction of `List` structure](list_struct.py)

Python has a great built in list type named `list`. List literals are written within square
brackets [].

#### 3.4 [Fibonacci Sequence](fibonacci_series.py)

The Fibonacci numbers may be defined by the recurrence relation F0 = 0, F1 = 1,
and F(n) = F(n-1) + F(n-2) for n > 1.

| F0 | F1 | F2 | F3 | F4 | F5 | F6 | F7 | F8 | F9 | F10 |
| -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | --  |
| 0  | 1  | 1  | 2  | 3  | 5  | 8  | 13 | 21 | 34 | 55  |

### 4. More Control Flow Tools

#### 4.1 [Control Flow](control_flow.py)

* The most well-known statement type is the `if` statement.
* Python's `for` statement iterates over the items of any sequence in the order.
* The `range()` function iterate over a sequence of numbers.
* `break` and `continue` statements.
* The `pass` statement does nothing.
* A `match` statement takes an expression and compares its value to successive patterns.

#### 4.2 [Defining Functions](define_function.py)

* A positional argument is an argument that is passed to a function based on its position in the
argument list. Positional arguments can appear at the beginning of an argument list and/or
be passed as elements of an iterable preceded by *.

```
complex(3, 5)
complex(*(3, 5))
```

* Keyword argument: an argument preceded by an identifier (e.g. name=) in a function call or
passed as a value in a dictionary preceded by **.

```
complex(real=3, imag=5)
complex(**{'real': 3, 'imag': 5})
```

#### 4.3 [More on Defining Functions](argument_list.py)

* A function definition may look like:

```
def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
      -----------    ----------     ----------
          |              |              |
          |    positional or keyword    |
          |                             - keyword only
           -- positional only
```

where / and * are optional.

### 5. Data Structures

More content reference [TheAlgorithms/Python](https://github.com/TheAlgorithms/Python)

#### 5.1 [Stack Implementation](stack_impl.py)

* A stack is an abstract data type that serves as a collection of elements with two main operations:

&emsp;&emsp; (1) Push, which adds an elements to the collection, and

&emsp;&emsp; (2) Pop, which removes the most recently added element.

#### 5.2 [Common Data Structure](data_structure.py)

* Tuples are immutable, and usually contain a heterogeneous sequence of elements that are
accessed via unpacking or indexing (or even by attribute in the case of namedtuples).
Lists are mutable, and their elements are usually homogeneous and are accessed by iterating
over the list.

* A set is an unordered collection with no duplicate elements. Basic uses include membership
testing and eliminating duplicate entries.

* Unlike sequences, which are indexed by a range of numbers, dictionaries are indexed by keys, which
can be any immutable type.


### 6. Modules and Packages

A module is a file containing Python definitions and statements. The file name is the module name
with the suffix `.py` appended.

#### 6.1 [The Introduction of Module](intro_module.py)

* When a module named `spam` is imported, the interpreter first searches for a built-in module
with that name. These module names are listed in `sys.builtin_module_names`. If not found, it
then searches for a file named `spam.py` in a list of directories given by the variable
`sys.path`. `sys.path` is initialized from these locations:

&emsp;&emsp; (1) The directory containing the input script.

&emsp;&emsp; (2) PYTHONPATH (a list of directory names, with the same syntax as the shell variable PATH).

&emsp;&emsp; (3) The installation-dependent default (by convention including a `site-packages` directory
handled by the `site` module).

* To speed up loading modules, Python caches the compiled version of each module in the `__pycache__`
directory under the name `module.version.pyc`, where the version encodes the format of the
compiled file; it generally contains the Python version number.

#### 6.2 Packages

Packages are a way of structuring Python's module namespace by using "dotted module names". For
example, the module name `A.B` designates a submodule name `B` in a package named `A`.

### 7. Input and Output

#### 7.1 [Format Output](output_format.py)

* To use formatted string literals, begin a string with `f` or `F` before the opening quotation
mark or triple quotation mark.

* The `str.format()` method of string requires more manual effort.

* Using string slicing and concatenation operations to create any layout you can imagine.

#### 7.2 [Reading and Writing Files](file_read_write.py)

* `open()` returns a file object, and is most commonly used with two positional arguments and one
key-word argument: `open(filename, mode, encoding=None)`.

### 8. Classes

Classes provide a means of bundling data and functionality  together. Creating a new class creates
a new type of object, allowing new instances of that type to be made. Each class instance
can have attributes attached to it for maintaining its state. Class instances can also have
methods (defined by its class) for modifying its state.

#### 8.1 [A First Look at Classes](class_intro.py)

* There are two kind of valid attribute names: data attributes and methods.

* Python inheritance syntax

```
# Define a superclass.
class SuperClass:
    # Attributes and method definition.
   
# inheritance
class SubClass(SuperClass):
    # Attributes and method of SuperClass.
    # Attributes and method of SubClass.
```

### 9. Errors and Exceptions

Errors detected duration exection are called exceptions.

9.1 [Handling Excpetions](error_exception.py)

The `try` statement works as follows:
* First, the try clause (the statement(s) between the `try` and `except` keywords) is executed.
* If no exception occurs, the except clause is skipped and exection of  the `try` statement is
finished.
* If an exception occurs during execution of the `try` clause, the rest of the clause is skipped.
Then, if its type matches the exception named after the `except` keyword, the except clause is
executed, and then execution continues after the try/except block.
* If an exception occurs which does not match the exception named in the except clause, it is
passed on to outer `try` statements; if no handler is found, it is an unhandled exception and
execution stops with an error message.
