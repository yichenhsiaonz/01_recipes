def equation():
    loop2 = 1
    while loop2 == 1:
        try:
            number = float(input("Enter original serving size "))
            number2 = float(input("Enter desired serving size "))
            loop2 = 2
            ratio = number2/number
            return ratio
        except ValueError:
            print("Please enter an integer or a float")
loop = 1
while loop == 1:
    scale_factor = equation()
    if scale_factor < 0.25:
        print("warning scale factor =", scale_factor, "(<0.25)")
    elif scale_factor > 4:
        print("warning scale factor =", scale_factor, "(>4)")
    else:
        print("scale factor =", scale_factor)
