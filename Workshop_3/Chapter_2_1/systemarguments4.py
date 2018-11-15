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
# parser.add_argument("--verbose", help="increase output verbosity", type=int)

parser.add_argument("--verbose",
                    help="increase output verbosity",
                    action="store_true")

args = parser.parse_args()
if args.verbose:
    print(args.square**2)