# Specjalny przypadek wielodziedziczenia
# gdzie jest możliwość zwrócenia się do
# inicializatorów klas

class Foo(object):

    def __init__(self, *args, **kwargs):
        super(Foo, self).__init__(*args, **kwargs)
        self.foo = kwargs['foo']

    def helloFoo(self):
        return self.foo


class Bar(object):

    def __init__(self, *args, **kwargs):
        super(Bar, self).__init__()
        self.bar = kwargs['bar']

    def helloBar(self):
        return self.bar


class FooBar(Foo, Bar):

    def __init__(self, *args, **kwargs):
        # Notice: only one call to super... due to mro
        super(FooBar, self).__init__(*args, **kwargs)

    def helloFooBar(self):
        print("Calling A: ", self.helloFoo())
        print("Calling B: ", self.helloBar())


def main():
    foobar = FooBar(foo="Foo", bar="Bar")
    foobar.helloFooBar()


if __name__ == '__main__':
    main()