import time
"""
    Dekorator.
    Jeśli mamy zdefiniowane dwie funkcje
    
    def target():
        print("running target")
    
    def decorator(func):              
            return result of func
        return inner
        
    to dekoracja to operacja:
    target = decorate(target)
    
    W Pythonie stosuje się skróconą wersję dekoracji
    @decorate
    def target():
        print("running target")
    
"""
def clock(func):
    def clocked(*args):
        t0 = time.perf_counter()
        result = func(*args)
        elapsed = time.perf_counter() - t0
        name = func.__name__
        arg_str = ', '.join(repr(arg) for arg in args)
        print("[%0.8fs] %s(%s) -> %r" % (elapsed, name, arg_str, result))
        return result
    return clocked

