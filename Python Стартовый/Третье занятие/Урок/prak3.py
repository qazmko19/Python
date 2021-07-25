a = int(input("Введите какое-нибудь первое число: "))
b = int(input("Введите какое-нибудь второе число: "))
move = input("Введите действие (+, -, *, /): ")

if move == "+":
    print(a + b)
elif move == "-":
    print(a - b)
elif move == "*":
    print(a * b)
elif move == "/" and b != 0:
    print(a / b)
else:
    print("Вы ввели не то")
