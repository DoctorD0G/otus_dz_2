def foo(x: tuple[str, int]):
    pass


foo(("foo", 1))
foo((1, 2))
foo(("foo", "bar"))
foo((1, "foo"))