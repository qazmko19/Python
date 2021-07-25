a = float(input("Введите какое-нибудь первое число: "))
b = float(input("Введите какое-нибудь второе число: "))
move = input("Введите действие (+, -, *, /) или напишите 'exit' для выхода: ")

while move != "exit":
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

    a = input("Введите какое-нибудь первое число: ")
    b = input("Введите какое-нибудь второе число: ")
    move = input("Введите действие (+, -, *, /): ")
