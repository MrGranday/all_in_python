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


# Step 1: Create a list of words
# Step 2: Use len() function
# Step 3: Print total number of words
list_of_words = ['osman', 'ghani', 'granday']

total_words = 0
for n in list_of_words:
    total_words += 1
print(total_words)


# Step 1: Create a list of numbers
# Step 2: Assume first number is largest
# Step 3: Loop through list
# Step 4: If current number > largest → update largest
# Step 5: Print largest number


list_of_numbers = [23, 4, 2, 4, 76, 33, 1, 23, 53,
                   23, 43, 65, 7, 6, 34, 3, 23, 23, 34, 45, 1, 8]

largest = list_of_numbers[0]
for n in list_of_numbers:
    if n > largest:
        largest = n
print(largest)


# Step 1: Create a dictionary with username and password
# Step 2: Ask user for username
# Step 3: Ask user for password
# Step 4: Check if username exists in dictionary
# Step 5: Check if password matches
# Step 6: Print "Login successful" or "Login failed"

# Step 1: Create a dictionary with username and password
users = {'osman': 'osman1234', 'ghani': 'ghani1234'}


def the_users(user_dict):
    # Step 2 & 3: Ask user for username and password
    name = input('Enter your name: ')
    password = input('Enter your password: ')

    # Step 4: Check if username exists
    if name in user_dict:
        # Step 5: Check if password matches
        if password == user_dict[name]:
            print('Login successful')
        else:
            print('Login failed: Incorrect password')
    else:
        print('Login failed: Username does not exist')


# Call the function
the_users(users)


# Step 1: Create a list of numbers
# Step 2: Create counter = 0
# Step 3: Loop through list
# Step 4: If number % 2 == 0 → increase counter
# Step 5: Print counter
