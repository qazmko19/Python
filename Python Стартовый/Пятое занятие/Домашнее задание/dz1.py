def print_name(name="Nikita"):
    print("Hello,", name)


input_name = input("Write your name: ")

if input_name == "":
    print_name()
else:
    print_name(input_name)
