calculation_list = []
file_name = input("enter file name")
f = open("{}.txt".format(file_name), "a")

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
            f.write("{}\n".format(calculation_list[-x-1]))