import random

n = 5           ### Количество элементов списка
list = []       ### Пустой список
x = 0           ### Переменная для хранения результата

print("elements = [", end='')
for i in range(n):
    list.append(random.randint(0, 10))
    if i < n - 1:
        print(list[i], end=', ')
    else:
        print(list[i], end='], ')
    if i % 2 == 0:
        x += list[i]
x *= list[n - 1]
print('result:', x)
