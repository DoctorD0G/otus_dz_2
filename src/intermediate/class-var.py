from typing import ClassVar


class Foo:
    bar: ClassVar[int]
    """Hint: No need to write __init__"""


Foo.bar = 1
Foo.bar = "1"
Foo().bar = 1