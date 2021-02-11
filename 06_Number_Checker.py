big_loop = ""
while big_loop == "":
    num_loop = ""
    while num_loop == "":
        number = (input("Enter a number: "))
        min = float(input("Minimum: "))
        if number.lstrip("-").replace(".", "", 1).isnumeric():
            number = float(number)
            if number >= min:
                num_loop = "s"
                break
            print("Too cold!!!")
        else:
            print("Enter proper number!!!")
    print("OK!")
