import math
class Pizza:
    """
        @classmethod
        Dekorator który może modyfikować stan klasy
        ale nie ingeruje w instancje klasy

        @staticmethod
        Dekorator który nie może modyfikować ani klasy
        ani instancji

        Głównie różnice są w tym jaki pierwszy argument zostaje przyjmowany

    """

    def __init__(self, radius, ingredients):
        self.ingredients = ingredients
        self.radius = radius

    def __repr__(self):
        return f"Pizza({self.ingredients})"

    @classmethod
    def margherita(cls):
        return cls(15, ['cheese', 'tomatoes'])

    @classmethod
    def prosciutto(cls):
        return cls(15, ['cheese', 'tomatoes', 'ham', 'mushrooms'])

    def area(self):
        return self._circle_area(self.radius)

    @staticmethod
    def _circle_area(r):
        return r ** 2 * math.pi


if __name__ == '__main__':

    print(Pizza(4.5, ['cheese']).area())
    print(Pizza._circle_area(12))
