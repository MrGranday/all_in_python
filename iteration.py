# For loop

even = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

for n in even:
    # print(n)
    print(n, end=" ")


# while Loops
x = 0
while x <= 20:
    print(x, end=" ")
    # if we just print this it will be infinite because
    # 20 will always be bigger then 0
    # and if we give condition to this
    x = x+2
    # this condition will stop till 20


print("Use Conditional")
# Use Conditional Statements
for n in range(10):
    print(2**n, end=' ')


list_2 = [67, 12, 34, 11, 12, 78, 9, 54, 34]
for n in list_2:
    if n <= 20:
        print('this is less then 20 :', n)


def the_count(number):
    total = 0
    for n in number:
        if n <= 20:
            total += 1
            print('the number: ', n, 'and the count: ', total)


print(the_count(list_2))

# Iterating over Dictionaries
prices = {
    "box_of_water": 3,
    "hamburger": 5,
    "oranges": 10
}
quantity = {
    "box_of_water": 1,
    "hamburger": 10,
    "oranges": 2
}

money_spent = 0
for n in prices:
    money_spent = money_spent+(prices[n]*quantity[n])
print(money_spent)
