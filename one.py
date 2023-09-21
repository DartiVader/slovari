n_1 = int(input())
n_2 = int(input())
set_1 = set()
set_2 = set()

print('Введите эллементы первого множества >>> ')
for i in range(n_1):
    n = int(input())
    set_1.add(n)

print('Введите эллементы второго множества >>> ')
for i in range(n_2):
    n = int(input())
    set_2.add(n)

print(*sorted(set_1.intersection(set_2), key=lambda x: x))