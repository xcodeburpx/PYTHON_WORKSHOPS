# Tworzenie stringów
str_1 = "ABC DEF"
str_2 = 'GHI JKL'
print(str_1)
print(str_2)

# Metody string
print(dir(str))


# Metoda split
l_str = "Mam na imię Szymon.\r\n Jestem studentem\r\t mam 22 lat"
print(l_str)
str_list = l_str.split('\n')
print(str_list)

# Metoda strip
s_str = "                One Two Three" 
print(s_str.strip())

# Metoda replace
s_str = "                One Two Three Two Two" 
print(s_str.replace("Two", "Dwa"))

# 'In' w string
l_str = "Mam na imię Szymon.\nJestem studentem"
print(l_str)
print("Szymon" in l_str)
