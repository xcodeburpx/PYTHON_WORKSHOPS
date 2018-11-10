"""
    Gettery i settery.
    W OOP program powinien mieć argumenty prywatne.
    Aby móc do nich dostać się z zewnątrz, potzebne są pewne metody.
    Getter to metoda która pozwala nam na uzystanie wartości dla atrybutu prywatnego.
    Natomiast setter pozwala na ustawienie wartości atrybutu.

"""


class CodeCouple(object):
    def __init__(self, name):
        self.set_name(name)

    def get_name(self):
        return self.__name

    def set_name(self, name):
        if name == 'Agnieszka':
            self.__name = 'beautiful'
        elif name == 'Krzysztof':
            self.__name = 'ugly'
        else:
            self.__name = 'CodeCouple'



if __name__ == '__main__':
    agnieszka = CodeCouple('Agnieszka')
    print(agnieszka.get_name())

    krzysztof = CodeCouple('Krzysztof')
    print(krzysztof.get_name())

    code_couple = CodeCouple('UglyKrzysztof')
    print(code_couple.get_name())

    print(agnieszka.__dict__)
    print(agnieszka._CodeCouple__name)