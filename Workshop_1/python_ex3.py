"""
	Przykład prostego modułu który można zaimportować 
	w Pythonie.
"""

def Myadd(a,b):
   return a+b

def Mysub(a,b):
   return a-b

def Mymul(a,b):
   return a*b

# Przykład funkcji z nieograniczoną ilością agrumentów
def Myprint(*args):
    for i in args:
        print(i)

# Przykład funkcji z nieograniczoną ilością agumentów kluczowych
def Myprint2(**kwargs):
    print(kwargs)


def Myprint3(*args, **kwargs):
    print(args)
    print(kwargs)
