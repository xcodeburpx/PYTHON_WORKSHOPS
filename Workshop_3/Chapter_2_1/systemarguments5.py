"""
    Pakiet argparse.

    Ten pakiet pozwala nam nie tylko interpretować argumenty linii komend
    ale także podać informację pomocniczą w razie gdyby nie wiadomo było
    co trzeba wprowadzić
"""

import argparse

# Dodajemy opis programu za pomocą słowa kluczowego 'description'
parser = argparse.ArgumentParser(description="Example of simple argument parser")

# Dodajemy nazwę argumentu linii komend <- zwykły pozycyjny
parser.add_argument(
    "square",           # <- nazwa argumentu
    help="display a square of given number",    # <- opis pomocniczy
    type=int    # <- typ argumentu
    )

# Dodajemy argument opcjonalny
parser.add_argument("-v", "--verbosity", type=int,
                    help="increase output verbosity")

args = parser.parse_args()
answer = args.square**2
if args.verbosity == 2:
    print("the square of {} equals {}".format(args.square, answer))
elif args.verbosity == 1:
    print("{}^2 == {}".format(args.square, answer))
else:
    print(answer)