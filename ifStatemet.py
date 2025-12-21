
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
print(compare_to_five(1))
print(compare_to_five(5))


# to get the length of the string
p = "this is osman"
print(len(p))

# if want to get the index of the string
print(p[0])


# printing the negative index
print(p[-1])

# if want to print from a specific index to the specific index then

print(p[0:3])


# the functions

def simple():
    return "this was simple"


print(simple())


def plus_ten(a):
    result = a+10
    print(result)
    # or we return it
    return result


plus_ten(100)
