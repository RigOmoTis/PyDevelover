import random

n = 5               ### Размер списка
L = []              ### Пустой список
x = 0               ### Переменная для хранения результата
max = -100          ### Переменная для хранения максимального элемента из списка
min = 100           ### Переменная для хранения минимального элемента из списка


for i in range(n):
    L.append(random.randint(-99, 99))
    if L[i] < min:
        min = L[i]
    if L[i] > max:
        max = L[i]
print( end='')
x = max - min
print('elements =', L ,', result: ', x)
