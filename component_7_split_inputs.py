import re

loop = ""
while loop == "":
    try:
        user_input = input("Please enter an ingredient listed in the recipe in the order of amount, unit, then name")
        ing_list = re.split(",", user_input, 3)
        amount = ing_list[0].replace(" ", "+")

        print("{} = {}".format(amount, eval(amount)))
        print(eval(amount), ing_list[1].strip(), ing_list[2].strip())
    except:
        print("please enter a number or equation first")