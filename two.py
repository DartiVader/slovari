n = int(input("Введите количество кустов: "))
while n < 3:
    d = input("Количество кустов не должно быть меньше 3! \nВведите количество кустов: ")
    n = d

numb = list()
for i in range(n):
    numb.append(int(input(f"Введите количество ягод на {i + 1} кусту : ")))

numb_count = list()
for i in range(len(numb) - 1):
    numb_count.append(numb[i - 1] + numb[i] + numb[i + 1])
numb_count.append(numb[-2] + numb[-1] + numb[0])

print(f"Максимальное число ягод: {max(numb_count)}")