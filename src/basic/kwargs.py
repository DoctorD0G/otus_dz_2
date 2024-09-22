
def foo(**kwargs: int | str):
    pass


foo(a=1, b="2")
foo(a=[1])