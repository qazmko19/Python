def prak1():
    a = list(map(int, input("Write your list through a space: ").split()))
    print("Max of your list is ", max(a), " and min of your list is ", min(a))
    return


def prak2():  # не было сделано это задание в прошлом уроке
    print("In progress...")
    return


def prak3():
    a = int(input("Write start number: "))
    b = int(input("Write end number: "))
    list_print = []

    for i in range(a, b + 1):
        count = 0
        d = 2
        while d < i:
            if i % d == 0:
                count += 1
            d += 1
        if count == 0:
            list_print.append(i)

    print(list_print)

    while True:
        printing = input("Write + or * to see to see the sum or product of prime numbers or 'exit' for ending: ")
        if printing == "+":
            result = 0
            for i in list_print:
                result += i
            print("The sum of the numbers in the list is ", result)
        elif printing == "*":
            result = 1
            for i in list_print:
                result *= i
            print("The product of the numbers in the list is ", result)
        elif printing == "exit":
            break
        else:
            print("Wrong value!")


while True:
    task = input("Write number of task you want to see or 'exit' for end: ")
    if task == "1":
        prak1()
    elif task == "2":
        prak2()
    elif task == "3":
        prak3()
    elif task == "exit":
        break
    else:
        print("You write wrong value! Try again.")
