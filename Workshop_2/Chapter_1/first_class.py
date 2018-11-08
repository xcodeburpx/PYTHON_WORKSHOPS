class Person(object):
    """
        Metoda __init__:
        Metoda specjalna języka Python.
        Zachowuje się jak konstruktor w innych językach OOP.
        Tutaj możemy zdefiniować jakie wartości dana klasa
        przyjmuje. Możliwe jest także odwołanie się do metod klasy
        w tym miejscu.
    """
    def __init__(self, name, surname, age):
        # Słowo kluczowe self.
        # 'self' jest to zmienna która odnosi się do
        # instancji klasy. Dzięki niej jesteśmy w stanie
        # zwrócić się bezpośrednio do elementów instancji,
        # zmieniać wartości, itp.
        self.__name = name
        self.__surname = surname
        self.__age = age
    """
        OOP.
        W programowaniu obiektowym jedną z ważniejszych zasad jest tworzenie 
        atrybutów klasy jako atrybuty prywatne. To znaczy żaden program, klasa, funkcja 
        zewnętrzna nie jest w stanie odwołać się do tych elementów. Są zamknięte.
        
        W pythonie nie istnieje coś takiego jak atrybut prywatny.
        Dlatego w Pythonie 'emulujemy' to zachowanie stosując system podkreśleń.
        
        self.name -> zmienna publiczna
        self._name -> zmienna chroniona
        self.__name -> zmienna prywatna
    """
    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name

    def getSurName(self):
        return self.__surname

    def setSurName(self, surname):
        self.__surname = surname

    def getAge(self):
        return self.__age

    def setAge(self, age):
        self.__age = age


if __name__ == '__main__':
    pers = Person("Simon", "Steczek", 22)

    # Wystąpi błąd
    # print(pers.name)

    # Wystąpi błąd
    # print(pers.__surname)

    # Można sprawdzić klasę
    print(pers.__dict__)
    print(pers._Person__name)

    # To samo działanie
    print(pers.getName())