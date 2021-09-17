# пунк 1
print("Моя Перша константа", False)
a = "Ура!"
b = []
# пункт 2
print(abs(-12.5), f"є рівним {abs(12.5)} {a}")
print(list([1, 2]))

#
if a == a:
    print("1")
else:
    print("yes")

print("1" if a == a else "yes")

A = False
print("Значить А=True" if A else "Значить А=False")

for i in range(1, 8):
    print("Зовнішній", i)
    for j in [1, 2, 3, 4, 5]:
        print("Внутрішній", j)
