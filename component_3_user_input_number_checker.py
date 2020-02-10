def number_check():
    loop = 1
    while loop ==1:
        try:
            num = float(input("Enter number"))
            if num > 0:
                print("valid")
            else:
                print("invalid")
        except ValueError:
            print("Please enter a valid integer or float")
number_check()