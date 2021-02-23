import re


def regex_check(string):
    if re.search("\s", file_name):
        return "Invalid file name - no spaces"
    if re.search("\.", file_name):
        return "Invalid file name - no periods"
    if file_name == "":
        return "Invalid file name - can't be blank"
    return "No Error"


calculation_list = []
file_name = input("Enter file name: ")
file_name_check = regex_check(file_name)
if file_name == "No Error":
    text_file = open("{}.txt".format(file_name), "a")

    loop = ""
    while loop == "":

        list_item = input("Enter an item: ")

        if list_item == "xxx":
            loop = 1
        else:
            calculation_list.append(list_item)

    print(calculation_list)

    list_len = len(calculation_list)

    if list_len == 0:
        print("List is empty")
    else:
        for x in range(list_len):
            if x+1 > list_len:
                break
            else:
                text_file.write("{}\n".format(calculation_list[-x-1]))
else:
    print(file_name_check)