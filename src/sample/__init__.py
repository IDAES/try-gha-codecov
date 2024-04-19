from importlib.metadata import version


__version__ = version("sample")


def some_function():
    "This code is never executed"
    a = 1
    b = 2
    c = 4
    return a, b, c


def some_other_function():
    a = 1
    b = 2
    c = 4
    return a, b, c


def yet_another_function():
    a = 1
    b = 2
    c = 4
    return a, b, c