class CodeCouple(object):

    """
        Dekorator @property

        @property pozwala nam na uzyskanie efektu odwołania
        bezpośredniego do zmiennej prywatnej.

        Przez to nie musimy wywoływać specjalnych metod get i set.

        Zwykle jest używany do kompaktybilności wstecznej.
    """

    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if name == 'Agnieszka':
            self.__name = 'beautiful'
        elif name == 'Krzysztof':
            self.__name = 'ugly'
        else:
            self.__name = 'CodeCouple'

if __name__ == '__main__':
    agnieszka = CodeCouple('Agnieszka')
    print(agnieszka.name)

    krzysztof = CodeCouple('Krzysztof')
    print(krzysztof.name)

    code_couple = CodeCouple('UglyKrzysztof')
    print(code_couple.name)