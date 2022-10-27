from random import randint

f = randint(0, 1000)
s = randint(0, 1000)
print(f"\tx = {f}, y = {s}\nРезультат: ", f // s, ',', f % s)
