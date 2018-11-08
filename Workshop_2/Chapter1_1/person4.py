class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def lastName(self):
        return self.name.split()[-1]

    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))

    def __str__(self):
        return '[Person: %s, %s]' % (self.name, self.pay)


class Manager(Person):
    # Redefinicja metody
    def giveRaise(self, percent, bonus=.10):
        Person.giveRaise(self, percent + bonus)  # <- Odwołanie się do metody klasy
                                                 #  nadrzędnej


if __name__ == '__main__':
    bob = Person("Robert Zielony")
    anna = Person("Anna Czerwona", job="programmer", pay=10000)

    print(bob)
    print(anna)

    print(bob.lastName(), anna.lastName())
    anna.giveRaise(.10)

    print(anna)

    tom = Manager('Tomasz Czarny', 'manager', 50000)
    tom.giveRaise(.10)
    print(tom.lastName())
    print(tom)

