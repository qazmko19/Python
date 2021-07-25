a = int(input("Введите число a: "))
b = int(input("Введите число b: "))
x = int(input("Введите число x: "))

# print(a < x < b)

if a < x < b:
    print("Число", x, "лежит между", a, "и", b, sep=" ")
else:
    print("Число", x, "не лежит между", a, "и", b, sep=" ")
