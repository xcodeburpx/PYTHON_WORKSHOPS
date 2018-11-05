# a = 1
# b = 2

#print(a+b)

# Przykład działania funkcji na referencji
def last_item_add1(list_a, elem_a=10):
    last_elem = list_a[-1]
    last_elem += elem_a
    list_a.append(last_elem)


# Funkcja zwracająca wartość
def last_item_add2(list_a, elem_a):
    last_elem = list_a[-1]
    last_elem += elem_a
    list_a.append(last_elem)
    
    return list(list_a)

# Funkcja z argumentem z wartością domyślną
def last_item_add3(list_a, elem_a=10):
    last_elem = list_a[-1]
    last_elem += elem_a
    list_a.append(last_elem)
    
    return list(list_a)

# Przykład działania last_item_add2
temp_list = [1,2,3,4]
temp_list_2 = last_item_add2(temp_list,5)

print(temp_list_2)
print(temp_list_2 is temp_list)   

# Przykład działania last_item_add1
temp_list_3 = last_item_add3(temp_list)
print(temp_list_3)  


