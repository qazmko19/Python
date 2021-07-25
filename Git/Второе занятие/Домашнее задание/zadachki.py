import random


def prak1():
    lst = list(map(int, input("Write your list of integer numbers through a comma: ").split(",")))
    print("Your list is:", lst)


def prak2():
    lst = list(input("Write you list: "))
    print("Your first element in list is '{}' and last element is '{}'".format(lst[0], lst[-1]))


def prak3():
    n = int(input("Write your number n: "))
    print("{} + {} + {} = {}".format(n, n ** 2, n ** 3, n + n ** 2 + n ** 3))


def prak4():
    lst = list(map(int, input("Write your list of integer numbers through a space: ").split()))
    for element in lst:
        if element % 2 == 0:
            print(element)
        elif element == 237:
            print("You write 237 in your list, so the program stopped printing even numbers.")
            break


def prak5():
    len_a = input("Write your first list or length (no more than 100) to generate random list in range 1 to 50: ")
    len_b = input("Write your second list or length (no more than 100) to generate random list in range 1 to 50: ")

    list_a = []
    list_b = []

    try:
        a = int(len_a)
        if 100 >= a > 0:
            for i in range(1, a):
                list_a.append(random.randint(1, 50))
            print("Your first list is:", list_a)
        elif a > 100:
            for symbol in len_a:
                list_a.append(symbol)
        else:
            return "You write wrong value!"
    except ValueError:
        for symbol in len_a:
            list_a.append(symbol)

    try:
        b = int(len_b)
        if 100 >= b > 0:
            for i in range(1, b):
                list_b.append(random.randint(1, 50))
            print("Your second list is:", list_b)
        elif b > 100:
            for symbol in len_b:
                list_b.append(symbol)
        else:
            return "You write wrong value!"
    except ValueError:
        for symbol in len_b:
            list_b.append(symbol)

    list_print = []
    count = 0

    for item_a in list_a:
        for item_b in list_b:
            if item_a == item_b:
                count += 1
                if count == 1:
                    list_print.append(item_a)
                else:
                    if item_a not in list_print:
                        list_print.append(item_a)

    print("List with identical elements: ", list_print)


def prak6():
    integer_input = input("Write an integer: ")
    summa = 0
    lst = []

    for item in integer_input:
        lst.append(item)

    try:
        for symbol in lst:
            s = int(symbol)
            summa += s
        print("The sum of the digits of the number you entered:", summa)
    except ValueError:
        print("You write wrong value!")


def prak7():
    input_string = input("Write your string: ")
    input_symbol = input("Write your symbol: ")
    count = 0

    for symbol in input_string:
        if symbol == input_symbol:
            count += 1

    print("Your symbol occurs in a string {} times".format(count))


def prak8():
    input_list = list(input("Write your list: "))

    print("Your reversed list is:", input_list[::-1])


def prak9():
    input_list = list(input("Write your list: "))
    input_length = int(input("Write length of your list (more or equal {}): ".format(len(input_list))))

    if input_length >= len(input_list):
        while True:
            input_element = input("Write element you want to append to list or write 'exit' to stop: ")
            if input_element == "exit":
                print("Your list is:", input_list)
                break
            elif len(input_list) < input_length:
                input_list.append(input_element)
                print("Your list now is:", input_list)
            elif len(input_list) >= input_length:
                input_list.pop(0)
                input_list.append(input_element)
                print("Your list now is:", input_list)
            else:
                print("You write wrong value!")
    else:
        print("You write wrong value!")


def prak10():
    try:
        num_a = int(input("Write first integer: "))
        num_b = int(input("Write second integer: "))

        if num_a == 0 or num_b == 0:
            print("Error! You cannot find out the common divisor while one of the numbers is 0!")
        elif num_a == num_b:
            print("The numbers entered by you are divided by each other")
        elif num_a < num_b:
            for num in range(num_a, 1, -1):
                if num_a % num == 0 and num_b % num == 0:
                    print("Greatest common divisor for numbers {} and {} is {}".format(num_a, num_b, num))
                    break
        elif num_b < num_a:
            for num in range(num_b, 1, -1):
                if num_a % num == 0 and num_b % num == 0:
                    print("Greatest common divisor for numbers {} and {} is {}".format(num_a, num_b, num))
                    break
    except ValueError:
        print("You write wrong value!")


def prak11():
    print("In progress...")


def prak12():
    pass


prak10()
