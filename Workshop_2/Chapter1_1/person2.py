class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def lastName(self):
        return self.name.split()[-1]

    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))


if __name__ == '__main__':
    bob = Person("Robert Zielony")
    anna = Person("Anna Czerwona", job="programmer", pay=10000)

    print(bob.name, bob.pay)
    print(anna.name, anna.pay)

    print(bob.lastName(), anna.lastName())
    anna.giveRaise(.10)
    
    print(anna.pay)