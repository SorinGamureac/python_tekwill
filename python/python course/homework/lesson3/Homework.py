Scrieti un program care afiseaza toate elementele din un invetar si calculeaza
suma lor
Ex, {‘scanue’: 33, ‘,mese’: 22}
Items: ‘scaune’, ‘mese’
total : 55

i = {"scaune":33, "mese":22,}
print(i.keys())
total = sum(i.values())
print(total)

Scrieti un program care transforma o lista de texte intr-un text separat prin
virgula si cuvintul “and” inaite de ultimul element.
(Ex: [“apples”, “bananas”, “cats”] -> “apples, bananas and cats”)

a = ["apples", "bananas", "cats"]
a.insert(2, "and")
b = ', '.join(a)
print(b)
b = b.replace('and,', 'and')
print(b)
