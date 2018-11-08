from person5 import Person, Manager

"""
    Polimorfizm
    
    Ogólnie jest to koncepcja zależności zachowania wywołanej metody.
    Medota będzie inaczej zachowywać się 
    jeśli będziemy ją wywoływać na różnych objektach.
"""


if __name__ == '__main__':
    bob = Person("Robert Zielony")
    anna = Person("Anna Czerwona", job="programmer", pay=10000)
    tom = Manager('Tomasz Czarny',50000)

    for object in (anna, bob, tom):
        object.giveRaise(.10)
        print(object)