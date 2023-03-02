mpass = input("what is your master password? ")


def view():
    with open("passcode.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("user:", user, "|" "password:", passw)


def add():
    name = input("account name: ")
    password = input("password: ")

    with open("passcode.txt", 'a') as f:
        f.write(name + '|' + password + '\n')


while 4 > 2:
    mode = input("would u like to add a new password or view existing ones or quit(view, add, q)? ").lower()
    if mode == 'q':
        quit()
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("plss get sense")
        continue
