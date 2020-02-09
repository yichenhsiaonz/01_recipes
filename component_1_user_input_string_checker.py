def string_check(string, condition):
    global valid
    if len(string) <= 5:
        if string in valid_list:
            valid = 0
            return valid
        else:
            valid = 1
            return valid
    else:
        valid = 0
        return valid

valid_list = ["sugar"]
valid = 1
while valid == 1:
    string_check