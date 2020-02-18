import csv


def number_check(question):
    loop3 = 1
    while loop3 == 1:
        try:

            # only allows numbers above 0

            num = float(input(question))
            if num > 0:
                return num

            # prints error for anything below 0 or not a number

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

        # does not allow blank answers

        if len(text) > 0:

            # condition 2 only allows for characters that can go into an equation (0-9, +, -, *, ?)

            if condition == 2:
                if any(num not in allowed_list for num in text):
                    valid = "FALSE"
            if valid == "TRUE":

                # allows "T" as an input for tbs

                if text == "T":
                    return text

            # returns text in lower case to keep code simple

                else:
                    return text.lower()

        # prints error if answer is blank

        if valid == "TRUE":
            print("Please enter something")

        # prints error if condition = 2 and an invalid character is inputted

        else:
            print("Please enter a float, integer, or equation")


# creates empty dictionary and adds rows from "01_ingredients_ml_to_g.csv" to it

groceries = open("01_ingredients_ml_to_g.csv")

csv_groceries = csv.reader(groceries)

food_dictionary = {}

for row in csv_groceries:
    food_dictionary[row[0]] = row[1]

# dictionary of units of volume and how many mLs they represent

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

# lists of alternative ways of spelling units to allow some flexibility in input

tsp = ["tsp", "teaspoon", "t", "teaspoons"]
tbs = ["tbs", "tablespoon", "T", "tbsp", "tablespoons"]
ounce = ["ounce", "oz",  "fl oz", "ounces"]
cup = ["cup", "c", "cups"]
pint = ["pint", "p", "pt", "fl pt", "pints"]
quart = ["quart", "q", "qt", "fl qt", "quarts"]
pound = ["pound", "lb", "#", "pounds"]
ml = ["ml", "milliliter", "millilitre", "milliliters", "millilitres"]
litre = ["litre", "liter", "l", "litres", "liters"]
unit_list = [tsp, tbs, ounce, cup, pint, quart, pound, ml, litre]

# list of valid inputs for an equation for use in function above

allowed_list = ["1", "2", "3", "4,", "5", "6", "7", "8", "9", "0", "+", "-", "*", "/", "."]

# allows user to input non blank values for recipe and source for use in header when printing updated ingredient list

recipe_name = string_check("Please enter the name of the recipe: ", 1)

recipe_source = string_check("Please enter the website the recipe is from: ", 1)

# Setting scale factor to 1 even though it is redefined without usage below because pycharm gets mad at me for no reason

ratio = 1

# loops for two serving sizes until user is okay with scale factor

loop2 = 1
while loop2 != "yes":
    number = number_check("Enter original serving size ")
    number2 = number_check("Enter desired serving size ")
    ratio = number2/number

    # warns user if the ratio is below 0.25 or above 4

    if ratio < 0.25:
        print("warning scale factor =", ratio, "(<0.25). Measurements")
    elif ratio > 4:
        print("warning scale factor =", ratio, "(>4)")
    else:
        print("scale factor =", ratio)
    loop2 = input("Please enter <yes> if you are okay with this: ").lower()

# loops adding ingredients, units, and amounts to empty list until user ends program

ing_list = []
list_items = 0
loop = ""
while loop == "":

    # adds name of ingredient to the list

    ing_list.append(string_check("Please enter the name of the ingredient: ", 1))
    unit = string_check("Please enter the unit this ingredient is measured in in the original recipe : ", 1)

    # checks for the unit in each list of alternative spellings by going through a list of every list and if the unit
    # is found in any list, the name of the unit is set to the first entry in the list it is found in which is the only
    # one that will be accepted by the dictionary of units

    for y in unit_list:
        if unit in y:
            unit = y[0]
            break

    # adds unit and amount to list

    ing_list.append(unit)
    ing_list.append(eval(string_check("Please enter the amount of this ingredient: ", 2)))

    # adds 1 to the total number of ingredients

    list_items += 1

    loop = input("press <enter> to continue adding ingredients or press any button to stop")

# prints recipe information from earlier as header

print()
print(recipe_name)
print("from", recipe_source)
print("scaled by", ratio)
print()

# loops the same number of times as the number of ingredients

for x in range(list_items):

    # entries of the ing_list that are multiples of 3 are ingredient names
    # entries that follow the pattern 3n + 1 are units
    # entries that follow 3n + 2 are amounts

    name = ing_list[3 * x]
    unit = ing_list[1 + 3 * x]
    amount = ing_list[2 + 3 * x]

    # checks for the unit in the unit dictionary, converts to ml if found

    if unit in unit_dictionary:
        ing_list[1 + 3 * x] = "ml"
        amount = ing_list[2 + 3 * x] * float(unit_dictionary.get(unit))
        unit = "ml"

    # if the unit is converted to ml and the name is in the food dictionary, it is converted to grams

    if unit == "ml" and name in food_dictionary:
        unit = "g"
        amount *= (float(food_dictionary.get(ing_list[3 * x])) / 250)

    # multiplies amount by scale factor

    amount *= ratio

    # prints ingredient name: , amount, unit

    print("{}: {:.1f}{}".format(name, amount, unit))
