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

login_username = input("what is your name: ")
login_password = input("Enter your password: ")
login_confirm_password = input("right password: ")
is_running = True
if login_password == confirm_password and login_confirm_password == login_password:
    print('Valid password')
else:
    while is_running:
        print("Wrong password ")
        login_confirm_password = input("right password ")
        if login_password == confirm_password and login_confirm_password == login_password:
            print('Valid password')
            break
        is_running=False