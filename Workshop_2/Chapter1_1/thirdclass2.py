from secondclass import SecondClass
class ThirdClass(SecondClass):
    # Modyfikacja konstruktora
    # Przykład 'ThirdClass(42)'
    def __init__(self, value, string):
        self.data = value
        self.string = string

    # Przeciążenie dodawania
    def __add__(self, other):
        return ThirdClass(self.data + other, self.string)

    # TODO: ZAKOMENTUJ -> POKAŻ
    # Przeciążenie domyślnej metody str
    def __str__(self):
        return '[ThirdClass: %s, %s]'% (self.data, self.string)

    def mul(self, other):
        self.data *= other

if __name__ == '__main__':
    a = ThirdClass('abc', "Random String")

    a.display()

    print(a)

    b = a + 'xyz'

    print(b)

    a.mul(3)
    print(a)
