import random

num_1 = random.randint(0, 1000)
num_2 = random.randint(0, 1000)
sum = num_1 + num_2
print(f"{sum} - сумма этих чисел")
comp = num_1 * num_2
print(f"{comp} - произведение этих чисел")
for i in range(0,1001,1):
    for j in range (0, 1001, 1):
        if i*j == comp and i+j == sum:
            print(f"{i} и {j} - искомые числа")
print("проверка!")
print (num_1, num_2)
