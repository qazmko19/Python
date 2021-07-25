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
            for num in range(num_a, 0, -1):
                if num_a % num == 0 and num_b % num == 0:
                    print("Greatest common divisor for numbers {} and {} is {}".format(num_a, num_b, num))
                    break
        elif num_b < num_a:
            for num in range(num_b, 0, -1):
                if num_a % num == 0 and num_b % num == 0:
                    print("Greatest common divisor for numbers {} and {} is {}".format(num_a, num_b, num))
                    break
    except ValueError:
        print("You write wrong value!")


def prak11():
    print("In progress...")


def prak12():
    input_list = list(input("Write your list: "))
    input_element = str(input("Write your element to check: "))

    count = 0

    for symbol in input_list:
        if input_element == symbol:
            count += 1

    if count > 1:
        print("This element is duplicated in list")
    else:
        print("This element isn`t duplicated in list")


def prak13():
    len_list = int(input("How long do you want the list: "))
    lst = []

    for i in range(1, len_list):
        lst.append(random.randint(1, 50))

    print("Your list is:", lst)

    for index, value in enumerate(lst):
        if value == 20:
            lst[index] = 200
            break

    if 200 in lst:
        print("I found 20 on the list and replaced it with 200. Your list now is:", lst)
    else:
        print("I did not find 20 on the list")


def prak14():
    input_list = list(input("Write your list: "))
    input_len = len(input_list)

    for index, value in enumerate(input_list):
        if value == "" or value == " ":
            input_list.pop(index)

    output_len = len(input_list)

    if output_len < input_len:
        print("Your list without spaces now is:", input_list)
    else:
        print("Your list did not have spaces, so now it is:", input_list)


print("1. Вы принимаете от пользователя последовательность чисел, разделённых запятой. Составьте список. (Список из "
      "чисел(без запятых)).")
print("2. Выведите первый и последний элемент списка.")
print("3. При заданном целом числе n посчитайте n + nn + nnn.")
print("4. Напишите программу, которая выводит чётные числа из заданного списка и останавливается, если встречает "
      "число 237.")
print("5. Напишите программу, которая принимает два списка и выводит все элементы первого, которых нет во втором.")
print("6. Сложите цифры целого числа.")
print("7. Посчитайте, сколько раз символ встречается в строке.")
print("8. Реверс списка")
print("9. Функция очереди (написать функцию которая принимает список и добавляет в него элементы как в очередь).")
print("10. Наибольший общий делитель.")
print("11. Циклический сдвиг.")
print("12. Проверить, есть ли в последовательности дубликаты.")
print("13. Дан список некоторых целых чисел, найдите значение 20 в нем и, если оно присутствует, замените его на 200. "
      "Обновите список только при первом вхождении числа 20.")
print("14. Необходимо удалить пустые строки из списка строк.")

while True:
    input_prak = input("Write a number of task: ")

    if input_prak == "1":
        prak1()
    elif input_prak == "2":
        prak2()
    elif input_prak == "3":
        prak3()
    elif input_prak == "4":
        prak4()
    elif input_prak == "5":
        prak5()
    elif input_prak == "6":
        prak6()
    elif input_prak == "7":
        prak7()
    elif input_prak == "8":
        prak8()
    elif input_prak == "9":
        prak9()
    elif input_prak == "10":
        prak10()
    elif input_prak == "11":
        prak11()
    elif input_prak == "12":
        prak12()
    elif input_prak == "13":
        prak13()
    elif input_prak == "14":
        prak14()
    elif input_prak == "exit":
        break
    else:
        print("You write wrong value!")
