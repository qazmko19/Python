correct_pass = input("Write new password: ")

attempt = 0

for attempt in range(3):
    password = input("Write your new password again: ")
    if password == correct_pass:
        print("Access is allowed")
        break
else:
    print("Access is denied")
