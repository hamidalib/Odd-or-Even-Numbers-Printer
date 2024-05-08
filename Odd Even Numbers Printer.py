while True:
    Ranger_Start = int(input("Enter start number: "))
    Ranger_End = int(input("Enter ending number: "))
    Command = input("Click E for even number, click O for Odd Numbers: ")

    if Command == "E" or Command == "e":
        for num in range (Ranger_Start, Ranger_End):
            if num % 2 == 0:
                print(num)
        print("You requested Even Numbers")
    elif Command == "O" or Command == "o":
        for num in range(Ranger_Start, Ranger_End):
            if num % 2 == 1:
                print(num)
        print("You requested Odd Numbers")
    elif Command == "Q" or Command == "q":
        print("Invalid Operation")
        break
    else:
        print("Only E and O are allowed commands")