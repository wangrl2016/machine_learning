
## [The Python Tutorial](https://docs.python.org/3/tutorial/index.html)

This tutorial does not attempt to be comprehensive and cover every single feature, or even
every commonly used feature. Instead, it introduces many of Python's most noteworthly features,
and will give you a good idea of the language's flavor and style.

### 1. Whetting Your Appetite

#### 1.1 What Python can do?

Python is simple to use, but it is a real programming language, offering much more structure and support for large
programs than shell scripts or batch files can offer.

The rest of the tutorial introduces various features of the Python language and system through examples, beginning
with simple expressions, statements and data types, through functions and modules, and finally touching upon
advanced concepts like exceptions and user-defined classes.

#### 1.2 Python Installing

Download python installer from [Python download page](https://www.python.org/downloads/)，install Python as prompted.
Open terminal type `python3` to see if installed successfully.

```
Python 3.12.2 (v3.12.2:6abddd9f6a, Feb  6 2024, 17:02:06) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
```

Everythin is OK, celebration!

#### 1.3 Code editor

There are many editors on the market, here are the recommended [Visual Studio code](https://code.visualstudio.com/).
Visual Studio code is a lightweight but powerful source code editor which runs on you desktop and is availabel for
Windows, macOS and Linux.

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

Typing and end-of-file character (Control-D on Unix, Control-Z on Windows) at the primary prompt causes the interpreter
to exit with a zero exit status. If that doesn't work, you can exit the interpreter by typing the following
command: `quit()`.

##### 2.1.2 Argument Passing

* PEP 299 - Special __main__() function in modules