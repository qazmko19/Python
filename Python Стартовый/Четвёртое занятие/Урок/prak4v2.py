correct_pass = input("Write new password: ")

attempt = 0

while attempt != 3:
    password = input("Write your new password again: ")
    if password == correct_pass:
        print("Access is allowed")
        break
    attempt += 1
else:
    print("Access is denied")