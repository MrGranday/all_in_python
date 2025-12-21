def sum(num, num1):
    return num + num1


def sub(num, num1):
    return num - num1


a = input("enter number 1 for SUM and 2 for Subtraction: ")
num = int(input("enter first number to add: "))
num1 = int(input("enter second number to add: "))

if a == "1":
    print("result: ", sum(num, num1))
if a == "2":
    print("result: ", sub(num, num1))


# the if statement
if 5 == 15/3:
    print("this was right")
else:
    print("this was wrong")
