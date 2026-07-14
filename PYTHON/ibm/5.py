percentage = float(input("Enter percentage: "))

if percentage >= 40:
    if percentage >= 90:
        print("Grade A")
    else:
        if percentage >= 75:
            print("Grade B")
        else:
            if percentage >= 60:
                print("Grade C")
            else:
                print("Grade D")
else:
    print("Fail")