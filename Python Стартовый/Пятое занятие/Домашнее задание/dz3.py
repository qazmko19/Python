def sum(a, b, res=0):
    res += a + b
    print("{} + {} = {}".format(a, b, res))


def diff(a, b, res=0):
    res += a - b
    print("{} - {} = {}".format(a, b, res))


def div(a, b, res=0):
    if b != 0:
        res += a / b
        print("{} / {} = {}".format(a, b, res))
    else:
        print("You cannot divide by 0.")


def mult(a, b, res=0):
    res += a * b
    print("{} * {} = {}".format(a, b, res))


while True:
    num_a = float(input("Write number a: "))
    num_b = float(input("Write number b: "))
    act = input("Write what do you want to do with a and b (+, -, /, *, exit): ")
    if act == "+":
        sum(num_a, num_b)
    elif act == "-":
        diff(num_a, num_b)
    elif act == "/":
        div(num_a, num_b)
    elif act == "*":
        mult(num_a, num_b)
    elif act == "exit":
        break
    else:
        print("You write wrong act!")
