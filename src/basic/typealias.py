from typing import TypeAlias

Vector: TypeAlias = list[float]


def foo(v: Vector):
    ...


foo([1.1, 2])
foo(1)
foo(["1"])