def do_twice(func):
    # W tym miejscu przyjmujemy argumenty
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper_do_twice

@do_twice
def greet(name):
    print(f"Hello {name}")


if __name__ == '__main__':
    greet("WERLD!")