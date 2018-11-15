"""
    Pakiet argparse.

    Ten pakiet pozwala nam nie tylko interpretować argumenty linii komend
    ale także podać informację pomocniczą w razie gdyby nie wiadomo było
    co trzeba wprowadzić
"""

import argparse

# Dodajemy opis programu za pomocą słowa kluczowego 'description'
parser = argparse.ArgumentParser(description="Example of simple argument parser")

# Dodajemy nazwę argumentu linii komend
parser.add_argument("echo")

args = parser.parse_args()

print(args.echo)