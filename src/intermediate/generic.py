from typing import TypeVar

T = TypeVar("T")


def add(a: T, b: T) -> T:
    ...


from typing import List, assert_type

assert_type(add(1, 2), int)
assert_type(add("1", "2"), str)
assert_type(add(["1"], ["2"]), List[str])
assert_type(add(1, "2"), int)