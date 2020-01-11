# Scrieti o functie care primeste la input un text cu cifre si il converteste in numar,
# in caz de exceptie (este introdus o litera), afisati un mesaj de erroare si chemati
# functia de convertire din nou.

def to_integer():
    
    try:
        a = int(input("Introduceti un numar "))
        print(f'Felicitari, ai introdus numarul {a}')
    except ValueError:
        print('Mai incearca')
        to_integer()
to_integer()