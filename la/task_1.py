n = int(input("Введите количество монеток на столе: "))
val_gerb = 0
val_reshka = 0

for _ in range(n):
    sorter = input(f"Введите, как лежит {_ + 1} монетка, гербом или решкой: ")
    if sorter == "гербом":
        val_gerb += 1
    else:
        val_reshka += 1
if (val_reshka <= val_gerb):
    print(f"Нужно перевернуть {val_reshka} монеток, которые повёрнуты решкой к нам")
else:
    print(f"Нужно перевернуть {val_gerb} монеток, которые повёрнуты гербом к нам")