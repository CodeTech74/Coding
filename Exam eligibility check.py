medical_cause=str(input("did you have a medical cause Y or N"))
medical_cause = medical_cause.capitalize()

atten = int(input("enter the attendance of the student: "))

if medical_cause == 'Y':
    print("You are allowed")
elif medical_cause == 'N':
    atten = int(input("enter the attendance of the student"))
    if atten>=75:
        print("Allowed")
    else:
        print("Not Allowed")
else:
    print("Enter Y or N")