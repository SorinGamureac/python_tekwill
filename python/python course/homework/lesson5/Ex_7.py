

#1. Scrieti un program care sa calculeze numarul de litere si cifre din un text.



s = []
t = []
d = []
text = input("introduceti textul")
for i in text:
    if i.isdigit():
        d.append(1)
    elif i.isalpha():
        s.append(1)
    else:
        t.append(1)
print(sum(t))
print(sum(d))
print(sum(s))


