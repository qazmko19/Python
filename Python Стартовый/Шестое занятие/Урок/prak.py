def recur_sum(limit):
    global start
    if limit == start:
        return start
    else:
        return limit + recur_sum(limit - 1)


start = int(input("Enter first positive number: "))
end = int(input("Enter second positive number: "))

print("The sum is: ", recur_sum(end))
