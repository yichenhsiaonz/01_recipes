# Component 11.

import re

print("please put a comma in between the amount, unit, and name")

loop = ""
while loop == "":
    try:
        user_input = input("Please enter an ingredient listed in the recipe in the order of amount, unit, then name")
        if len(re.findall(",", user_input)) > 2:
            raise ValueError
        ing_list = re.split(",", user_input, 3)
        for x in ing_list:
            if x == "":
                raise ValueError
        amount = ing_list[0].replace(" ", "+")
        print("{} = {}".format(amount, eval(amount)))
        print(eval(amount), ing_list[1].strip(), ing_list[2].strip())
    except:
        print("please enter a number or equation first")