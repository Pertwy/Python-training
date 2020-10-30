
try:
    number = int(input("enter an number"))
    print(number)
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("invalid input")
