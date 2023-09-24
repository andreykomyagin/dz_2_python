N = int(input("Введите число: "))
if N > 2:
    count = 1
    i = 2
    while(i <= N):
        print(2**count)
        count += 1
        i *= 2
else:
    print(0)