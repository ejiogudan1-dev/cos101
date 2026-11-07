count = 0
for i in range(5):
    number = int(input("enter a number: "))
    if number < 1:
        print("number cannot be less than 1 or press e or E to end")
        stop = input("press e or E to end: ")
        if stop == "E" or stop == "e":
            print("end")
        break
    if number > 1:
        for num in range(1, 13):
            count = number * num
            print(f"{number} * {num} = {count}")
        break
