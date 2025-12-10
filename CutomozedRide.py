print("Select your ride : ")
print("1. Bike")
print("2. Car")
choice1 = int(input("Enter your choice : "))
if choice1 == 1:
    print("Select your Bike : ")
    print("1. Activa")
    print("2. Honda")
    choice2 = int(input("Enter your choice : "))
    if choice2 == 1:
        print("User have selected Activa as a ride")
    elif choice2 == 2:
        print("User have selected Honda as a ride")
    else:
        print("Invalid input")
elif choice1 == 2:
    print("Select your Car : ")
    print("1. Suzuki")
    print("2. Nano")
    choice3 = int(input("Enter your choice : "))
    if choice3 == 1:
        print("User have selected Suzuki as a ride")
    elif choice3 == 2:
        print("User have selected Nano as a ride")
    else:
        print("Invalid input")
else:
    print("Invalid input")
                