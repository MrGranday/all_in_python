the_list = ['osman', 'ghani', 'granday']
print(the_list)
print(the_list[1])


# replacing the index
# so this will replace the late name GRANDAY with OMAR
the_list[2] = 'OMAR'
print(the_list)


# if we want to delete the index
del the_list[1]
print(the_list)

# so we have deleted the second index or element


numbers = [1, 2, 3, 4, 5]
print(numbers)
print(numbers[3])


# if i want to add a new name to the list we use .append() methods

the_list.append('khan')
print(the_list)

# we can use the .extend[ ] methods
the_list.extend(['Haroon', 'mustafa'])
print(the_list)


# if we want the  length we use  len() method
print(len(the_list))


# slicing the list
print(the_list[1:3])
print(the_list)


# Tuples in Python

x = (2, 3, 4, 5)

print(x)
# we can access the elements also like this
print(x[0])


# we can do the Tuple like this
y = 4, 5, 6, 7
print(y)

# and we can do it like this
a, b, c = 7, 8, 9


# when storing tuples in list
list_1 = [x, y]
print(list_1)


# Dictionaries  in python
dic = {'k1': "osman", 'k2': "Ghani", 'k3': "Granday"}

# if we want to print one key
print(dic['k1'])

# if i want to add another element

dic['k4'] = "khan"

# now printing all the elements
print(dic)
