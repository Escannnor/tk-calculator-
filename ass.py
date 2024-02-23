# calculator
def add():
    x = int(input("first number: "))
    y = int(input("second number: "))
    results = f"your answer is {x + y}"
    print(results)
    print("thank you calculating with us")
    return (results)


def division():
    x = int(input("your first number: "))
    y = int(input("your second number: "))
    results = f"your answer is {x / y}"
    print(results)
    print("thank you for using our calculator")
    return (results)


def substraction():
    x = int(input("your first number: "))
    y = (input("your second number: "))
    results = f"your answer is {x - y}"
    print(results)
    print("thank you for using our calculator")
    return (results)


def multiplication():
    x = int(input("your first number: "))
    y = int(input("your second number is: "))
    results = f"your answer is {x * y}"
    print(results)
    print("thank you for using our calculator")
    return (results)


def choose_options():
    print("welcome to my first project calculator")
    option = input("select your operstion \n1. addition \n2. division \n3 substraction \n4 multiplication\n")
    if option == "addition" or option == "1":
        add()
    elif option == "division" or option == "2":
        division()
    elif option == "substraction" or option == "3":
        substraction()
    elif option == "multiplication" or option == "4":
        multiplication()

    else:
        print("input a valid option")


more_operation = input("do you want to perform a new operation: ")
if more_operation == "yeah" or more_operation == "yes" or more_operation == "sure":
    choose_options()
else:
    print("no come again xoxo")

choose_options()
