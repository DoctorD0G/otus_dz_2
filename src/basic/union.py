from typing import Union


def foo(x: Union[str, int]):
    pass


foo("foo")
foo(1)

foo([])