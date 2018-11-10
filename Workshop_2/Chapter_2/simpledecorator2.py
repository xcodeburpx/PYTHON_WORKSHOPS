# Definujemy dekorator
def my_decorator(func):
    # Funkcja dekorująca <- wrapper
    def wrapper():
        print("Something is happening before the function is called.")
        func() # <- Nasza funkcja
        print("Something is happening after the function is called.")
    return wrapper # <- zwróć dekorator

# 'Właściwy' sposób użycia dekoratora
@my_decorator
def say_whee():
    print("Whee!")

if __name__ == '__main__':
    say_whee()


