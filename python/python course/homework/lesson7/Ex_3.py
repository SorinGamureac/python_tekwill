# Scrieti un program care transforma o lista cu elemente compuse intr-o lista
# simpla ( [1, [2, 3, [4, 5]]] -> [1,2,3,4,5] )
output = [] 
a = [1, [2, 3, [4, 5]]]
def reemovNestings(l): 
    for i in l: 
        if type(i) == list: 
            reemovNestings(i) 
        else: 
            output.append(i) 
reemovNestings(a)
print(output)