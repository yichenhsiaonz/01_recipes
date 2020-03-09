import csv
import re
import string


# safer eval() from stack overflow that prevents eval() from running code

def less_dangerous_eval(equation):
    if not set(equation).intersection(string.ascii_letters + '{}[]_;\n'):
        return eval(equation)
    else:
        error_msg("!!Illegal character!!")
        return None


def string_check(question, condition):
    string_check_loop = 1
    while string_check_loop == 1:
        try:
            text = input(question).strip().replace(" ", "+").replace("^", "**")
            valid = "TRUE"

            # does not allow blank answers, including just spaces

            if text is not "" and text is not " ":

                # condition 2 only allows for characters that can go into an equation (0-9, +, -, *, ?)

                if condition == 2:
                    if less_dangerous_eval(text) is None:
                        raise ValueError
                    else:
                        return less_dangerous_eval(text)
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

            error_msg("!!Please enter a number or equation!!")


# separated error message into function since the same code is repeated twice

def error_msg(error):
    print("\n{}\n{}\n{}\n".format("!" * len(error), error, "!" * len(error)))


# separated border into function since code is repeated often

def border():
    print("\n{}\n".format("-"*109))

# creates empty dictionary and adds rows from "01_ingredients_ml_to_g.csv" to it

groceries = open("01_ingredients_ml_to_g.csv")

csv_groceries = csv.reader(groceries)

food_dictionary = {}

for row in csv_groceries:
    food_dictionary[row[0]] = row[1]

# dictionary of units of volume and how many mLs they represent
# dictionary now properly converts mass to grams and volume to milliliters
# added sticks for butter because I saw it in the word document

unit_dictionary = {
    "tsp": [5, "ml"],
    "tbs": [15, "ml"],
    "cup": [237, "ml"],
    "ounce": [28, "g"],
    "fluid ounce": [30, "ml"],
    "pint": [473, "ml"],
    "quart": [946, "ml"],
    "stick": [113, "g"],
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
stick = ["stick", "sticks"]
ml = ["ml", "milliliter", "millilitre", "milliliters", "millilitres"]
litre = ["litre", "liter", "l", "litres", "liters"]
unit_list = [tsp, tbs, ounce, fluid_ounce, cup, pint, quart, pound, stick, ml, litre]

# list of valid inputs for an equation for use in function above
# removed in favour of except

border()
print("This programs takes the ingredients of recipes measured in imperial units and converts them to metric")
border()
# allows user to input non-blank values for recipe and source for use in header when printing updated ingredient list
recipe_name = string_check("Please enter the name of the recipe: ", 1)

recipe_source = string_check("Please enter the website the recipe is from: ", 1)

# Setting scale factor to 1 even though it is redefined without usage below because pycharm gets mad at me for no reason

ratio = 1

# loops for two serving sizes until user is okay with scale factor

border()
print("Please enter the serving size indicated in the recipe and your desired serving size.\n"
      "The amounts of ingredients in the recipe will be adjusted to fit the desired serving size.\n"
      "\nPlease enter a number or equation")
border()

serving_size_loop = "1"
while serving_size_loop != "":

    number = string_check("Enter original serving size: ", 2)
    number2 = string_check("Enter desired serving size: ", 2)
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

border()
print("Please list the ingredients listed in the original recipe.\n"
      "For each ingredient, you will be asked for it's name, unit it is measured in,\n"
      "and the amount of the ingredient in said unit\n\n"
      "Applicable units of volume will be converted to millilitres and units of mass will be converted to grams.\n"
      "If the ingredient is either originally measured in mL or converted to mL and is in the list of ingredients,\n"
      "it will be converted into grams.\n"
      "\nPlease keep in mind that fluid ounces and ounces are separate units\n"
      "\nPlease enter an ingredient listed in the recipe in the order of amount, unit, then name\n"
      "E.g: 1, cup, flour\n"
      "\nYou can end the loop by typing \"xxx\"")
border()
ing_list = []
list_items = 0
ing_list_loop = ""
while ing_list_loop == "":
    try:
        ing_line = input(
            "Please enter an ingredient listed in the recipe in the order of amount, unit, then name: ")

        # ends the loop if the user enters "xxx" and there is at least one ingredient

        if ing_line == "xxx" and list_items > 0:
            break

        # raises an error if more than 2 separators are found (commas)

        if len(re.findall(",", ing_line)) > 2:
            raise ValueError

        # splits input into three at every comma

        temp_ing_list = re.split(",", ing_line, 3)

        # removes whitespace from front and back of ingredient name entered

        temp_name = temp_ing_list[2].strip()

        # removes white space from front and back of unit entered
        # iterates through the list of lists of alternate spellings and if found, sets the unit to the spelling
        # that works with the dictionary of units

        temp_unit = temp_ing_list[1].strip()
        for y in unit_list:
            if temp_unit in y:
                temp_ing_list[1] = y[0]
                break

        # replaces all whitespace in number / equation entered with + to allow inputs like 1 1/2 (one and a half)
        # any error raised if eval() doesn't work will be caught by except and will repeat the loop without adding
        # to the total number of ingredients

        temp_amount = less_dangerous_eval(temp_ing_list[0].replace(" ", "+").replace("^", "**"))

        # raises an error if entries are blank

        for x in temp_ing_list:
            if x == "" or x == " ":
                raise ValueError

        # adds to ing_list

        ing_list.append(temp_name)
        ing_list.append(temp_unit)
        ing_list.append(temp_amount)

        # adds 1 to the total number of ingredients

        list_items += 1

        print()

    except(ValueError, SyntaxError, NameError):
        error_msg("!!Please follow the instructions above!!")
    except IndexError:
        error_msg("!!Please enter an amount, unit, and name!!")

# prints recipe information from earlier as header

border()
print(recipe_name)
print("from", recipe_source)
print("scaled by", ratio)
border()
print("Ingredients:\n")

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
        amount = float(amount) * float(unit_dictionary.get(unit)[0])
        unit = unit_dictionary.get(unit)[1]
    else:

        # adds whitespace to units not in the dictionary of units to prevent strange formatting like 10pinches

        unit = " {}".format(unit)

    # if the unit is converted to ml and the name is in the food dictionary, it is converted to grams

    if unit == "ml" and name in food_dictionary:
        unit = "g"
        amount *= (float(food_dictionary.get(ing_list[3 * x])) / 250)

    # multiplies amount by scale factor

    amount *= ratio

    # prints ingredient name: , amount, unit

    print("{}: {:.1f}{}".format(name, amount, unit))
