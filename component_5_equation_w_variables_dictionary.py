unit_dictionary = {
    "tsp": 5,
    "tbs": 15,
    "cup": 237,
    "ounce": 30,
    "pint": 30,
    "quart": 30,
    "pound": 30,
}
loop = 1
while loop == 1:
    amount = float(eval(input("How much? ")))
    unit = input("Unit? ")
    if unit in unit_dictionary:
        amount *= unit_dictionary.get(unit)
        print("Amount in ml:", amount)
    else:
        print(amount, "is unchanged")