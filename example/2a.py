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

A = 0
try:
    print("Що буде якщо", 10 / A, "?")
except ZeroDivisionError as e:
    print(e)
finally:
    print("А вот воно що!")

with open("README.md", "r") as f:
    for line in f:
        print("Стрічка -> ", line)


def my_fun():
    return "Це повернула функція"


print(my_fun())


this_is_lambda = lambda first, last: f'Цей код написав: {first} {last}'
print("Це просто функція:", this_is_lambda)
print("Це її виклик:", this_is_lambda('Богдан', 'Бугиль'))
print("Просто функція", my_fun)
lambda_2 = lambda: 1 + 2
print("Сума", lambda_2())
