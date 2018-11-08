from first_class import Person

class Employee(Person):

    def __init__(self, name, surname, age, job_title):
        # Metoda super.
        # Metoda ta odwołuje się do superklasy.
        # Dzięki niej jesteśmy w stanie uruchamiać
        # metody superklasy
        super(Employee, self).__init__(name, surname, age)
        self.__job_title = job_title

    def getJobTitle(self):
        return self.__job_title

    def setJobTitle(self, job_title):
        self.__job_title = job_title


"""
    Operacja __name__ == __main__
    Python podczas uruchamiania interpretera inicjalizuje pewnie zmienne 
    specjalne. Jedną z nich jest __name__.

    Zmienna ta zawiera wartość:
    '__main__' gdy uruchamiamy moduł z pomocą pythona bezpośrednio
    'nazwa modułu' gdy moduł ten jest importowany z innego pliku

"""
if __name__ == '__main__':
    emp = Employee("Simon", "Steczek", 22, "Nokia")

    # print(emp.__dict__)
    print(emp.getSurName())