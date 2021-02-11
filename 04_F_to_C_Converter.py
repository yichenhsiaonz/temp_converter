loop = ""
while loop == "":
    f = ""
    while f.isnumeric() is False:
        f = (input("Enter fahrenheit: "))
    f = int(f)
    c = ((f - 32) * 5 /9)
    print("Celsius = {}".format(c))