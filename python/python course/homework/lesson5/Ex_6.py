
# 6. Scrieti un program care sa primeasca la input un numar N intreg si sa creeze
# un dictionar care contine numer mai mici sau egale decit N si N*2. Ex(4 - > {1:
# 1, 2: 4, 3: 9, 4: 16})


d = {}
z = abs(input("introduceti un numar intreg"))
for i in range(z):
    d.update({i:i*i})
print(d)

