from typing import Optional

def foo(x: Optional[int] = None):
    pass


foo(10)
foo(None)
foo()

foo("10")