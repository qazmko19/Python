def calculating(x):
    for i in range(x + 1):
        calculate = 2 ** i
        print(calculate)
    return ""


num = int(input("Write your x: "))
print(calculating(num))
