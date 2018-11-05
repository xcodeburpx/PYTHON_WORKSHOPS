# Tworzenie listy
list_test = list()
print(list_test)

# Długość listy
print(len(list_test))

# Dodawanie elementów do listy
list_test.append(1)
list_test.append("Hello world")
list_test.append(sorted)
print(list_test)

# Jakie metody są w klasie lista
print(dir(list))

# Numer indeksu dla danej wartości
list_test.index(1)
list_test.index("Hello world")

# Czyszczenie listy
list_test.clear()


list_1 = [1,2,3,4]
list_2 = ["one", "two", "three", "four"]

# Łączenie list 1
print(list_1 + list_2)

# Lista dodana jako element listy
list_1.append(list_2)
print(list_1)

# Łączenie list 2
list_1 = [1,2,3,4]
list_1.extend(list_2)
print(list_1)

# sortowanie listy
list_3 = [1,20,39,21,6,2,834,23]
list_3.sort()
list_3
list_3 = [1,20,39,21,6,2,834,23]
sorted(list_3)

# Porównywanie list
list_1 = [1,2,3,4]
list_2 = [1,4,9,16]
print(list_1 == list_2)
list_2 = [1,2,3,4]
print(list_1 == list_2)
list_2.reverse()
print(list_1 == list_2)

# 'Is' statement
print(list_1 is list_2)
list_3 = list_1
print(list_3 is list_1)
list_3[0] = 10
print(list_3 is list_1)

# Is (not) None
print(list_1 == list_2)
print(list_1 is not None)
print(list_1 is None)





