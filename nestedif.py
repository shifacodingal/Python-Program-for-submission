attendance = int(input("Enter Student's Attendance : "))
if attendance < 75:
    medical_cause = input("Did you have medical cause Y / N : ")
    if medical_cause.upper() == 'Y':
        print("Allowed for the Examination")
    elif medical_cause.upper() == 'N':
        print("Not allowed for  the Examination")
    else:
        print("Please enter valid input")
elif attendance >= 75 and attendance <=100:
    print("You are allowed for the Examination")
else:
    print("Invalid input")