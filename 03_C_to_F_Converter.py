loop = ""
while loop == "":
    c = ""
    while c.isnumeric() is False:
        c = (input("enter celsius: "))
    c = int(c)
    f = (c * 9 / 5 + 32)
    print("Fahrenheit = {}".format(f))