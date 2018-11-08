"""Przykład prostej klasy w Pythonie"""
class FirstClass(object):

    # Definicja metody
    def setdata(self, value):
        self.data = value    # <- tutaj tworzymy atrybut klasy
    def display(self):
        print(self.data)     # <- tutaj wykorzystujemy atrybut


if __name__ == '__main__':
    # W tym miejscu są tworzone instancje klas
    x = FirstClass()
    y = FirstClass()

    # Tutaj przypisujemy wartość do atrybutów
    x.setdata("Artur")
    y.setdata(3.14159)

    # Wywołanie drugiej metody
    x.display()
    y.display()

    # Modyfikacja bezpośrednia atrybutu
    x.data = "New message"
    x.display()

    # Generacja nowego atrybutu
    x.anotherattrib = "Hello world"
    print(x.anotherattrib)