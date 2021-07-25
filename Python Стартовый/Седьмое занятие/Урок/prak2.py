list_a = [99, 0, 35, 1, 6, 2]
list_b = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
list_print = []

for i in list_b:
    if i in list_a:
        list_print.append(i)

print(list_print)
