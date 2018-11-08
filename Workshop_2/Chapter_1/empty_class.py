class Empty(object):
    # Słowo kluczowe pass jest używane jako wyrażenie puste(null).
    # Chcemy w ten sposób zasygnalizować interpreterowi,
    # że w tym miejscu nic się nie wykonuje
    # pass != return None !!!!
    pass

if __name__ == '__main__':
    empty = Empty()
    empty.name = "Empty"
    empty.age = 0.01

    print(empty.name)
    print(empty.age)
