from typing import TypeVar

T = TypeVar("T", bound=int)


def add(a: T) -> T:
    ...

from typing import assert_type


class MyInt(int):
    pass


assert_type(add(1), int)
assert_type(add(MyInt(1)), MyInt)
assert_type(add("1"), str)
add(["1"], ["2"])
add("1", 2)