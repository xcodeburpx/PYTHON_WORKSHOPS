import time
import functools
from decorator_2 import clock

@clock
def snooze(secs):
    time.sleep(secs)

@clock
def factorial(n):
    return 1 if n < 2 else n*factorial(n-1)


# @functools.lru_cache()  # <- pozwala na zmienszenie ilości wywołań rekursji
@clock
def fibonacci(n):
    return n if n < 2 else fibonacci(n-2) + fibonacci(n-1)

if __name__ == '__main__':
    print("*" * 40, 'Calling snooze(.123)')
    snooze(.123)
    print("*" * 40, 'Calling factorial(6)')
    print("6! =", factorial(6))
    print("*" * 40, 'Calling fibonacci6)')
    print("6! =", fibonacci(6))