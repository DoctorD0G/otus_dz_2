from typing import TypeVar

T = TypeVar("T", int, str)


def add(a: T, b: T) -> T:
    ...


from typing import assert_type

assert_type(add(1, 2), int)
assert_type(add("1", "2"), str)

add(["1"], ["2"])
add("1", 2)