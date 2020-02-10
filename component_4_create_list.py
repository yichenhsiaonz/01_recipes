def string_check(condition):
    loop1 = 1
    while loop1 == 1:
        text = input("Enter string ").lower()
        if condition == 0:
            if text in valid_list:
                return text
            else:
                print("invalid")
        else:
            return text


def number_check():
    loop2 = 1
    while loop2 == 1:
        try:
            num = float(input("Enter number"))
            if num > 0:
                return num
            else:
                print("invalid input")
        except ValueError:
            print("Please enter a valid integer or float")

valid_list = ["pints", "pounds"]
ing_list = []

loop = ""
while loop == "":

    ing_list.append(string_check(1))
    ing_list.append(number_check())
    ing_list.append(string_check(0))

    loop = input("press <enter> to continue or press any button to stop")
print(ing_list)
