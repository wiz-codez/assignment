username = input("what is your name: ")
password = input("Enter your password: ")
confirm_password = input("right password: ")
is_running = True
if password == confirm_password:
    print('Valid password')
else:
    while is_running:
        print("Wrong password ")
        confirm_password = input("right password ")
        if password == confirm_password:
            print('Valid password')
            break
        is_running=False