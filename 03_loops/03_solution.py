number = int(input("Enter the number: "))

for i in range(1, 11):
    if i != 5:
        print(number, "X", i, "=", number*i)