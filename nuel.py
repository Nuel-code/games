while True:
    operators = input('''
please type in a math operator you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
% for percentage
''')
    kin = {'-', '/', '+', '*', '%'}
    if operators in kin:
        first_number = int(input("first number: "))
        second_number = int(input("second number:"))
        if operators == '+':
            print("{} + {} = ".format(first_number, second_number))
            print(first_number + second_number)

        elif operators == '-':
            print(first_number - second_number)

        elif operators == '*':
            print(first_number * second_number)

        elif operators == '/':
            print(first_number / second_number)
        elif operators == "%":
            print(first_number / 100 * second_number)
    else:
        print("no operators found")