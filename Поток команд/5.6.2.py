x = int(input("Введите число: "))
if x % 2 == 1:
    print("Результат: \"Плохо\"")
elif (x >= 2) and (x <= 5):
    print("Результат: \"Нелохо\"")
elif (x >= 6) and (x <= 20):
    print("Результат: \"Так себе\"")
elif x > 20:
    print("Результат: \"Отлично\"")
