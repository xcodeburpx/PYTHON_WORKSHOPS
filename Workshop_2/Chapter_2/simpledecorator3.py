def do_twice(func):
    def wrapper_do_twice():
        func()
        func()
    return wrapper_do_twice


@do_twice
def greet(name):
    print(f"Hello {name}")


if __name__ == '__main__':
    greet("WERLD!")