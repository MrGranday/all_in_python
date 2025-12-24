# Step 1: Create a function
# Step 2: Function should take one number as input
# Step 3: Use if condition
# Step 4: If number % 2 == 0 → print "Even"
# Step 5: Else → print "Odd"


def number(num):
    if num % 2 == 0:
        return 'Even'
    else:
        return 'Odd'


print(number(10))


# Step 1: Create a list of numbers
# Step 2: Create a variable sum = 0
# Step 3: Use for loop to go through list
# Step 4: Add each number to sum
# Step 5: Print final sum


list_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 23, 45, 12, 78, 4, 23, 65]


def sum_of(list_num):
    sum = 0
    for n in list_num:
        sum = sum + n
    return sum


print(sum_of(list_num))
