class FirstClass(object):

    # Definicja metody
    def setdata(self, value):
        self.data = value    # <- tutaj tworzymy atrybut klasy
    def display(self):
        print(self.data)     # <- tutaj wykorzystujemy atrybut


class SecondClass(FirstClass):
    def display(self):
        print("Aktualna wartość = %s" % self.data)

if __name__ == '__main__':
    z = SecondClass()
    z.setdata(42)
    z.display()