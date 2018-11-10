temp_list = []
for i in range(100):
    temp_list.append(i**2)

print(temp_list)


temp_list_2 = [i**2 for i in range(100)]
print(temp_list_2)

print(temp_list == temp_list_2)





