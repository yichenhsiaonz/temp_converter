import re


def regex_check(string):
    if re.search("\s", file_name):
        return "Invalid file name - no spaces"
    if re.search("\.", file_name):
        return "Invalid file name - no periods"
    if file_name == "":
        return "Invalid file name - can't be blank"
    return "You entered a valid file name"


loop = ""
while loop == "":

    file_name = input("enter a file name: ")

    checked_name = regex_check(file_name)

    print(checked_name)



