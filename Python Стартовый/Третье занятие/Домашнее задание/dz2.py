import math

x = float(input("Enter your x: "))

if -math.pi <= x <= math.pi:
    y = math.cos(3 * x)
else:
    y = x

print(y)
