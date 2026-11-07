while True:
    number = input("Enter a number (or E to exit): ")

    if number.lower() == "e":
        print("Program ended.")
        break

    number = int(number)

    if number < 1:
        print("Number cannot be less than one")
        continue
    print(f"Multiplication table of {number}")
    for i in range(1, 13):
        print(number, "x", i, "=", number * i)
    break
