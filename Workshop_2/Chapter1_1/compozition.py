"""
    Kompozycja
    Tworzenie obiektu z wielu obiektów.

    Obiekt posiada wiele składowych a te składowe są budowane w oparciu o inne obiekty

"""

from inherit import PizzaRobot, Server

class Customer:
    def __init__(self,name):
        self.name = name
    def order(self, server):
        print(self.name, "zamawia od", server)
    def pay(self,server):
        print(self.name, "płaci za zamówienie",server)

class Over:
    def bake(self):
        print("piec piecze")


class PizzaShop:
    def __init__(self):
        self.server = Server("Ernest")
        self.chef = PizzaRobot("Rober")
        self.oven = Over()

    def order(self, name):
        customer = Customer(name)
        customer.order(self.server)
        self.chef.work()
        self.oven.bake()
        customer.pay(self.server)

if __name__ == '__main__':
    scene = PizzaShop()
    scene.order("Amadeusz")
    print("...")
    scene.order("Aleksiej")