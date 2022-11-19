import random

n = 5               ### Размер списка
list = []           ### Пустой список
x = 0               ### Переменная для хранения результата
max = -100          ### Переменная для хранения максимального элемента из списка
min = 100           ### Переменная для хранения минимального элемента из списка


for i in range(n):
    list.append(random.randint(-99, 99))
    if list[i] < min:
        min = list[i]
    if list[i] > max:
        max = list[i]
print( end='')
x = max - min
print('elements =', list, ', result: ', x)
