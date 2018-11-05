# Pętla for
temp_list = [1,4,9,16,25,36]
for i in temp_list:
    print(i*i)

for i in range(len(temp_list)):
    elem = temp_list[i]
    print(elem*elem)

# Range
print(list(range(1,10)))
print(list(range(10)))

# Importowanie modułu 
# TRZEBA BYĆ W TYM SAMYM KATALOGU!
import python_ex3
python_ex3.Myadd(1,2)
python_ex3.Myprint("One", "Two", 3, 4)
python_ex3.Myprint2(one=1, two=2, three=3)
python_ex3.Myprint3("One", "Two", 3, 4, mam=1, imie="Einz", two="dwa")
