import csv


def string_check(question, condition):
    string_check_loop = 1
    while string_check_loop == 1:
        try:
            text = input(question)
            valid = "TRUE"

            # does not allow blank answers

            if len(text) > 0:

                # condition 2 only allows for characters that can go into an equation (0-9, +, -, *, ?)

                if condition == 2:
                    return eval(text)
                if valid == "TRUE":

                    # allows "T" as an input for tbs

                    if text == "T":
                        return text

                # returns text in lower case to keep code simple

                    else:
                        return text.lower()

            # prints error if answer is blank

            if valid == "TRUE":
                error = "!!Please enter something!!"
                print("\n{}\n{}\n{}\n".format("!"*len(error), error, "!"*len(error)))
            # prints error if an invalid character is inputted
        except(ValueError, SyntaxError, NameError):

            # error message only needed for these three because the only errors that should be raised would be
            # from eval()

            error = "!!Please enter a number or equation!!"
            print("\n{}\n{}\n{}\n".format("!" * len(error), error, "!" * len(error)))


# creates empty dictionary and adds rows from "01_ingredients_ml_to_g.csv" to it

groceries = open("01_ingredients_ml_to_g.csv")

csv_groceries = csv.reader(groceries)

food_dictionary = {}

for row in csv_groceries:
    food_dictionary[row[0]] = row[1]

# dictionary of units of volume and how many mLs they represent

# dictionary now properly converts mass to grams and volume to milliliters

unit_dictionary = {
    "tsp": [5, "ml"],
    "tbs": [15, "ml"],
    "cup": [237, "ml"],
    "ounce": [28, "g"],
    "fluid ounce": [30, "ml"],
    "pint": [473, "ml"],
    "quart": [946, "ml"],
    "pound": [454, "g"],
    "litre": [1000, "ml"]
}

# lists of alternative ways of spelling units to allow some flexibility in input

# separated fluid ounces and ounces

tsp = ["tsp", "teaspoon", "t", "teaspoons"]
tbs = ["tbs", "tablespoon", "T", "tbsp", "tablespoons"]
ounce = ["ounce", "oz", "ounces"]
fluid_ounce = ["fluid ounce", "fluid ounces", "fl oz"]
cup = ["cup", "c", "cups"]
pint = ["pint", "p", "pt", "fl pt", "pints"]
quart = ["quart", "q", "qt", "fl qt", "quarts"]
pound = ["pound", "lb", "#", "pounds"]
ml = ["ml", "milliliter", "millilitre", "milliliters", "millilitres"]
litre = ["litre", "liter", "l", "litres", "liters"]
unit_list = [tsp, tbs, ounce, fluid_ounce, cup, pint, quart, pound, ml, litre]

# list of valid inputs for an equation for use in function above

# removed in favour of except
border = "-------------------------------------------------------------------------------------------------------------"
print(border, "\n")
print("This programs takes the ingredients of recipes measured in imperial units and converts them to metric")
print("\n{}\n".format(border))
# allows user to input non blank values for recipe and source for use in header when printing updated ingredient list
recipe_name = string_check("Please enter the name of the recipe: ", 1)

recipe_source = string_check("Please enter the website the recipe is from: ", 1)

# Setting scale factor to 1 even though it is redefined without usage below because pycharm gets mad at me for no reason

ratio = 1

# loops for two serving sizes until user is okay with scale factor

print("\n{}\n".format(border))
print("Please enter the serving size indicated in the recipe and your desired serving size.\n"
      "The amounts of ingredients in the recipe will be adjusted to fit the desired serving size")
print("\n{}\n".format(border))

serving_size_loop = "1"
while serving_size_loop != "":
    print()
    number = string_check("Enter original serving size ", 2)
    number2 = string_check("Enter desired serving size ", 2)
    ratio = number2/number

    # warns user if the ratio is below 0.25 or above 4

    if ratio < 0.25:
        print("\nwarning scale factor = x{} (<0.25)\n".format(ratio))
    elif ratio > 4:
        print("\nwarning scale factor = x{} (>4)\n".format(ratio))
    else:
        print("\nscale factor = {}\n".format(ratio))
    serving_size_loop = input("Please press <enter> if you are okay with this or press any key to re-enter serving "
                              "sizes: ")

# loops adding ingredients, units, and amounts to empty list until user ends program

print("\n{}\n".format(border))
print("Please list the ingredients listed in the original recipe.\n"
      "Applicable units of volume will be converted to millilitres and units of mass will be converted to grams.\n"
      "If the ingredient is either originally measured in mL or converted to mL and is in the list of ingredients,\n"
      "it will be converted into grams")
print()
print("Please keep in mind that fluid ounces and ounces are separate units")
print("\n{}".format(border))
ing_list = []
list_items = 0
ing_list_loop = ""
while ing_list_loop == "":

    # adds name of ingredient to the list

    print()
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
    ing_list.append(string_check("Please enter the amount of this ingredient: ", 2))
    print()

    # adds 1 to the total number of ingredients

    list_items += 1

    ing_list_loop = input("press <enter> to continue adding ingredients or press any button to stop: ")

# prints recipe information from earlier as header

print("\n{}\n".format(border))
print(recipe_name)
print("from", recipe_source)
print("scaled by", ratio)
print("\n{}\n\nIngredients:\n".format(border))

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
        amount = ing_list[2 + 3 * x] * float(unit_dictionary.get(unit)[0])
        unit = unit_dictionary.get(unit)[1]

    # if the unit is converted to ml and the name is in the food dictionary, it is converted to grams

    if unit == "ml" and name in food_dictionary:
        unit = "g"
        amount *= (float(food_dictionary.get(ing_list[3 * x])) / 250)

    # multiplies amount by scale factor

    amount *= ratio

    # prints ingredient name: , amount, unit

    print("{}: {:.1f}{}".format(name, amount, unit))
