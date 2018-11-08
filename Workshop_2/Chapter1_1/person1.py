class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay


if __name__ == '__main__':
    bob = Person("Robert Zielony")
    anna = Person("Anna Czerwona", job="programmer", pay=10000)

    print(bob.name, bob.pay)
    print(anna.name, anna.pay)


