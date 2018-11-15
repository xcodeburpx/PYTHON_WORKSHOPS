"""
    Pakiet sys.
    The functions python sys module provides allows us to operate on underlying interpreter,
    irrespective of it being a Windows Platform, Macintosh or Linux.

    You don't need to install this module with pip.
"""

import sys

print(sys.modules.keys()) # <- Lista aktualnie pobranych modułów

# Wypisz wszystkie argumenty z linii komend
for i in sys.argv:
    print(i)

# Wypisuje wartość zmiennej środowiskowej PYTHONPATH
print("PYTHONPATH =", sys.path)

# Wejście od użytkownika
user_input = sys.stdin.readline()
print("Input : " + user_input)

# Wyjdź z programu z kodem błędu
sys.exit(1)