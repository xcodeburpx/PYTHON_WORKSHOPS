# Tworzenie słowników
dict_1 = {"one":1, "two":2, "three":3}
print(dict_1)
dict_2 = dict()
print(dir(dict))
print(dict_2)
dict_2["ichi"] = 1.0
print(dict_2)
dict_2["ni"] = 2.0
print(dict_2)

# Wybór elementów
print(dict_1["one"])
print(dict_1["four"])
print(dict_1.get("three",0))
print(dict_1.get("four",0))

# Klucze oraz wartości
print(dict_1.keys())
print(dict_1.values())


