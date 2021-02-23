calculation_list = []

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
    for x in range(3):
        if x+1 > list_len:
            break
        else:
            print(calculation_list[-x-1])