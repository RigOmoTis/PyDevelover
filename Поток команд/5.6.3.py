n = int(input("Введите значение для числа N (от 1 до 9): "))
if (n < 1) or (n > 9):
    print("Значение N не входит в диапазон от 1 до 9!")
    exit(0)
for i in range(n):
    print(i + 1, end='')
