number = int(input("enter a number between 2 & 13: "))
if number <= 0:
    print("number cannot be zero")
if number == 1:
    print("number must be greater than 1!!!")
if number > 13:
    print("number should be between 2 & 13")
else:
    for count in range(1, 13):
        print(f"{number} * {count} = {number * count}")
