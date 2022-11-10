import random

n = 5           ### Количество элементов списка
L = []          ### Пустой список
x = 0           ### Переменная для хранения результата

print("elements = [", end='')
for i in range(n):
    L.append(random.randint(0, 10))
    if i < n - 1:
        print(L[i], end=', ')
    else:
        print(L[i],end='], ')
    if i % 2 == 0:
        x += L[i]
x *= L[n - 1]
print('result:', x)
