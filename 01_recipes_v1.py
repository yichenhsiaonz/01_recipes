import csv


def number_check():
    loop3 = 1
    while loop3 == 1:
        try:
            num = float(input("Enter number"))
            if num > 0:
                return num
            else:
                print("Please enter a valid integer float")
        except ValueError:
            print("Please enter a valid integer or float")


def string_check(question, condition):
    global allowed_list
    loop4 = 1
    while loop4 == 1:
        text = input(question)
        valid = "TRUE"
        if len(text) > 0:
            if condition == 2:
                if any(num not in allowed_list for num in text):
                    valid = "FALSE"
            if valid == "TRUE":
                if text == "T":
                    return text
                else:
                    return text.lower()
        if valid == "TRUE":
            print("Please enter something")
        else:
            print("Please enter a float, integer, or equation")


groceries = open("01_ingredients_ml_to_g.csv")

csv_groceries = csv.reader(groceries)

food_dictionary = {}

for row in csv_groceries:
    food_dictionary[row[0]] = row[1]

unit_dictionary = {
    "tsp": 5,
    "tbs": 15,
    "cup": 237,
    "ounce": 30,
    "pint": 473,
    "quart": 946,
    "pound": 454,
    "litre": 1000
}

teaspoon =["tsp", "teaspoon", "t", "teaspoons"]
tablespoon = ["tbs", "tablespoon", "T", "tbsp", "tablespoons"]
ounce = ["oz", "ounce", "fl oz", "ounces"]
cup = ["c", "cup", "cups"]
pint = ["p", "pt", "fl pt", "pint", "pints"]
quart = ["q", "qt", "fl qt", "quart", "quarts"]
pound = ["pound", "lb", "#", "pounds"]
mls = ["ml", "milliliter", "millilitre", "milliliters", "millilitres"]
litre = ["litre", "liter", "l", "litres", "liters"]

allowed_list = ["1", "2", "3", "4,", "5", "6", "7", "8", "9", "0", "+", "-", "*", "/", "."]

recipe_name = string_check("Please enter the name of the recipe: ", 1)

recipe_source = string_check("Please enter the website the recipe is from: ", 1)

ratio = 1

loop2 = 1
while loop2 != "yes":
    try:
        number = float(input("Enter original serving size "))
        number2 = float(input("Enter desired serving size "))
        loop2 = 2
        ratio = number2/number
        if ratio < 0.25:
            print("warning scale factor =", ratio, "(<0.25). Measurements")
        elif ratio > 4:
            print("warning scale factor =", ratio, "(>4)")
        else:
            print("scale factor =", ratio)
        loop2 = input("Please enter <yes> if you are okay with this ").lower()
    except ValueError:
        print("Please enter an integer or a float")

ing_list = []
list_items = 0
loop = ""
while loop == "":

    ing_list.append(string_check("Please enter the name of ingredient: ", 1))
    unit = string_check("Please enter the unit for this ingredient: ", 1)
    if unit in teaspoon:
        unit = "tsp"
    elif unit in tablespoon:
        unit = "tbs"
    elif unit in ounce:
        unit = "ounce"
    elif unit in pint:
        unit = "pint"
    elif unit in quart:
        unit = "quart"
    elif unit in pound:
        unit = "pound"
    elif unit in mls:
        unit = "ml"
    elif unit in litre:
        unit = "litre"

    ing_list.append(unit)
    ing_list.append(eval(string_check("Please enter the amount of this ingredient: ", 2)))
    list_items += 1

    loop = input("press <enter> to continue or press any button to stop")

for x in range(list_items):
    name = ing_list[3 * x]
    unit = ing_list[1 + 3 * x]
    amount = ing_list[2 + 3 * x]

    if unit in unit_dictionary:
        ing_list[1 + 3 * x] = "ml"
        amount = ing_list[2 + 3 * x] * float(unit_dictionary.get(unit))
        unit = "ml"
    if unit == "ml" and name in food_dictionary:
        unit = "g"
        amount *= ratio * (float(food_dictionary.get(ing_list[3 * x])) / 250)
    print("{}: {:.1f}{}".format(name, amount, unit))
