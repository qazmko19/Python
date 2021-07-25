def calculating(x):
    calculate = 1
    for i in range(1, x):
        if i % 2 != 0:
            calculate *= i
    return calculate


num = int(input("Write your x: "))
calculating(num)
