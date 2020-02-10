def string_check(string):
    global valid
    if len(string) <= 5:
        if string in valid_list:
            return "valid"
        else:
            return "invalid"
    else:
        return "valid"

valid_list = ["sugar"]
valid = 1
while valid == 1:
    text = input("Enter a string ")
    print(string_check(text))