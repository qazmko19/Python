x = int(input("Write number for calculating factorial: "))

factorial = 1

for i in range(1, x+1):
    factorial *= i

print("Factorial of number {} = {}".format(x, factorial))
