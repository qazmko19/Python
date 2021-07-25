a = int(input("Write number a: "))
b = int(input("Write number b (b is greater than a): "))

summa = 0

if a < b:
    for i in range(a, b+1):
        summa += i
    print(summa)
else:
    print("Number b isn`t greater than a.")
