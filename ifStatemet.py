
# the if statement
if 5 == 15/3:
    print("this was right")
else:
    print("this was wrong")


# an else statement
x = 1
if x > 3:
    print("x is bigger then 3 ")
if x <= 3:
    print("x is equal or smaller then 3 ")


# this is else if, for brief elif

def compare_to_five(y):
    if y > 5:
        return "y is greater"
    elif y < 5:
        return "y is less "
    else:
        return "this was equal"


print(compare_to_five(10))
